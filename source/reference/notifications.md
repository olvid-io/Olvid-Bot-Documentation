# Notifications

Events you can subscribe to, and the associated notifications content.

:::{contents} Notifications
:depth: 1
:local:
:::
(service-messagenotificationservice)=
## Message Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-message`
:::
(rpc-messagereceived)=
### MessageReceived
::::::{card}
> Receive a notification each time you receive a new message.

(message-subscribetomessagereceivednotification)=
**Subscription**: *SubscribeToMessageReceivedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagereceivednotification)=
**Notification *(Stream)***: *MessageReceivedNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagesent)=
### MessageSent
::::::{card}
> Receive a notification each time an you sent a new message.

(message-subscribetomessagesentnotification)=
**Subscription**: *SubscribeToMessageSentNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagesentnotification)=
**Notification *(Stream)***: *MessageSentNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagedeleted)=
### MessageDeleted
::::::{card}
> Receive a notification each time a message has been deleted.  
> This can happen under different circumstances:  
> - you deleted a message locally  
> - someone else deleted it's own message for everyone in the discussion

(message-subscribetomessagedeletednotification)=
**Subscription**: *SubscribeToMessageDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagedeletednotification)=
**Notification *(Stream)***: *MessageDeletedNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagebodyupdated)=
### MessageBodyUpdated
::::::{card}
> datatypes.v1.Message updates

(message-subscribetomessagebodyupdatednotification)=
**Subscription**: *SubscribeToMessageBodyUpdatedNotification*
MessageBodyUpdated
Receive a notification each time a message text body have been updated.
Only the message sender can edit its own messages.

**Error codes**:
`NOT_FOUND`: at least one of the _message_ids_ does not exists.
`UNAUTHENTICATED`: client key is invalid.

* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagebodyupdatednotification)=
**Notification *(Stream)***: *MessageBodyUpdatedNotification*
* `message` ({ref}`message-message`)
* `previous_body` (string)

::::::

(rpc-messageuploaded)=
### MessageUploaded
::::::{card}
> Receive a notification each time an outbound message have been uploaded on server.  
> Note: You cannot guarantee this notification will arrive when working with ephemeral message

(message-subscribetomessageuploadednotification)=
**Subscription**: *SubscribeToMessageUploadedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messageuploadednotification)=
**Notification *(Stream)***: *MessageUploadedNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `INVALID_ARGUMENT`: at least one of _message_ids_ is not an outbound message.
 - `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagedelivered)=
### MessageDelivered
::::::{card}
> Receive a notification each time an outbound message have been delivered on at least one recipient's device.  
> Note: You cannot guarantee this notification will arrive when working with ephemeral message

(message-subscribetomessagedeliverednotification)=
**Subscription**: *SubscribeToMessageDeliveredNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagedeliverednotification)=
**Notification *(Stream)***: *MessageDeliveredNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `INVALID_ARGUMENT`: at least one of _message_ids_ is not an outbound message.
 - `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messageread)=
### MessageRead
::::::{card}
> Receive a notification each time an outbound message have been read by at least one recipient.  
> Note: You cannot guarantee this notification will arrive when working with ephemeral message

(message-subscribetomessagereadnotification)=
**Subscription**: *SubscribeToMessageReadNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagereadnotification)=
**Notification *(Stream)***: *MessageReadNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `INVALID_ARGUMENT`: at least one of _message_ids_ is not an outbound message.
 - `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagelocationreceived)=
### MessageLocationReceived
::::::{card}
> location message

(message-subscribetomessagelocationreceivednotification)=
**Subscription**: *SubscribeToMessageLocationReceivedNotification*
MessageLocationReceived
Receive a notification each time you received a location message.
Location messages are different from location sharing messages as they contains one static position.
A received location message also triggers the MessageReceived notification.

**Error codes**:
`UNAUTHENTICATED`: client key is invalid.

* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagelocationreceivednotification)=
**Notification *(Stream)***: *MessageLocationReceivedNotification*
* `message` ({ref}`message-message`)

::::::

(rpc-messagelocationsent)=
### MessageLocationSent
::::::{card}
> Receive a notification each time you sent a location message.  
> Location messages are different from location sharing messages as they contains one static position.  
> A sent location message also triggers the MessageSent notification.

(message-subscribetomessagelocationsentnotification)=
**Subscription**: *SubscribeToMessageLocationSentNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagelocationsentnotification)=
**Notification *(Stream)***: *MessageLocationSentNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagelocationsharingstart)=
### MessageLocationSharingStart
::::::{card}
> Receive a notification each time you sent or you received a new location sharing message.  
> Location sharing messages are supposed to be updated for a given while.  
> A new location sharing message also triggers the MessageReceived or MessageSent notification.

(message-subscribetomessagelocationsharingstartnotification)=
**Subscription**: *SubscribeToMessageLocationSharingStartNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagelocationsharingstartnotification)=
**Notification *(Stream)***: *MessageLocationSharingStartNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagelocationsharingupdate)=
### MessageLocationSharingUpdate
::::::{card}
> Receive a notification each time a location sharing message have been updated with a new location.  
> This might concern inbound or outbound messages.

(message-subscribetomessagelocationsharingupdatenotification)=
**Subscription**: *SubscribeToMessageLocationSharingUpdateNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagelocationsharingupdatenotification)=
**Notification *(Stream)***: *MessageLocationSharingUpdateNotification*
* `message` ({ref}`message-message`)
* `previous_location` ({ref}`message-messagelocation`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `INVALID_ARGUMENT`: one of _message_ids_ is not a live location sharing.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagelocationsharingend)=
### MessageLocationSharingEnd
::::::{card}
> Receive a notification each time a location sharing message have been stopped or automatically finished.  
> This might concern inbound or outbound messages.

(message-subscribetomessagelocationsharingendnotification)=
**Subscription**: *SubscribeToMessageLocationSharingEndNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)

(message-messagelocationsharingendnotification)=
**Notification *(Stream)***: *MessageLocationSharingEndNotification*
* `message` ({ref}`message-message`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `INVALID_ARGUMENT`: one of _message_ids_ is not a live location sharing.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagereactionadded)=
### MessageReactionAdded
::::::{card}
> datatypes.v1.Message reactions

(message-subscribetomessagereactionaddednotification)=
**Subscription**: *SubscribeToMessageReactionAddedNotification*
MessageReactionAdded
Receive a notification each time a reaction was added to a message.
It can concern your reactions or any contact reactions.

**Error codes**:
`NOT_FOUND`: at least one of the _message_ids_ does not exists.
`UNAUTHENTICATED`: client key is invalid.

* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)
* `reaction_filter` (**optional** {ref}`message-reactionfilter` - *you will only receive notifications about reactions that match this filter.*)

(message-messagereactionaddednotification)=
**Notification *(Stream)***: *MessageReactionAddedNotification*
* `message` ({ref}`message-message`)
* `reaction` ({ref}`message-messagereaction`)

::::::

(rpc-messagereactionupdated)=
### MessageReactionUpdated
::::::{card}
> Receive a notification each time a reaction on a message was updated.  
> It can concern your reactions or any contact reactions.

(message-subscribetomessagereactionupdatednotification)=
**Subscription**: *SubscribeToMessageReactionUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `message_filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)
* `reaction_filter` (**optional** {ref}`message-reactionfilter` - *you will only receive notifications about reactions that match this filter.*)
* `previous_reaction_filter` (**optional** {ref}`message-reactionfilter` - *you will only receive notifications about reactions that match this filter, before update.*)

(message-messagereactionupdatednotification)=
**Notification *(Stream)***: *MessageReactionUpdatedNotification*
* `message` ({ref}`message-message`)
* `reaction` ({ref}`message-messagereaction`)
* `previous_reaction` ({ref}`message-messagereaction`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-messagereactionremoved)=
### MessageReactionRemoved
::::::{card}
> Receive a notification each time a reaction on a message was removed.  
> It can concern your reactions or any contact reactions.

(message-subscribetomessagereactionremovednotification)=
**Subscription**: *SubscribeToMessageReactionRemovedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about messages specified in this list.*)
* `filter` (**optional** {ref}`message-messagefilter` - *you will only receive notifications about messages that match this filter.*)
* `reaction_filter` (**optional** {ref}`message-reactionfilter` - *you will only receive notifications about reactions that match this filter.*)

(message-messagereactionremovednotification)=
**Notification *(Stream)***: *MessageReactionRemovedNotification*
* `message` ({ref}`message-message`)
* `reaction` ({ref}`message-messagereaction`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _message_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-attachmentnotificationservice)=
## Attachment Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-attachment`
:::
(rpc-attachmentreceived)=
### AttachmentReceived
::::::{card}
> Receive a notification every time you receive an attachment in a discussion (one-to-one or group discussion).  
> When you receive a message with multiple attachments, you will receive one notification for each attachment.

(message-subscribetoattachmentreceivednotification)=
**Subscription**: *SubscribeToAttachmentReceivedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-attachmentfilter` - *you will only receive notifications about attachments that match all the filter params.*)

(message-attachmentreceivednotification)=
**Notification *(Stream)***: *AttachmentReceivedNotification*
* `attachment` ({ref}`message-attachment`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-attachmentuploaded)=
### AttachmentUploaded
::::::{card}
> Receive a notification every time an attachment you sent has been marked as uploaded.  
> A message with attachments is delivered to recipients only when all attachments have been uploaded.

(message-subscribetoattachmentuploadednotification)=
**Subscription**: *SubscribeToAttachmentUploadedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-attachmentfilter` - *you will only receive notifications about attachments that match all the filter params.*)
* `message_ids` (**repeated** {ref}`message-messageid` - *you will only receive notifications about attachments related to messages specified in this list.*)
* `attachment_ids` (**repeated** {ref}`message-attachmentid` - *you will only receive notifications about attachments specified in this list.*)

(message-attachmentuploadednotification)=
**Notification *(Stream)***: *AttachmentUploadedNotification*
* `attachment` ({ref}`message-attachment`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INVALID_ARGUMENT`: cannot subscribe for non-outbound messages.
 - `NOT_FOUND`: at least one of the _message_ids_ is incorrect.
::::::

---

(service-discussionnotificationservice)=
## Discussion Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-discussion`
:::
(rpc-discussionnew)=
### DiscussionNew
::::::{card}
> Receive a notification every time a discussion is created or re-used.  
> This can happen under different circumstances:  
> - a new contact was added  
> - you created or joined a group

(message-subscribetodiscussionnewnotification)=
**Subscription**: *SubscribeToDiscussionNewNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)

(message-discussionnewnotification)=
**Notification *(Stream)***: *DiscussionNewNotification*
* `discussion` ({ref}`message-discussion`)

**Error Codes**:
- `UNAUTHENTICATED`: Client key is invalid.
::::::

(rpc-discussionlocked)=
### DiscussionLocked
::::::{card}
> Receive a notification each time a discussion is locked.  
> This can happen under different circumstances:  
> - the contact associated to this discussion was removed from your contact book  
> - you left the associated group or the group was disbanded

(message-subscribetodiscussionlockednotification)=
**Subscription**: *SubscribeToDiscussionLockedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)
* `discussion_ids` (**repeated** uint64 - *you will only receive notifications about discussions specified in this list.*)

(message-discussionlockednotification)=
**Notification *(Stream)***: *DiscussionLockedNotification*
* `discussion` ({ref}`message-discussion`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _discussion_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussiontitleupdated)=
### DiscussionTitleUpdated
::::::{card}
> Receive a notification each time a discussion title changed.  
> This can happen under different circumstances:  
> - the contact associated to this discussion changed it's details  
> - the associated group was renamed

(message-subscribetodiscussiontitleupdatednotification)=
**Subscription**: *SubscribeToDiscussionTitleUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)
* `discussion_ids` (**repeated** uint64 - *you will only receive notifications about discussions specified in this list.*)

(message-discussiontitleupdatednotification)=
**Notification *(Stream)***: *DiscussionTitleUpdatedNotification*
* `discussion` ({ref}`message-discussion`)
* `previous_title` (string)

**Error Codes**:
- `NOT_FOUND`: at least one of the _discussion_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussionsettingsupdated)=
### DiscussionSettingsUpdated
::::::{card}
> Receive a notification each time the discussion shared settings have been updated.  
> Any group group member with the _change_settings_ permission can update shared settings.  
> By default admin members have this permission.

(message-subscribetodiscussionsettingsupdatednotification)=
**Subscription**: *SubscribeToDiscussionSettingsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-discussionfilter` - *you will only receive notifications about discussions that match all the filter params.*)
* `discussion_ids` (**repeated** uint64 - *you will only receive notifications about discussions specified in this list.*)

(message-discussionsettingsupdatednotification)=
**Notification *(Stream)***: *DiscussionSettingsUpdatedNotification*
* `discussion` ({ref}`message-discussion`)
* `new_settings` ({ref}`message-discussionsettings` - *the new current discussion settings*)
* `previous_settings` ({ref}`message-discussionsettings` - *settings before this update*)

**Error Codes**:
- `NOT_FOUND`: at least one of the _discussion_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-contactnotificationservice)=
## Contact Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-contact`
:::
(rpc-contactnew)=
### ContactNew
::::::{card}
> Receive a notification each time a contact is added to your contact book.

(message-subscribetocontactnewnotification)=
**Subscription**: *SubscribeToContactNewNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)

(message-contactnewnotification)=
**Notification *(Stream)***: *ContactNewNotification*
* `contact` ({ref}`message-contact`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactdeleted)=
### ContactDeleted
::::::{card}
> Receive a notification each time a contact is removed from your contact book.  
> This can happen under different circumstances:  
> - you deleted the contact  
> - he contact deleted you  
> - the contact deleted his identity and chose to notify his contacts

(message-subscribetocontactdeletednotification)=
**Subscription**: *SubscribeToContactDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)
* `contact_ids` (**repeated** uint64 - *you will only receive notifications about contacts specified in this list.*)

(message-contactdeletednotification)=
**Notification *(Stream)***: *ContactDeletedNotification*
* `contact` ({ref}`message-contact`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _contact_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactdetailsupdated)=
### ContactDetailsUpdated
::::::{card}
> Receive a notification each time a contact update it's identity details.  
> This implies that this contact display name changed.  
> This can happen under different circumstances:  
> - the contact updated his details  
> - for _keycloak_managed_ contacts the directory updated it's details

(message-subscribetocontactdetailsupdatednotification)=
**Subscription**: *SubscribeToContactDetailsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)
* `contact_ids` (**repeated** uint64 - *you will only receive notifications about contacts specified in this list.*)

(message-contactdetailsupdatednotification)=
**Notification *(Stream)***: *ContactDetailsUpdatedNotification*
* `contact` ({ref}`message-contact`)
* `previous_details` ({ref}`message-identitydetails`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _contact_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactphotoupdated)=
### ContactPhotoUpdated
::::::{card}
> Receive a notification each time a contact profile picture has been updated.

(message-subscribetocontactphotoupdatednotification)=
**Subscription**: *SubscribeToContactPhotoUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-contactfilter` - *you will only receive notifications about contacts that match all the filter params.*)
* `contact_ids` (**repeated** uint64 - *you will only receive notifications about contacts specified in this list.*)

(message-contactphotoupdatednotification)=
**Notification *(Stream)***: *ContactPhotoUpdatedNotification*
* `contact` ({ref}`message-contact`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _contact_ids_ was not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-groupnotificationservice)=
## Group Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-group`
:::
(rpc-groupnew)=
### GroupNew
::::::{card}
> Receive a notification each time you join a new group.  
> This can happen under different circumstances:  
> - you created a group  
> - you accepted a group invitation  
> - for keycloak managed group: the directory created a group or added you to an existing group

(message-subscribetogroupnewnotification)=
**Subscription**: *SubscribeToGroupNewNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)

(message-groupnewnotification)=
**Notification *(Stream)***: *GroupNewNotification*
* `group` ({ref}`message-group`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupdeleted)=
### GroupDeleted
::::::{card}
> Receive a notification each time you leave a group.  
> This can happen under different circumstances:  
> - you chose to leave a group  
> - you disbanded a group (you must be admin of this group)  
> - a group admin disbanded the group  
> - a group admin removed you from the group  
> - for keycloak managed group: the keycloak directory removed you from the group or disbanded the group

(message-subscribetogroupdeletednotification)=
**Subscription**: *SubscribeToGroupDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)

(message-groupdeletednotification)=
**Notification *(Stream)***: *GroupDeletedNotification*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exist.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupnameupdated)=
### GroupNameUpdated
::::::{card}
> Receive a notification each time a group name have been updated.  
> This can happen under different circumstances:  
> - you updated the group name (you must be admin of this group)  
> - an admin updated the group name  
> - for keycloak managed groups: the group name were changed by the keycloak directory

(message-subscribetogroupnameupdatednotification)=
**Subscription**: *SubscribeToGroupNameUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `previous_name_search` (**optional** string - *regexp filter on *group.name* field, before update*)

(message-groupnameupdatednotification)=
**Notification *(Stream)***: *GroupNameUpdatedNotification*
* `group` ({ref}`message-group`)
* `previous_name` (string - *the group name before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupphotoupdated)=
### GroupPhotoUpdated
::::::{card}
> Receive a notification when a group picture have been updated.  
> This can happen under different circumstances:  
> - you updated the group picture (you must be admin of this group)  
> - an admin updated the group picture  
> - for keycloak managed groups: the group picture were changed by the keycloak directory

(message-subscribetogroupphotoupdatednotification)=
**Subscription**: *SubscribeToGroupPhotoUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)

(message-groupphotoupdatednotification)=
**Notification *(Stream)***: *GroupPhotoUpdatedNotification*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupdescriptionupdated)=
### GroupDescriptionUpdated
::::::{card}
> Receive a notification when a group description have been updated.  
> This can happen under different circumstances:  
> - you updated the group description (you must be admin of this group)  
> - an admin updated the group description  
> - for keycloak managed groups: the group description were changed by the keycloak directory

(message-subscribetogroupdescriptionupdatednotification)=
**Subscription**: *SubscribeToGroupDescriptionUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `previous_description_search` (**optional** string - *regexp filter on previous *group.description* field, before update*)

(message-groupdescriptionupdatednotification)=
**Notification *(Stream)***: *GroupDescriptionUpdatedNotification*
* `group` ({ref}`message-group`)
* `previous_description` (string)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-grouppendingmemberadded)=
### GroupPendingMemberAdded
::::::{card}
> Receive a notification when a pending member was added from a group.  
> This can happen under different circumstances:  
> - an admin added a new member to the group  
> - you joined a group and all group members are all considered as pending until each one acknowledge you joined this group

(message-subscribetogrouppendingmemberaddednotification)=
**Subscription**: *SubscribeToGroupPendingMemberAddedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `pending_member_filter` (**optional** {ref}`message-pendinggroupmemberfilter` - *you will only receive notifications about groups with a pending member that match this filter.*)

(message-grouppendingmemberaddednotification)=
**Notification *(Stream)***: *GroupPendingMemberAddedNotification*
* `group` ({ref}`message-group`)
* `pending_member` ({ref}`message-pendinggroupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-grouppendingmemberremoved)=
### GroupPendingMemberRemoved
::::::{card}
> Receive a notification when a pending member was removed from a group.  
> This can happen under different circumstances:  
> - a pending group member accepted or declined the group invitation  
> - you joined a group and a member acknowledged you joined this group

(message-subscribetogrouppendingmemberremovednotification)=
**Subscription**: *SubscribeToGroupPendingMemberRemovedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `pending_member_filter` (**optional** {ref}`message-pendinggroupmemberfilter` - *you will only receive notifications about groups with a pending member that match this filter.*)

(message-grouppendingmemberremovednotification)=
**Notification *(Stream)***: *GroupPendingMemberRemovedNotification*
* `group` ({ref}`message-group`)
* `pending_member` ({ref}`message-pendinggroupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupmemberjoined)=
### GroupMemberJoined
::::::{card}
> Receive a notification when a new member joined a group.  
> This can happen under different circumstances:  
> - a pending group member accepted the group invitation  
> - for keycloak managed groups: directory added a new group member / a user registered on directory and was automatically added to existing groups

(message-subscribetogroupmemberjoinednotification)=
**Subscription**: *SubscribeToGroupMemberJoinedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `member_filter` (**optional** {ref}`message-groupmemberfilter` - *you will only receive notifications about groups with a member that match this filter.*)

(message-groupmemberjoinednotification)=
**Notification *(Stream)***: *GroupMemberJoinedNotification*
* `group` ({ref}`message-group`)
* `member` ({ref}`message-groupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupmemberleft)=
### GroupMemberLeft
::::::{card}
> Receive a notification when a group member was removed from a group.  
> This can happen under different circumstances:  
> - you removed a group member (you must be a group admin)  
> - a group member was removed by an admin  
> - for keycloak managed groups: directory removed a group member / a user unregistered from directory and was automatically removed from groups

(message-subscribetogroupmemberleftnotification)=
**Subscription**: *SubscribeToGroupMemberLeftNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `member_filter` (**optional** {ref}`message-groupmemberfilter` - *you will only receive notifications about groups with a member that match this filter.*)

(message-groupmemberleftnotification)=
**Notification *(Stream)***: *GroupMemberLeftNotification*
* `group` ({ref}`message-group`)
* `member` ({ref}`message-groupmember`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupownpermissionsupdated)=
### GroupOwnPermissionsUpdated
::::::{card}
> Receive a notification when your permissions have been updated in a group.

(message-subscribetogroupownpermissionsupdatednotification)=
**Subscription**: *SubscribeToGroupOwnPermissionsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `permissions_filter` (**optional** {ref}`message-grouppermissionfilter` - *you will only receive notifications about groups where your permissions match this filter.*)
* `previous_permissions_filter` (**optional** {ref}`message-grouppermissionfilter` - *you will only receive notifications about groups where your permissions match this filter, before update.*)

(message-groupownpermissionsupdatednotification)=
**Notification *(Stream)***: *GroupOwnPermissionsUpdatedNotification*
* `group` ({ref}`message-group`)
* `permissions` ({ref}`message-groupmemberpermissions` - *your new permissions*)
* `previous_permissions` ({ref}`message-groupmemberpermissions` - *your permissions before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupmemberpermissionsupdated)=
### GroupMemberPermissionsUpdated
::::::{card}
> Receive a notification when a group member permissions have been updated.

(message-subscribetogroupmemberpermissionsupdatednotification)=
**Subscription**: *SubscribeToGroupMemberPermissionsUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `group_ids` (**repeated** uint64 - *you will only receive notifications about groups specified in this list.*)
* `group_filter` (**optional** {ref}`message-groupfilter` - *you will only receive notifications about groups that match all the filter params.*)
* `member_filter` (**optional** {ref}`message-groupmemberfilter` - *you will only receive notifications about group members that match this filter.*)
* `previous_permission_filter` (**optional** {ref}`message-groupmemberfilter` - *you will only receive notifications about group members that match this filter.
TODO update to GroupPermissionsFilter !*)

(message-groupmemberpermissionsupdatednotification)=
**Notification *(Stream)***: *GroupMemberPermissionsUpdatedNotification*
* `group` ({ref}`message-group`)
* `member` ({ref}`message-groupmember` - *the group member permissions have been updated for*)
* `previous_permissions` ({ref}`message-groupmemberpermissions` - *the member permissions before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of the _group_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-invitationnotificationservice)=
## Invitation Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-invitation`
:::
(rpc-invitationreceived)=
### InvitationReceived
::::::{card}
> Receive a notification each time you receive a new invitation.  
> A new invitation marks the first step of an invitation protocol.

(message-subscribetoinvitationreceivednotification)=
**Subscription**: *SubscribeToInvitationReceivedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)

(message-invitationreceivednotification)=
**Notification *(Stream)***: *InvitationReceivedNotification*
* `invitation` ({ref}`message-invitation`)

**Error Codes**:
- `UNAUTHENTICATED`: Client key is invalid.
::::::

(rpc-invitationsent)=
### InvitationSent
::::::{card}
> Receive a notification each time you send a new invitation.  
> A new invitation is the first step of an invitation protocol.

(message-subscribetoinvitationsentnotification)=
**Subscription**: *SubscribeToInvitationSentNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)

(message-invitationsentnotification)=
**Notification *(Stream)***: *InvitationSentNotification*
* `invitation` ({ref}`message-invitation`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-invitationdeleted)=
### InvitationDeleted
::::::{card}
> Receive a notification each time an invitation is deleted.  
> This can happen under different circumstances:  
> - an invitation protocol ended and invitation was automatically removed  
> - you aborted a protocol  
> - you deleted an invitation

(message-subscribetoinvitationdeletednotification)=
**Subscription**: *SubscribeToInvitationDeletedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)
* `invitation_ids` (**repeated** uint64 - *you will only receive notifications about invitations specified in this list.*)

(message-invitationdeletednotification)=
**Notification *(Stream)***: *InvitationDeletedNotification*
* `invitation` ({ref}`message-invitation`)

**Error Codes**:
- `NOT_FOUND`: at least one of the _invitation_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-invitationupdated)=
### InvitationUpdated
::::::{card}
> Receive a notification each time an invitation status have been updated.  
> Invitation status are updated when a new protocol step is passed.

(message-subscribetoinvitationupdatednotification)=
**Subscription**: *SubscribeToInvitationUpdatedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)
* `filter` (**optional** {ref}`message-invitationfilter` - *you will only receive notifications about invitations that match this filter.*)
* `invitation_ids` (**repeated** uint64 - *you will only receive notifications about invitations specified in this list.*)

(message-invitationupdatednotification)=
**Notification *(Stream)***: *InvitationUpdatedNotification*
* `invitation` ({ref}`message-invitation`)
* `previous_invitation_status` ({ref}`enum-invitation.status` - *_invitation.status_ before update*)

**Error Codes**:
- `NOT_FOUND`: at least one of the _invitation_ids_ does not exists.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-callnotificationservice)=
## Call Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-call`
:::
(rpc-callincomingcall)=
### CallIncomingCall
::::::{card}
> Receive a notification when someone tries to call you.  
> Daemon will automatically answer with a busy message to notify that you won't be able to answer.  
> Call details are available in notification content.

(message-subscribetocallincomingcallnotification)=
**Subscription**: *SubscribeToCallIncomingCallNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

(message-callincomingcallnotification)=
**Notification *(Stream)***: *CallIncomingCallNotification*
* `call_identifier` (string)
* `discussion_id` (uint64 - *set to group discussion if calling a group, else to contact's discussion, even if there are multiple participants*)
* `participant_id` ({ref}`message-callparticipantid` - *obviously contains a contact id*)
* `caller_display_name` (string)
* `participant_count` (uint32)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-callringing)=
### CallRinging
::::::{card}
> When you initiated a call, receive a notification when a participant phone starts to ring.  
> Under some network circumstances a participant phone might never start ringing.

(message-subscribetocallringingnotification)=
**Subscription**: *SubscribeToCallRingingNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

(message-callringingnotification)=
**Notification *(Stream)***: *CallRingingNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`message-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-callaccepted)=
### CallAccepted
::::::{card}
> When you initiated a call, receive a notification if a participant accepted the call.  
> Daemon will automatically hang up when a participant accept the call because we currently cannot manage the call.

(message-subscribetocallacceptednotification)=
**Subscription**: *SubscribeToCallAcceptedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

(message-callacceptednotification)=
**Notification *(Stream)***: *CallAcceptedNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`message-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-calldeclined)=
### CallDeclined
::::::{card}
> When you initiated a call, receive a notification if a participant declined the call.

(message-subscribetocalldeclinednotification)=
**Subscription**: *SubscribeToCallDeclinedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

(message-calldeclinednotification)=
**Notification *(Stream)***: *CallDeclinedNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`message-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-callbusy)=
### CallBusy
::::::{card}
> (Outbound call)  
> When you initiated a call, receive a notification if a participant accepted the call.

(message-subscribetocallbusynotification)=
**Subscription**: *SubscribeToCallBusyNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

(message-callbusynotification)=
**Notification *(Stream)***: *CallBusyNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`message-callparticipantid`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-callended)=
### CallEnded
::::::{card}
> :  
> For inbound or outbound call, receive a notification when every call participant left a call or declined it.

(message-subscribetocallendednotification)=
**Subscription**: *SubscribeToCallEndedNotification*
* `count` (**optional** uint64 - *limit the number of notifications you will receive , set to 0 to disable*)

(message-callendednotification)=
**Notification *(Stream)***: *CallEndedNotification*
* `call_identifier` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::
