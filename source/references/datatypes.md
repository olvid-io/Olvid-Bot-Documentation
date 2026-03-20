# 📚️ References
This section describes the core entities used by Olvid daemon and exposed entrypoints.  
This page describe all datatypes used by daemon api, and you can find these api description in the [](commands), [](notifications) and [](admins) sections.

:::{toctree}
:maxdepth: 1
:hidden:
Datatypes<self>
commands
notifications
admins
:::

:::{contents} Datatypes
:depth: 1
:local:
:::

(datatype-message)=
## Message

> **Related Endpoints:**
> * **Command:** {ref}`service-messagecommandservice`
> * **Notification:** {ref}`service-messagenotificationservice`


### Message

:::{card}
```text
Describe an Olvid message.
```

**Message Fields:**
* `id` ({ref}`datatype-messageid`)
* `discussion_id` (uint64)
* `sender_id` (uint64 - *0 if you sent the message*)
* `body` (string)
* `sort_index` (double)
* `timestamp` (uint64)
* `attachments_count` (uint64)
* `replied_message_id` (**optional** {ref}`datatype-messageid`)
* `message_location` (**optional** {ref}`datatype-messagelocation`)
* `reactions` (**repeated** {ref}`datatype-messagereaction`)
* `forwarded` (bool)
* `edited_body` (bool)
:::
(datatype-messageid)=
### MessageId

:::{card}
**Message Fields:**
* `type` ({ref}`datatype-messageid.type`)
* `id` (uint64)
:::
(datatype-messageid.type)=
### MessageId.Type

:::{card}
**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INBOUND`: 1
* `TYPE_OUTBOUND`: 2
:::
(datatype-messageephemerality)=
### MessageEphemerality

:::{card}
**Message Fields:**
* `read_once` (bool)
* `existence_duration` (uint64 - *seconds*)
* `visibility_duration` (uint64 - *seconds*)
:::
(datatype-messagereaction)=
### MessageReaction

:::{card}
**Message Fields:**
* `contact_id` (uint64 - *id == 0 if own reaction*)
* `reaction` (string)
* `timestamp` (uint64)
:::
(datatype-messagelocation)=
### MessageLocation

:::{card}
**Message Fields:**
* `type` ({ref}`datatype-messagelocation.locationtype`)
* `timestamp` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)
* `address` (**optional** string)
:::
(datatype-messagelocation.locationtype)=
### MessageLocation.LocationType

:::{card}
**Enum Values:**
* `LOCATION_TYPE_UNSPECIFIED`: 0
* `LOCATION_TYPE_SEND`: 1
* `LOCATION_TYPE_SHARING`: 2
* `LOCATION_TYPE_SHARING_FINISHED`: 3
:::
(datatype-messagefilter)=
### MessageFilter

:::{card}
**Message Fields:**
* `type` (**optional** {ref}`datatype-messageid.type` - *sender and recipient*)
* `discussion_id` (**optional** uint64)
* `sender_contact_id` (**optional** uint64)
* `body_search` (**optional** string - *content*)
* `attachment` (**optional** {ref}`datatype-messagefilter.attachment`)
* `location` (**optional** {ref}`datatype-messagefilter.location`)
* `min_timestamp` (**optional** uint64)
* `max_timestamp` (**optional** uint64)
* `has_reaction` (**optional** {ref}`datatype-messagefilter.reaction` - *reactions*)
* `reactions_filter` (**repeated** {ref}`datatype-reactionfilter`)
* `reply_to_a_message` (bool)
* `do_not_reply_to_a_message` (bool)
* `replied_message_id` ({ref}`datatype-messageid`)
:::
(datatype-messagefilter.attachment)=
### MessageFilter.Attachment

:::{card}
**Enum Values:**
* `ATTACHMENT_UNSPECIFIED`: 0
* `ATTACHMENT_HAVE`: 1
* `ATTACHMENT_HAVE_NOT`: 2 - *currently not implementable
ATTACHMENT_HAVE_IMAGE = 3;
ATTACHMENT_HAVE_VIDEO = 4;
ATTACHMENT_HAVE_IMAGE_VIDEO = 5;
ATTACHMENT_HAVE_AUDIO = 6;*: 2
:::
(datatype-messagefilter.location)=
### MessageFilter.Location

:::{card}
**Enum Values:**
* `LOCATION_UNSPECIFIED`: 0
* `LOCATION_HAVE`: 1
* `LOCATION_HAVE_NOT`: 2
* `LOCATION_IS_SEND`: 3
* `LOCATION_IS_SHARING`: 5
* `LOCATION_IS_SHARING_FINISHED`: 6
:::
(datatype-messagefilter.reaction)=
### MessageFilter.Reaction

:::{card}
**Enum Values:**
* `REACTION_UNSPECIFIED`: 0
* `REACTION_HAS`: 1
* `REACTION_HAS_NOT`: 2
:::
(datatype-reactionfilter)=
### ReactionFilter

:::{card}
**Message Fields:**
* `reacted_by_me` (bool)
* `reacted_by_contact_id` (uint64)
* `reaction` (**optional** string - *contains this reaction emoji (combined with reacted_by parameter)*)
:::
(datatype-attachment)=
## Attachment

> **Related Endpoints:**
> * **Command:** {ref}`service-attachmentcommandservice`
> * **Notification:** {ref}`service-attachmentnotificationservice`


### Attachment

:::{card}
**Message Fields:**
* `id` ({ref}`datatype-attachmentid`)
* `discussion_id` (uint64)
* `message_id` ({ref}`datatype-messageid`)
* `file_name` (string)
* `mime_type` (string)
* `size` (uint64)
:::
(datatype-attachmentid)=
### AttachmentId

:::{card}
**Message Fields:**
* `type` ({ref}`datatype-attachmentid.type`)
* `id` (uint64)
:::
(datatype-attachmentid.type)=
### AttachmentId.Type

:::{card}
**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INBOUND`: 1
* `TYPE_OUTBOUND`: 2
:::
(datatype-attachmentfilter)=
### AttachmentFilter

:::{card}
**Message Fields:**
* `type` (**optional** {ref}`datatype-attachmentid.type`)
* `file_type` (**optional** {ref}`datatype-attachmentfilter.filetype`)
* `discussion_id` (**optional** uint64)
* `message_id` (**optional** {ref}`datatype-messageid` - *optional uint64 contact_id = 4; not implementable now*)
* `filename_search` (**optional** string)
* `mime_type_search` (**optional** string)
* `min_size` (**optional** uint64)
* `max_size` (**optional** uint64)
:::
(datatype-attachmentfilter.filetype)=
### AttachmentFilter.FileType

:::{card}
**Enum Values:**
* `FILE_TYPE_UNSPECIFIED`: 0
* `FILE_TYPE_IMAGE`: 3
* `FILE_TYPE_VIDEO`: 4
* `FILE_TYPE_IMAGE_VIDEO`: 5
* `FILE_TYPE_AUDIO`: 6
* `FILE_TYPE_LINK_PREVIEW`: 7
* `FILE_TYPE_NOT_LINK_PREVIEW`: 8
:::
(datatype-discussion)=
## Discussion

> **Related Endpoints:**
> * **Command:** {ref}`service-discussioncommandservice`
> * **Notification:** {ref}`service-discussionnotificationservice`


### Discussion

:::{card}
**Message Fields:**
* `id` (uint64)
* `title` (string)
* `contact_id` (uint64)
* `group_id` (uint64)
:::
(datatype-discussionfilter)=
### DiscussionFilter

:::{card}
**Message Fields:**
* `type` (**optional** {ref}`datatype-discussionfilter.type`)
* `contact_id` (uint64)
* `group_id` (uint64)
* `title_search` (**optional** string)
:::
(datatype-discussionfilter.type)=
### DiscussionFilter.Type

:::{card}
**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_OTO`: 1
* `TYPE_GROUP`: 2
:::
(datatype-contact)=
## Contact

> **Related Endpoints:**
> * **Command:** {ref}`service-contactcommandservice`
> * **Notification:** {ref}`service-contactnotificationservice`


### Contact

:::{card}
**Message Fields:**
* `id` (uint64)
* `display_name` (string)
* `details` ({ref}`datatype-identitydetails`)
* `established_channel_count` (uint32)
* `device_count` (uint32)
* `has_one_to_one_discussion` (bool)
* `has_a_photo` (bool)
* `keycloak_managed` (bool)
:::
(datatype-contactfilter)=
### ContactFilter

:::{card}
**Message Fields:**
* `one_to_one` (**optional** {ref}`datatype-contactfilter.onetoone`)
* `photo` (**optional** {ref}`datatype-contactfilter.photo`)
* `keycloak` (**optional** {ref}`datatype-contactfilter.keycloak`)
* `display_name_search` (**optional** string)
* `details_search` (**optional** {ref}`datatype-identitydetails`)
:::
(datatype-contactfilter.onetoone)=
### ContactFilter.OneToOne

:::{card}
**Enum Values:**
* `ONE_TO_ONE_UNSPECIFIED`: 0
* `ONE_TO_ONE_IS`: 1
* `ONE_TO_ONE_IS_NOT`: 2
:::
(datatype-contactfilter.photo)=
### ContactFilter.Photo

:::{card}
**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS`: 1
* `PHOTO_HAS_NOT`: 2
:::
(datatype-contactfilter.keycloak)=
### ContactFilter.Keycloak

:::{card}
**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_MANAGED`: 1
* `KEYCLOAK_NOT_MANAGED`: 2
:::
(datatype-group)=
## Group

> **Related Endpoints:**
> * **Command:** {ref}`service-groupcommandservice`
> * **Notification:** {ref}`service-groupnotificationservice`


### Group

:::{card}
**Message Fields:**
* `id` (uint64)
* `type` ({ref}`datatype-group.type`)
* `advanced_configuration` (**optional** {ref}`datatype-group.advancedconfiguration` - *only set if group.type is TYPE_ADVANCED*)
* `own_permissions` ({ref}`datatype-groupmemberpermissions` - *your permissions in this group*)
* `members` (**repeated** {ref}`datatype-groupmember`)
* `pending_members` (**repeated** {ref}`datatype-pendinggroupmember`)
* `update_in_progress` (bool)
* `keycloak_managed` (bool)
* `name` (string - *group details*)
* `description` (string)
* `has_a_photo` (bool)
:::
(datatype-group.type)=
### Group.Type

:::{card}
**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_STANDARD`: 1
* `TYPE_CONTROLLED`: 2
* `TYPE_READ_ONLY`: 3
* `TYPE_ADVANCED`: 4
:::
(datatype-group.advancedconfiguration)=
### Group.AdvancedConfiguration

:::{card}
**Message Fields:**
* `read_only` (bool)
* `remote_delete` ({ref}`datatype-group.advancedconfiguration.remotedelete`)
:::
(datatype-group.advancedconfiguration.remotedelete)=
### Group.AdvancedConfiguration.RemoteDelete

:::{card}
**Enum Values:**
* `REMOTE_DELETE_UNSPECIFIED`: 0
* `REMOTE_DELETE_NOBODY`: 1
* `REMOTE_DELETE_ADMINS`: 2
* `REMOTE_DELETE_EVERYONE`: 3
:::
(datatype-groupmember)=
### GroupMember

:::{card}
**Message Fields:**
* `contact_id` (uint64)
* `permissions` ({ref}`datatype-groupmemberpermissions`)
:::
(datatype-pendinggroupmember)=
### PendingGroupMember

:::{card}
**Message Fields:**
* `pending_member_id` (uint64)
* `contact_id` (uint64 - *set to 0 if not in your contacts*)
* `display_name` (string)
* `declined` (bool)
* `permissions` ({ref}`datatype-groupmemberpermissions`)
:::
(datatype-groupmemberpermissions)=
### GroupMemberPermissions

:::{card}
**Message Fields:**
* `admin` (bool)
* `remote_delete_anything` (bool)
* `edit_or_remote_delete_own_messages` (bool)
* `change_settings` (bool)
* `send_message` (bool)
:::
(datatype-groupfilter)=
### GroupFilter

:::{card}
**Message Fields:**
* `type` (**optional** {ref}`datatype-group.type`)
* `empty` (**optional** {ref}`datatype-groupfilter.empty`)
* `photo` (**optional** {ref}`datatype-groupfilter.photo`)
* `keycloak` (**optional** {ref}`datatype-groupfilter.keycloak`)
* `own_permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter` - *your permission*)
* `name_search` (**optional** string)
* `description_search` (**optional** string)
* `member_filters` (**repeated** {ref}`datatype-groupmemberfilter`)
* `pending_member_filters` (**repeated** {ref}`datatype-pendinggroupmemberfilter`)
:::
(datatype-groupfilter.empty)=
### GroupFilter.Empty

:::{card}
**Enum Values:**
* `EMPTY_UNSPECIFIED`: 0
* `EMPTY_IS_NOT`: 1
* `EMPTY_IS`: 2
:::
(datatype-groupfilter.keycloak)=
### GroupFilter.Keycloak

:::{card}
**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_IS_NOT`: 1
* `KEYCLOAK_IS`: 2
:::
(datatype-groupfilter.photo)=
### GroupFilter.Photo

:::{card}
**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS_NOT`: 1
* `PHOTO_HAS`: 2
:::
(datatype-groupmemberfilter)=
### GroupMemberFilter

:::{card}
**Message Fields:**
* `contact_id` (**optional** uint64)
* `permissions` (**optional** {ref}`datatype-grouppermissionfilter`)
:::
(datatype-pendinggroupmemberfilter)=
### PendingGroupMemberFilter

:::{card}
**Message Fields:**
* `is_contact` (**optional** {ref}`datatype-pendinggroupmemberfilter.contact`)
* `has_declined` (**optional** {ref}`datatype-pendinggroupmemberfilter.declined`)
* `contact_id` (**optional** uint64)
* `display_name_search` (**optional** string)
* `permissions` (**optional** {ref}`datatype-grouppermissionfilter`)
:::
(datatype-pendinggroupmemberfilter.contact)=
### PendingGroupMemberFilter.Contact

:::{card}
**Enum Values:**
* `CONTACT_UNSPECIFIED`: 0
* `CONTACT_IS`: 1
* `CONTACT_IS_NOT`: 2
:::
(datatype-pendinggroupmemberfilter.declined)=
### PendingGroupMemberFilter.Declined

:::{card}
**Enum Values:**
* `DECLINED_UNSPECIFIED`: 0
* `DECLINED_HAS`: 1
* `DECLINED_HAS_NOT`: 2
:::
(datatype-grouppermissionfilter)=
### GroupPermissionFilter

:::{card}
**Message Fields:**
* `admin` (**optional** {ref}`datatype-grouppermissionfilter.admin`)
* `send_message` (**optional** {ref}`datatype-grouppermissionfilter.sendmessage`)
* `remote_delete_anything` (**optional** {ref}`datatype-grouppermissionfilter.remotedeleteanything`)
* `edit_or_remote_delete_own_messages` (**optional** {ref}`datatype-grouppermissionfilter.editorremotedeleteownmessage`)
* `change_settings` (**optional** {ref}`datatype-grouppermissionfilter.changesettings`)
:::
(datatype-grouppermissionfilter.admin)=
### GroupPermissionFilter.Admin

:::{card}
**Enum Values:**
* `ADMIN_UNSPECIFIED`: 0
* `ADMIN_IS`: 1
* `ADMIN_IS_NOT`: 2
:::
(datatype-grouppermissionfilter.sendmessage)=
### GroupPermissionFilter.SendMessage

:::{card}
**Enum Values:**
* `SEND_MESSAGE_UNSPECIFIED`: 0
* `SEND_MESSAGE_CAN`: 1
* `SEND_MESSAGE_CANNOT`: 2
:::
(datatype-grouppermissionfilter.remotedeleteanything)=
### GroupPermissionFilter.RemoteDeleteAnything

:::{card}
**Enum Values:**
* `REMOTE_DELETE_ANYTHING_UNSPECIFIED`: 0
* `REMOTE_DELETE_ANYTHING_CAN`: 1
* `REMOTE_DELETE_ANYTHING_CANNOT`: 2
:::
(datatype-grouppermissionfilter.editorremotedeleteownmessage)=
### GroupPermissionFilter.EditOrRemoteDeleteOwnMessage

:::{card}
**Enum Values:**
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_UNSPECIFIED`: 0
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CAN`: 1
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CANNOT`: 2
:::
(datatype-grouppermissionfilter.changesettings)=
### GroupPermissionFilter.ChangeSettings

:::{card}
**Enum Values:**
* `CHANGE_SETTINGS_UNSPECIFIED`: 0
* `CHANGE_SETTINGS_CAN`: 1
* `CHANGE_SETTINGS_CANNOT`: 2
:::
(datatype-identity)=
## Identity

> **Related Endpoints:**
> * **Command:** {ref}`service-identitycommandservice`
> * **Admin:** {ref}`service-identityadminservice`


### Identity

:::{card}
```text
id == 0 is equivalent to null identity
invitation_url field is deprecated, and will be removed in next major release
use IdentityCommandService.IdentityGetInvitationLink or IdentityAdminService.IdentityAdminGetInvitationLink instead
```

**Message Fields:**
* `id` (uint64)
* `display_name` (string)
* `details` ({ref}`datatype-identitydetails`)
* `invitation_url` (***deprecated*** string - *TODO TODEL !!!!*)
* `keycloak_managed` (bool)
* `has_a_photo` (bool)
* `api_key` ({ref}`datatype-identity.apikey`)
:::
(datatype-identity.apikey)=
### Identity.ApiKey

:::{card}
**Message Fields:**
* `permission` ({ref}`datatype-identity.apikey.permission`)
* `expiration_timestamp` (uint64)
:::
(datatype-identity.apikey.permission)=
### Identity.ApiKey.Permission

:::{card}
**Message Fields:**
* `call` (bool)
* `multi_device` (bool)
:::
(datatype-identitydetails)=
### IdentityDetails

:::{card}
**Message Fields:**
* `first_name` (**optional** string)
* `last_name` (**optional** string)
* `company` (**optional** string)
* `position` (**optional** string)
:::
(datatype-identityfilter)=
### IdentityFilter

:::{card}
**Message Fields:**
* `keycloak` (**optional** {ref}`datatype-identityfilter.keycloak`)
* `photo` (**optional** {ref}`datatype-identityfilter.photo`)
* `api_key` (**optional** {ref}`datatype-identityfilter.apikey`)
* `display_name_search` (**optional** string)
* `details_search` (**optional** {ref}`datatype-identitydetails`)
:::
(datatype-identityfilter.keycloak)=
### IdentityFilter.Keycloak

:::{card}
**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_IS_NOT`: 1
* `KEYCLOAK_IS`: 2
:::
(datatype-identityfilter.photo)=
### IdentityFilter.Photo

:::{card}
**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS_NOT`: 1
* `PHOTO_HAS`: 2
:::
(datatype-identityfilter.apikey)=
### IdentityFilter.ApiKey

:::{card}
**Enum Values:**
* `API_KEY_UNSPECIFIED`: 0
* `API_KEY_HAS_NOT`: 1
* `API_KEY_HAS`: 2
:::
(datatype-client_key)=
## Client_Key

> **Related Endpoints:**
> * **Admin:** {ref}`service-clientkeyadminservice`


(datatype-clientkey)=
### ClientKey

:::{card}
**Message Fields:**
* `name` (string)
* `key` (string)
* `identity_id` (uint64 - *0 if an admin key*)
:::
(datatype-clientkeyfilter)=
### ClientKeyFilter

:::{card}
**Message Fields:**
* `admin_key` (bool)
* `identity_id` (uint64)
* `name_search` (**optional** string)
* `key` (**optional** string)
:::
(datatype-invitation)=
## Invitation

> **Related Endpoints:**
> * **Command:** {ref}`service-invitationcommandservice`
> * **Notification:** {ref}`service-invitationnotificationservice`


### Invitation

:::{card}
**Message Fields:**
* `id` (uint64)
* `status` ({ref}`datatype-invitation.status`)
* `display_name` (string)
* `timestamp` (uint64)
* `sas` (**optional** string - *for STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE and STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE, set to pin code to exchange*)
* `mediatorId` (**optional** uint64 - *For introductions only: the contact id of the person who initiated introduction protocol*)
:::
(datatype-invitation.status)=
### Invitation.Status

:::{card}
**Enum Values:**
* `STATUS_UNSPECIFIED`: 0
* `STATUS_INVITATION_WAIT_YOU_TO_ACCEPT`: 1
* `STATUS_INVITATION_WAIT_IT_TO_ACCEPT`: 2
* `STATUS_INVITATION_STATUS_IN_PROGRESS`: 3
* `STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE`: 4
* `STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE`: 5
* `STATUS_INTRODUCTION_WAIT_IT_TO_ACCEPT`: 7
* `STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT`: 8
* `STATUS_ONE_TO_ONE_INVITATION_WAIT_IT_TO_ACCEPT`: 9
* `STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT`: 10
* `STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT`: 11
:::
(datatype-invitationfilter)=
### InvitationFilter

:::{card}
**Message Fields:**
* `status` (**optional** {ref}`datatype-invitation.status`)
* `type` (**optional** {ref}`datatype-invitationfilter.type`)
* `display_name_search` (**optional** string)
* `min_timestamp` (**optional** uint64)
* `max_timestamp` (**optional** uint64)
:::
(datatype-invitationfilter.type)=
### InvitationFilter.Type

:::{card}
**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INVITATION`: 1
* `TYPE_INTRODUCTION`: 2
* `TYPE_GROUP`: 3
* `TYPE_ONE_TO_ONE`: 4
:::
(datatype-settings)=
## Settings

> **Related Endpoints:**
> * **Command:** {ref}`service-settingscommandservice`


(datatype-identitysettings)=
### IdentitySettings

:::{card}
**Message Fields:**
* `invitation` ({ref}`datatype-identitysettings.autoacceptinvitation`)
* `message_retention` ({ref}`datatype-identitysettings.messageretention`)
* `keycloak` ({ref}`datatype-identitysettings.keycloak`)
:::
(datatype-identitysettings.autoacceptinvitation)=
### IdentitySettings.AutoAcceptInvitation

:::{card}
**Message Fields:**
* `auto_accept_introduction` (bool)
* `auto_accept_group` (bool)
* `auto_accept_one_to_one` (bool)
* `auto_accept_invitation` (bool)
:::
(datatype-identitysettings.messageretention)=
### IdentitySettings.MessageRetention

:::{card}
**Message Fields:**
* `existence_duration` (uint64 - *0 -> disabled (seconds)*)
* `discussion_count` (uint64 - *0 -> disabled*)
* `global_count` (uint64 - *0 -> disabled*)
* `clean_locked_discussions` (bool)
* `preserve_is_sharing_location_messages` (bool)
:::
(datatype-identitysettings.keycloak)=
### IdentitySettings.Keycloak

:::{card}
**Message Fields:**
* `auto_invite_new_members` (bool)
:::
(datatype-discussionsettings)=
### DiscussionSettings

:::{card}
**Message Fields:**
* `discussion_id` (uint64)
* `read_once` (bool - *message ephemerality settings (does not use a proper message for legacy reasons)*)
* `existence_duration` (uint64 - *0 -> disabled (seconds)*)
* `visibility_duration` (uint64 - *0 -> disabled (seconds)*)
:::
(datatype-storage)=
## Storage

> **Related Endpoints:**
> * **Command:** {ref}`service-storagecommandservice`


(datatype-storageelement)=
### StorageElement

:::{card}
**Message Fields:**
* `key` (string)
* `value` (string)
:::
(datatype-storageelementfilter)=
### StorageElementFilter

:::{card}
**Message Fields:**
* `key_search` (**optional** string)
* `value_search` (**optional** string)
:::
(datatype-backup)=
## Backup

> **Related Endpoints:**
> * **Admin:** {ref}`service-backupadminservice`


### Backup

:::{card}
**Message Fields:**
* `admin_backup` ({ref}`datatype-backup.adminbackup`)
* `profile_backups` (**repeated** {ref}`datatype-backup.profilebackup`)
:::
(datatype-backup.adminbackup)=
### Backup.AdminBackup

:::{card}
**Message Fields:**
* `admin_client_key_count` (uint64)
* `storage_elements_count` (uint64)
:::
(datatype-backup.profilebackup)=
### Backup.ProfileBackup

:::{card}
**Message Fields:**
* `profile_display_name` (string)
* `already_exists_locally` (bool)
* `keycloak_managed` (bool)
* `snapshots` (**repeated** {ref}`datatype-backup.profilebackup.snapshot`)
:::
(datatype-backup.profilebackup.snapshot)=
### Backup.ProfileBackup.Snapshot

:::{card}
**Message Fields:**
* `id` (string)
* `timestamp` (uint64)
* `from_device_name` (string)
* `contact_count` (uint64)
* `group_count` (uint64)
* `client_key_count` (uint64)
* `storage_elements_count` (uint64)
* `identity_settings` ({ref}`datatype-identitysettings`)
:::
(datatype-call)=
## Call

> **Related Endpoints:**
> * **Command:** {ref}`service-callcommandservice`
> * **Notification:** {ref}`service-callnotificationservice`


(datatype-callparticipantid)=
### CallParticipantId

:::{card}
**Message Fields:**
* `contact_id` (uint64)
* `participant_id` (string)
:::
(datatype-keycloak)=
## Keycloak

> **Related Endpoints:**
> * **Command:** {ref}`service-keycloakcommandservice`


(datatype-keycloakuser)=
### KeycloakUser

:::{card}
**Message Fields:**
* `keycloak_id` (string)
* `display_name` (string)
* `details` ({ref}`datatype-identitydetails`)
* `contact_id` (**optional** uint64)
:::
(datatype-keycloakuserfilter)=
### KeycloakUserFilter

:::{card}
**Message Fields:**
* `contact` (**optional** {ref}`datatype-keycloakuserfilter.contact`)
* `display_name_search` (**optional** string)
* `details_search` (**optional** {ref}`datatype-identitydetails`)
:::
(datatype-keycloakuserfilter.contact)=
### KeycloakUserFilter.Contact

:::{card}
**Enum Values:**
* `CONTACT_UNSPECIFIED`: 0
* `CONTACT_IS`: 1
* `CONTACT_IS_NOT`: 2