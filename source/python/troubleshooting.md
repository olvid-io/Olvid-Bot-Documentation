# 👩‍🔧 Dépannage

## Erreurs courantes
:::{contents}
:local: true
:depth: 3
:::

### **No module named 'olvid'**
:::{card}
Le module `olvid-bot` n'a pas été trouvé. Si vous utilisez un environnement virtuel, pensez à l'activer.
```shell
source .venv/bin/activate
```
Sinon, installez la dernière version du module à l'aide de la commande pip.
```shell
pip3 install olvid-bot
```
:::

### **Client key not found**
:::{card}
Votre clé client n'a pas pu être trouvée. Vérifiez qu'elle se trouve soit dans votre environnement avec la commande `env`, 
soit que le fichier `.env` existe bien, contient les bonnes valeurs et se trouve dans le répertoire courant.
:::

### **Admin client key not found**
:::{card}
Impossible de trouver une clé client administrateur. Si vous n'utilisez pas les API d'administration (gestion d'identité ou de clé client) utilisez la classe `OlvidClient` plutôt que la classe `OlvidAdminClient`.

Sinon, vérifiez que la clé est bien définie en utilisant la variable `OLVID_ADMIN_CLIENT_KEY` et non `OLVID_CLIENT_KEY`.

Enfin, vérifiez à l'aide de la CLI que la clé que vous utilisez est valide et possède les droits administrateurs. (cf. [Gestion des clés client](/cli/usage.md#gestion-des-cles-client))
:::

### **Failed to connect to all addresses**
:::{card}

Votre programme n'a pas réussi à se connecter au daemon. Vérifiez que le daemon est bien lancé et fonctionnel.
```shell
# start daemon in the background
docker compose up -d daemon
# check daemon logs
docker compose logs -f daemon
```
Si vous venez de lancer le daemon, patientez un peu avant de réessayer, il est possible qu'il n'ait pas fini sa séquence de lancement et ne soit donc pas prêt à recevoir des connections client.

Si le daemon semble fonctionner, vérifiez que le port 50051 est exposé ou accessible depuis l'environnement d'exécution de votre programme.

Dans le cas d'une configuration différente de celle de notre page d'installation, pensez à stipuler l'adresse du daemon.
Pour cela, vous pouvez utiliser la variable `OLVID_DAEMON_TARGET` en tant que variable d'environnement ou dans un fichier `.env`.

Il faut spécifier le nom de domaine ou l'adresse IP du daemon, suivie du port. Par exemple :
```shell
OLVID_DAEMON_TARGET=localhost:50051
# ou
OLVID_DAEMON_TARGET=daemon:50051
```
:::

### **Invalid client key**
:::{card}
La clé client que vous utilisez n'est pas reconnue par le daemon.

- Vérifiez qu'il n'y a pas de conflit entre deux valeurs de clé entre un fichier `.env`, vos variables d'environnement et votre code.
- Si vous avez plusieurs instances de daemon, vérifiez que vous vous connectez à la bonne.
:::