# Datatypes

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

:::::::{card}
> An Olvid message posted in a discussion.  
> Sent message are Outbound, received messages are Inbound.  
> Messages must have a body and/or one or more attachment.

**Fields:**
* `id` ({ref}`datatype-messageid` - *the message unique identifier*)
* `discussion_id` (uint64 - *the discussion the message belongs to*)
* `sender_id` (uint64 - *set to a contact_id, or 0 if you sent the message*)
* `body` (string - *text body*)
* `sort_index` (double - *index used to sort messages in a discussion*)
* `timestamp` (uint64 - *the timestamp on which the message was received*)
* `attachments_count` (uint64 - *number of attachments for this message*)
* `replied_message_id` (**optional** {ref}`datatype-messageid` - *set if this message is a reply to another message in this discussion*)
* `message_location` (**optional** {ref}`datatype-messagelocation` - *set if this message is a location message*)
* `reactions` (**repeated** {ref}`datatype-messagereaction` - *list of the reactions added on this message*)
* `forwarded` (bool - *does this message have been forwarded from another discussion by sender*)
* `edited_body` (bool - *does this message body have been edited*)

:::::::
(datatype-messageid)=
### MessageId

:::::::{card}
> A composite id to uniquely identify a message.

**Fields:**
* `type` ({ref}`datatype-messageid.type` - *inbound or outbound message*)
* `id` (uint64)

::::::{card}
(datatype-messageid.type)=
#### MessageId.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INBOUND`: 1 - *received message*
* `TYPE_OUTBOUND`: 2 - *sent message*

::::::
:::::::
(datatype-messageephemerality)=
### MessageEphemerality

:::::::{card}
> Describe message ephemerality.

**Fields:**
* `read_once` (bool - *message can only be read once (destroyed when discusion is closed)*)
* `existence_duration` (uint64 - *message in destroyed after this duration, in seconds*)
* `visibility_duration` (uint64 - *message is only visible for this duration, in seconds

seconds*)

:::::::
(datatype-messagereaction)=
### MessageReaction

:::::::{card}
> Describe a reaction to a message, by a contact or yourself.

**Fields:**
* `contact_id` (uint64 - *set to 0 for owned reactions*)
* `reaction` (string - *reaction emoji*)
* `timestamp` (uint64 - *the timestamp at which the reaction was added.*)

:::::::
(datatype-messagelocation)=
### MessageLocation

:::::::{card}
> A location message content.  
> There are two location message families:  
> - location sending: send a specific location.  
> - location sharing: share someone's location for a given duration.

**Fields:**
* `type` ({ref}`datatype-messagelocation.locationtype`)
* `timestamp` (uint64 - *sending: when location was sent
sharing: the last location update timestamp*)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float - *the accuracy this location was recorded with.*)
* `address` (**optional** string - *optionally set for sending, a human readable address for this location*)

::::::{card}
(datatype-messagelocation.locationtype)=
#### MessageLocation.LocationType

**Enum Values:**
* `LOCATION_TYPE_UNSPECIFIED`: 0
* `LOCATION_TYPE_SEND`: 1 - *a one shot location sending*
* `LOCATION_TYPE_SHARING`: 2 - *a live location sharing*
* `LOCATION_TYPE_SHARING_FINISHED`: 3 - *a completed location sharing*

::::::
:::::::
(datatype-messagefilter)=
### MessageFilter

:::::::{card}
> Filter messages by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`datatype-messageid.type` - *is message inbound or outbound*)
* `discussion_id` (**optional** uint64 - *does message belongs to a specific discussion*)
* `sender_contact_id` (**optional** uint64 - *is message sent by a specific contact*)
* `body_search` (**optional** string - *regexp filter on *body* field*)
* `attachment` (**optional** {ref}`datatype-messagefilter.attachment` - *does message have attachments or not*)
* `location` (**optional** {ref}`datatype-messagefilter.location` - *is message a location message*)
* `min_timestamp` (**optional** uint64 - *is timestamp less or equal than *min_timestamp**)
* `max_timestamp` (**optional** uint64 - *is timestamp more or equal than *max_timestamp**)
* `has_reaction` (**optional** {ref}`datatype-messagefilter.reaction` - *does message have reactions or not*)
* `reactions_filter` (**repeated** {ref}`datatype-reactionfilter` - *message must have at least one matching reaction for each *reactions_filter**)
* **Oneof `reply`**:
  * `reply_to_a_message` (bool - *is message a reply to another message*)
  * `do_not_reply_to_a_message` (bool - *is message not a reply to a message*)
  * `replied_message_id` ({ref}`datatype-messageid` - *is message a reply to a specific message id*)

::::::{card}
(datatype-messagefilter.attachment)=
#### MessageFilter.Attachment

**Enum Values:**
* `ATTACHMENT_UNSPECIFIED`: 0
* `ATTACHMENT_HAVE`: 1
* `ATTACHMENT_HAVE_NOT`: 2

::::::
::::::{card}
(datatype-messagefilter.location)=
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
(datatype-messagefilter.reaction)=
#### MessageFilter.Reaction

**Enum Values:**
* `REACTION_UNSPECIFIED`: 0
* `REACTION_HAS`: 1
* `REACTION_HAS_NOT`: 2

::::::
:::::::
(datatype-reactionfilter)=
### ReactionFilter

:::::::{card}
**Fields:**
* **Oneof `reacted_by`**:
  * `reacted_by_me` (bool - *is the reaction from yourself*)
  * `reacted_by_contact_id` (uint64 - *is the reaction from a specific contact*)
* `reaction` (**optional** string - *is *reaction* equal to the *reaction* field*)

:::::::

---

(datatype-attachment)=
## Attachment

> **Related Endpoints:**
> * **Command:** {ref}`service-attachmentcommandservice`
> * **Notification:** {ref}`service-attachmentnotificationservice`


### Attachment

:::::::{card}
> An attachment represents a file attached to a message.  
> It is associated to a *message_id* and a *discussion_id*.  
>   
> Link previews are attachments with specific mime type: *olvid/link-preview*.

**Fields:**
* `id` ({ref}`datatype-attachmentid`)
* `discussion_id` (uint64)
* `message_id` ({ref}`datatype-messageid`)
* `file_name` (string)
* `mime_type` (string)
* `size` (uint64 - *file size in bytes*)

:::::::
(datatype-attachmentid)=
### AttachmentId

:::::::{card}
> A composite id to uniquely identify an attachment.

**Fields:**
* `type` ({ref}`datatype-attachmentid.type` - *inbound or outbound attachment*)
* `id` (uint64)

::::::{card}
(datatype-attachmentid.type)=
#### AttachmentId.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_INBOUND`: 1 - *received attachments*
* `TYPE_OUTBOUND`: 2 - *sent attachments*

::::::
:::::::
(datatype-attachmentfilter)=
### AttachmentFilter

:::::::{card}
> Filter attachments by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`datatype-attachmentid.type` - *select only INBOUND or OUTBOUND attachments*)
* `file_type` (**optional** {ref}`datatype-attachmentfilter.filetype` - *filter by file type (pre-defined regexp for *mime_type*)*)
* `discussion_id` (**optional** uint64)
* `message_id` (**optional** {ref}`datatype-messageid` - *optional uint64 contact_id = 4; not implementable now*)
* `filename_search` (**optional** string - *regexp filter on *filename* field*)
* `mime_type_search` (**optional** string - *regexp filter on *mime_type* field*)
* `min_size` (**optional** uint64 - *minimum or equal file size*)
* `max_size` (**optional** uint64 - *maximum or equal file size*)

::::::{card}
(datatype-attachmentfilter.filetype)=
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

(datatype-discussion)=
## Discussion

> **Related Endpoints:**
> * **Command:** {ref}`service-discussioncommandservice`
> * **Notification:** {ref}`service-discussionnotificationservice`


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
(datatype-discussionfilter)=
### DiscussionFilter

:::::::{card}
> Filter discussions by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`datatype-discussionfilter.type` - *select group or contact discussions*)
* **Oneof `identifier`**:
  * `contact_id` (uint64)
  * `group_id` (uint64)
* `title_search` (**optional** string - *regexp filter on title field*)

::::::{card}
(datatype-discussionfilter.type)=
#### DiscussionFilter.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_OTO`: 1
* `TYPE_GROUP`: 2

::::::
:::::::

---

(datatype-contact)=
## Contact

> **Related Endpoints:**
> * **Command:** {ref}`service-contactcommandservice`
> * **Notification:** {ref}`service-contactnotificationservice`


### Contact

:::::::{card}
> A contact is an other olvid identity you are in contact with.  
> A contact can have an associated discussion if has_one_to_one_discussion is true, else it's probably a collected contact you met in a group discussion.  
> If keycloak_managed managed contact is registered on the same keycloak.

**Fields:**
* `id` (uint64)
* `display_name` (string - *computed from *details**)
* `details` ({ref}`datatype-identitydetails`)
* `established_channel_count` (uint32 - *shall be equal to device_count to exchange messages*)
* `device_count` (uint32)
* `has_one_to_one_discussion` (bool)
* `has_a_photo` (bool)
* `keycloak_managed` (bool)

:::::::
(datatype-contactfilter)=
### ContactFilter

:::::::{card}
> Filter contacts by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `one_to_one` (**optional** {ref}`datatype-contactfilter.onetoone` - *select only contacts with or without one to one discussions*)
* `photo` (**optional** {ref}`datatype-contactfilter.photo` - *select only contacts with or without profile photo*)
* `keycloak` (**optional** {ref}`datatype-contactfilter.keycloak` - *select only contacts registered or not on you keycloak*)
* `display_name_search` (**optional** string - *regexp filter on *display_name**)
* `details_search` (**optional** {ref}`datatype-identitydetails` - *a set of regexp filters, one for each field of *details**)

::::::{card}
(datatype-contactfilter.onetoone)=
#### ContactFilter.OneToOne

**Enum Values:**
* `ONE_TO_ONE_UNSPECIFIED`: 0
* `ONE_TO_ONE_IS`: 1
* `ONE_TO_ONE_IS_NOT`: 2

::::::
::::::{card}
(datatype-contactfilter.photo)=
#### ContactFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS`: 1
* `PHOTO_HAS_NOT`: 2

::::::
::::::{card}
(datatype-contactfilter.keycloak)=
#### ContactFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_MANAGED`: 1
* `KEYCLOAK_NOT_MANAGED`: 2

::::::
:::::::

---

(datatype-group)=
## Group

> **Related Endpoints:**
> * **Command:** {ref}`service-groupcommandservice`
> * **Notification:** {ref}`service-groupnotificationservice`


### Group

:::::::{card}
> An Olvid group.  
> *keycloak_managed* groups are not editable, and you cannot leave them. Group is managed from the keycloak admin console.

**Fields:**
* `id` (uint64)
* `type` ({ref}`datatype-group.type` - *specify a pre-set of permissions given to group members.*)
* `advanced_configuration` (**optional** {ref}`datatype-group.advancedconfiguration` - *only set if group.type is TYPE_ADVANCED*)
* `own_permissions` ({ref}`datatype-groupmemberpermissions` - *your permissions in this group*)
* `members` (**repeated** {ref}`datatype-groupmember` - *members that accepted invitation*)
* `pending_members` (**repeated** {ref}`datatype-pendinggroupmember` - *members invited to join group*)
* `update_in_progress` (bool - *group is locked, edition will be delayed*)
* `keycloak_managed` (bool - *group automatically pushed by keycloak*)
* `name` (string)
* `description` (string)
* `has_a_photo` (bool)

::::::{card}
(datatype-group.type)=
#### Group.Type

**Enum Values:**
* `TYPE_UNSPECIFIED`: 0
* `TYPE_STANDARD`: 1 - *all members are admin*
* `TYPE_CONTROLLED`: 2 - *non admin members cannot manage the group*
* `TYPE_READ_ONLY`: 3 - *only admin members can post messages*
* `TYPE_ADVANCED`: 4 - *specify an advanced configuration field*

::::::
::::::{card}
(datatype-group.advancedconfiguration)=
#### Group.AdvancedConfiguration

**Fields:**
* `read_only` (bool - *is group read only*)
* `remote_delete` ({ref}`datatype-group.advancedconfiguration.remotedelete` - *who has permission to delete message for everyone*)

:::::{card}
(datatype-group.advancedconfiguration.remotedelete)=
##### Group.AdvancedConfiguration.RemoteDelete

**Enum Values:**
* `REMOTE_DELETE_UNSPECIFIED`: 0
* `REMOTE_DELETE_NOBODY`: 1
* `REMOTE_DELETE_ADMINS`: 2
* `REMOTE_DELETE_EVERYONE`: 3

:::::
::::::
:::::::
(datatype-groupmember)=
### GroupMember

:::::::{card}
> Associate a contact, member of a group, with its permissions in this group.

**Fields:**
* `contact_id` (uint64)
* `permissions` ({ref}`datatype-groupmemberpermissions`)

:::::::
(datatype-pendinggroupmember)=
### PendingGroupMember

:::::::{card}
> Member of a group who has not yet accepted the invitation to join the group.

**Fields:**
* `pending_member_id` (uint64 - *unique identifier*)
* `contact_id` (uint64 - *set to 0 if this identity is not a contact yet*)
* `display_name` (string - *computed display name from their identity details.*)
* `declined` (bool - *does pending member declined invitation*)
* `permissions` ({ref}`datatype-groupmemberpermissions` - *permissions given to this member*)

:::::::
(datatype-groupmemberpermissions)=
### GroupMemberPermissions

:::::::{card}
> Describe permission set associated to any group member.

**Fields:**
* `admin` (bool - *can edit the group (change name or description, and manage group members)*)
* `remote_delete_anything` (bool - *can delete everywhere someone's else message*)
* `edit_or_remote_delete_own_messages` (bool - *can edit or delete everywhere own messages*)
* `change_settings` (bool - *can change discussion shared settings (message ephemerality)*)
* `send_message` (bool - *can post message in the group discussion*)

:::::::
(datatype-groupfilter)=
### GroupFilter

:::::::{card}
> Filter groups by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `type` (**optional** {ref}`datatype-group.type`)
* `empty` (**optional** {ref}`datatype-groupfilter.empty` - *does group have members or not*)
* `photo` (**optional** {ref}`datatype-groupfilter.photo` - *does group have a photo or not*)
* `keycloak` (**optional** {ref}`datatype-groupfilter.keycloak` - *is group keycloak managed or not*)
* `own_permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter` - *filter on your own permissions in the group*)
* `name_search` (**optional** string - *regexp filter on *name_search* field*)
* `description_search` (**optional** string - *regexp filter on *description_search* field*)
* `member_filters` (**repeated** {ref}`datatype-groupmemberfilter` - *group must have at least one matching member for each *member_filters**)
* `pending_member_filters` (**repeated** {ref}`datatype-pendinggroupmemberfilter` - *group must have at least one pending member matching each *pending_member_filters**)

::::::{card}
(datatype-groupfilter.empty)=
#### GroupFilter.Empty

**Enum Values:**
* `EMPTY_UNSPECIFIED`: 0
* `EMPTY_IS_NOT`: 1
* `EMPTY_IS`: 2

::::::
::::::{card}
(datatype-groupfilter.keycloak)=
#### GroupFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_IS_NOT`: 1
* `KEYCLOAK_IS`: 2

::::::
::::::{card}
(datatype-groupfilter.photo)=
#### GroupFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS_NOT`: 1
* `PHOTO_HAS`: 2

::::::
:::::::
(datatype-groupmemberfilter)=
### GroupMemberFilter

:::::::{card}
**Fields:**
* `contact_id` (**optional** uint64 - *is member a specific contact*)
* `permissions` (**optional** {ref}`datatype-grouppermissionfilter` - *does member's permissions match this permission filter*)

:::::::
(datatype-pendinggroupmemberfilter)=
### PendingGroupMemberFilter

:::::::{card}
**Fields:**
* `is_contact` (**optional** {ref}`datatype-pendinggroupmemberfilter.contact` - *is pending member a contact or not*)
* `has_declined` (**optional** {ref}`datatype-pendinggroupmemberfilter.declined` - *does pending member declined invitation or not*)
* `contact_id` (**optional** uint64 - *is pending member a specific known contact*)
* `display_name_search` (**optional** string - *regexp filter applied on *display_name* field*)
* `permissions` (**optional** {ref}`datatype-grouppermissionfilter` - *pending member's permissions match this permission filter*)

::::::{card}
(datatype-pendinggroupmemberfilter.contact)=
#### PendingGroupMemberFilter.Contact

**Enum Values:**
* `CONTACT_UNSPECIFIED`: 0
* `CONTACT_IS`: 1
* `CONTACT_IS_NOT`: 2

::::::
::::::{card}
(datatype-pendinggroupmemberfilter.declined)=
#### PendingGroupMemberFilter.Declined

**Enum Values:**
* `DECLINED_UNSPECIFIED`: 0
* `DECLINED_HAS`: 1
* `DECLINED_HAS_NOT`: 2

::::::
:::::::
(datatype-grouppermissionfilter)=
### GroupPermissionFilter

:::::::{card}
**Fields:**
* `admin` (**optional** {ref}`datatype-grouppermissionfilter.admin` - *is user a group admin or not*)
* `send_message` (**optional** {ref}`datatype-grouppermissionfilter.sendmessage` - *does user can post message in discussion*)
* `remote_delete_anything` (**optional** {ref}`datatype-grouppermissionfilter.remotedeleteanything` - *does user can remote delete any message, even other members messages*)
* `edit_or_remote_delete_own_messages` (**optional** {ref}`datatype-grouppermissionfilter.editorremotedeleteownmessage` - *does user can edit or remote delete its messages*)
* `change_settings` (**optional** {ref}`datatype-grouppermissionfilter.changesettings` - *does user can change group settings*)

::::::{card}
(datatype-grouppermissionfilter.admin)=
#### GroupPermissionFilter.Admin

**Enum Values:**
* `ADMIN_UNSPECIFIED`: 0
* `ADMIN_IS`: 1
* `ADMIN_IS_NOT`: 2

::::::
::::::{card}
(datatype-grouppermissionfilter.sendmessage)=
#### GroupPermissionFilter.SendMessage

**Enum Values:**
* `SEND_MESSAGE_UNSPECIFIED`: 0
* `SEND_MESSAGE_CAN`: 1
* `SEND_MESSAGE_CANNOT`: 2

::::::
::::::{card}
(datatype-grouppermissionfilter.remotedeleteanything)=
#### GroupPermissionFilter.RemoteDeleteAnything

**Enum Values:**
* `REMOTE_DELETE_ANYTHING_UNSPECIFIED`: 0
* `REMOTE_DELETE_ANYTHING_CAN`: 1
* `REMOTE_DELETE_ANYTHING_CANNOT`: 2

::::::
::::::{card}
(datatype-grouppermissionfilter.editorremotedeleteownmessage)=
#### GroupPermissionFilter.EditOrRemoteDeleteOwnMessage

**Enum Values:**
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_UNSPECIFIED`: 0
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CAN`: 1
* `EDIT_OR_REMOTE_DELETE_OWN_MESSAGE_CANNOT`: 2

::::::
::::::{card}
(datatype-grouppermissionfilter.changesettings)=
#### GroupPermissionFilter.ChangeSettings

**Enum Values:**
* `CHANGE_SETTINGS_UNSPECIFIED`: 0
* `CHANGE_SETTINGS_CAN`: 1
* `CHANGE_SETTINGS_CANNOT`: 2

::::::
:::::::

---

(datatype-identity)=
## Identity

> **Related Endpoints:**
> * **Command:** {ref}`service-identitycommandservice`
> * **Admin:** {ref}`service-identityadminservice`


### Identity

:::::::{card}
> Your own Olvid identity, stored on this daemon instance.  
> A daemon can manage multiple Olvid identities.

**Fields:**
* `id` (uint64)
* `display_name` (string - *computed from *details**)
* `details` ({ref}`datatype-identitydetails`)
* `invitation_url` (***deprecated*** string - *TODO TODEL !!!!*)
* `keycloak_managed` (bool - *identity is linked to a keycloak directory*)
* `has_a_photo` (bool)
* `api_key` ({ref}`datatype-identity.apikey` - *Olvid api key to grant permissions*)

::::::{card}
(datatype-identity.apikey)=
#### Identity.ApiKey

**Fields:**
* `permission` ({ref}`datatype-identity.apikey.permission`)
* `expiration_timestamp` (uint64)

:::::{card}
(datatype-identity.apikey.permission)=
##### Identity.ApiKey.Permission

**Fields:**
* `call` (bool)
* `multi_device` (bool)

:::::
::::::
:::::::
(datatype-identitydetails)=
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
(datatype-identityfilter)=
### IdentityFilter

:::::::{card}
> Filter identities by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `keycloak` (**optional** {ref}`datatype-identityfilter.keycloak` - *is identity keycloak managed or not*)
* `photo` (**optional** {ref}`datatype-identityfilter.photo` - *does identity have a profile photo or not*)
* `api_key` (**optional** {ref}`datatype-identityfilter.apikey` - *does identity have an Olvid api key or not*)
* `display_name_search` (**optional** string - *regexp filter on *display_name**)
* `details_search` (**optional** {ref}`datatype-identitydetails` - *a set of regexp filters, one for each field of *details**)

::::::{card}
(datatype-identityfilter.keycloak)=
#### IdentityFilter.Keycloak

**Enum Values:**
* `KEYCLOAK_UNSPECIFIED`: 0
* `KEYCLOAK_IS_NOT`: 1
* `KEYCLOAK_IS`: 2

::::::
::::::{card}
(datatype-identityfilter.photo)=
#### IdentityFilter.Photo

**Enum Values:**
* `PHOTO_UNSPECIFIED`: 0
* `PHOTO_HAS_NOT`: 1
* `PHOTO_HAS`: 2

::::::
::::::{card}
(datatype-identityfilter.apikey)=
#### IdentityFilter.ApiKey

**Enum Values:**
* `API_KEY_UNSPECIFIED`: 0
* `API_KEY_HAS_NOT`: 1
* `API_KEY_HAS`: 2

::::::
:::::::

---

(datatype-client_key)=
## Client_Key

> **Related Endpoints:**
> * **Admin:** {ref}`service-clientkeyadminservice`


(datatype-clientkey)=
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
(datatype-clientkeyfilter)=
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

(datatype-invitation)=
## Invitation

> **Related Endpoints:**
> * **Command:** {ref}`service-invitationcommandservice`
> * **Notification:** {ref}`service-invitationnotificationservice`


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
* `status` ({ref}`datatype-invitation.status` - *current protocol step*)
* `display_name` (string - *display name of the other identity or the group name*)
* `timestamp` (uint64 - *latest status update timestamp*)
* `sas` (**optional** string - *only set for STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE and STATUS_INVITATION_WAIT_IT_FOR_SAS_EXCHANGE
four digit code to give to the other in an invitation protocol*)
* `mediatorId` (**optional** uint64 - *introductions protocol only
the contact id of the person who initiated introduction protocol*)

::::::{card}
(datatype-invitation.status)=
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
(datatype-invitationfilter)=
### InvitationFilter

:::::::{card}
> Filter invitation by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `status` (**optional** {ref}`datatype-invitation.status` - *does invitation have a specific status*)
* `type` (**optional** {ref}`datatype-invitationfilter.type` - *does invitation belongs to a specific protocol*)
* `display_name_search` (**optional** string - *regexp filter on *display_name* field*)
* `min_timestamp` (**optional** uint64 - *is timestamp less or equal than *min_timestamp**)
* `max_timestamp` (**optional** uint64 - *is timestamp more or equal than *max_timestamp**)

::::::{card}
(datatype-invitationfilter.type)=
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

(datatype-settings)=
## Settings

> **Related Endpoints:**
> * **Command:** {ref}`service-settingscommandservice`


(datatype-identitysettings)=
### IdentitySettings

:::::::{card}
> Settings for an Identity managed by a daemon.  
> - AutoAcceptInvitation: when enabled the daemon will automatically accept incoming and existing invitations from specified protocol.  
> - MessageRetention: when at least one element is set daemon will regularly check if some message can be deleted, matching filled criteria. This allows to save space and save performances by keeping database as small as possible.  
> - Keycloak: directory related settings

**Fields:**
* `invitation` ({ref}`datatype-identitysettings.autoacceptinvitation`)
* `message_retention` ({ref}`datatype-identitysettings.messageretention`)
* `keycloak` ({ref}`datatype-identitysettings.keycloak`)

::::::{card}
(datatype-identitysettings.autoacceptinvitation)=
#### IdentitySettings.AutoAcceptInvitation

**Fields:**
* `auto_accept_introduction` (bool - *auto accept introductions (a trusted contact pushed a new contact)*)
* `auto_accept_group` (bool - *auto accept invitations to a group*)
* `auto_accept_one_to_one` (bool - *auto accept contact invitations to one to one discussions*)
* `auto_accept_invitation` (bool - *auto accept olvid invitations (mind this will only accept invitation and not exchange sas code for you)*)

::::::
::::::{card}
(datatype-identitysettings.messageretention)=
#### IdentitySettings.MessageRetention

**Fields:**
* `existence_duration` (uint64 - *if set, message older than *existence_duration* seconds will be deleted
set to 0 to disable*)
* `discussion_count` (uint64 - *if set, if a discussion has more than *discussion_count* messages, older messages will be deleted.
set to 0 to disable*)
* `global_count` (uint64 - *if set, if identty has more than *global_count* messages, older messages will be deleted.
set to 0 to disable*)
* `clean_locked_discussions` (bool - *if true, messages in locked discussions will be deleted.*)
* `preserve_is_sharing_location_messages` (bool - *if true, live sharing location messages will never be deleted.*)

::::::
::::::{card}
(datatype-identitysettings.keycloak)=
#### IdentitySettings.Keycloak

**Fields:**
* `auto_invite_new_members` (bool - *if true, directory will regularly be scanned to add new members as contacts.*)

::::::
:::::::
(datatype-discussionsettings)=
### DiscussionSettings

:::::::{card}
> Settings for a discussion. Those settings are shared with other contacts in this discussion.

**Fields:**
* `discussion_id` (uint64)
* `read_once` (bool - *are message read once*)
* `existence_duration` (uint64 - *if set, message are destroyed after *existence_duration* seconds, 0 to disable*)
* `visibility_duration` (uint64 - *if set, message are only visible for *visibility_duration* seconds, 0 to disable*)

:::::::

---

(datatype-storage)=
## Storage

> **Related Endpoints:**
> * **Command:** {ref}`service-storagecommandservice`


(datatype-storageelement)=
### StorageElement

:::::::{card}
> Daemon embed a key-value storage, accessible for clients.  
> Each client-key have it's own global storage space, and a dedicated storage space for each discussion (see DiscussionStorageCommandService).  
> StorageElement is used for global and discussion storage.

**Fields:**
* `key` (string)
* `value` (string)

:::::::
(datatype-storageelementfilter)=
### StorageElementFilter

:::::::{card}
> Filter storage elements by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `key_search` (**optional** string - *regexp filter applied on *key_search* field*)
* `value_search` (**optional** string - *regexp filter applied on *value_search* field*)

:::::::

---

(datatype-keycloak)=
## Keycloak

> **Related Endpoints:**
> * **Command:** {ref}`service-keycloakcommandservice`


(datatype-keycloakuser)=
### KeycloakUser

:::::::{card}
> One of your directory user.

**Fields:**
* `keycloak_id` (string - *unique identifier for directory, to use to add this user as a contact*)
* `display_name` (string - *name computed from details*)
* `details` ({ref}`datatype-identitydetails` - *full identity details*)
* `contact_id` (**optional** uint64 - *filled if this user is already a contact, else set to 0*)

:::::::
(datatype-keycloakuserfilter)=
### KeycloakUserFilter

:::::::{card}
> Filter keycloak users by attributes.  
> To pass a filter an element must match all specified conditions.

**Fields:**
* `contact` (**optional** {ref}`datatype-keycloakuserfilter.contact` - *is user a contact or not*)
* `display_name_search` (**optional** string - *regexp filter on *display_name* field*)
* `details_search` (**optional** {ref}`datatype-identitydetails` - *a set of regexp filters, one for each field of *details**)

::::::{card}
(datatype-keycloakuserfilter.contact)=
#### KeycloakUserFilter.Contact

**Enum Values:**
* `CONTACT_UNSPECIFIED`: 0
* `CONTACT_IS`: 1
* `CONTACT_IS_NOT`: 2

::::::
:::::::

---

(datatype-call)=
## Call

> **Related Endpoints:**
> * **Command:** {ref}`service-callcommandservice`
> * **Notification:** {ref}`service-callnotificationservice`


(datatype-callparticipantid)=
### CallParticipantId

:::::::{card}
> Identify a call participant by it's contact id, or a random identifier if it is not a contact.

**Fields:**
* **Oneof `id`**:
  * `contact_id` (uint64)
  * `participant_id` (string)

:::::::

---

(datatype-backup)=
## Backup

> **Related Endpoints:**
> * **Admin:** {ref}`service-backupadminservice`


### Backup

:::::::{card}
> Describe a full backup obtained with a backup key.  
> A backup contains multiple parts.  
> The AdminBackup contains the admin client keys and the elements contained in the global daemon storage.  
> A backup may contains multiple profile backup (one per identity), and each may contains one or more snapshot.  
> A profile snapshot contains an identity it's discussion, contacts, groups, client keys, and discussion storage.  
>   
> Mind a backup does not contain any message or attachment.

**Fields:**
* `admin_backup` ({ref}`datatype-backup.adminbackup`)
* `profile_backups` (**repeated** {ref}`datatype-backup.profilebackup`)

::::::{card}
(datatype-backup.adminbackup)=
#### Backup.AdminBackup

**Fields:**
* `admin_client_key_count` (uint64)
* `storage_elements_count` (uint64)

::::::
::::::{card}
(datatype-backup.profilebackup)=
#### Backup.ProfileBackup

**Fields:**
* `profile_display_name` (string)
* `already_exists_locally` (bool)
* `keycloak_managed` (bool)
* `snapshots` (**repeated** {ref}`datatype-backup.profilebackup.snapshot`)

:::::{card}
(datatype-backup.profilebackup.snapshot)=
##### Backup.ProfileBackup.Snapshot

**Fields:**
* `id` (string - *id to specify to restore an identity backup*)
* `timestamp` (uint64)
* `from_device_name` (string)
* `contact_count` (uint64)
* `group_count` (uint64)
* `client_key_count` (uint64)
* `storage_elements_count` (uint64)
* `identity_settings` ({ref}`datatype-identitysettings`)

:::::
::::::
:::::::