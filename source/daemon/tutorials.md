# 👩‍🏫 Tutoriels

:::{contents}
:local:
:depth: 1
:::

## Déployer en production
Avant de déployer un bot ou un programme en production, nous vous conseillons très fortement de lire et de considérer les points suivants.

:::{danger}
Gardez absolument les points suivants à l'esprit.

- Le daemon et ses données sont extrêmement sensibles. Ils ont accès à l'ensemble des messages, des pièces jointes et bien plus.
Il vous appartient de faire le nécessaire pour que ces données soient correctement hébergées et protégées.
- Le trafic entre le daemon et ses clients n'est pas chiffré par défaut (voir [Chiffrement Tls](#configuration-tls)). Il ne doit en aucun cas être exposé.
- Sans [chiffrement TLS](#configuration-tls), les clés clientes ne servent qu'à compartimenter les appels API, et ne peuvent être utilisées à des fins d'authentification.
:::

## Creer un bot keycloak
:::{note}
Cette section ne s'adresse qu'aux clients qui ont un plugin Keycloak deployé 😬. 

Si vous ne savez pas ce que c'est vous pouvez cliquer 👉️ [ici](https://www.olvid.io/faq/olvid-management-console) 👈️ pour en apprendre plus sur cette fonctionalité premium.
:::

### Configurer un Bot Keycloak

Configurer un Bot Keycloak vous permet de le gérer comme l'un de vos utilisateurs standard Keycloak.
Il peut être ajouté ou supprimé des groupes, et les utilisateurs peuvent interagir avec le bot via l'onglet "Annuaire" dans leur application.
Cela facilite considérablement son intégration et son utilisation à grande échelle.

Les étapes suivantes nécessitent un accès à la console de gestion Olvid de votre Keycloak.

### Activer les bots dans Keycloak

:::{tip}
Cette étape n'est nécessaire que pour votre premier bot.
:::

Pour votre realm, si vous ne voyez pas le bouton "Bots" dans la barre latérale gauche, cliquez sur le bouton "Paramètres" de votre realm.

::::{grid}
:::{grid-item-card}
Bouton Bot
^^^

```{image} /_static/images/keycloak-bot-button.png
:alt: Bouton de paramètres du bot dans la console d'administration Keycloak
:align: center
```
:::

:::{grid-item-card}
Bouton Paramètres du realm
^^^
```{image} /_static/images/keycloak-settings-button.png
:alt: Bouton de paramètres du realm dans la console d'administration Keycloak
:align: center
```
:::
::::

Ensuite, dans les paramètres de votre realm, activez l'option "Activer les bots".

::::{grid}
:::{grid-item-card}
Activer les bots
^^^
```{image} /_static/images/keycloak-enable-bot-switch.png
:alt: Section des paramètres personnalisables dans la page de paramètres de votre realm.
:align: center
```
:::
::::

### Créer un nouveau Bot Keycloak

Accédez à la page "Bots" de votre Realm. Le bouton est situé dans le panneau latéral gauche.

::::{grid}
:::{grid-item-card}
Bouton Bots
^^^
```{image} /_static/images/keycloak-bot-button.png
:alt: Bouton de paramètres du bot dans la console d'administration Keycloak
:align: center
```
:::
::::

Lorsque vous êtes sur la page de gestion des bots, cliquez sur le bouton "Créer un bot" en haut à gauche.

::::{grid}
:::{grid-item-card}
Page de gestion des bots
^^^
```{image} /_static/images/keycloak-bots-management-page.png
:alt: Page de gestion des bots dans la console d'administration Keycloak.
:align: center
```
:::
::::

Cela affichera un formulaire à remplir avec le nom d'utilisateur et les détails d'identité de votre nouveau bot.

::::{grid}
:::{grid-item-card}
Formulaire de création du bot
^^^
```{image} /_static/images/keycloak-bot-creation-form.png
:alt: Formulaire pour créer un nouveau bot dans la console d'administration Keycloak.
:align: center
```
:::
::::

Lorsque vous avez validé le formulaire, un lien de configuration (commençant par `https://configuration.olvid.io/#`) sera affiché. Enregistrez ce lien pour les étapes suivantes.

:::{tip} Si vous avez perdu votre lien de configuration, vous pouvez le réinitialiser avec le bouton "Actualiser" dans la liste des bots.
:::

### Créer l'identité du bot

Lorsque vous disposez du lien de configuration, vous devrez utiliser la CLI. Cliquez [ici](/cli/cli.md) si vous ne vous souvenez pas comment l'utiliser.

:::{dropdown} {octicon}`command-palette;1em` Créer une nouvelle identité Keycloak
:open:

Démarrez la CLI et créez votre nouvelle identité en utilisant le lien de configuration. Elle générera automatiquement une clé client à passer à votre futur bot.

```shell
# create keycloak identity
0 > identity kc new https://configuration.olvid.io/#AAAAAAAAA.....
# client is automatically created
identity creation > Here is your client key to connect to daemon with this identity: 00000000-0000-0000-0000-000000000000
```
:::

:::{note}
Tous les utilisateurs Keycloak peuvent maintenant découvrir et interagir avec votre bot via leur bouton "Annuaire" dans l'application Olvid.

Vous pouvez également gérer votre bot à partir de la console d'administration !
:::

## Configuration SSL

:::{versionadded} 1.4.1
:::

### Configuration du Daemon
Voici un exemple de configuration nginx pour mettre en place un daemon derrière un reverse-proxy HTTP.
Vous pouvez ensuite installer un certificat letsencrypt à l'aide de la commande `certbot` afin d'utiliser le protocole HTTPS.

::: {include} /_static/code/grpc-reverse-proxy.conf
   :code: nginx
:::

Fichier téléchargeable ici:
{download}`grpc-reverse-proxy.conf </_static/code/grpc-reverse-proxy.conf>`

:::{important}
Si le daemon utilise également du chiffrement [TLS](#configuration-tls) remplacer **grpc://** par **grpcs://** dans la directive gprc_pass.
:::

### Configuration du Client Python
Pour se connecter à un daemon en utilisant https, il suffit d'utiliser le préfixe `https://` dans la valeur de la variable d'environnement *OLVID_DAEMON_URL*.

### Configuration du Client Javascript
Pour se connecter à un daemon en utilisant https, il suffit d'utiliser le préfixe `https://` dans la valeur de la variable d'environnement *OLVID_DAEMON_URL*.

## Configuration TLS

:::{versionadded} 1.0.1
:::

Nativement gRPC prend en charge le chiffrement TLS. Nous pouvons distinguer deux modes :

- [](#authentification-serveur) : Le daemon utilise son propre certificat auto-signé et sa clé privée associée. 
Les clients utiliseront ce certificat pour chiffrer les communications avec le daemon.
- [](#authentification-client) : On crée notre propre Autorité de Certification (CA). 
On peut ainsi créer un certificat et une clé privée pour le daemon et un par client.
Ainsi, les clients peuvent chiffrer les communications avec le daemon, et le daemon peut vérifier que les clients ont été autorisés à se connecter.

### Authentification serveur
#### Configuration du Daemon

Dans un premier temps, on génère le certificat et la cle privée du serveur à l'aide de la commande `openssl`. 

:::{important}
Remplacez `localhost` par le nom d'hôte de votre daemon. Le nom d'hôte est l'adresse IP ou le nom de domaine que les clients utiliseront pour établir une connexion avec le daemon.
:::

```shell
openssl req -x509 -newkey rsa:4096 -keyout server.key \
    -days 36500 -out server.pem -nodes -subj '/CN=localhost'
```

Si vous utilisez Docker, créez un répertoire *credentials* contenant le certificat et la clé générés précédemment.
Ajoutez ce répertoire en tant que volume en lecture seule et utilisez une variable d'environnement pour activer l'authentification TLS simple dans le daemon.

On utilise les variables d'environnement suivantes pour configurer le daemon :
- `DAEMON_CERTIFICATE_FILE`
- `DAEMON_KEY_FILE`

Ce qui nous donne un fichier `docker-compose.yaml` similaire à celui-ci.

```{code-block} yaml
  :substitutions:
daemon:
  image: olvid/bot-daemon::{{docker_version}}
  environment:
    - OLVID_ADMIN_CLIENT_KEY_CLI=ToSet
    - DAEMON_CERTIFICATE_FILE=./credentials/server.pem
    - DAEMON_KEY_FILE=./credentials/server.key
  ports:
    - 50051:50051
  restart: unless-stopped
  volumes:
    - ./data:/daemon/data
    - ./backups:/daemon/backups
    - ./credentials:/daemon/credentials:ro
```

#### Configuration du Client Python

Pour assurer le chiffrement des communications, votre bot a besoin du certificat du daemon.

On suppose que vous avez un répertoire **credentials** contenant le fichier `server.pem` généré précédemment.
Il existe plusieurs moyens de faire en sorte que votre *client* utilise ce fichier pour authentifier le daemon et chiffrer le traffic.

:::{dropdown} {material-regular}`settings;1em` Environnement
:open:

Configurez la variable d'environnement dans votre fichier *docker-compose.yaml*, dans votre commande docker ou votre environnement local.

```shell
OLVID_SERVER_CERTIFICATE_PATH=./credentials/server.pem
```

N'importe quel sous-classe de la classe **OlvidClient** chargera automatiquement la configuration TLS.
:::

:::{dropdown} {material-regular}`settings;1em` Fichiers
Au démarrage les sous-classes de la classe **OlvidClient** cherchent des noms de fichiers spécifiques pour charger les configurations TLS.
Si un fichier *.server.pem* existe il sera automatiquement utilisé pour configurer le TLS. 

```shell
ln -s ./credentials/server.pem .server.pem
```
:::

:::{dropdown} {material-regular}`settings;1em` Code
Vous pouvez également configurer manuellement les certificats et clés à utiliser dans votre code Python.

Dans ce cas, il faut créer un object **GrpcSimpleTlsConfiguration** et le passer en tant que *tls_configuration* à la creation du client. 

```python
import asyncio
from olvid import OlvidClient

async def main():
    client = OlvidClient(tls_configuration=OlvidClient.GrpcSimpleTlsConfiguration(
            server_certificate_path="./credentials/server.pem"
    ))
    print(await client.identity_get())

asyncio.set_event_loop(asyncio.get_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```
:::

#### Configuration du Client Javascript
Actuellement notre implementation de [](/js/js) ne supporte pas nativement l'utilisation du protocole TLS.

### Authentification client

#### Génération des certificats

Nous vous recommandons de créer un répertoire **credentials** et d'exécuter les commandes suivantes depuis celui-ci.

:::{note}
Pour générer le CA et le certificat serveur, vous aurez besoin de ces deux modèles openssl.
Téléchargez-les ou créez-les dans votre répertoire de travail actuel.

- {download}`ca-openssl.cnf </_static/code/ca-openssl.cnf>`
- {download}`server-openssl.cnf </_static/code/server-openssl.cnf>`
:::


:::{card}
**Génération de notre autorité de certification locale (CA)**
^^^
```shell
# you can leave default values
openssl req -x509 -new -newkey rsa:2048 -nodes -keyout ca.key -out ca.pem \
  -config ca-openssl.cnf -days 36500 -extensions v3_req
```
:::

:::{card}
**Génération du certificat et la clé serveur.**
^^^
{material-outlined}`warning;1em;sd-text-danger` Remplacez `localhost` par le nom d'hôte de votre daemon.
Le nom d'hôte correspond à l'adresse IP ou le nom de domaine que les clients utiliseront pour établir une connexion avec le daemon.

```shell
# generate server private key
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out server.key
# generate server certificate
openssl req -new -key server.key -out server.csr -config server-openssl.cnf \
    -subj '/CN=localhost'
openssl x509 -req -CA ca.pem -CAkey ca.key -CAcreateserial -in server.csr \
  -out server.pem -extensions v3_req -extfile server-openssl.cnf -days 36500
```
:::

:::{card}
**Génération d'un certificat et d'une clé privée pour un client**
^^^

```shell
# generate client private key
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out client.key

# generate client certificate request (leave default values)
openssl req -new -key client.key -out client.csr
openssl x509 -req -CA ca.pem -CAkey ca.key -CAcreateserial -in client.csr \
  -out client.pem -days 36500
```
:::

#### Configuration du Daemon
Le daemon aura besoin de son certificat, de sa clé privée et du CA pour vérifier que les clients sont autorisés à se connecter.
Nous allons utiliser trois variables d'environnement pour spécifier les chemins des fichiers :

- `DAEMON_CERTIFICATE_FILE`
- `DAEMON_KEY_FILE`
- `DAEMON_ROOT_CERTIFICATE_FILE`

Créez un répertoire **credentials** et copiez-y les fichiers générés précédemment.

Ce qui nous donne un fichier *docker-compose.yaml* similaire à celui-ci.

```{code-block} yaml
  :substitutions:
daemon:
  image: olvid/bot-daemon:{{docker_version}}
  environment:
    - OLVID_ADMIN_CLIENT_KEY_CLI=ToSet
    - DAEMON_CERTIFICATE_FILE=./credentials/server.pem
    - DAEMON_KEY_FILE=./credentials/server.key
    - DAEMON_ROOT_CERTIFICATE_FILE=./credentials/ca.pem
  ports:
    - 50051:50051
  restart: unless-stopped
  volumes:
    - ./data:/daemon/data
    - ./backups:/daemon/backups
    - ./credentials:/daemon/credentials:ro
```

#### Configuration du Client Python

Pour configurer le client, vous pouvez utiliser l'une des méthodes suivantes :

:::{dropdown} {material-regular}`settings;1em` Environnement
:open:
Configurez les variables d’environnement suivantes dans votre fichier docker-compose.yaml, dans votre commande docker ou votre environnement local.
```shell
OLVID_CLIENT_TLS_CERTIFICATE_FILE=./credentials/client.pem
OLVID_CLIENT_TLS_KEY_FILE=./credentials/client.key
OLVID_CLIENT_TLS_CA_FILE=./credentials/ca.pem
```
N’importe quel sous-classe de la classe OlvidClient chargera automatiquement la configuration TLS.
:::

:::{dropdown} {material-regular}`settings;1em` Fichiers
Au démarrage les sous-classes de la classe **OlvidClient** cherchent des noms de fichiers spécifiques pour charger les configurations TLS.
Si elle trouve les trois fichiers suivants, ils seront automatiquement utilisé pour configurer le TLS. 
- *.ca.pem*
- *.client.pem*
- *.client.key*

```shell
ln -s ./credentials/ca.pem .ca.pem
ln -s ./credentials/client.pem .client.pem
ln -s ./credentials/client.key .client.key
```
:::

:::{dropdown} {material-regular}`settings;1em` Code
Vous pouvez également configurer manuellement les certificats et clés à utiliser dans votre code Python.
Dans ce cas il faut créer un objet **GrpcMutualAuthTlsConfiguration** et le passer en tant que paramètre **tls_configuration** au constructeur d'une sous-classe **OlvidClient**.

```python
import asyncio
from olvid import OlvidClient

async def main():
    client = OlvidClient(tls_configuration=OlvidClient.GrpcMutualAuthTlsConfiguration(
            root_certificate_path="/path/to/ca.pem",
            certificate_chain_path="/path/to/client.pem",
            private_key_path="/path/to/client.key"
    ))
    print(await client.identity_get())

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```
:::

#### Configuration du Client Javascript
Actuellement notre implementation de [](/js/js) ne supporte pas nativement l'utilisation du protocole TLS.

## Sauvegardes
Dans vos projets, le daemon est un élément central, c'est là où toutes les données sont stockées.
En réalité, les données que vous manipulez (identités, messages, ...) ne constituent qu'une petite partie des données gérées par le daemon.
Ce sont ces donnée invisibles qui doivent être sauvegardées, car elles permettent un échange sécurisé avec les contacts du bot.

### Avertissements

:::{danger}
Veuillez examiner attentivement les recommandations et avertissements suivants avant de continuer.

- Les sauvegardes contiennent des données sensibles équivalentes au répertoire de données du daemon.
Il est impératif de les manipuler avec la même rigueur et niveau de sécurité.
- Les sauvegardes mentionnées ici sont des sauvegardes Olvid, qui ne contiennent pas de messages ou de pièces jointes
Ces sauvegardes vous permettent de restaurer votre carnet d'adresses, vos groupes et votre stockage, mais pas le contenu des discussions (messages et pièces jointes).
- Les sauvegardes sont... des sauvegardes. Vous devrez les conserver dans un endroit sûr pour pouvoir les réutiliser si nécessaire.
- La restauration d'une sauvegarde sur un autre daemon et l'exécution simultanée sur l'ancienne instance entraînera un comportement imprévisible.
:::

### Configuration des sauvegardes automatiques

Le daemon crée automatiquement des sauvegardes chaque fois que cela est nécessaire (votre bot a ajouté un contact, rejoint ou quitte un groupe, ...).
Ces sauvegardes sont stockées sur un serveur Olvid, et sont accessibles à l'aide d'une clé. Cette clé est accessible à l'aide de la commande cli `backup key get`.

La clé de sauvegarde est également stockée dans le dossier */daemon/backups*. Vous pouvez accéder au fichier en montant le répertoire */daemon/backups* en tant que volume.
Voici un exemple de fichier *docker-compose.yaml*.

```{code-block} yaml
  :substitutions:
services:
  daemon:
    image: olvid/bot-daemon:{{docker_version}}
    volumes:
      - ./data:/daemon/data
      - ./backups:/daemon/backups
```

### Validation d'une sauvegarde
Pour valider le fonctionnement des sauvegardes vous pouvez accéder au contenu de votre sauvegarde à l'aide de la [CLI](/cli/cli) et de la commande `backup get $BACKUP_KEY`, en remplaçant *$BACKUP_KEY* par votre clé de sauvegarde.

### Restauration d'une sauvegarde

:::{danger}
La restauration d'une sauvegarde n'est pas une action triviale et ne doit être effectuée qu'en dernier recours.
Vous perdrez tous vos messages et pièces jointes stockés dans le daemon au cours de ce processus.
Seuls les éléments enregistrés à l'aide de l'API de stockage, les clés client et les settings seront encore disponibles.
:::

Une procédure de restauration de sauvegarde classique devrait se faire comme suit.
- Valider que le daemon d'origine ne tourne plus
- Dans la nouvelle installation exécuter la commande [CLI](/cli/cli) suivante: `backup restore daemon $BACKUP_KEY`.
- Valider la restauration des identités à l'aide de la commande cli: `identity get`

### Commandes utiles
Voici une liste non-exhaustive de commandes [CLI](/cli/cli) en lien avec les sauvegardes. 
- `backup key get`: afficher la clé de sauvegarde actuelle.
- `backup now`: forcer le lancement d'une sauvegarde.
- `backup get $BACKUP_KEY`: affiche le contenu d'une sauvegarde

- `backup restore daemon $BACKUP_KEY`: restaurer la totalité d'une sauvegarde dans son état le plus récent.
- `backup restore admin $BACKUP_KEY`: restaure les clés clients administrateur et le stockage associé.
- `backup restore admin $BACKUP_KEY $SNAPHOST_ID`: restaure une identité en particulier, à un état (snapshot) donné (contact, groupes, stockage, clé clients, settings). Les identifiants des snapshots sont disponibles dans la description des sauvegardes. 

## Configuration JVM
:::{versionadded} 1.0.1
:::

Il est possible de passer des options arbitraires à la JVM qui fait tourner votre daemon.
Pour cela, vous pouvez utiliser la variable d'environnement **JAVA_FLAGS**.

### Configuration proxy
Pour permettre au daemon d'utiliser un proxy HTTP, il faut passer des paramètres spécifiques a la JVM. (cf: [Proxy Properties](https://docs.oracle.com/en/java/javase/21/core/java-networking.html#GUID-2C88D6BD-F278-4BD5-B0E5-F39B2BFAA840)).

Voici un exemple de configuration possible pour utiliser un proxy fictif accessible en tant que *proxy.example.com* sur le port 8000, avec usage d'un login et mot de passe. Cette configuration est adaptable à vos besoins. 

```shell
JAVA_FLAGS=-Dhttps.proxyHost=proxy.example.com -Dhttps.proxyPort=8000 -Dhttp.proxyUser=username -Dhttp.proxyPassword=password
```
