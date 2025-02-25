# {material-regular}`history;1em` CHANGELOG

:::{note}
Les versions sont synchronisées entre les versions de l'image Docker du [daemon](https://hub.docker.com/r/olvid/bot-daemon), du module Python [olvid-bot](https://pypi.org/project/olvid-bot/) et de l'image Docker [bot-python-runner](https://hub.docker.com/r/olvid/bot-python-runner).

Les versions suivent la sémantique suivante : MAJOR.MINOR.PATCH.
Tous les éléments sont supposés fonctionner ensemble dans la mesure où ils partagent la même version majeure et mineure.
Il est tout de même recommandé de toujours utiliser la même version de patch.

Les versions mineures et/ou majeures seront incrémentées à minima pour chaque changement dans l'API [gRPC-Protobuf](https://github.com/olvid-io/Olvid-Bot-Protobuf)
:::

## Dernière version : 1.3.0
Il est maintenant possible d'envoyer des messages de partage de position en continu 🗺️ !

### Ajouts
- **Daemon**
  - Ajout de l'envoi de partage de position dans le service `MessageCommand`, avec les méthodes *MessageStartLocationSharing*, *MessageUpdateLocationSharing* et *MessageUpdateLocationSharing*.
  - Ajout de la notification *MessageLocationSent* dans le service `MessageNotification` pour harmoniser l'API.
  - Modification du comportement des méthodes *MessageLocationSharingStart*, *MessageLocationSharingUpdate* et *MessageLocationSharingEnd* qui sont maintenant aussi émises pour les messages sortants.

- **CLI**
  - Ajout du groupe de commande `message location` avec les commandes:
    - `message location send`
    - `message location start`
    - `message location update`
    - `message location end`
  - Ajout de la commande `contact reset` (à utiliser prudemment !) pour résoudre certains blocages une identité et ses contacts.
  - Ajout de la commande `storage reset` pour supprimer toutes les entrées du stockage (dans le stockage global, et tous les stockages de discussion).  

### Correctif
- **Python Client**
  - tools.ChatBot: les messages d'aide étaient envoyés deux fois dans certaines conditions.
  - tools.SelfCleaningBot: les messages étaient tous supprimés au démarrage lorsque la fonction *is_message_for_cleaning* était renseignée.

## Version 1.2.0

### Ajouts
- **Daemon**
  - Ajout du service `KeycloakCommand` avec les méthodes *KeycloakUserList* et *KeycloakAddUserAsContact* afin de lister les utilisateurs présents sur Keycloak et de les ajouter en tant que contacts.
  (⚠️ Nécessite la version 4.1 ou supérieure du plugin Olvid pour Keycloak)
  - Ajout de la commande `downloadPhoto` pour les identités, les contacts et les groupes.
  - Ajout des notifications `photoUpdated` pour les contacts et les groupes.
  - Ajout des commandes `getBytesIdentifier` pour les identités, les contacts, les groupes et les discussions. Cela permet de les identifier de manière unique à long terme, même en cas de restauration de sauvegarde.
  - Ajout de la commande `getInvitationLink` pour les identités et les contacts (datatypes.Identity.invitation_link est maintenant marqué comme déprécié).
  - Ajout des champs *editedBody* et *forwarded* dans le message `datatypes.Message`

- **Python Client**
  - Ajout de la classe *tools.KeycloakAutoInvitationBot* pour ajouter automatiquement tous les nouveaux utilisateurs Keycloak à ses contacts.

- **CLI**
  - Implémentation des nouveaux points d'entrée du daemon dans les commandes suivantes :
    - `contact kc get/add` : *KeycloakCommandService*
    - `identity/contact/group photo save` : *downloadPhoto*
    - `identity/contact get -l` : *getInvitationLink*

### Corrections
- **Daemon**
  - Les champs *has_a_photo* n'étaient pas correctement remplis pour les contacts et les groupes.

- **CLI**
  - `storage get -f` : l'option n'était pas bien gérée.
  - `olvid-cli -k` affichait une erreur inutile.
  - `group get -f` : correction de la présentation.

## Version 1.1.0

### Ajouts

- **Daemon**
  - il est maintenant possible d'envoyer des messages de position à l'aide de la nouvelle méthode gRPC `messageSendLocation`. (implementé dans les clients et la CLI).
  - ajout de la possibilité de chiffrer les communications entre le daemon et les clients en utilisant du TLS. ([](/daemon/tutorials.md#configuration-tls))
  - possibilité d'ajouter des options personalisées a la JVM et notamment d'utiliser un proxy HTTP. ([](/daemon/tutorials.md#configuration-jvm)) 
- **Client Python**
  - ajout du sous-paquet `olvid.errors` pour gérer les exceptions de manière plus simple.

### Modifications

- **Client Python**: 
  - remplacement des variables d'environnement *DAEMON_HOSTNAME* et *DAEMON_PORT* par *DAEMON_TARGET*.
  - les fichiers *.client_key* et *.admin_client_key* sont dépréciés, utilisez un fichier `.env` à la place.
  - la classe `OlvidBot` est maintenant dépréciée, utilisez la classe `OlvidClient` à la place.
- **Docker**: 
  - la construction et la taille des images Docker [bot-daemon](https://hub.docker.com/r/olvid/bot-daemon) et [bot-python-runner](https://hub.docker.com/r/olvid/bot-python-runner) ont été grandement améliorées.

### Corrections

- **Client Python**:
  - `tools.SelfCleaningBot`: les paramètres `clean_inbound_messages` et `clean_outbound_messages` sont maintenant correctement gérés.

---

## Version 1.0.0

Version initiale du projet.
