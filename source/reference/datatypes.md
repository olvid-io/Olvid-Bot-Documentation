# Datatypes

This section describes the core entities used by Olvid daemon and exposed entrypoints.  
:::{contents} Datatypes
:depth: 1
:local:
:::

(file-message)=
## Message

> **Related Endpoints:**
> * **Command:** {ref}`service-messagecommandservice`
> * **Notification:** {ref}`service-messagenotificationservice`


(message-message)=
### Message

:::::::{card}
> An Olvid message posted in a discussion.  
> Sent messages are Outbound, received messages are Inbound.  
> Messages must have a body and/or one or more attachments.

**Fields:**
* `id` ({ref}`message-messageid` - *the message unique identifier*)
* `discussion_id` (uint64 - *the discussion the message belongs to*)
* `sender_id` (uint64 - *set to 0 if you sent the message, or to the contact id referencing the sender*)
* `body` (string - *text body*)
* `sort_index` (double - *index used to sort messages in a discussion*)
* `timestamp` (uint64 - *the timestamp on which the message was received*)
* `attachments_count` (uint64 - *number of attachments for this message*)
* `replied_message_id` (**optional** {ref}`message-messageid` - *set if this message is a reply to another message in this discussion*)
* `message_location` (**optional** {ref}`message-messagelocation` - *set if this message is a location message*)
* `reactions` (**repeated** {ref}`message-messagereaction` - *list of the reactions added on this message*)
* `forwarded` (bool - *does this message have been forwarded from another discussion by sender*)
* `edited_body` (bool - *does this message body have been edited*)

:::::::
(message-messageid)=
### MessageId

:::::::{card}
> A composite id to uniquely identify a message.

**Fields:**
* `type` ({ref}`enum-messageid.type` - *inbound or outbound message*)
* `id` (uint64)

::::::{card}
(enum-messageid.type)=
#### MessageId.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INBOUND`: 1 - *received message*
* `TYPE_OUTBOUND`: 2 - *sent message*
::::::

:::::::
(message-messageephemerality)=
### MessageEphemerality

:::::::{card}
> Describe message ephemerality.

**Fields:**
* `read_once` (bool - *message can only be read once (destroyed when discussion is closed)*)
* `existence_duration` (uint64 - *message is destroyed after this duration, in seconds*)
* `visibility_duration` (uint64 - *message is only visible for this duration, in seconds

seconds*)

:::::::
(message-messagereaction)=
### MessageReaction

:::::::{card}
> Describe a reaction to a message, by a contact or yourself.

**Fields:**
* `contact_id` (uint64 - *set to 0 for owned reactions*)
* `reaction` (string - *reaction emoji*)
* `timestamp` (uint64 - *the timestamp at which the reaction was added.*)

:::::::
(message-messagelocation)=
### MessageLocation

:::::::{card}
> A location message content.  
> There are two location message families:  
> - location sending: send a specific location.  
> - location sharing: share someone's location for a given duration.

**Fields:**
* `type` ({ref}`enum-messagelocation.locationtype`)
* `timestamp` (uint64 - *sending: when location was sent
sharing: the last location update timestamp*)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float - *the accuracy this location was recorded with.*)
* `address` (**optional** string - *optionally set for sending, a human readable address for this location*)

::::::{card}
(enum-messagelocation.locationtype)=
#### MessageLocation.LocationType

**Enum Values:**
* `LOCATION_TYPE_UNSPECIFIED`: 0
* `LOCATION_TYPE_SEND`: 1 - *a one shot location sending*
* `LOCATION_TYPE_SHARING`: 2 - *a live location sharing*
* `LOCATION_TYPE_SHARING_FINISHED`: 3 - *a completed location sharing*
::::::

:::::::
(message-messagefilter)=
### MessageFilter

:::::::{card}
> Filter messages by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`enum-messageid.type` - *is message inbound or outbound*)
* `discussion_id` (**optional** uint64 - *does message belongs to a specific discussion*)
* `sender_contact_id` (**optional** uint64 - *is message sent by a specific contact*)
* `body_search` (**optional** string - *regexp filter on *body* field*)
* `attachment` (**optional** {ref}`enum-messagefilter.attachment` - *does message have attachments or not*)
* `location` (**optional** {ref}`enum-messagefilter.location` - *is message a location message*)
* `min_timestamp` (**optional** uint64 - *is timestamp less or equal than *min_timestamp**)
* `max_timestamp` (**optional** uint64 - *is timestamp more or equal than *max_timestamp**)
* `has_reaction` (**optional** {ref}`enum-messagefilter.reaction` - *does message have reactions or not*)
* `reaction_filters` (**repeated** {ref}`message-reactionfilter` - *message must have at least one matching reaction for each *reactions_filter**)
* **Oneof `reply`**:
  * `reply_to_a_message` (bool - *is message a reply to another message*)
  * `do_not_reply_to_a_message` (bool - *is message not a reply to a message*)
  * `replied_message_id` ({ref}`message-messageid` - *is message a reply to a specific message id*)

::::::{card}
(enum-messagefilter.attachment)=
#### MessageFilter.Attachment

**Enum Values:**
* `ATTACHMENT_UNSPECIFIED`: 0
* `ATTACHMENT_HAVE`: 1
* `ATTACHMENT_HAVE_NOT`: 2
::::::

::::::{card}
(enum-messagefilter.location)=
#### MessageFilter.Location

**Enum Values:**
* `LOCATION_UNSPECIFIED`: 0
* `LOCATION_HAVE`: 1
* `LOCATION_HAVE_NOT`: 2
* `LOCATION_IS_SEND`: 3
* `LOCATION_IS_SHARING`: 5
* `LOCATION_IS_SHARING_FINISHED`: 6
::::::

::::::{card}
(enum-messagefilter.reaction)=
#### MessageFilter.Reaction

**Enum Values:**
* `REACTION_UNSPECIFIED`: 0
* `REACTION_HAS`: 1
* `REACTION_HAS_NOT`: 2
::::::

:::::::
(message-reactionfilter)=
### ReactionFilter

:::::::{card}
**Fields:**
* **Oneof `reacted_by`**:
  * `reacted_by_me` (bool - *is the reaction from yourself*)
  * `reacted_by_contact_id` (uint64 - *is the reaction from a specific contact*)
* `reaction` (**optional** string - *is *reaction* equal to the *reaction* field*)

:::::::

---

(file-attachment)=
## Attachment

> **Related Endpoints:**
> * **Command:** {ref}`service-attachmentcommandservice`
> * **Notification:** {ref}`service-attachmentnotificationservice`


(message-attachment)=
### Attachment

:::::::{card}
> An attachment represents a file attached to a message.  
> It is associated to a *message_id* and a *discussion_id*.  
>   
> Link previews are attachments with specific mime type: *olvid/link-preview*.

**Fields:**
* `id` ({ref}`message-attachmentid`)
* `discussion_id` (uint64)
* `message_id` ({ref}`message-messageid`)
* `file_name` (string)
* `mime_type` (string)
* `size` (uint64 - *file size in bytes*)

:::::::
(message-attachmentid)=
### AttachmentId

:::::::{card}
> A composite id to uniquely identify an attachment.

**Fields:**
* `type` ({ref}`enum-attachmentid.type` - *inbound or outbound attachment*)
* `id` (uint64)

::::::{card}
(enum-attachmentid.type)=
#### AttachmentId.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INBOUND`: 1 - *received attachments*
* `TYPE_OUTBOUND`: 2 - *sent attachments*
::::::

:::::::
(message-attachmentfilter)=
### AttachmentFilter

:::::::{card}
> Filter attachments by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`enum-attachmentid.type` - *select only INBOUND or OUTBOUND attachments*)
* `file_type` (**optional** {ref}`enum-attachmentfilter.filetype` - *filter by file type (pre-defined regexp for *mime_type*)*)
* `discussion_id` (**optional** uint64)
* `message_id` (**optional** {ref}`message-messageid` - *optional uint64 contact_id = 4; not implementable now*)
* `filename_search` (**optional** string - *regexp filter on *filename* field*)
* `mime_type_search` (**optional** string - *regexp filter on *mime_type* field*)
* `min_size` (**optional** uint64 - *minimum or equal file size*)
* `max_size` (**optional** uint64 - *maximum or equal file size*)

::::::{card}
(enum-attachmentfilter.filetype)=
#### AttachmentFilter.FileType

> apply pre-defined regexp filters on *mime_type* field.

**Enum Values:**
* `FILE_TYPE_UNSPECIFIED`: 0
* `FILE_TYPE_IMAGE`: 3
* `FILE_TYPE_VIDEO`: 4
* `FILE_TYPE_IMAGE_VIDEO`: 5 - *image or video*
* `FILE_TYPE_AUDIO`: 6
* `FILE_TYPE_LINK_PREVIEW`: 7
* `FILE_TYPE_NOT_LINK_PREVIEW`: 8 - *all except link previews*
::::::

:::::::

---

(file-discussion)=
## Discussion

> **Related Endpoints:**
> * **Command:** {ref}`service-discussioncommandservice`
> * **Notification:** {ref}`service-discussionnotificationservice`


(message-discussion)=
### Discussion

:::::::{card}
> A discussion must be associated to a contact or to a group.  
> If *contact_id* and *group_id* are both zero, then it is an existing locked discussion.

**Fields:**
* `id` (uint64)
* `title` (string - *contact.display_name* or *group.name**)
* **Oneof `identifier`**:
  * `contact_id` (uint64)
  * `group_id` (uint64)

:::::::
(message-discussionfilter)=
### DiscussionFilter

:::::::{card}
> Filter discussions by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`enum-discussionfilter.type` - *select group or contact discussions*)
* **Oneof `identifier`**:
  * `contact_id` (uint64)
  * `group_id` (uint64)
* `title_search` (**optional** string - *regexp filter on title field*)

::::::{card}
(enum-discussionfilter.type)=
#### DiscussionFilter.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_OTO`: 1
* `TYPE_GROUP`: 2
::::::

:::::::

---

(file-contact)=
## Contact

> **Related Endpoints:**
> * **Command:** {ref}`service-contactcommandservice`
> * **Notification:** {ref}`service-contactnotificationservice`


(message-contact)=
### Contact

:::::::{card}
> A contact is another Olvid identity you are in contact with.  
> A contact can have an associated discussion if has_one_to_one_discussion is true, else it's probably a collected contact you met in a group discussion.

**Fields:**
* `id` (uint64)
* `display_name` (string - *computed from *details**)
* `details` ({ref}`message-identitydetails`)
* `established_channel_count` (uint32 - *shall be equal to device_count to exchange messages*)
* `device_count` (uint32)
* `has_one_to_one_discussion` (bool)
* `has_a_photo` (bool)
* `keycloak_managed` (bool - *contact is registered on the same directory*)

:::::::
(message-contactfilter)=
### ContactFilter

:::::::{card}
> Filter contacts by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `one_to_one` (**optional** {ref}`enum-contactfilter.onetoone` - *select only contacts with or without one to one discussions*)
* `photo` (**optional** {ref}`enum-contactfilter.photo` - *select only contacts with or without profile photo*)
* `keycloak` (**optional** {ref}`enum-contactfilter.keycloak` - *select only contacts registered or not on your keycloak*)
* `display_name_search` (**optional** string - *regexp filter on *display_name**)
* `details_search` (**optional** {ref}`message-identitydetails` - *a set of regexp filters, one for each field of *details**)

::::::{card}
(enum-contactfilter.onetoone)=
#### ContactFilter.OneToOne

**Enum Values:**
* `ONE_TO_ONE_UNSPECIFIED`: 0
* `ONE_TO_ONE_IS`: 1
* `ONE_TO_ONE_IS_NOT`: 2
::::::

::::::{card}
(enum-contactfilter.photo)=
#### ContactFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS`: 1
* `PHOTO_HAS_NOT`: 2
::::::

::::::{card}
(enum-contactfilter.keycloak)=
#### ContactFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_MANAGED`: 1
* `KEYCLOAK_NOT_MANAGED`: 2
::::::

:::::::

---

(file-group)=
## Group

> **Related Endpoints:**
> * **Command:** {ref}`service-groupcommandservice`
> * **Notification:** {ref}`service-groupnotificationservice`


(message-group)=
### Group

:::::::{card}
> An Olvid group is a discussion with you and other Olvid identities.  
> Other identities in a group are automatically added to your contact book if they were not before as collected contacts (you do not have a one to one discussion with them).  
> *keycloak_managed* groups are not editable, and you cannot leave them. Group is managed from the keycloak admin console.

**Fields:**
* `id` (uint64)
* `type` ({ref}`enum-group.type` - *specify a pre-set of permissions given to group members.*)
* `advanced_configuration` (**optional** {ref}`message-group.advancedconfiguration` - *only set if group.type is TYPE_ADVANCED*)
* `own_permissions` ({ref}`message-groupmemberpermissions` - *your permissions in this group*)
* `members` (**repeated** {ref}`message-groupmember` - *members that accepted invitation*)
* `pending_members` (**repeated** {ref}`message-pendinggroupmember` - *members invited to join group*)
* `update_in_progress` (bool - *group is locked, edition will be delayed*)
* `keycloak_managed` (bool - *group automatically pushed by keycloak*)
* `name` (string)
* `description` (string)
* `has_a_photo` (bool)

::::::{card}
(enum-group.type)=
#### Group.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_STANDARD`: 1 - *all members are admin*
* `TYPE_CONTROLLED`: 2 - *non admin members cannot manage the group*
* `TYPE_READ_ONLY`: 3 - *only admin members can post messages*
* `TYPE_ADVANCED`: 4 - *specify an advanced configuration field*
::::::

::::::{card}
(message-group.advancedconfiguration)=
#### Group.AdvancedConfiguration

**Fields:**
* `read_only` (bool - *is group read only*)
* `remote_delete` ({ref}`enum-group.advancedconfiguration.remotedelete` - *who has permission to delete message for everyone*)
::::::

:::::{card}
(enum-group.advancedconfiguration.remotedelete)=
##### Group.AdvancedConfiguration.RemoteDelete

**Enum Values:**
* `REMOTE_DELETE_UNSPECIFIED`: 0
* `REMOTE_DELETE_NOBODY`: 1
* `REMOTE_DELETE_ADMINS`: 2
* `REMOTE_DELETE_EVERYONE`: 3
:::::

:::::::
(message-groupmember)=
### GroupMember

:::::::{card}
> Associate a contact, member of a group, with its permissions in this group.

**Fields:**
* `contact_id` (uint64)
* `permissions` ({ref}`message-groupmemberpermissions`)

:::::::
(message-pendinggroupmember)=
### PendingGroupMember

:::::::{card}
> Member of a group who has not yet accepted the invitation to join the group.

**Fields:**
* `pending_member_id` (uint64 - *unique identifier*)
* `contact_id` (uint64 - *set to 0 if this identity is not a contact yet*)
* `display_name` (string - *computed display name from their identity details.*)
* `declined` (bool - *does pending member declined invitation*)
* `permissions` ({ref}`message-groupmemberpermissions` - *permissions given to this member*)

:::::::
(message-groupmemberpermissions)=
### GroupMemberPermissions

:::::::{card}
> Describe permission set associated to any group member.

**Fields:**
* `admin` (bool - *can edit the group (change name or description, and manage group members)*)
* `remote_delete_anything` (bool - *can delete everywhere someone else's message*)
* `edit_or_remote_delete_own_messages` (bool - *can edit or delete everywhere own messages*)
* `change_settings` (bool - *can change discussion shared settings (message ephemerality)*)
* `send_message` (bool - *can post message in the group discussion*)

:::::::
(message-groupfilter)=
### GroupFilter

:::::::{card}
> Filter groups by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`enum-group.type`)
* `empty` (**optional** {ref}`enum-groupfilter.empty` - *does group have members or not*)
* `photo` (**optional** {ref}`enum-groupfilter.photo` - *does group have a photo or not*)
* `keycloak` (**optional** {ref}`enum-groupfilter.keycloak` - *is group keycloak managed or not*)
* `own_permissions_filter` (**optional** {ref}`message-grouppermissionfilter` - *filter on your own permissions in the group*)
* `name_search` (**optional** string - *regexp filter on *name_search* field*)
* `description_search` (**optional** string - *regexp filter on *description_search* field*)
* `member_filters` (**repeated** {ref}`message-groupmemberfilter` - *group must have at least one matching member for each *member_filters**)
* `pending_member_filters` (**repeated** {ref}`message-pendinggroupmemberfilter` - *group must have at least one pending member matching each *pending_member_filters**)

::::::{card}
(enum-groupfilter.empty)=
#### GroupFilter.Empty

**Enum Values:**
* `EMPTY_UNSPECIFIED`: 0
* `EMPTY_IS_NOT`: 1
* `EMPTY_IS`: 2
::::::

::::::{card}
(enum-groupfilter.keycloak)=
#### GroupFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_IS_NOT`: 1
* `KEYCLOAK_IS`: 2
::::::

::::::{card}
(enum-groupfilter.photo)=
#### GroupFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS_NOT`: 1
* `PHOTO_HAS`: 2
::::::

:::::::
(message-groupmemberfilter)=
### GroupMemberFilter

:::::::{card}
**Fields:**
* `contact_id` (**optional** uint64 - *is member a specific contact*)
* `permissions` (**optional** {ref}`message-grouppermissionfilter` - *does member's permissions match this permission filter*)

:::::::
(message-pendinggroupmemberfilter)=
### PendingGroupMemberFilter

:::::::{card}
**Fields:**
* `is_contact` (**optional** {ref}`enum-pendinggroupmemberfilter.contact` - *is pending member a contact or not*)
* `has_declined` (**optional** {ref}`enum-pendinggroupmemberfilter.declined` - *does pending member declined invitation or not*)
* `contact_id` (**optional** uint64 - *is pending member a specific known contact*)
* `display_name_search` (**optional** string - *regexp filter applied on *display_name* field*)
* `permissions` (**optional** {ref}`message-grouppermissionfilter` - *pending member's permissions match this permission filter*)

::::::{card}
(enum-pendinggroupmemberfilter.contact)=
#### PendingGroupMemberFilter.Contact

**Enum Values:**
* `CONTACT_UNSPECIFIED`: 0
* `CONTACT_IS`: 1
* `CONTACT_IS_NOT`: 2
::::::

::::::{card}
(enum-pendinggroupmemberfilter.declined)=
#### PendingGroupMemberFilter.Declined

**Enum Values:**
* `DECLINED_UNSPECIFIED`: 0
* `DECLINED_HAS`: 1
* `DECLINED_HAS_NOT`: 2
::::::

:::::::
(message-grouppermissionfilter)=
### GroupPermissionFilter

:::::::{card}
**Fields:**
* `admin` (**optional** {ref}`enum-grouppermissionfilter.admin` - *is user a group admin or not*)
* `send_message` (**optional** {ref}`enum-grouppermissionfilter.sendmessage` - *can the user post a message in the discussion*)
* `remote_delete_anything` (**optional** {ref}`enum-grouppermissionfilter.remotedeleteanything` - *can the user remote-delete any message, even other members' messages*)
* `edit_or_remote_delete_own_messages` (**optional** {ref}`enum-grouppermissionfilter.editorremotedeleteownmessage` - *can the user edit or remote-delete their own messages*)
* `change_settings` (**optional** {ref}`enum-grouppermissionfilter.changesettings` - *can the user change group settings*)

::::::{card}
(enum-grouppermissionfilter.admin)=
#### GroupPermissionFilter.Admin

**Enum Values:**
* `ADMIN_UNSPECIFIED`: 0
* `ADMIN_IS`: 1
* `ADMIN_IS_NOT`: 2
::::::

::::::{card}
(enum-grouppermissionfilter.sendmessage)=
#### GroupPermissionFilter.SendMessage

**Enum Values:**
* `SEND_MESSAGE_UNSPECIFIED`: 0
* `SEND_MESSAGE_CAN`: 1
* `SEND_MESSAGE_CANNOT`: 2
::::::

::::::{card}
(enum-grouppermissionfilter.remotedeleteanything)=
#### GroupPermissionFilter.RemoteDeleteAnything

**Enum Values:**
* `REMOTE_DELETE_ANYTHING_UNSPECIFIED`: 0
* `REMOTE_DELETE_ANYTHING_CAN`: 1
* `REMOTE_DELETE_ANYTHING_CANNOT`: 2
::::::

::::::{card}
(enum-grouppermissionfilter.editorremotedeleteownmessage)=
#### GroupPermissionFilter.EditOrRemoteDeleteOwnMessage

**Enum Values:**
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_UNSPECIFIED`: 0
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CAN`: 1
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CANNOT`: 2
::::::

::::::{card}
(enum-grouppermissionfilter.changesettings)=
#### GroupPermissionFilter.ChangeSettings

**Enum Values:**
* `CHANGE_SETTINGS_UNSPECIFIED`: 0
* `CHANGE_SETTINGS_CAN`: 1
* `CHANGE_SETTINGS_CANNOT`: 2
::::::

:::::::

---

(file-identity)=
## Identity

> **Related Endpoints:**
> * **Command:** {ref}`service-identitycommandservice`
> * **Admin:** {ref}`service-identityadminservice`


(message-identity)=
### Identity

:::::::{card}
> Your own Olvid identity, stored on this daemon instance.  
> A daemon can manage multiple Olvid identities.

**Fields:**
* `id` (uint64)
* `display_name` (string - *computed from *details**)
* `details` ({ref}`message-identitydetails`)
* `keycloak_managed` (bool - *identity is linked to a keycloak directory*)
* `has_a_photo` (bool)
* `api_key` ({ref}`message-identity.apikey` - *Olvid api key to grant permissions*)

::::::{card}
(message-identity.apikey)=
#### Identity.ApiKey

**Fields:**
* `permission` ({ref}`message-identity.apikey.permission`)
* `expiration_timestamp` (uint64)
::::::

:::::{card}
(message-identity.apikey.permission)=
##### Identity.ApiKey.Permission

**Fields:**
* `call` (bool)
* `multi_device` (bool)
:::::

:::::::
(message-identitydetails)=
### IdentityDetails

:::::::{card}
> Represents an Olvid identity details.  
> Used for any Olvid identity (owned identity or other contact).  
> Details are valid only if at least one field is not blank.

**Fields:**
* `first_name` (**optional** string)
* `last_name` (**optional** string)
* `company` (**optional** string)
* `position` (**optional** string)

:::::::
(message-identityfilter)=
### IdentityFilter

:::::::{card}
> Filter identities by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `keycloak` (**optional** {ref}`enum-identityfilter.keycloak` - *is identity keycloak managed or not*)
* `photo` (**optional** {ref}`enum-identityfilter.photo` - *does identity have a profile photo or not*)
* `api_key` (**optional** {ref}`enum-identityfilter.apikey` - *does identity have an Olvid api key or not*)
* `display_name_search` (**optional** string - *regexp filter on *display_name**)
* `details_search` (**optional** {ref}`message-identitydetails` - *a set of regexp filters, one for each field of *details**)

::::::{card}
(enum-identityfilter.keycloak)=
#### IdentityFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_IS_NOT`: 1
* `KEYCLOAK_IS`: 2
::::::

::::::{card}
(enum-identityfilter.photo)=
#### IdentityFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS_NOT`: 1
* `PHOTO_HAS`: 2
::::::

::::::{card}
(enum-identityfilter.apikey)=
#### IdentityFilter.ApiKey

**Enum Values:**
* `API_KEY_UNSPECIFIED`: 0
* `API_KEY_HAS_NOT`: 1
* `API_KEY_HAS`: 2
::::::

:::::::

---

(file-client_key)=
## Client_Key

> **Related Endpoints:**
> * **Admin:** {ref}`service-clientkeyadminservice`


(message-clientkey)=
### ClientKey

:::::::{card}
> A client key can be used to authenticate on the daemon.  
> It can be associated to a daemon identity if identity_id is specified, if not (identity_id is equal to zero) it is an admin client.  
> An admin client key can use admin command services and impersonate any daemon identity.

**Fields:**
* `name` (string - *user defined name*)
* `key` (string)
* `identity_id` (uint64 - *0 if an admin client key*)

:::::::
(message-clientkeyfilter)=
### ClientKeyFilter

:::::::{card}
> Filter client keys by attributes.

**Fields:**
* **Oneof `identity`**:
  * `admin_key` (bool - *filter admin client keys*)
  * `identity_id` (uint64 - *filter keys associated to an identity id*)
* `name_search` (**optional** string - *regexp filter on *name**)
* `key` (**optional** string - *key value*)

:::::::

---

(file-invitation)=
## Invitation

> **Related Endpoints:**
> * **Command:** {ref}`service-invitationcommandservice`
> * **Notification:** {ref}`service-invitationnotificationservice`


(message-invitation)=
### Invitation

:::::::{card}
> An invitation represents an instance of a protocol among several possibilities.  
> Protocols can be:  
> - Invitation: the classic Olvid invitation protocol to add someone else to your contact book. Protocol implies multiple manual steps, with invitation acceptation and four digit code exchange.  
> - Introduction: a third party identity presents two of its contacts to each other.  
> - One to one invitation: One of your contact asked you to create a one to one discussion.  
> - Group invitation: Someone invited you to join a group.  
>   
> Each invitation have a status representing the protocol, and it's current step.

**Fields:**
* `id` (uint64 - *invitation unique identifier*)
* `status` ({ref}`enum-invitation.status` - *current protocol step*)
* `display_name` (string - *display name of the other identity or the group name*)
* `timestamp` (uint64 - *latest status update timestamp*)
* `sas` (**optional** string - *only set for STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE and STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE
four digit code to give to the other in an invitation protocol*)
* `mediator_id` (**optional** uint64 - *introductions protocol only
the contact id of the person who initiated introduction protocol*)

::::::{card}
(enum-invitation.status)=
#### Invitation.Status

**Enum Values:**
* `STATUS_UNSPECIFIED`: 0
* `STATUS_INVITATION_WAIT_YOU_TO_ACCEPT`: 1 - *you received an invitation, accept or decline it*
* `STATUS_INVITATION_WAIT_IT_TO_ACCEPT`: 2 - *you sent an invitation, recipient must accept it to continue*
* `STATUS_INVITATION_STATUS_IN_PROGRESS`: 3 - *invitation process is in progress and will continue after automatic protocol message exchange between protagonist*
* `STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE`: 4 - *you must set other sas code*
* `STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE`: 5 - *you set other sas code, give your sas code to other*
* `STATUS_INTRODUCTION_WAIT_IT_TO_ACCEPT`: 7 - *you accepted an introduction, wait for the other to accept too*
* `STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT`: 8 - *you received an introduction*
* `STATUS_ONE_TO_ONE_INVITATION_WAIT_IT_TO_ACCEPT`: 9 - *you sent a one to one invitation, wait for the other to accept*
* `STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT`: 10 - *you received a one to one invitation, accept or decline it*
* `STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT`: 11 - *you received a group invitation, accept or decline it*
::::::

:::::::
(message-invitationfilter)=
### InvitationFilter

:::::::{card}
> Filter invitation by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `status` (**optional** {ref}`enum-invitation.status` - *does invitation have a specific status*)
* `type` (**optional** {ref}`enum-invitationfilter.type` - *does invitation belongs to a specific protocol*)
* `display_name_search` (**optional** string - *regexp filter on *display_name* field*)
* `min_timestamp` (**optional** uint64 - *is timestamp less or equal than *min_timestamp**)
* `max_timestamp` (**optional** uint64 - *is timestamp more or equal than *max_timestamp**)

::::::{card}
(enum-invitationfilter.type)=
#### InvitationFilter.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INVITATION`: 1 - *is status one of :
- STATUS_INVITATION_WAIT_YOU_TO_ACCEPT
- STATUS_INVITATION_WAIT_IT_TO_ACCEPT
- STATUS_INVITATION_STATUS_IN_PROGRESS
- STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE
- STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE*
* `TYPE_INTRODUCTION`: 2 - *is status one of :
- STATUS_INTRODUCTION_WAIT_IT_TO_ACCEPT
- STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT*
* `TYPE_GROUP`: 3 - *is status equals to:
- STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT*
* `TYPE_ONE_TO_ONE`: 4 - *is status one of :
- STATUS_ONE_TO_ONE_INVITATION_WAIT_IT_TO_ACCEPT
- STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT*
::::::

:::::::

---

(file-settings)=
## Settings

> **Related Endpoints:**
> * **Command:** {ref}`service-settingscommandservice`


(message-identitysettings)=
### IdentitySettings

:::::::{card}
> Settings for an Identity managed by a daemon.  
> - AutoAcceptInvitation: when enabled the daemon will automatically accept incoming and existing invitations from specified protocol.  
> - MessageRetention: when at least one element is set daemon will regularly check if some message can be deleted, matching filled criteria. This allows to save space and save performances by keeping database as small as possible.  
> - Keycloak: directory related settings

**Fields:**
* `invitation` ({ref}`message-identitysettings.autoacceptinvitation`)
* `message_retention` ({ref}`message-identitysettings.messageretention`)
* `keycloak` ({ref}`message-identitysettings.keycloak`)

::::::{card}
(message-identitysettings.autoacceptinvitation)=
#### IdentitySettings.AutoAcceptInvitation

**Fields:**
* `auto_accept_introduction` (bool - *auto accept introductions (a trusted contact pushed a new contact)*)
* `auto_accept_group` (bool - *auto accept invitations to a group*)
* `auto_accept_one_to_one` (bool - *auto accept contact invitations to one to one discussions*)
* `auto_accept_invitation` (bool - *auto accept olvid invitations (mind this will only accept invitation and not exchange sas code for you)*)
::::::

::::::{card}
(message-identitysettings.messageretention)=
#### IdentitySettings.MessageRetention

**Fields:**
* `existence_duration` (uint64 - *if set, message older than *existence_duration* seconds will be deleted
set to 0 to disable*)
* `discussion_count` (uint64 - *if set, if a discussion has more than *discussion_count* messages, older messages will be deleted.
set to 0 to disable*)
* `global_count` (uint64 - *if set, if identity has more than *global_count* messages, older messages will be deleted.
set to 0 to disable*)
* `clean_locked_discussions` (bool - *if true, messages in locked discussions will be deleted.*)
* `preserve_is_sharing_location_messages` (bool - *if true, live sharing location messages will never be deleted.*)
::::::

::::::{card}
(message-identitysettings.keycloak)=
#### IdentitySettings.Keycloak

**Fields:**
* `auto_invite_new_members` (bool - *if true, directory will regularly be scanned to add new members as contacts.*)
::::::

:::::::
(message-discussionsettings)=
### DiscussionSettings

:::::::{card}
> Settings for a discussion. Those settings are shared with other contacts in this discussion.

**Fields:**
* `discussion_id` (uint64)
* `read_once` (bool - *are message read once*)
* `existence_duration` (uint64 - *if set, messages are destroyed after *existence_duration* seconds, 0 to disable*)
* `visibility_duration` (uint64 - *if set, messages are only visible for *visibility_duration* seconds, 0 to disable*)

:::::::

---

(file-storage)=
## Storage

> **Related Endpoints:**
> * **Command:** {ref}`service-storagecommandservice`


(message-storageelement)=
### StorageElement

:::::::{card}
> Daemon embed a key-value storage, accessible for clients.  
> Each client-key have it's own global storage space, and a dedicated storage space for each discussion (see DiscussionStorageCommandService).  
> StorageElement is used for global and discussion storage.

**Fields:**
* `key` (string)
* `value` (string)

:::::::
(message-storageelementfilter)=
### StorageElementFilter

:::::::{card}
> Filter storage elements by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `key_search` (**optional** string - *regexp filter applied on *key_search* field*)
* `value_search` (**optional** string - *regexp filter applied on *value_search* field*)

:::::::

---

(file-keycloak)=
## Keycloak

> **Related Endpoints:**
> * **Command:** {ref}`service-keycloakcommandservice`


(message-keycloakuser)=
### KeycloakUser

:::::::{card}
> One of your directory user.

**Fields:**
* `keycloak_id` (string - *unique identifier for directory, to use to add this user as a contact*)
* `display_name` (string - *name computed from details*)
* `details` ({ref}`message-identitydetails` - *full identity details*)
* `contact_id` (**optional** uint64 - *filled if this user is already a contact, else set to 0*)

:::::::
(message-keycloakuserfilter)=
### KeycloakUserFilter

:::::::{card}
> Filter keycloak users by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `contact` (**optional** {ref}`enum-keycloakuserfilter.contact` - *is user a contact or not*)
* `display_name_search` (**optional** string - *regexp filter on *display_name* field*)
* `details_search` (**optional** {ref}`message-identitydetails` - *a set of regexp filters, one for each field of *details**)

::::::{card}
(enum-keycloakuserfilter.contact)=
#### KeycloakUserFilter.Contact

**Enum Values:**
* `CONTACT_UNSPECIFIED`: 0
* `CONTACT_IS`: 1
* `CONTACT_IS_NOT`: 2
::::::

:::::::

---

(file-call)=
## Call

> **Related Endpoints:**
> * **Command:** {ref}`service-callcommandservice`
> * **Notification:** {ref}`service-callnotificationservice`


(message-callparticipantid)=
### CallParticipantId

:::::::{card}
> Identify a call participant by its contact id, or a random identifier if it is not a contact.

**Fields:**
* **Oneof `id`**:
  * `contact_id` (uint64)
  * `participant_id` (string)

:::::::

---

(file-backup)=
## Backup

> **Related Endpoints:**
> * **Admin:** {ref}`service-backupadminservice`


(message-backup)=
### Backup

:::::::{card}
> Describe a full backup obtained with a backup key.  
> A backup contains multiple parts.  
> The AdminBackup contains the admin client keys and the elements contained in the global daemon storage.  
> A backup may contain multiple profile backups (one per identity), and each may contain one or more snapshots.  
> A profile snapshot contains an identity, its discussions, contacts, groups, client keys, and discussion storage.  
>   
> Note: a backup does not contain any messages or attachments.

**Fields:**
* `admin_backup` ({ref}`message-backup.adminbackup`)
* `profile_backups` (**repeated** {ref}`message-backup.profilebackup`)

::::::{card}
(message-backup.adminbackup)=
#### Backup.AdminBackup

**Fields:**
* `admin_client_key_count` (uint64)
* `storage_elements_count` (uint64)
::::::

::::::{card}
(message-backup.profilebackup)=
#### Backup.ProfileBackup

**Fields:**
* `profile_display_name` (string)
* `already_exists_locally` (bool)
* `keycloak_managed` (bool)
* `snapshots` (**repeated** {ref}`message-backup.profilebackup.snapshot`)
::::::

:::::{card}
(message-backup.profilebackup.snapshot)=
##### Backup.ProfileBackup.Snapshot

**Fields:**
* `id` (string - *id to specify to restore an identity backup*)
* `timestamp` (uint64)
* `from_device_name` (string)
* `contact_count` (uint64)
* `group_count` (uint64)
* `client_key_count` (uint64)
* `storage_elements_count` (uint64)
* `identity_settings` ({ref}`message-identitysettings`)
:::::

:::::::