# 📚️ References

This section describes the core entities used by Olvid daemon and exposed entrypoints.

:::{toctree}
:maxdepth: 1
:hidden:
Datatypes<self>
commands
notifications
admins
:::
:::{contents}
:depth: 1
:local:
:::
(datatype-message)=
## `Message`

> **Related Endpoints:**
> * **Command:** {ref}`service-messagecommandservice`
> * **Notification:** {ref}`service-messagenotificationservice`


(datatype-messageid)=
### MessageId

**Fields:**
* `type` ({ref}`datatype-messageid.type`)
* `id` (uint64)

---

(datatype-messageid.type)=
### MessageId.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`
* `TYPE_INBOUND`
* `TYPE_OUTBOUND`

---

### Message

**Fields:**
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

---

(datatype-messageephemerality)=
### MessageEphemerality

**Fields:**
* `read_once` (bool)
* `existence_duration` (uint64 - *seconds*)
* `visibility_duration` (uint64 - *seconds*)

---

(datatype-messagereaction)=
### MessageReaction

**Fields:**
* `contact_id` (uint64 - *id == 0 if own reaction*)
* `reaction` (string)
* `timestamp` (uint64)

---

(datatype-messagelocation)=
### MessageLocation

**Fields:**
* `type` ({ref}`datatype-messagelocation.locationtype`)
* `timestamp` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)
* `address` (**optional** string)

---

(datatype-messagelocation.locationtype)=
### MessageLocation.LocationType

**Enum Values:**
* `LOCATION_TYPE_UNSPECIFIED`
* `LOCATION_TYPE_SEND`
* `LOCATION_TYPE_SHARING`
* `LOCATION_TYPE_SHARING_FINISHED`

---

(datatype-messagefilter)=
### MessageFilter

**Fields:**
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

---

(datatype-messagefilter.attachment)=
### MessageFilter.Attachment

**Enum Values:**
* `ATTACHMENT_UNSPECIFIED`
* `ATTACHMENT_HAVE`
* `ATTACHMENT_HAVE_NOT` - *currently not implementable
    ATTACHMENT_HAVE_IMAGE = 3;
    ATTACHMENT_HAVE_VIDEO = 4;
    ATTACHMENT_HAVE_IMAGE_VIDEO = 5;
    ATTACHMENT_HAVE_AUDIO = 6;*

---

(datatype-messagefilter.location)=
### MessageFilter.Location

**Enum Values:**
* `LOCATION_UNSPECIFIED`
* `LOCATION_HAVE`
* `LOCATION_HAVE_NOT`
* `LOCATION_IS_SEND`
* `LOCATION_IS_SHARING`
* `LOCATION_IS_SHARING_FINISHED`

---

(datatype-messagefilter.reaction)=
### MessageFilter.Reaction

**Enum Values:**
* `REACTION_UNSPECIFIED`
* `REACTION_HAS`
* `REACTION_HAS_NOT`

---

(datatype-reactionfilter)=
### ReactionFilter

**Fields:**
* `reacted_by_me` (bool)
* `reacted_by_contact_id` (uint64)
* `reaction` (**optional** string - *contains this reaction emoji (combined with reacted_by parameter)*)

---

(datatype-attachment)=
## `Attachment`

> **Related Endpoints:**
> * **Command:** {ref}`service-attachmentcommandservice`
> * **Notification:** {ref}`service-attachmentnotificationservice`


(datatype-attachmentid)=
### AttachmentId

**Fields:**
* `type` ({ref}`datatype-attachmentid.type`)
* `id` (uint64)

---

(datatype-attachmentid.type)=
### AttachmentId.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`
* `TYPE_INBOUND`
* `TYPE_OUTBOUND`

---

### Attachment

**Fields:**
* `id` ({ref}`datatype-attachmentid`)
* `discussion_id` (uint64)
* `message_id` ({ref}`datatype-messageid`)
* `file_name` (string)
* `mime_type` (string)
* `size` (uint64)

---

(datatype-attachmentfilter)=
### AttachmentFilter

**Fields:**
* `type` (**optional** {ref}`datatype-attachmentid.type`)
* `file_type` (**optional** {ref}`datatype-attachmentfilter.filetype`)
* `discussion_id` (**optional** uint64)
* `message_id` (**optional** {ref}`datatype-messageid` - *optional uint64 contact_id = 4; not implementable now*)
* `filename_search` (**optional** string)
* `mime_type_search` (**optional** string)
* `min_size` (**optional** uint64)
* `max_size` (**optional** uint64)

---

(datatype-attachmentfilter.filetype)=
### AttachmentFilter.FileType

**Enum Values:**
* `FILE_TYPE_UNSPECIFIED`
* `FILE_TYPE_IMAGE`
* `FILE_TYPE_VIDEO`
* `FILE_TYPE_IMAGE_VIDEO`
* `FILE_TYPE_AUDIO`
* `FILE_TYPE_LINK_PREVIEW`
* `FILE_TYPE_NOT_LINK_PREVIEW`

---

(datatype-discussion)=
## `Discussion`

> **Related Endpoints:**
> * **Command:** {ref}`service-discussioncommandservice`
> * **Notification:** {ref}`service-discussionnotificationservice`


### Discussion

**Fields:**
* `id` (uint64)
* `title` (string)
* `contact_id` (uint64)
* `group_id` (uint64)

---

(datatype-discussionfilter)=
### DiscussionFilter

**Fields:**
* `type` (**optional** {ref}`datatype-discussionfilter.type`)
* `contact_id` (uint64)
* `group_id` (uint64)
* `title_search` (**optional** string)

---

(datatype-discussionfilter.type)=
### DiscussionFilter.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`
* `TYPE_OTO`
* `TYPE_GROUP`

---

(datatype-contact)=
## `Contact`

> **Related Endpoints:**
> * **Command:** {ref}`service-contactcommandservice`
> * **Notification:** {ref}`service-contactnotificationservice`


### Contact

**Fields:**
* `id` (uint64)
* `display_name` (string)
* `details` ({ref}`datatype-identitydetails`)
* `established_channel_count` (uint32)
* `device_count` (uint32)
* `has_one_to_one_discussion` (bool)
* `has_a_photo` (bool)
* `keycloak_managed` (bool)

---

(datatype-contactfilter)=
### ContactFilter

**Fields:**
* `one_to_one` (**optional** {ref}`datatype-contactfilter.onetoone`)
* `photo` (**optional** {ref}`datatype-contactfilter.photo`)
* `keycloak` (**optional** {ref}`datatype-contactfilter.keycloak`)
* `display_name_search` (**optional** string)
* `details_search` (**optional** {ref}`datatype-identitydetails`)

---

(datatype-contactfilter.onetoone)=
### ContactFilter.OneToOne

**Enum Values:**
* `ONE_TO_ONE_UNSPECIFIED`
* `ONE_TO_ONE_IS`
* `ONE_TO_ONE_IS_NOT`

---

(datatype-contactfilter.photo)=
### ContactFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`
* `PHOTO_HAS`
* `PHOTO_HAS_NOT`

---

(datatype-contactfilter.keycloak)=
### ContactFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`
* `KEYCLOAK_MANAGED`
* `KEYCLOAK_NOT_MANAGED`

---

(datatype-group)=
## `Group`

> **Related Endpoints:**
> * **Command:** {ref}`service-groupcommandservice`
> * **Notification:** {ref}`service-groupnotificationservice`


### Group

**Fields:**
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

---

(datatype-group.type)=
### Group.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`
* `TYPE_STANDARD`
* `TYPE_CONTROLLED`
* `TYPE_READ_ONLY`
* `TYPE_ADVANCED`

---

(datatype-group.advancedconfiguration)=
### Group.AdvancedConfiguration

**Fields:**
* `read_only` (bool)
* `remote_delete` ({ref}`datatype-group.advancedconfiguration.remotedelete`)

---

(datatype-group.advancedconfiguration.remotedelete)=
### Group.AdvancedConfiguration.RemoteDelete

**Enum Values:**
* `REMOTE_DELETE_UNSPECIFIED`
* `REMOTE_DELETE_NOBODY`
* `REMOTE_DELETE_ADMINS`
* `REMOTE_DELETE_EVERYONE`

---

(datatype-groupmember)=
### GroupMember

**Fields:**
* `contact_id` (uint64)
* `permissions` ({ref}`datatype-groupmemberpermissions`)

---

(datatype-pendinggroupmember)=
### PendingGroupMember

**Fields:**
* `pending_member_id` (uint64)
* `contact_id` (uint64 - *set to 0 if not in your contacts*)
* `display_name` (string)
* `declined` (bool)
* `permissions` ({ref}`datatype-groupmemberpermissions`)

---

(datatype-groupmemberpermissions)=
### GroupMemberPermissions

**Fields:**
* `admin` (bool)
* `remote_delete_anything` (bool)
* `edit_or_remote_delete_own_messages` (bool)
* `change_settings` (bool)
* `send_message` (bool)

---

(datatype-groupfilter)=
### GroupFilter

**Fields:**
* `type` (**optional** {ref}`datatype-group.type`)
* `empty` (**optional** {ref}`datatype-groupfilter.empty`)
* `photo` (**optional** {ref}`datatype-groupfilter.photo`)
* `keycloak` (**optional** {ref}`datatype-groupfilter.keycloak`)
* `own_permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter` - *your permission*)
* `name_search` (**optional** string)
* `description_search` (**optional** string)
* `member_filters` (**repeated** {ref}`datatype-groupmemberfilter`)
* `pending_member_filters` (**repeated** {ref}`datatype-pendinggroupmemberfilter`)

---

(datatype-groupfilter.empty)=
### GroupFilter.Empty

**Enum Values:**
* `EMPTY_UNSPECIFIED`
* `EMPTY_IS`
* `EMPTY_IS_NOT`

---

(datatype-groupfilter.keycloak)=
### GroupFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`
* `KEYCLOAK_IS`
* `KEYCLOAK_IS_NOT`

---

(datatype-groupfilter.photo)=
### GroupFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`
* `PHOTO_HAS`
* `PHOTO_HAS_NOT`

---

(datatype-groupmemberfilter)=
### GroupMemberFilter

**Fields:**
* `contact_id` (**optional** uint64)
* `permissions` (**optional** {ref}`datatype-grouppermissionfilter`)

---

(datatype-pendinggroupmemberfilter)=
### PendingGroupMemberFilter

**Fields:**
* `is_contact` (**optional** {ref}`datatype-pendinggroupmemberfilter.contact`)
* `has_declined` (**optional** {ref}`datatype-pendinggroupmemberfilter.declined`)
* `contact_id` (**optional** uint64)
* `display_name_search` (**optional** string)
* `permissions` (**optional** {ref}`datatype-grouppermissionfilter`)

---

(datatype-pendinggroupmemberfilter.contact)=
### PendingGroupMemberFilter.Contact

**Enum Values:**
* `CONTACT_UNSPECIFIED`
* `CONTACT_IS`
* `CONTACT_IS_NOT`

---

(datatype-pendinggroupmemberfilter.declined)=
### PendingGroupMemberFilter.Declined

**Enum Values:**
* `DECLINED_UNSPECIFIED`
* `DECLINED_HAS`
* `DECLINED_HAS_NOT`

---

(datatype-grouppermissionfilter)=
### GroupPermissionFilter

**Fields:**
* `admin` (**optional** {ref}`datatype-grouppermissionfilter.admin`)
* `send_message` (**optional** {ref}`datatype-grouppermissionfilter.sendmessage`)
* `remote_delete_anything` (**optional** {ref}`datatype-grouppermissionfilter.remotedeleteanything`)
* `edit_or_remote_delete_own_messages` (**optional** {ref}`datatype-grouppermissionfilter.editorremotedeleteownmessage`)
* `change_settings` (**optional** {ref}`datatype-grouppermissionfilter.changesettings`)

---

(datatype-grouppermissionfilter.admin)=
### GroupPermissionFilter.Admin

**Enum Values:**
* `ADMIN_UNSPECIFIED`
* `ADMIN_IS`
* `ADMIN_IS_NOT`

---

(datatype-grouppermissionfilter.sendmessage)=
### GroupPermissionFilter.SendMessage

**Enum Values:**
* `SEND_MESSAGE_UNSPECIFIED`
* `SEND_MESSAGE_CAN`
* `SEND_MESSAGE_CANNOT`

---

(datatype-grouppermissionfilter.remotedeleteanything)=
### GroupPermissionFilter.RemoteDeleteAnything

**Enum Values:**
* `REMOTE_DELETE_ANYTHING_UNSPECIFIED`
* `REMOTE_DELETE_ANYTHING_CAN`
* `REMOTE_DELETE_ANYTHING_CANNOT`

---

(datatype-grouppermissionfilter.editorremotedeleteownmessage)=
### GroupPermissionFilter.EditOrRemoteDeleteOwnMessage

**Enum Values:**
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_UNSPECIFIED`
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CAN`
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CANNOT`

---

(datatype-grouppermissionfilter.changesettings)=
### GroupPermissionFilter.ChangeSettings

**Enum Values:**
* `CHANGE_SETTINGS_UNSPECIFIED`
* `CHANGE_SETTINGS_CAN`
* `CHANGE_SETTINGS_CANNOT`

---

(datatype-identity)=
## `Identity`

> **Related Endpoints:**
> * **Command:** {ref}`service-identitycommandservice`
> * **Admin:** {ref}`service-identityadminservice`


(datatype-identitydetails)=
### IdentityDetails

**Fields:**
* `first_name` (**optional** string)
* `last_name` (**optional** string)
* `company` (**optional** string)
* `position` (**optional** string)

---

### Identity

id == 0 is equivalent to null identity
 invitation_url field is deprecated, and will be removed in next major release
   use IdentityCommandService.IdentityGetInvitationLink or IdentityAdminService.IdentityAdminGetInvitationLink instead

**Fields:**
* `id` (uint64)
* `display_name` (string)
* `details` ({ref}`datatype-identitydetails`)
* `invitation_url` (***deprecated*** string)
* `keycloak_managed` (bool)
* `has_a_photo` (bool)
* `api_key` ({ref}`datatype-identity.apikey`)

---

(datatype-identity.apikey)=
### Identity.ApiKey

**Fields:**
* `permission` ({ref}`datatype-identity.apikey.permission`)
* `expiration_timestamp` (uint64)

---

(datatype-identity.apikey.permission)=
### Identity.ApiKey.Permission

**Fields:**
* `call` (bool)
* `multi_device` (bool)

---

(datatype-identityfilter)=
### IdentityFilter

**Fields:**
* `keycloak` (**optional** {ref}`datatype-identityfilter.keycloak`)
* `photo` (**optional** {ref}`datatype-identityfilter.photo`)
* `api_key` (**optional** {ref}`datatype-identityfilter.apikey`)
* `display_name_search` (**optional** string)
* `details_search` (**optional** {ref}`datatype-identitydetails`)

---

(datatype-identityfilter.keycloak)=
### IdentityFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`
* `KEYCLOAK_IS`
* `KEYCLOAK_IS_NOT`

---

(datatype-identityfilter.photo)=
### IdentityFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`
* `PHOTO_HAS`
* `PHOTO_HAS_NOT`

---

(datatype-identityfilter.apikey)=
### IdentityFilter.ApiKey

**Enum Values:**
* `API_KEY_UNSPECIFIED`
* `API_KEY_HAS`
* `API_KEY_HAS_NOT`

---

(datatype-client_key)=
## `Client_Key`

> **Related Endpoints:**
> * **Admin:** {ref}`service-clientkeyadminservice`


(datatype-clientkey)=
### ClientKey

**Fields:**
* `name` (string)
* `key` (string)
* `identity_id` (uint64 - *0 if an admin key*)

---

(datatype-clientkeyfilter)=
### ClientKeyFilter

**Fields:**
* `admin_key` (bool)
* `identity_id` (uint64)
* `name_search` (**optional** string)
* `key` (**optional** string)

---

(datatype-invitation)=
## `Invitation`

> **Related Endpoints:**
> * **Command:** {ref}`service-invitationcommandservice`
> * **Notification:** {ref}`service-invitationnotificationservice`


### Invitation

**Fields:**
* `id` (uint64)
* `status` ({ref}`datatype-invitation.status`)
* `display_name` (string)
* `timestamp` (uint64)
* `sas` (**optional** string - *for STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE and STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE, set to pin code to exchange*)
* `mediatorId` (**optional** uint64 - *For introductions only: the contact id of the person who initiated introduction protocol*)

---

(datatype-invitation.status)=
### Invitation.Status

**Enum Values:**
* `STATUS_UNSPECIFIED`
* `STATUS_INVITATION_WAIT_YOU_TO_ACCEPT`
* `STATUS_INVITATION_WAIT_IT_TO_ACCEPT`
* `STATUS_INVITATION_STATUS_IN_PROGRESS`
* `STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE`
* `STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE`
* `STATUS_INTRODUCTION_WAIT_IT_TO_ACCEPT`
* `STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT`
* `STATUS_ONE_TO_ONE_INVITATION_WAIT_IT_TO_ACCEPT`
* `STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT`
* `STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT`

---

(datatype-invitationfilter)=
### InvitationFilter

**Fields:**
* `status` (**optional** {ref}`datatype-invitation.status`)
* `type` (**optional** {ref}`datatype-invitationfilter.type`)
* `display_name_search` (**optional** string)
* `min_timestamp` (**optional** uint64)
* `max_timestamp` (**optional** uint64)

---

(datatype-invitationfilter.type)=
### InvitationFilter.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`
* `TYPE_INVITATION`
* `TYPE_INTRODUCTION`
* `TYPE_GROUP`
* `TYPE_ONE_TO_ONE`

---

(datatype-settings)=
## `Settings`

> **Related Endpoints:**
> * **Command:** {ref}`service-settingscommandservice`


(datatype-identitysettings)=
### IdentitySettings

**Fields:**
* `invitation` ({ref}`datatype-identitysettings.autoacceptinvitation`)
* `message_retention` ({ref}`datatype-identitysettings.messageretention`)
* `keycloak` ({ref}`datatype-identitysettings.keycloak`)

---

(datatype-identitysettings.autoacceptinvitation)=
### IdentitySettings.AutoAcceptInvitation

**Fields:**
* `auto_accept_introduction` (bool)
* `auto_accept_group` (bool)
* `auto_accept_one_to_one` (bool)
* `auto_accept_invitation` (bool)

---

(datatype-identitysettings.messageretention)=
### IdentitySettings.MessageRetention

**Fields:**
* `existence_duration` (uint64 - *0 -> disabled (seconds)*)
* `discussion_count` (uint64 - *0 -> disabled*)
* `global_count` (uint64 - *0 -> disabled*)
* `clean_locked_discussions` (bool)
* `preserve_is_sharing_location_messages` (bool)

---

(datatype-identitysettings.keycloak)=
### IdentitySettings.Keycloak

**Fields:**
* `auto_invite_new_members` (bool)

---

(datatype-discussionsettings)=
### DiscussionSettings

**Fields:**
* `discussion_id` (uint64)
* `read_once` (bool - *message ephemerality settings (does not use a proper message for legacy reasons)*)
* `existence_duration` (uint64 - *0 -> disabled (seconds)*)
* `visibility_duration` (uint64 - *0 -> disabled (seconds)*)

---

(datatype-storage)=
## `Storage`

> **Related Endpoints:**
> * **Command:** {ref}`service-storagecommandservice`


(datatype-storageelement)=
### StorageElement

**Fields:**
* `key` (string)
* `value` (string)

---

(datatype-storageelementfilter)=
### StorageElementFilter

**Fields:**
* `key_search` (**optional** string)
* `value_search` (**optional** string)

---

(datatype-backup)=
## `Backup`

> **Related Endpoints:**
> * **Admin:** {ref}`service-backupadminservice`


### Backup

**Fields:**
* `admin_backup` ({ref}`datatype-backup.adminbackup`)
* `profile_backups` (**repeated** {ref}`datatype-backup.profilebackup`)

---

(datatype-backup.adminbackup)=
### Backup.AdminBackup

**Fields:**
* `admin_client_key_count` (uint64)
* `storage_elements_count` (uint64)

---

(datatype-backup.profilebackup)=
### Backup.ProfileBackup

**Fields:**
* `profile_display_name` (string)
* `already_exists_locally` (bool)
* `keycloak_managed` (bool)
* `snapshots` (**repeated** {ref}`datatype-backup.profilebackup.snapshot`)

---

(datatype-backup.profilebackup.snapshot)=
### Backup.ProfileBackup.Snapshot

**Fields:**
* `id` (string)
* `timestamp` (uint64)
* `from_device_name` (string)
* `contact_count` (uint64)
* `group_count` (uint64)
* `client_key_count` (uint64)
* `storage_elements_count` (uint64)
* `identity_settings` ({ref}`datatype-identitysettings`)

---

(datatype-call)=
## `Call`

> **Related Endpoints:**
> * **Command:** {ref}`service-callcommandservice`
> * **Notification:** {ref}`service-callnotificationservice`


(datatype-callparticipantid)=
### CallParticipantId

**Fields:**
* `contact_id` (uint64)
* `participant_id` (string)

---

(datatype-keycloak)=
## `Keycloak`

> **Related Endpoints:**
> * **Command:** {ref}`service-keycloakcommandservice`


(datatype-keycloakuser)=
### KeycloakUser

**Fields:**
* `keycloak_id` (string)
* `display_name` (string)
* `details` ({ref}`datatype-identitydetails`)
* `contact_id` (**optional** uint64)

---

(datatype-keycloakuserfilter)=
### KeycloakUserFilter

**Fields:**
* `contact` (**optional** {ref}`datatype-keycloakuserfilter.contact`)
* `display_name_search` (**optional** string)
* `details_search` (**optional** {ref}`datatype-identitydetails`)

---

(datatype-keycloakuserfilter.contact)=
### KeycloakUserFilter.Contact

**Enum Values:**
* `CONTACT_UNSPECIFIED`
* `CONTACT_IS`
* `CONTACT_IS_NOT`

---
