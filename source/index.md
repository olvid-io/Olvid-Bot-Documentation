```{image} _static/images/olvid.png
:align: right
:alt: Olvid logo
:scale: 20
:target: https://olvid.io
```

```{toctree}
:maxdepth: 2
:hidden:

self
python/python
js/js
cli/cli
daemon/daemon
glossary
changelog
```

# 🚀 Quickstart

Bienvenue dans la documentation des bots Olvid !

Nous avons conçu cet ensemble d'outils pour vous permettre de créer vos propres chatbots et intégrations pour l'application [Olvid](https://olvid.io), tout en conservant ses standards de sécurité maximale.

Nous vous recommandons de commencer par notre procédure d'[](#installation).
Elle vous permettra d'installer et configurer votre propre daemon Olvid.
Ce daemon peut être vu comme une application Olvid pilotable par l'intermédiaire d'une API gRPC.

Une fois l'installation effectuée, vous pourrez commencer à écrire le code de vos premiers clients, afin d'interagir et de commander le profil Olvid que vous aurez créé sur le daemon.

%todo todel
:::{note}
Cette documentation est toujours en cours d'écriture. Si quelque chose vous semble incorrect, mal écrit ou peu clair vous pouvez:
- créer une issue et/ou ouvrir une pull request en cliquant sur le bouton GitHub disponible dans la barre supérieure.
- Nous contacter par mail: [bot@olvid.io](mailto:bot@olvid.io)
:::

# Installation
## Pré-requis

Pour suivre cette procédure, vous aurez besoin que Docker soit installé sur votre machine. 
La procédure d'installation est disponible ici : [Installer Docker](https://docs.docker.com/engine/install/).

## Infrastructure

Nous allons utiliser un fichier Docker Compose pour configurer et lancer notre infrastructure.

Vous pouvez copier le contenu suivant dans un fichier nommé `docker-compose.yaml`.

```yaml
services:
  daemon:
    image: olvid/bot-daemon
    environment:
      - OLVID_ADMIN_CLIENT_KEY_CLI=SetARandomValue
    ports:
      - 50051:50051
    volumes:
      - ./data:/daemon/data
  cli:
    image: olvid/bot-python-runner
    entrypoint: "olvid-cli"
    environment:
      - OLVID_ADMIN_CLIENT_KEY=SetARandomValue
      - OLVID_DAEMON_TARGET=daemon:50051
    stdin_open: true
    tty: true
    profiles: ["cli"]
```

Nous allons maintenant lancer le daemon en tâche de fond avec la commande suivante :

```shell
docker compose up -d
```

Pour vérifier que le daemon a démarré correctement, on peut regarder ses logs.

```shell
docker compose logs -f daemon
```

Une fois que les logs ont fini de défiler, le daemon a démarré et on peut sortir de l'affichage en utilisant CTRL + C.

## Identité Olvid

L'interface en ligne de commande Olvid (CLI) permet de se connecter directement au daemon et lui envoyer manuellement des commandes. 
On l'utilise a minima pour créer notre identité Olvid et entrer en contact avec. 
Mais elle pourra également servir plus tard pour débugger nos programmes ou déclencher manuellement des actions.  

Pour lancer la CLI en mode interactif, on utilisera la commande suivante :

```shell
docker compose run --rm cli
```

Un nouveau prompt s'affiche maintenant. Le nombre affiché correspond à l'identifiant de l'identité utilisée actuellement. 
Dans notre cas, il affiche 0 car nous n'avons pas encore d'identité sur le daemon.
Pour plus d'informations, rendez-vous dans la section [](/cli/cli).

Pour créer notre première identité, nous allons utiliser la commande `identity new`. 
Voici un exemple complet et commenté du déroulement de la commande.

```shell
# Création d'une nouvelle identité. Remplacez FirstName, LastName, ... par la valeur souhaitée.
# LastName, Position, et Company sont optionnels. Et les valeurs saisies peuvent être mises à jour plus tard.
0 > identity new FirstName LastName Position Company

# Une clé client pour authentifier vos futurs bots est automatiquement créée. 
# Conservez-la en attendant.
identity creation > Here is your client key to connect to daemon with this identity:
AAAAAAAA-BBBB-AAAA-AAAA-AAAAAAAAAAAA

# Entrez "yes" pour valider que vous avez conservé votre clé client.
identity creation > Did you saved your client key ? (y/N)

# Entrez "yes" pour entrer en contact depuis votre identité personnelle Olvid avec cette nouvelle identité.
# Cette étape est optionnelle mais nécessaire si vous voulez créer une discussion avec votre bot.
identity creation > Do you want to add this identity to your contacts ? (y/N)
>yes

# Ceci est le lien d'invitation de l'identité du bot.
# Vous pouvez l'ouvrir dans un navigateur internet pour afficher le QR code à scanner dans votre application mobile.
# Vous pouvez aussi le copier pour l'importer dans votre application desktop
identity creation > Send an invitation to this invitation link: https://invitation.olvid.io/#........

# La CLI attend maintenant qu'une invitation arrive ...
# Lorsqu'elle reçoit votre invitation, le processus reprend.
identity creation > Please enter sas code displayed on the other device

# Entrez le code à 4 chiffres affiché dans votre Olvid personnel
> 0000

# Entrez le code affiché dans votre Olvid personnel.
identity creation > Please enter this sas code on the other device: 1111

# Le processus est maintenant terminé.
Now using identity: 1
You can now send messages to YOUR NAME in discussion 1

# Vous pouvez vous envoyer un message de test en utilisant la commande suivante
1 > message send 1 Hello World !

# Pour sortir du mode interactif, utilisez CTRL + D ou la commande exit
1 > exit
```

## Premier programme

Vous avez maintenant une infrastructure fonctionnelle, avec un daemon  hébergeant une identité Olvid. 
Vous pouvez utiliser l'API gRPC du daemon pour contrôler cette identité. 

Pour continuer, il vous faut choisir la technologie que vous souhaitez utiliser pour écrire votre premier bot.

Actuellement, les langages suivants sont disponibles :

- [](python/python)
- [](js/js)
