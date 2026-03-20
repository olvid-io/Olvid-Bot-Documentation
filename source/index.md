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
n8n/n8n
openclaw/openclaw
cli/cli
daemon/daemon
references/datatypes
glossary
changelog
migrations/migration_1_2
```

# 🚀 Quickstart

Bienvenue dans la documentation des bots Olvid !

Nous avons conçu cet ensemble d'outils pour vous permettre de créer vos propres chatbots et intégrations pour l'application [Olvid](https://olvid.io/faq/bots-olvid/), tout en conservant ses standards de sécurité maximale.

Nous vous recommandons de commencer par notre procédure [d'installation](#installation).
Elle vous permettra d'installer et configurer votre propre daemon Olvid.
Ce daemon peut être vu comme une application Olvid pilotable par l'intermédiaire d'une API gRPC.

Une fois l'installation effectuée, vous pourrez commencer à écrire le code de vos premiers clients, afin d'interagir et de commander le profil Olvid que vous aurez créé sur le daemon.

%todo todel
:::{note}
Cette documentation est toujours en cours d'écriture. Si quelque chose vous semble incorrect, mal écrit ou peu clair, vous pouvez :
- créer une issue et/ou ouvrir une pull request en cliquant sur le bouton GitHub disponible dans la barre supérieure.
- nous contacter par mail : [bot@olvid.io](mailto:bot@olvid.io)
:::

# Installation
## Prérequis

Pour suivre cette procédure, vous aurez besoin que Docker soit installé sur votre machine.
La procédure d'installation est disponible ici : [Installer Docker](https://docs.docker.com/engine/install/).

## Infrastructure

Nous allons utiliser un fichier Docker Compose pour configurer et lancer notre infrastructure.

Vous pouvez copier le contenu suivant dans un fichier nommé `docker-compose.yaml`.

```{code-block} yaml
  :substitutions:
services:
  daemon:
    image: olvid/bot-daemon:{{docker_version}}
    environment:
      - OLVID_ADMIN_CLIENT_KEY_CLI=SetARandomValue
    ports:
      - 50051:50051
    volumes:
      - ./data:/daemon/data
  cli:
    image: olvid/bot-python-runner:{{docker_version}}
    entrypoint: "olvid-cli"
    environment:
      - OLVID_ADMIN_CLIENT_KEY=SetARandomValue
      - OLVID_DAEMON_URL=http://daemon:50051
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

L'interface en ligne de commande d'Olvid (CLI) permet de se connecter directement au daemon et lui envoyer manuellement des commandes.
On l'utilise, a minima, pour créer notre identité Olvid et entrer en contact avec elle.
Mais elle pourra également servir plus tard pour débugger nos programmes ou déclencher manuellement des actions.

Pour lancer la CLI en mode interactif, on utilisera la commande suivante :

```shell
docker compose run --rm cli
```

Un nouveau prompt s'affiche désormais. Le nombre affiché correspond à l'identifiant de l'identité actuellement utilisée.
Dans notre cas, il affiche 0 car nous n'avons pas encore d'identité sur le daemon.
Pour plus d'informations, rendez-vous dans la section [](/cli/cli).

Pour créer notre première identité, nous allons utiliser la commande `identity new`.
Voici un exemple complet et commenté du déroulement de cette commande.

% TODO change this ... screen ...
% TODO translate comments if we do not change this
```shell
# Create a new identity. Replace FirstName, LastName, ... with expected values
# LastName, Position and Company are optionals and these details can be updated later.
0 > identity new FirstName LastName Position Company

# A client key to connect to daemon is automatically created
# Save it somewhere, you will need it to write your bots.
identity creation > Here is your client key to connect to daemon with this identity:
AAAAAAAA-BBBB-AAAA-AAAA-AAAAAAAAAAAA

# Enter "yes" to get in touch with this new identity with your personal identity in Olvid.
# This step is optional but necessary if you want to create a discussion with your bot.
identity creation > Do you want to add this identity to your contacts ? (y/N)
>yes

# This is your Bot invitation link
# You can open it in you web browser to show the QR to scan with your mobile application
# You can also copy it to import it in your desktop client.
identity creation > Send an invitation to this invitation link: https://invitation.olvid.io/#........

# The CLI is now waiting for your invitation to arrive
# When your invitation arrive process restarts 
identity creation > Please enter sas code displayed on the other device

# Enter 4 digits code shown in your Olvid Application 
> 0000

# Enter code shown in your Olvid Application
identity creation > Please enter this sas code on the other device: 1111

# Process is now finished
Now using identity: 1
You can now send messages to YOUR NAME in discussion 1

# You can send a test message with this command
1 > message send 1 Hello World !

# to leave interactive mode use CTRL + D or exit command
1 > exit
```

## Premier programme

Vous disposez maintenant d'une infrastructure fonctionnelle, avec un daemon hébergeant une identité Olvid.
Vous pouvez utiliser l'API gRPC du daemon pour contrôler cette identité.

Pour continuer, il vous faut choisir la technologie que vous souhaitez utiliser pour écrire votre premier bot.

Actuellement, les langages suivants sont disponibles :

- [](python/python)
- [](js/js)

Vous pouvez également mettre en place votre propre [instance N8N](n8n/n8n.md) pour réaliser des bots sans code.
