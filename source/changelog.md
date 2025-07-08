# {material-regular}`history;1em` CHANGELOG

:::{note}
Les versions sont synchronisées entre les versions de l'image Docker du [daemon](https://hub.docker.com/r/olvid/bot-daemon), du module Python [olvid-bot](https://pypi.org/project/olvid-bot/) et de l'image Docker [bot-python-runner](https://hub.docker.com/r/olvid/bot-python-runner).

Les versions suivent la sémantique suivante : MAJOR.MINOR.PATCH.
Tous les éléments sont supposés fonctionner ensemble dans la mesure où ils partagent la même version majeure et mineure.
Il est tout de même recommandé de toujours utiliser la même version de patch.

Les versions mineures et/ou majeures seront incrémentées à minima pour chaque changement dans l'API [gRPC-Protobuf](https://github.com/olvid-io/Olvid-Bot-Protobuf)
:::

## Dernière version : 1.5.0
### Nouveautés
Trois nouveaux modules sont maintenant officiellement supportés :
- **[@olvid/bot-node](https://www.npmjs.com/package/@olvid/bot-node)**: un module npm écrit en typescript qui vous permet de développer des bots et des scripts en Typescript ou Node.js.
  (cf: [](/js/js.md))
- **[@olvid/bot-web](https://www.npmjs.com/package/@olvid/bot-web)**: une version arrangée du module précédent qui peut tourner dans un navigateur web pour créer des pages web ou des applications métier qui intéragissent avec Olvid.
  (cf: [](/js/browser.md))
- **[n8n-nodes-olvid](https://www.npmjs.com/package/n8n-nodes-olvid)**: le noeud Olvid est maintenant disponible dans n8n en tant que noeud communautaire. Intégrer facilement Olvid avec des services extérieurs dans des workflow no-code.
  (cf: [](/n8n/n8n.md))

### Ajouts
- **Daemon**
  - Ajout du service tool et la command ping. Il s'agit d'un point non authentifié qui permet juste de vérifier que la connection au daemon est possible.

### Correctifs
- **Daemon**
  - La notification MessageDeletedNotification était envoyée deux fois dans le cas oú un message était supprimé à distance
  - *MessageNotificationService*: il n'était pas possible de filtrer certaines notifications par *messageId* pour des messages entrants. (*messageBodyUpdated*, *messageReactionAdded*, ...) 
  - *MessageCommandService*: Il n'est plus possible de répondre à un message d'une autre discussion 

-----

## Version: 1.4.1
### Ajouts
- **Daemon**
  - il est maintenant possible de se connecter à un daemon en utilisant une connection https. La mise en place est documentée ici: [](daemon/tutorials.md#configuration-ssl).

- **Python Client**
  - **tools.AutoInvitationBot**: il est maintenant possible de choisir les types d'invitation à accepter (invitation de groupe, présentations, ...).

### Correctifs
- **Daemon**
  - TLS: changement de la JVM utilisée dans l'image docker. La précédente plantait lors de la mise en place du chiffrement TLS.  
  - Correctifs divers

## Version : 1.4.0

### Nouveautés
- **Filtrage des Notifications**: Il est maintenant possible d'utiliser des paramètres au moment de l'abonnement à un type de notifications. 
Dans ce cas seules les notifications en accord avec ces paramètres (filtre, compteur ...) seront envoyées au client.
- **Gestion minimaliste des appels**: Il est maintenant possible de démarrer des appels avec un/plusieurs contacts ou dans une discussion et de s'abonner aux événements en lien avec cet appel (quelqu'un a décroché, quelqu'un est déjà en communication ...)

### Ajouts
- **Daemon**
  - **Filtrage des Notifications**: ajout de paramètres à toutes les méthodes du service de notifications, notamment des filtres et un compteur. Ces paramètres sont tous optionnels et donc rétro compatible.
  - **Gestion minimaliste des appels**: Ajout des services gRPC CallCommandService et CallNotificationService
    - commandes: *CallStartDiscussionCall*, *CallStartCustomCall*
    - notifications: *CallIncoming*, *CallRinging*, *CallAccepted*, *CallDeclined*, *CallBusy*, *CallEnded*.
    - datatypes: *Call*

- **CLI**: 
  - ajout de la commande `call start` pour commencer un appel en utilisant la nouvelle API d'appel (la command `message voip` est maintenant dépréciée).
  - ajout de l'option `-i` aux commandes `identity get` et `contact get` pour afficher l'identifiant en bytes.

### Correctifs
- **Daemon**
  - Changement dans l'envoi de notifications
    - *ContactNewNotification*: est maintenant envoyée la première fois qu'un contact est ajouté (indépendamment de son status one-to-one). La notification est envoyé après qu'un canal sécurisé a été établie et les capabilities du contact aient été téléchargées.
    - *DiscussionNewNotification*: est toujours envoyée quand une discussion est crée ou qu'elle passe du status Locked à Unlocked (retour dans un groupe, passage en one to one d'un contact).
    - *MessageReceivedNotification* et *AttachmentReceivedNotification*: sont maintenant envoyées en même temps, lorsque le message et toute les pièces jointes ont été correctement écrites en base de données. (résout les problèmes de listing des pièces jointes qui viennent d'arriver).
    - Corrections diverses de notifications qui pouvaient être envoyées deux fois
  - `datatypes.ReactionFilter`: changement de nom, le champs `reaction` devient `has_reaction`

- **CLI**
  - `identity get -l`: la commande renvoyait toujours le lien d'invitation de la première identité.

- **Python Client**
  - tools.SelfCleaningBot: les messages pouvaient être supprimés à tort lorsque la fonction *is_message_for_cleaning* était renseignée.

## Version : 1.3.0

### Nouveautés
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
