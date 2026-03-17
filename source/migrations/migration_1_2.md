# ➡️ Migrations

## Passage en V2

:::{note}
Cette page référence tous les changements non rétrocompatibles apportés par la version 2 du framework. 
Il est important de la lire intégralement pour mettre à jour vos configurations et votre code lors de la mise à jour des différents outils
d'une version 1.X.X vers une version 2.0.0 ou supérieure.
:::

[//]: # (TODO add references to already migrated bots)
[//]: # (TODO add somewhere a way to create a community: write us, ask us, ...)

### Python
#### OlvidClient
##### Configuration
La configuration des différents clients Olvid a été normalisées.
Cela peut induire des changements dans les variables d'environnement des fichiers *docker-compose.yaml*, dans les fichiers *.env*, ou dans l'instanciation des classes *OlvidClient* et *OlvidAdminClient*. 

- Les variables d'environnement *DAEMON_HOSTNAME*, *DAEMON_PORT* et *OLVID_DAEMON_TARGET* ont été supprimées au profit de la variable *OLVID_DAEMON_URL*.
  La nouvelle variable correspond à l'URL complète d'accès au daemon.

```dotenv
OLVID_DAEMON_URL=http://daemon:50051
```

:::{note}
L'attribut d'OlvidClient *daemon_target* a également été renommé *daemon_url*.  
:::

- Les fichiers de configuration *.client_key* et *.admin_client_key* ne sont plus supportés, utilisez un fichier *.env* à la place, avec les variables suivantes:
```{code-block} dotenv
OLVID_CLIENT_KEY=00000000-0000-0000-0000-000000000000
OLVID_ADMIN_CLIENT_KEY=00000000-0000-0000-0000-000000000000
```

##### Méthodes
- les méthodes *add_command* et *remove_command* sont supprimées et remplacées par *add_listener* et *remove_listener*.
```python
from olvid import OlvidClient, datatypes, listeners

async def help_cmd(message: datatypes.Message):
    await client.message_send(discussion_id=message.discussion_id, body="Help")

client: OlvidClient = OlvidClient()
client.add_listener(listeners.Command(handler=help_cmd, regexp_filter="!help"))
```
- normalisation des noms de méthodes qui utilisent des fichiers, impliquant le renommage de certaines méthodes.
```python
from olvid import OlvidClient, datatypes, listeners

client: OlvidClient = OlvidClient()

async def change_identity_photo(photo_path: str):
    await client.identity_set_photo_file(file_path=photo_path)

async def change_group_photo(group_id: int, photo_path: str):
    await client.group_set_photo_file(group_id=group_id, file_path=photo_path)
```

#### OlvidBot
Les classes *OlvidBot* et *OlvidClient* ont été fusionnées, vous pouvez remplacer tous les usages de la classe *OlvidBot* par *OlvidClient*.
```python
from olvid import OlvidClient, datatypes

class Bot(OlvidClient):
    @OlvidClient.command("!help")
    async def help_cmd(self, message: datatypes.Message):
        await self.message_send(discussion_id=message.discussion_id, body="Help")
```

#### datatypes
Certaines méthodes associées aux objets du module `datatypes` prennent maintenant une instance de la classe *OlvidClient* en paramètre. 
Voici quelque exemples **NON EXHAUSTIFS** de changements.

```python
from olvid import OlvidClient, datatypes

class Bot(OlvidClient):
    async def on_message_received(self, message: datatypes.Message):
        await message.reply(client=self, body=f"**{message.body}**")
        await message.react(client=self, reaction="🪿") 
    
    async def on_discussion_new(self, discussion: datatypes.Discussion):
        await discussion.post_message(client=self, body="Welcome !")
```

#### tools
Suppression des classes *tools.AutoInvitationBot*, tools.DiscussionRetentionPolicyBot, tools.SelfCleaningBot et tools.KeycloakAutoInvitationBot.  
La classe OlvidClient embarque maintenant des méthodes permettant de paramètrer le comportement du daemon. 

```python
from olvid import OlvidClient

async def main():
    client = OlvidClient()
    # replace tools.AutoInvitationBot()
    # accept any invitation
    await client.enable_auto_invitation(accept_all=True)

    # replace tools.SelfCleaningBot() and/or tools.DiscussionRetentionPolicyBot()
    # keep only 20 messages by discussion, delete messages older than one day and delete messages in locked discussions
    await client.set_message_retention_policy(existence_duration=60*60*24, discussion_count=20, clean_locked_discussions=True)

    # replace tools.KeycloakAutoInvitationBot()
    # for keycloak bots only: invite every new user on your keycloak instance
    await client.enable_keycloak_auto_invite(auto_invite_new_members=True)
```

#### Listeners
La notion de listeners a évolué pour utiliser le mécanisme de filtrage des notifications sorti dans la version 1.4.0.
Les changements suivants découlent de cette volonté de normalisation avec les autres clients.  
Pour en savoir plus sur l'usage des listeners rendez-vous ici: [](/python/tutorials.md#listener).
- suppression de la notion de *checkers*, utilisez les filtres à la place. 
- suppression du paramètre *priority*.
- le paramètre *count* est maintenant strictement positif, il faut maintenant utiliser la valeur 0 pour avoir un listener infini (et plus -1). 

### Javascript
#### Configuration
La configuration des différents clients Olvid a été normalisées.
Cela peut induire des changements dans les variables d'environnement des fichiers *docker-compose.yaml*, dans les fichiers *.env*, ou dans l'instanciation des classes *OlvidClient* et *OlvidAdminClient*.
- La variable d'environnement *OLVID_DAEMON_TARGET* ont été remplacée par la variable *OLVID_DAEMON_URL*. La nouvelle variable correspond à l'URL complète d'accès au daemon.

```dotenv
OLVID_DAEMON_URL=http://daemon:50051
```

:::{note}
L'attribut d'OlvidClient *serverUrl* a également été renommé *daemonUrl*.  
:::

#### Protobuf
La version de la librairie protobuf a été mise à jour dans les paquet npm *@olvid/bot-node* et *@olvid/bot-web*. Cela a un impact sur l'usage du code généré.
Pour en savoir plus sur ces changements rendez-vous sur le guide de migration de [bufbuild](https://blog.bufbuild.ru/protobuf-es-v2/).

Le changement principal concerne la création de nouveaux objets protobuf
```{code-block} node
import {OlvidClient} from "@olvid/bot-node";
import {create} from "@bufbuild/protobuf";

let messageFilter = create(datatypes.MessageFilterSchema, {location: datatypes.MessageFilter_Location.HAVE})}
```


#### tools
Suppression des classes *tools.AutoInvitationBot*, tools.DiscussionRetentionPolicyBot, tools.SelfCleaningBot et tools.KeycloakAutoInvitationBot.  
La classe OlvidClient embarque maintenant des méthodes permettant de paramètrer le comportement du daemon. 

```python
from olvid import OlvidClient

async def main():
    client = OlvidClient()
    # replace tools.AutoInvitationBot()
    # accept any invitation
    await client.enable_auto_invitation(accept_all=True)

    # replace tools.SelfCleaningBot() and/or tools.DiscussionRetentionPolicyBot()
    # keep only 20 messages by discussion, delete messages older than one day and delete messages in locked discussions
    await client.set_message_retention_policy(existence_duration=60*60*24, discussion_count=20, clean_locked_discussions=True)

    # replace tools.KeycloakAutoInvitationBot()
    # for keycloak bots only: invite every new user on your keycloak instance
    await client.enable_keycloak_auto_invite(auto_invite_new_members=True)
```

#### datatypes
Les méthodes raccourcies associées aux objets du module `datatypes` ont été déplacé dans un module `helpers` indépendant.
Voici deux exemples avec la méthode *Message.reply* et *Discussion.postMessage*, mais ce ne sont **pas les seules** méthodes impactées.

```typescript
import {OlvidClient, datatypes, helpers, onMessageReceived, onDiscussionNew} from "@olvid/bot-node";

class ExampleBot extends OlvidClient {
    @onMessageReceived()
    async messageReceived(message: datatypes.Message) {
        // replace: await message.reply(this, "pong")
        await helpers.message.reply(this, message,  "pong")
    }

    @onDiscussionNew()
    async discussionNew(discussion: datatypes.Discussion) {
        // replace: await discussion.postMessage(this, "Welcome !")
        await helpers.discussion.postMessage(this, discussion,  "Welcome!")
    }
}
```

### Daemon
Les changements suivants dans l'API du daemon peuvent toucher tous les clients. Il faut donc vérifier pour chaque modification si votre code est concerné.

#### Sauvegardes
La version 2 amène le nouveau système de sauvegarde Olvid.
Les backups sont maintenant stockés sur notre serveur et il vous suffit de stocker la clé de chiffrement associée pour récupérer ou transférer tout ou partie de votre daemon.

Comme dans la v1 le dossier `backups` du daemon contient tout le nécessaire à la restauration d'une sauvegarde,
si vous sauvegardiez déjà son contenu aucun changement ne devrait être nécessaire, mais nous vous conseillons tout de même de vérifier que tout se passe bien.

Pour en savoir plus sur la mise en place des sauvegardes: [](/daemon/tutorials.md#sauvegardes).

#### Commandes

##### MessageCommandeService
- **messageSendVoip**: Suppression de la commande, utilisez le service callCommandService à la place.
```python
from olvid import OlvidClient

client = OlvidClient()
async def call(discussion_id: int):
    client.call_start_discussion_call(discussion_id=discussion_id)
```

##### IdentityCommandeService
- **keycloakBind** et **keycloakUnbind**: déplacement dans le service **keycloakCommandService**
```python
from olvid import OlvidClient

client = OlvidClient()
async def bind_to_keycloak(configuration_link: str):
    # replace: client.identity_keycloak_bind(configuration_link)
    client.keycloak_bind_identity(configuration_link=configuration_link)
```

##### DiscussionCommandService
- **discussionEmpty**: suppression du paramètre delete_everywhere qui ne fonctionnait plus (plus possible de supprimer à distance les messages d'autrui).
```python
from olvid import OlvidClient

client = OlvidClient()
async def empty_discussion(discussion_id: int):
    # replace: client.discussion_empty(discussion_id=discussion_id, delete_everywhere=True)
    client.discussion_empty(discussion_id=discussion_id)
```

- **discussionSettingsGet** et **discussionSettingsSet**: déplacement dans le nouveau service **settingsCommandService**
```python
from olvid import OlvidClient

client = OlvidClient()
async def get_discussion_settings(discussion_id: int):
    # replace: client.settings_discussion_get()
    client.settings_discussion_get(discussion_id=discussion_id)
```

#### Notifications

##### GroupNotificationService
- **GroupUpdateInProgress** et **GroupUpdateFinished**: suppression des notifications devenues inutiles (les modifications de groupes ont été rendues synchrones et attendent que le groupe soit disponible).

#### Admin

##### IdentityAdminService
- **identityNew**: suppression du paramètre api_key, utilisez la commande **identitySetApiKey** une fois l'identité crée.

#### Datatypes

##### Invitation
- suppression du status *STATUS_GROUP_INVITATION_FROZEN* devenu inutile.

##### Discussion
- déplacement du message protobuf **DiscussionSettings** du fichier *discussion.proto* vers *settings.proto*, mais il reste dans le module `datatypes`, cela ne devrait donc pas affecter le code.

### N8n
:::{warning}
Les nœuds Olvid pour n8n ont été remaniés en profondeur et pourraient donc en pas être rétrocompatibles. Nous vous recommandons de faire des sauvegardes de vos flows existants avant de mettre à jour le paquet.
:::

#### Credentials
Les credentials Olvid ont été mis à jour. Si vos nœuds ne trouvent plus leur credentials, il faut en ajouter de nouveau et mettre à jour les credentials utilisés par chaque noeud Olvid.
Pour créer vos nouveaux credential rendez-vous dans la section [](/n8n/n8n.md#configurer-le-noeud-olvid).
