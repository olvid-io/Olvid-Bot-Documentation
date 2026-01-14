# ➡️ Migrations

## Passage en V2

:::{note}
Cette page référence tous les changements non rétrocompatibles apportés par la version 2 du framework. 
Il est important de la lire intégralement pour mettre à jour vos configurations et votre code lors de la mise à jour des différents outils
d'une version 1.X.X vers une version 2.0.0 ou supérieure.
:::

### Python
#### Configuration
Les variables d'environnement de configuration des différents clients ont été normalisées. 
Cela peut induire des changements dans les variables d'environnement des fichiers *docker-compose.yaml*, ou dans les fichiers *.env*.

- Les variables d'environnement *DAEMON_HOSTNAME* et *DAEMON_PORT* ont été supprimées au profit de la variable *OLVID_DAEMON_TARGET*. 
La nouvelle variable correspond à l'URL complète d'accès au daemon.

```.dotenv
DAEMON_HOSTNAME=daemon
DAEMON_PORT=50051
  => OLVID_DAEMON_TARGET=http://daemon:50051
```

- Les fichiers *.client_key* et *.admin_client_key* ne sont plus supportés, à la place utilisez un fichier *.env* pour définir les variables suivantes:
```.dotenv
OLVID_CLIENT_KEY=00000000-0000-0000-0000-000000000000
OLVID_ADMIN_CLIENT_KEY=00000000-0000-0000-0000-000000000000
```

#### Suppression de la classe OlvidBot
Les classes *OlvidBot* et *OlvidClient* ont été fusionnées, vous pouvez remplacer tous les usages de la classe *OlvidBot* par *OlvidClient*.
```
OlvidBot => OlvidClient
```

#### OlvidClient
- les méthodes *add_command* et *remove_command* sont supprimées et remplacées par *add_listener* et *remove_listener*.
```
add_command => add_listener
remove_command => remove_listener
```
- normalisation des noms de méthodes qui utilisent des fichiers, impliquant le renommage de certaines méthodes.
```
identity_set_photo => identity_set_photo_file
group_set_photo => identity_set_photo_file
```

#### datatypes
Certaines méthodes associées aux objets du module `datatypes` prennent maintenant une instance de la classe *OlvidClient* en paramètre. 
Voici quelque exemples **NON EXHAUSTIFS** de changements.
```
client: OlvidClient
message: datatypes.Message
discussion: datatypes.Discussion

message.reply(body="Reply") => message.reply(client, body="Reply")
message.react("💚") => message.reply(client, "💚")
discussion.post_message(body="new message") => discussion.post_message(client, body="new message")
```

#### tools
Suppression des classes *tools.AutoInvitationBot*, tools.DiscussionRetentionPolicyBot, tools.SelfCleaningBot et tools.KeycloakAutoInvitationBot.  
Il suffit maintenant de paramètrer le daemon avec l'API **SettingsCommandService**.

```
tools.AutoInvitationBot()
tools.SelfCleaningBot()
tools.DiscussionRetentionPolicyBot(discussion_retention_number=10, global_retention_number=100, retention_delay_s=86_400)
tools.KeycloakAutoInvitationBot()

=>

# retrieve original settings
settings: datatypes.IdentitySettings = await client.settings_identity_get()

# update settings depending on your needs
settings.invitation = datatypes.IdentitySettings.AutoAcceptInvitation(True, True, True, True)
settings.message_retention = datatypes.IdentitySettings.MessageRetention(discussion_count=5, global_count=100, existence_duration=86_400, clean_locked_discussions=True)
settings.keycloak = datatypes.IdentitySettings.Keycloak(auto_invite_new_members=True) 

# set new settings
await client.settings_identity_set(settings)
```

#### Listeners
La notion de listeners a évolué pour utiliser le mécanisme de filtrage des notifications sorti dans la version 1.4.0.
Les changements suivants découlent de cette volonté de normalisation avec les autres clients.  
Pour en savoir plus sur l'usage des listeners rendez-vous ici: [](/python/tutorials.md#listener).
- suppression de la notion de *checkers*, utilisez les filtres à la place. 
- suppression du paramètre *priority*.

### Daemon
Les changements suivants peuvent toucher tous les clients d'un daemon. Il faut donc vérifier pour chaque point d'entrée s'il est utilisé dans le code.

#### Sauvegardes
La version 2 amène le nouveau système de sauvegarde Olvid.
Les backups sont maintenant stockés sur notre serveur et il vous suffit de stocker la clé de chiffrement associée pour récupérer ou transférer tout ou partie de votre daemon.

Comme dans la v1 le dossier `backups` du daemon contient tout le nécessaire à la restauration d'une sauvegarde,
si vous sauvegardiez déjà son contenu aucun changement ne devrait être nécessaire, mais nous vous conseillons tout de même de vérifier que tout se passe bien.

Pour en savoir plus sur la mise en place des sauvegardes: [](/daemon/tutorials.md#sauvegardes).

#### Commandes

##### MessageCommandeService
- **messageSendVoip**: Suppression de la commande, utilisez le service callCommandService à la place.
```
message_send_voip => call_start_discussion_call
```

##### IdentityCommandeService
- **keycloakBind** et **keycloakUnbind**: déplacement dans le service **keycloakCommandService**
```
identity_keycloak_bind => keycloak_bind_identity 
identity_keycloak_unbind => keycloak_unbind_identity 
```

##### DiscussionCommandService
- **discussionSettingsGet** et **discussionSettingsSet**: déplacement dans le nouveau service **settingsCommandService**
```
discussion_settings_get 
  => settings_discussion_get
discussion_settings_set(settings=settings) 
  => settings_discussion_set(discussion_settings=settings)
```

- **discussionEmpty**: suppression du paramètre delete_everywhere qui ne fonctionnait plus (plus possible de supprimer à distance les messages d'autrui).
```
discussion_empty(discussion_id=id, delete_everywhere=True) 
  => discussion_empty(discussion_id=id) 
```

#### Notifications

##### GroupNotificationService
- **GroupUpdateInProgress** et **GroupUpdateFinished**: suppression des notifications devenues inutiles (les modifications de groupes ont été rendues synchrones et attendent que le groupe soit disponible).
```
group_update_in_progress =>
group_update_finished =>
```

#### Admin

##### IdentityAdminService
- **identityNew**: suppression du paramètre api_key, utilisez la commande **identitySetApiKey** une fois l'identité crée.
```
identity_new(api_key="XXXXXX") 
  => identity_new()
     identity_set_api_key("XXXXXX")
```

#### Datatypes

##### Invitation
- suppression du status *STATUS_GROUP_INVITATION_FROZEN* devenu inutile.
```
datatypes.Invitation.Status.STATUS_GROUP_INVITATION_FROZEN =>
```

##### Discussion
- déplacement du message **DiscussionSettings** du fichier *discussion.proto* vers *settings.proto*, mais il reste dans le module `datatypes`, cela ne devrait donc pas affecter le code.
```
discussion_setings_get => settings_discussion_get
discussion_setings_set => settings_discussion_set
```