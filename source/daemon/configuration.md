# ⚙️ Configuration

Le daemon Olvid est distribué sous forme [d'image Docker](https://hub.docker.com/r/olvid/bot-daemon).

Le comportement du conteneur Docker ainsi créé peut être configuré à l'aide de deux mécanismes :
- les variables d'environnement
- les options en ligne de commande

**Nous vous conseillons très fortement d'utiliser les variables d'environnement !**

Il existe deux moyens pour passer une variable d'environnement, selon que vous utilisez un fichier `docker-compose.yaml` ou la commande `docker run`.

:::{dropdown} **docker-compose.yaml**
:open:

```yaml
services:
  daemon:
    image: olvid/bot-daemon
    environment:
      - KEY=VALUE
```
:::

:::{dropdown} **docker run**

```shell
docker run -e KEY_VALUE olvid/bot-daemon
```
:::

Pour ajouter des options en ligne de commande, il faut modifier votre fichier ou votre commande comme suit.
:::{dropdown} **docker-compose.yaml**
:open:

```yaml
services:
  daemon:
    image: olvid/bot-daemon
    command: --key mySuperSecretKey
```
:::

:::{dropdown} **docker run**

```shell
docker run -e KEY_VALUE olvid/bot-daemon --key mySuperSecretKey
```
:::

# Options disponibles

## gRPC

Changer le port d'écoute gRPC.

*(par défaut : 50051)*

:::{dropdown} Environnement
:open:
```shell
DAEMON_PORT=8080
```
:::

:::{dropdown} CLI
```shell
-p, --port 8080
```
:::

## Logs

Changer la verbosité des logs.

*(défaut : INFO)*

:::{dropdown} Environnement
:open:
```sh
DAEMON_LOG_LEVEL=DEBUG|INFO|WARNING|ERROR  # daemon logs
ENGINE_LOG_LEVEL=DEBUG|INFO|WARNING|ERROR  # cryptographic engine logs
```
:::

## Clés client administrateur
### Créer
Il est possible de mettre en place une clé client administrateur temporaire (non sauvegardée en base de données).

Cela est nécessaire au moins pour la première connexion au daemon.

:::{dropdown} Environnement
:open:

Il est possible de créer plusieurs clés en ajoutant un suffixe à la variable *OLVID_ADMIN_CLIENT_KEY*.
```shell
OLVID_ADMIN_CLIENT_KEY=random-uuid
OLVID_ADMIN_CLIENT_KEY_OTHER=other-random-uuid
```
:::

:::{dropdown} CLI
```shell
-k, --key 00000000-0000-0000-0000-000000000000
```
:::

### Lister
Il est également possible de lister les clés client disponibles. Dans ce cas, le daemon affiche les clés et se termine.

:::{dropdown} CLI
:open:
```shell
-l, --list
```
:::

## TLS
Pour plus d'informations sur l'utilisation du TLS avec le daemon, rendez-vous dans notre section [](/daemon/tutorials.md#configuration-tls).

### TLS avec authentification serveur

Les deux éléments sont nécessaires.

:::{dropdown} Environnement
:open:
```shell
DAEMON_CERTIFICATE_FILE=server.pem
DAEMON_KEY_FILE=server.key
```
:::

:::{dropdown} CLI
```shell
--certificate-file server.pem
--key-file server.key
```
:::

### TLS avec authentification client
Les trois éléments sont nécessaires pour la mise en place de l'authentification client.

:::{dropdown} Environnement
:open:
```sh
--certificate-file server.pem
--key-file server.key
--root-file ca.pem
```
:::
:::{dropdown} CLI
```sh
DAEMON_CERTIFICATE_FILE=server.pem
DAEMON_KEY_FILE=server.key
DAEMON_ROOT_CERTIFICATE_FILE=ca.pem
```
:::

### Sauvegarde

#### Restaurer une sauvegarde

Pour restaurer une sauvegarde rendez-vous a la section: [](/daemon/tutorials.md#sauvegardes)

:::{dropdown} CLI
:open:
La restauration d'une sauvegarde peut être lancée avec l'option:
```shell
-r, --restore-backup backup-file-path.bytes
```
:::
