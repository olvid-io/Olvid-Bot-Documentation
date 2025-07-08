# 🌐 Navigateur

Nous avons développé une librairie écrite en typescript qui permet d'écrire des applications clientes d'un daemon Olvid dans une page web.
L'utilisation de ce module est cependant limité, amène des contraintes et des enjeux en termes de sécurité.

## Limitations et contraintes

###  Utilisation d'un proxy
Actuellement une page web ne peut parler directement à un daemon gRPC. Il faut utiliser un proxy. Celui-ci sera mis en place en même temps que notre daemon dans la procédure suivante.

### Envoi de fichiers impossible
Les outils que nous utilisons pour développer cette librairie ne permettent pas d'utiliser des méthodes de type *client side streaming* et *bidirectional streaming* de gRPC.
Il en résulte qu'il n'est pas possible d'envoyer des pièces jointes, ou de changer les photos de profil.

### Sécurité
Dans le cas oú votre page / application web doit être accessible sur Internet nous vous recommandons d'être très prudent lors de l'exposition de votre daemon.
Nous vous recommandons de mettre en place à minima une authentification HTTP, et si possible une authentification par certificat.

Faites également attention à ne pas stocker en clair votre *clé client* dans votre page web.
Si votre proxy gRPC est authentifié (idéalement par certificat), vous pouvez ajouter la clé client directement au niveau du reverse-proxy, en ajoutant un header **daemon-client-key**.  

## Installation
### Daemon et proxy
Voici un exemple d'infrastructure *docker compose* pour déployer un daemon et son proxy gRPC.

```{code-block} yaml
  :substitutions:
services:
  daemon:
    image: olvid/bot-daemon:{{docker_version}}
    environment:
      - OLVID_ADMIN_CLIENT_KEY_CLI=SetARandomValue
    volumes:
      - ./data:/daemon/data

  proxy:
    image: olvid/grpc-web-proxy
    ports:
      - "8080:8080"
    command: ["--backend_addr=daemon:50051", "--run_tls_server=false", "--server_http_max_read_timeout=0s", "--server_http_max_write_timeout=0s"]
    restart: unless-stopped

  cli:
    image: olvid/bot-python-runner:{{docker_version}}
    entrypoint: "olvid-cli"
    environment:
      - OLVID_ADMIN_CLIENT_KEY=SetARandomValue
      - OLVID_DAEMON_TARGET=daemon:50051
    stdin_open: true
    tty: true
    profiles: ["cli"]
```

Vous pouvez ensuite lancer votre daemon et son proxy.
```shell
docker compose up -d daemon proxy
```

Pour l'initialisation et la mise en place de ce daemon je vous invite à regarder notre section [🚀 Quickstart](/index.md#identité-olvid).

### Client
Une fois votre daemon en place vous pouvez commencer à écrire votre page / application web.
Il existe de nombreux moyens et framework pour faire cela, nous ne pourrons pas tous les détailler, mais nous allons voir les bases. 

Pour notre exemple nous réaliserons une page web simple qui envoie un message dans toutes les discussions de votre bot.
Pour cela nous utiliserons `npm` pour l'installation du module, et le framework`vite`.

On commence par préparer notre projet et installer les dépendances.
```shell
npm install @olvid/bot-web
npm install vite
npm pkg set scripts.dev="npx vite"
```

On peut ensuite créer deux fichiers qui contiennent le code de notre page de démonstration.

`index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <script type="module" src="./index.js"></script>
    <title>Olvid in a Web Page</title>
</head>
<body>
    <input id="send-input" type="text"/>
    <button id="send-button">Send</button>
</body>
</html>
```

`index.js`
```javascript
import {OlvidClient} from "@olvid/bot-web";

const client = new OlvidClient({
    serverUrl: "http://localhost:8080",
    clientKey: ""  // TODO set me !
});

let input = document.getElementById("send-input");
let button = document.getElementById("send-button");

// callback to send a message in every bot discussion
async function broadcastMessage(body) {
    if (!body) {
        console.error("Message body cannot be empty");
        return
    }
    for await (let discussion of client.discussionList()) {
        await client.messageSend({discussionId: discussion.id, body: body})
    }
}

// send message when you click send or press enter in input 
button.onclick = async () => { await broadcastMessage(input.value) }
input.addEventListener("keydown", async (e) => {
    if (e.code === "Enter") {
        await broadcastMessage(input.value)
    }
});

client.onMessageSent({callback: message => {
  console.log("> ", message.body)
}});
client.onMessageReceived({callback: message => {
  console.log("< ", message.body);
}})
```

Pensez à remplacer la valeur de votre clé client dans le fichier `index.js` au moment de l'instanciation de la classe *OlvidClient*, et à modifier la valeur de `serverUrl` dans le cas oú celle par défaut ne conviendrait pas à votre infrastructure.

Pour tester votre programme il suffit de lancer la commande suivante et de vous rendre à l'adresse indiquée. 

```shell
npm run dev
```

## Reverse-proxy
Une fois votre daemon en place et votre application web developpé, vous pourriez avoir besoin de la déployer en dehors de votre machine locale. 
Nous allons donc voir les différentes configurations possibles de nginx en reverse-proxy.

### Configuration basique
Voici un exemple de configuration basique sans authentification. Attention, n'exposez pas ce proxy sur un réseau en l'état.
```nginx
server {
    listen 80;
    server_name daemon-proxy.example.com
    
    access_log /var/log/nginx/daemon-proxy-access.log;
    error_log /var/log/nginx/daemon-proxy-error.log;
    
    location / {
      proxy_pass http://localhost:5174;
      proxy_buffering off;
      proxy_read_timeout 1d;
      proxy_connect_timeout 1d;
      proxy_send_timeout 1d;
    }
}
```

### Ajouter de l'authentification
#### HTTP
Il faut tout d'abord créer un fichier de mot de passe. Vous pouvez suivre la [documentation officielle de nginx](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/#creating-a-password-file).

Il suffit ensuite d'activer l'authentification HTTP pour notre reverse-proxy.

```nginx
server {
    listen 80;
    server_name daemon-proxy.example.com
    
    access_log /var/log/nginx/daemon-proxy-access.log;
    error_log /var/log/nginx/daemon-proxy-error.log;
    
    location / {
      auth_basic "Daemon Proxy";
      auth_basic_user_file /etc/nginx/.htpasswd; 
      proxy_pass http://localhost:5174;
      proxy_buffering off;
      proxy_read_timeout 1d;
      proxy_connect_timeout 1d;
      proxy_send_timeout 1d;
    }
}
```

#### Certificats
Nous vous recommandons de mettre plutôt en place une authentification par certificat, pour cela vous pouvez vous réferrer à la [documentation officielle nginx](https://docs.nginx.com/nginx-instance-manager/system-configuration/secure-traffic/).

### Clé Client
:::{warning}
Cette section ne doit être suivie que dans le cas oú l'accès à votre reverse-proxy est correctement authentifié  
(cf [](#ajouter-de-lauthentification)) !
Dans le cas contraire votre daemon pourrait devenir librement accessible sur internet.
:::

Pour éviter de mettre la clé client dans votre page / application web vous pouvez la spécifier au niveau de votre reverse-proxy.

Pour cela vous pouvez ajouter la ligne suivante (en la modifiant) au bloc `location` de votre configuration nginx.

```nginx
proxy_set_header daemon-client-key MY_CLIENT_KEY;
```

⚠️ Cela permettra que n'importe quel client, authentifié sur le proxy, accéde au daemon avec la clé client spécifié dans la configuration nginx.

### Filtrage API
Il est possible de n'exposer que les points d'entrée API nécessaires à votre application en faisant du filtrage au niveau du reverse-proxy.

Pour cela au lieu de spécifier un seul bloc `location` dans notre configuration nginx, on en ajoute un par point d'entrée à exposer, avec le même contenu, mais des *path* différents.

Voici un exemple de configuration qui n'autorise que les commandes messageSend et discussionGet, et la notification onMessageReceived.

⚠️ Cette configuration ne met pas en place d'authentification, mais nous vous conseillons fortement de le faire cf [](#ajouter-de-lauthentification).

```nginx
server {
    listen 80;
    server_name daemon-proxy.example.com
    
    access_log /var/log/nginx/daemon-proxy-access.log;
    error_log /var/log/nginx/daemon-proxy-error.log;
    
    location /olvid.daemon.services.v1.MessageCommandservice/MessageSend {
      proxy_pass http://localhost:5174;
      proxy_buffering off;
      proxy_read_timeout 1d;
      proxy_connect_timeout 1d;
      proxy_send_timeout 1d;
    }
    location /olvid.daemon.services.v1.DiscussionCommandservice/DiscussionGet {
      proxy_pass http://localhost:5174;
      proxy_buffering off;
      proxy_read_timeout 1d;
      proxy_connect_timeout 1d;
      proxy_send_timeout 1d;
    }
    location /olvid.daemon.services.v1.MessageNotificationService/MessageReceived {
      proxy_pass http://localhost:5174;
      proxy_buffering off;
      proxy_read_timeout 1d;
      proxy_connect_timeout 1d;
      proxy_send_timeout 1d;
    }
}
```

#### Partager le domaine
Pour des raisons de praticité ou pour éviter des soucis de *Cross-Origin* vous pouvez être amené à héberger votre proxy daemon et votre page/application web sur le même domaine.
Voici un exemple de configuration nginx pour ce cas de figure.

Dans ce cas, pensez à changer l'URL de connection à votre daemon en ajoutant le suffixe `/proxy` dans votre application.

```nginx
server {
    listen 80;
    server_name daemon-proxy.example.com
    
    access_log /var/log/nginx/daemon-proxy-access.log;
    error_log /var/log/nginx/daemon-proxy-error.log;

    # proxy is only accessible with /proxy prefix, but we remove it before transfering requests to grpc-web-proxy     
    location /proxy/ {
      rewrite /proxy/(.*) /$1 break;
      proxy_pass http://localhost:5174;
      proxy_buffering off;
      proxy_read_timeout 1d;
      proxy_connect_timeout 1d;
      proxy_send_timeout 1d;
    }
    
    # configuration to your web page / application
    location / {
      [...]
    }
}
```
