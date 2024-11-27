# {material-regular}`history;1em` CHANGELOG

:::{note}
Les versions sont synchronisées entre les versions de l'image Docker du [daemon](https://hub.docker.com/r/olvid/bot-daemon), du module Python [olvid-bot](https://pypi.org/project/olvid-bot/) et de l'image Docker [bot-python-runner](https://hub.docker.com/r/olvid/bot-python-runner).

Les versions suivent la sémantique suivante : MAJOR.MINOR.PATCH.
Tous les éléments sont supposés fonctionner ensemble dans la mesure où ils partagent la même version majeure et mineure.
Il est tout de même recommandé de toujours utiliser la même version de patch.

Les versions mineures et/ou majeures seront incrémentées à minima pour chaque changement dans l'API [gRPC-Protobuf](https://github.com/olvid-io/Olvid-Bot-Protobuf)
:::

## Dernière version : 1.1.0

### Ajouts

- **API**
  - il est maintenant possible d'envoyer des messages de position à l'aide de la nouvelle méthode gRPC `messageSendLocation`. (implementé dans les clients et la CLI).
- **Daemon**
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
