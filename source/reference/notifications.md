# Notifications

Events you can subscribe to, and notification content.

:::{contents} Notifications
:depth: 1
:local:
:::
(service-messagenotificationservice)=
## Message Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-message`
:::
### MessageReceived
:::{card}
> Receive a notification when an you received a new message.

**Subscription**: *SubscribeToMessageReceivedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageReceivedNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### MessageSent
:::{card}
> Receive a notification when an you sent a new message.

**Subscription**: *SubscribeToMessageSentNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageSentNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### MessageDeleted
:::{card}
> Receive a notification when a message has been deleted.  
> This can arrive under different circumstances:  
> - you deleted a message locally  
> - someone else deleted it's own message for everyone in the discussion

**Subscription**: *SubscribeToMessageDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageDeletedNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageBodyUpdated
:::{card}
> datatypes.v1.Message updates

**Subscription**: *SubscribeToMessageBodyUpdatedNotification*
MessageBodyUpdated
Receive a notification when a message text body have been updated.
Only the message sender can edit its own messages.

**Error codes**:
`NOT_FOUND`: at least one of _message_ids_ does not exists.
`UNAUTHENTICATED`: client key is invalid.

* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageBodyUpdatedNotification*
* `message` ({ref}`datatype-message`)
* `previous_body` (string)

:::

### MessageUploaded
:::{card}
> Receive a notification when an outbound message have been uploaded on server.  
> Note: You cannot guarantee this notification will arrive when working with ephemeral message

**Subscription**: *SubscribeToMessageUploadedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageUploadedNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `INVALID_ARGUMENT`: at least one of _message_ids_ is not an outbound message.
 - `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageDelivered
:::{card}
> Receive a notification when an outbound message have been delivered on at least one recipient's device.  
> Note: You cannot guarantee this notification will arrive when working with ephemeral message

**Subscription**: *SubscribeToMessageDeliveredNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageDeliveredNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `INVALID_ARGUMENT`: at least one of _message_ids_ is not an outbound message.
 - `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageRead
:::{card}
> Receive a notification when an outbound message have been read by at least one recipient.  
> Note: You cannot guarantee this notification will arrive when working with ephemeral message

**Subscription**: *SubscribeToMessageReadNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageReadNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `INVALID_ARGUMENT`: at least one of _message_ids_ is not an outbound message.
 - `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageLocationReceived
:::{card}
> location message

**Subscription**: *SubscribeToMessageLocationReceivedNotification*
MessageLocationReceived
Receive a notification when you received a location message.
Location messages are different from location sharing messages as they contains one static position.
A received location message also triggers the MessageReceived notification.

**Error codes**:
`UNAUTHENTICATED`: client key is invalid.

* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageLocationReceivedNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageLocationSent
:::{card}
> Receive a notification when you sent a location message.  
> Location messages are different from location sharing messages as they contains one static position.  
> A sent location message also triggers the MessageSent notification.

**Subscription**: *SubscribeToMessageLocationSentNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageLocationSentNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### MessageLocationSharingStart
:::{card}
> Receive a notification when you sent or you received a new location sharing message.  
> Location sharing messages are supposed to be updated for a given while.  
> A new location sharing message also triggers the MessageReceived or MessageSent notification.

**Subscription**: *SubscribeToMessageLocationSharingStartNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageLocationSharingStartNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### MessageLocationSharingUpdate
:::{card}
> Receive a notification when a location sharing message have been updated with a new location.  
> This might concern inbound or outbound messages.

**Subscription**: *SubscribeToMessageLocationSharingUpdateNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageLocationSharingUpdateNotification*
* `message` ({ref}`datatype-message`)
* `previous_location` ({ref}`datatype-messagelocation`)

**Error Codes**:
- `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `INVALID_ARGUMENT`: one of _message_ids_ is not a live location sharing.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageLocationSharingEnd
:::{card}
> Receive a notification when a location sharing message have been stopped or automatically finished.  
> This might concern inbound or outbound messages.

**Subscription**: *SubscribeToMessageLocationSharingEndNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)

**Notification *(Stream)***: *MessageLocationSharingEndNotification*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `INVALID_ARGUMENT`: one of _message_ids_ is not a live location sharing.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageReactionAdded
:::{card}
> datatypes.v1.Message reactions

**Subscription**: *SubscribeToMessageReactionAddedNotification*
MessageReactionAdded
Receive a notification when a reaction was added to a message.
It can concern your reactions or any contact reactions.

**Error codes**:
`NOT_FOUND`: at least one of _message_ids_ does not exists.
`UNAUTHENTICATED`: client key is invalid.

* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter` - *you will only receive notifications about reactions that match this filter.*)

**Notification *(Stream)***: *MessageReactionAddedNotification*
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)

:::

### MessageReactionUpdated
:::{card}
> Receive a notification when a reaction on a message was updated.  
> It can concern your reactions or any contact reactions.

**Subscription**: *SubscribeToMessageReactionUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `message_filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter` - *you will only receive notifications about reactions that match this filter.*)
* `previous_reaction_filter` (**optional** {ref}`datatype-reactionfilter` - *you will only receive notifications about reactions that match this filter, before update.*)

**Notification *(Stream)***: *MessageReactionUpdatedNotification*
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)
* `previous_reaction` ({ref}`datatype-messagereaction`)

**Error Codes**:
- `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### MessageReactionRemoved
:::{card}
> Receive a notification when a reaction on a message was removed.  
> It can concern your reactions or any contact reactions.

**Subscription**: *SubscribeToMessageReactionRemovedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`datatype-messagefilter` - *you will only receive notifications about messages that match this filter.*)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter` - *you will only receive notifications about reactions that match this filter.*)

**Notification *(Stream)***: *MessageReactionRemovedNotification*
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)

**Error Codes**:
- `NOT_FOUND`: at least one of _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-attachmentnotificationservice)=
## Attachment Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-attachment`
:::
### AttachmentReceived
:::{card}
> Receive a notification every time you receive an attachment in a discussion (one to one or group discussion).  
> When you receive a message with multiple attachments, you will receive one notification per attachment.

**Subscription**: *SubscribeToAttachmentReceivedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-attachmentfilter` - *you will only receive notifications about attachments that match all the filter params.*)

**Notification *(Stream)***: *AttachmentReceivedNotification*
* `attachment` ({ref}`datatype-attachment`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### AttachmentUploaded
:::{card}
> Receive a notification every time an attachment you sent have been marked as uploaded.  
> A message with attachments is delivered to recipients only when all attachments have been uploaded.

**Subscription**: *SubscribeToAttachmentUploadedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-attachmentfilter` - *you will only receive notifications about attachments that match all the filter params.*)
* `message_ids` (**repeated** {ref}`datatype-messageid` - *you will only receive notifications about attachments related to messages specified in this list.*)
* `attachment_ids` (**repeated** {ref}`datatype-attachmentid` - *you will only receive notifications about attachments specified in this list.*)

**Notification *(Stream)***: *AttachmentUploadedNotification*
* `attachment` ({ref}`datatype-attachment`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INVALID_ARGUMENT`: cannot subscribe for non outbound messages.
 - `NOT_FOUND`: at least one of _message_ids_ is incorrect.
:::

---

(service-discussionnotificationservice)=
## Discussion Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-discussion`
:::
### DiscussionNew
:::{card}
> Receive a notification each time a discussion is created or re-used.  
> This can arrive under different circumstances:  
> - a new contact was added  
> - you created or joined a group

**Subscription**: *SubscribeToDiscussionNewNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)

**Notification *(Stream)***: *DiscussionNewNotification*
* `discussion` ({ref}`datatype-discussion`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionLocked
:::{card}
> Receive a notification each time a discussion is locked.  
> This can arrive under different circumstances:  
> - the contact associated to this discussion was removed from your contact book  
> - you left the associated group or the group was disbanded

**Subscription**: *SubscribeToDiscussionLockedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)
* `discussion_ids` (**repeated** uint64 - *you will only receive notifications about discussions specified in this list.*)

**Notification *(Stream)***: *DiscussionLockedNotification*
* `discussion` ({ref}`datatype-discussion`)

**Error Codes**:
- `NOT_FOUND`: at least one of _discussion_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionTitleUpdated
:::{card}
> Receive a notification each time a discussion title changed.  
> This can arrive under different circumstances:  
> - the contact associated to this discussion changed it's details  
> - the associated group was renamed

**Subscription**: *SubscribeToDiscussionTitleUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)
* `discussion_ids` (**repeated** uint64 - *you will only receive notifications about discussions specified in this list.*)

**Notification *(Stream)***: *DiscussionTitleUpdatedNotification*
* `discussion` ({ref}`datatype-discussion`)
* `previous_title` (string)

**Error Codes**:
- `NOT_FOUND`: at least one of _discussion_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionSettingsUpdated
:::{card}
> Receive a notification each time the discussion shared settings have been updated.

**Subscription**: *SubscribeToDiscussionSettingsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)
* `discussion_ids` (**repeated** uint64 - *you will only receive notifications about discussions specified in this list.*)

**Notification *(Stream)***: *DiscussionSettingsUpdatedNotification*
* `discussion` ({ref}`datatype-discussion`)
* `new_settings` ({ref}`datatype-discussionsettings` - *the new current discussion settings*)
* `previous_settings` ({ref}`datatype-discussionsettings` - *settings before this update*)

**Error Codes**:
- `NOT_FOUND`: at least one of _discussion_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-contactnotificationservice)=
## Contact Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-contact`
:::
### ContactNew
:::{card}
> Receive a notification every time a contact is added to your contact book.

**Subscription**: *SubscribeToContactNewNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)

**Notification *(Stream)***: *ContactNewNotification*
* `contact` ({ref}`datatype-contact`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### ContactDeleted
:::{card}
> Receive a notification every time a contact is removed from your contact book.  
> This might happen if you manually removed contact, if he did, or if he deleted it's identity and chose to notify it's contact about it.

**Subscription**: *SubscribeToContactDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)
* `contact_ids` (**repeated** uint64 - *you will only receive notifications about contacts specified in this list.*)

**Notification *(Stream)***: *ContactDeletedNotification*
* `contact` ({ref}`datatype-contact`)

**Error Codes**:
- `NOT_FOUND`: at least one of _contact_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ContactDetailsUpdated
:::{card}
> Receive a notification each time a contact update it's identity details.  
> This implies that this contact display name changed.

**Subscription**: *SubscribeToContactDetailsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)
* `contact_ids` (**repeated** uint64 - *you will only receive notifications about contacts specified in this list.*)

**Notification *(Stream)***: *ContactDetailsUpdatedNotification*
* `contact` ({ref}`datatype-contact`)
* `previous_details` ({ref}`datatype-identitydetails`)

**Error Codes**:
- `NOT_FOUND`: at least one of _contact_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ContactPhotoUpdated
:::{card}
> Receive a notification each time a contact profile picture has been updated.

**Subscription**: *SubscribeToContactPhotoUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)
* `contact_ids` (**repeated** uint64 - *you will only receive notifications about contacts specified in this list.*)

**Notification *(Stream)***: *ContactPhotoUpdatedNotification*
* `contact` ({ref}`datatype-contact`)

**Error Codes**:
- `NOT_FOUND`: at least one of _contact_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-groupnotificationservice)=
## Group Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-group`
:::
### GroupNew
:::{card}
> Receive a notification when you join a new group.  
> This can arrive under different circumstances:  
> - you created a group  
> - you accepted a group invitation  
> - for keycloak managed group: the directory created a group or added you to an existing group

**Subscription**: *SubscribeToGroupNewNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)

**Notification *(Stream)***: *GroupNewNotification*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### GroupDeleted
:::{card}
> Receive a notification when you left a group.  
> This can arrive under different circumstances:  
> - you chose to leave a group  
> - you disbanded a group (you must be admin of this group)  
> - a group admin disbanded the group  
> - a group admin removed you from the group  
> - for keycloak managed group: the keycloak directory removed you from the group or disbanded the group

**Subscription**: *SubscribeToGroupDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)

**Notification *(Stream)***: *GroupDeletedNotification*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupNameUpdated
:::{card}
> Receive a notification when a group name have been updated.  
> This can arrive under different circumstances:  
> - you updated the group name (you must be admin of this group)  
> - an admin updated the group name  
> - for keycloak managed groups: the group name were changed by the keycloak directory

**Subscription**: *SubscribeToGroupNameUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `previous_name_search` (**optional** string - *regexp filter on *group.name* field, before update*)

**Notification *(Stream)***: *GroupNameUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `previous_name` (string - *the group name before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupPhotoUpdated
:::{card}
> Receive a notification when a group picture have been updated.  
> This can arrive under different circumstances:  
> - you updated the group picture (you must be admin of this group)  
> - an admin updated the group picture  
> - for keycloak managed groups: the group picture were changed by the keycloak directory

**Subscription**: *SubscribeToGroupPhotoUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)

**Notification *(Stream)***: *GroupPhotoUpdatedNotification*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupDescriptionUpdated
:::{card}
> Receive a notification when a group description have been updated.  
> This can arrive under different circumstances:  
> - you updated the group description (you must be admin of this group)  
> - an admin updated the group description  
> - for keycloak managed groups: the group description were changed by the keycloak directory

**Subscription**: *SubscribeToGroupDescriptionUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `previous_description_search` (**optional** string - *regexp filter on previous *group.description* field, before update*)

**Notification *(Stream)***: *GroupDescriptionUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `previous_description` (string)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupPendingMemberAdded
:::{card}
> Receive a notification when a pending member was added from a group.  
> This can arrive under different circumstances:  
> - an admin added a new member to the group  
> - you joined a group and all group members are all considered as pending until each one acknowledge you joined this group

**Subscription**: *SubscribeToGroupPendingMemberAddedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `pending_member_filter` (**optional** {ref}`datatype-pendinggroupmemberfilter` - *you will only receive notifications about groups with a pending member that match this filter.*)

**Notification *(Stream)***: *GroupPendingMemberAddedNotification*
* `group` ({ref}`datatype-group`)
* `pending_member` ({ref}`datatype-pendinggroupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupPendingMemberRemoved
:::{card}
> Receive a notification when a pending member was removed from a group.  
> This can arrive under different circumstances:  
> - a pending group member accepted or declined the group invitation  
> - you joined a group and a member acknowledged you joined this group

**Subscription**: *SubscribeToGroupPendingMemberRemovedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `pending_member_filter` (**optional** {ref}`datatype-pendinggroupmemberfilter` - *you will only receive notifications about groups with a pending member that match this filter.*)

**Notification *(Stream)***: *GroupPendingMemberRemovedNotification*
* `group` ({ref}`datatype-group`)
* `pending_member` ({ref}`datatype-pendinggroupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupMemberJoined
:::{card}
> Receive a notification when a new member joined a group.  
> This can arrive under different circumstances:  
> - a pending group member accepted the group invitation  
> - for keycloak managed groups: directory added a new group member / a user registered on directory and was automatically added to existing groups

**Subscription**: *SubscribeToGroupMemberJoinedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter` - *you will only receive notifications about groups with a member that match this filter.*)

**Notification *(Stream)***: *GroupMemberJoinedNotification*
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupMemberLeft
:::{card}
> Receive a notification when a group member was removed from a group.  
> This can arrive under different circumstances:  
> - you removed a group member (you must be a group admin)  
> - a group member was removed by an admin  
> - for keycloak managed groups: directory removed a group member / a user unregistered from directory and was automatically removed from groups

**Subscription**: *SubscribeToGroupMemberLeftNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter` - *you will only receive notifications about groups with a member that match this filter.*)

**Notification *(Stream)***: *GroupMemberLeftNotification*
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupOwnPermissionsUpdated
:::{card}
> Receive a notification when your permissions have been updated in a group.

**Subscription**: *SubscribeToGroupOwnPermissionsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter` - *you will only receive notifications about groups where your permissions match this filter.*)
* `previous_permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter` - *you will only receive notifications about groups where your permissions match this filter, before update.*)

**Notification *(Stream)***: *GroupOwnPermissionsUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `permissions` ({ref}`datatype-groupmemberpermissions` - *your new permissions*)
* `previous_permissions` ({ref}`datatype-groupmemberpermissions` - *your permissions before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupMemberPermissionsUpdated
:::{card}
> Receive a notification when a group member permissions have been updated.

**Subscription**: *SubscribeToGroupMemberPermissionsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`datatype-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter` - *you will only receive notifications about group members that match this filter.*)
* `previous_permission_filter` (**optional** {ref}`datatype-groupmemberfilter` - *you will only receive notifications about group members that match this filter.
TODO update to GroupPermissionsFilter !*)

**Notification *(Stream)***: *GroupMemberPermissionsUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember` - *the group member permissions have been updated for*)
* `previous_permissions` ({ref}`datatype-groupmemberpermissions` - *the member permissions before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-invitationnotificationservice)=
## Invitation Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-invitation`
:::
### InvitationReceived
:::{card}
> Receive a notification when you receive a new invitation.  
> A new invitation is the first step of an invitation protocol.

**Subscription**: *SubscribeToInvitationReceivedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)

**Notification *(Stream)***: *InvitationReceivedNotification*
* `invitation` ({ref}`datatype-invitation`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### InvitationSent
:::{card}
> Receive a notification when you send a new invitation.  
> A new invitation is the first step of an invitation protocol.

**Subscription**: *SubscribeToInvitationSentNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)

**Notification *(Stream)***: *InvitationSentNotification*
* `invitation` ({ref}`datatype-invitation`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### InvitationDeleted
:::{card}
> Receive a notification when an invitation is deleted.  
> This can arrive under different circumstances:  
> - an invitation protocol ended and invitation was automatically removed  
> - you aborted a protocol  
> - you deleted an invitation

**Subscription**: *SubscribeToInvitationDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)
* `invitation_ids` (**repeated** uint64 - *you will only receive notifications about invitations specified in this list.*)

**Notification *(Stream)***: *InvitationDeletedNotification*
* `invitation` ({ref}`datatype-invitation`)

**Error Codes**:
- `NOT_FOUND`: at least one of _invitation_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### InvitationUpdated
:::{card}
> Receive a notification when an invitation status have been updated.  
> Invitation status are updated when a new protocol step is passed.

**Subscription**: *SubscribeToInvitationUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`datatype-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)
* `invitation_ids` (**repeated** uint64 - *you will only receive notifications about invitations specified in this list.*)

**Notification *(Stream)***: *InvitationUpdatedNotification*
* `invitation` ({ref}`datatype-invitation`)
* `previous_invitation_status` ({ref}`datatype-status` - *_invitation.status_ before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of _invitation_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-callnotificationservice)=
## Call Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-call`
:::
### CallIncomingCall
:::{card}
> Receive a notification when someone tries to call you. (InboundCal)  
> Daemon will automatically answer with a busy message to notify you won't be able to answer.  
> Call details are available in notification content.

**Subscription**: *SubscribeToCallIncomingCallNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

**Notification *(Stream)***: *CallIncomingCallNotification*
* `call_identifier` (string)
* `discussion_id` (uint64 - *set to group discussion if calling a group, else to contact's discussion, even if there are multiple participants*)
* `participant_id` ({ref}`datatype-callparticipantid` - *obviously contains a contact id*)
* `caller_display_name` (string)
* `participant_count` (uint32)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### CallRinging
:::{card}
> When you initiated a call, receive a notification when a participant phone starts to ring.  
> Under some network circumstances a participant phone might never start ringing.

**Subscription**: *SubscribeToCallRingingNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

**Notification *(Stream)***: *CallRingingNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### CallAccepted
:::{card}
> When you initiated a call, receive a notification if a participant accepted the call.  
> Daemon will automatically hang up when a participant accept the call because we currently cannot manage the call.

**Subscription**: *SubscribeToCallAcceptedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

**Notification *(Stream)***: *CallAcceptedNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### CallDeclined
:::{card}
> When you initiated a call, receive a notification if a participant declined the call.

**Subscription**: *SubscribeToCallDeclinedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

**Notification *(Stream)***: *CallDeclinedNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### CallBusy
:::{card}
> (Outbound call)  
> When you initiated a call, receive a notification if a participant accepted the call.

**Subscription**: *SubscribeToCallBusyNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

**Notification *(Stream)***: *CallBusyNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### CallEnded
:::{card}
> :  
> For inbound or outbound call, receive a notification when every call participant left a call or declined it.

**Subscription**: *SubscribeToCallEndedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

**Notification *(Stream)***: *CallEndedNotification*
* `call_identifier` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::
