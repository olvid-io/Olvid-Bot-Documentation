# Notifications

Events you can subscribe to, and notification content.

:::{contents}
:depth: 1
:local:
:::
(service-messagenotificationservice)=
## MessageNotificationService

> **Associated Datatype:** {ref}`datatype-message`

### MessageReceived
**Subscription: `SubscribeToMessageReceivedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageReceivedNotification`**
* `message` ({ref}`datatype-message`)



### MessageSent
**Subscription: `SubscribeToMessageSentNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageSentNotification`**
* `message` ({ref}`datatype-message`)



### MessageDeleted
**Subscription: `SubscribeToMessageDeletedNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageDeletedNotification`**
* `message` ({ref}`datatype-message`)



### MessageBodyUpdated
datatypes.v1.Message updates

**Subscription: `SubscribeToMessageBodyUpdatedNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageBodyUpdatedNotification`**
* `message` ({ref}`datatype-message`)
* `previous_body` (string)



### MessageUploaded
**Subscription: `SubscribeToMessageUploadedNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageUploadedNotification`**
* `message` ({ref}`datatype-message`)



### MessageDelivered
**Subscription: `SubscribeToMessageDeliveredNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageDeliveredNotification`**
* `message` ({ref}`datatype-message`)



### MessageRead
**Subscription: `SubscribeToMessageReadNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageReadNotification`**
* `message` ({ref}`datatype-message`)



### MessageLocationReceived
location message

**Subscription: `SubscribeToMessageLocationReceivedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageLocationReceivedNotification`**
* `message` ({ref}`datatype-message`)



### MessageLocationSent
**Subscription: `SubscribeToMessageLocationSentNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageLocationSentNotification`**
* `message` ({ref}`datatype-message`)



### MessageLocationSharingStart
**Subscription: `SubscribeToMessageLocationSharingStartNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageLocationSharingStartNotification`**
* `message` ({ref}`datatype-message`)



### MessageLocationSharingUpdate
**Subscription: `SubscribeToMessageLocationSharingUpdateNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageLocationSharingUpdateNotification`**
* `message` ({ref}`datatype-message`)
* `previous_location` ({ref}`datatype-messagelocation`)



### MessageLocationSharingEnd
**Subscription: `SubscribeToMessageLocationSharingEndNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)*: `MessageLocationSharingEndNotification`**
* `message` ({ref}`datatype-message`)



### MessageReactionAdded
datatypes.v1.Message reactions

**Subscription: `SubscribeToMessageReactionAddedNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter`)

**Notification *(Stream)*: `MessageReactionAddedNotification`**
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)



### MessageReactionUpdated
**Subscription: `SubscribeToMessageReactionUpdatedNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `message_filter` (**optional** {ref}`datatype-messagefilter`)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter`)
* `previous_reaction_filter` (**optional** {ref}`datatype-reactionfilter`)

**Notification *(Stream)*: `MessageReactionUpdatedNotification`**
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)
* `previous_reaction` ({ref}`datatype-messagereaction`)



### MessageReactionRemoved
**Subscription: `SubscribeToMessageReactionRemovedNotification`**
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter`)

**Notification *(Stream)*: `MessageReactionRemovedNotification`**
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)



---

(service-attachmentnotificationservice)=
## AttachmentNotificationService

> **Associated Datatype:** {ref}`datatype-attachment`

### AttachmentReceived
**Subscription: `SubscribeToAttachmentReceivedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-attachmentfilter`)

**Notification *(Stream)*: `AttachmentReceivedNotification`**
* `attachment` ({ref}`datatype-attachment`)



### AttachmentUploaded
**Subscription: `SubscribeToAttachmentUploadedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-attachmentfilter`)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `attachment_ids` (**repeated** {ref}`datatype-attachmentid`)

**Notification *(Stream)*: `AttachmentUploadedNotification`**
* `attachment` ({ref}`datatype-attachment`)



---

(service-discussionnotificationservice)=
## DiscussionNotificationService

> **Associated Datatype:** {ref}`datatype-discussion`

### DiscussionNew
**Subscription: `SubscribeToDiscussionNewNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)

**Notification *(Stream)*: `DiscussionNewNotification`**
* `discussion` ({ref}`datatype-discussion`)



### DiscussionLocked
**Subscription: `SubscribeToDiscussionLockedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)
* `discussion_ids` (**repeated** uint64)

**Notification *(Stream)*: `DiscussionLockedNotification`**
* `discussion` ({ref}`datatype-discussion`)



### DiscussionTitleUpdated
**Subscription: `SubscribeToDiscussionTitleUpdatedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)
* `discussion_ids` (**repeated** uint64)

**Notification *(Stream)*: `DiscussionTitleUpdatedNotification`**
* `discussion` ({ref}`datatype-discussion`)
* `previous_title` (string)



### DiscussionSettingsUpdated
**Subscription: `SubscribeToDiscussionSettingsUpdatedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)
* `discussion_ids` (**repeated** uint64)

**Notification *(Stream)*: `DiscussionSettingsUpdatedNotification`**
* `discussion` ({ref}`datatype-discussion`)
* `new_settings` ({ref}`datatype-discussionsettings`)
* `previous_settings` ({ref}`datatype-discussionsettings`)



---

(service-contactnotificationservice)=
## ContactNotificationService

> **Associated Datatype:** {ref}`datatype-contact`

### ContactNew
**Subscription: `SubscribeToContactNewNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)

**Notification *(Stream)*: `ContactNewNotification`**
* `contact` ({ref}`datatype-contact`)



### ContactDeleted
**Subscription: `SubscribeToContactDeletedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)
* `contact_ids` (**repeated** uint64)

**Notification *(Stream)*: `ContactDeletedNotification`**
* `contact` ({ref}`datatype-contact`)



### ContactDetailsUpdated
**Subscription: `SubscribeToContactDetailsUpdatedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)
* `contact_ids` (**repeated** uint64)

**Notification *(Stream)*: `ContactDetailsUpdatedNotification`**
* `contact` ({ref}`datatype-contact`)
* `previous_details` ({ref}`datatype-identitydetails`)



### ContactPhotoUpdated
**Subscription: `SubscribeToContactPhotoUpdatedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)
* `contact_ids` (**repeated** uint64)

**Notification *(Stream)*: `ContactPhotoUpdatedNotification`**
* `contact` ({ref}`datatype-contact`)



---

(service-groupnotificationservice)=
## GroupNotificationService

> **Associated Datatype:** {ref}`datatype-group`

### GroupNew
**Subscription: `SubscribeToGroupNewNotification`**
* `count` (**optional** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)

**Notification *(Stream)*: `GroupNewNotification`**
* `group` ({ref}`datatype-group`)



### GroupDeleted
**Subscription: `SubscribeToGroupDeletedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)

**Notification *(Stream)*: `GroupDeletedNotification`**
* `group` ({ref}`datatype-group`)



### GroupNameUpdated
**Subscription: `SubscribeToGroupNameUpdatedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `previous_name_search` (**optional** string)

**Notification *(Stream)*: `GroupNameUpdatedNotification`**
* `group` ({ref}`datatype-group`)
* `previous_name` (string)



### GroupPhotoUpdated
**Subscription: `SubscribeToGroupPhotoUpdatedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)

**Notification *(Stream)*: `GroupPhotoUpdatedNotification`**
* `group` ({ref}`datatype-group`)



### GroupDescriptionUpdated
**Subscription: `SubscribeToGroupDescriptionUpdatedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `previous_description_search` (**optional** string)

**Notification *(Stream)*: `GroupDescriptionUpdatedNotification`**
* `group` ({ref}`datatype-group`)
* `previous_description` (string)



### GroupPendingMemberAdded
**Subscription: `SubscribeToGroupPendingMemberAddedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `pending_member_filter` (**optional** {ref}`datatype-pendinggroupmemberfilter`)

**Notification *(Stream)*: `GroupPendingMemberAddedNotification`**
* `group` ({ref}`datatype-group`)
* `pending_member` ({ref}`datatype-pendinggroupmember`)



### GroupPendingMemberRemoved
**Subscription: `SubscribeToGroupPendingMemberRemovedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `pending_member_filter` (**optional** {ref}`datatype-pendinggroupmemberfilter`)

**Notification *(Stream)*: `GroupPendingMemberRemovedNotification`**
* `group` ({ref}`datatype-group`)
* `pending_member` ({ref}`datatype-pendinggroupmember`)



### GroupMemberJoined
**Subscription: `SubscribeToGroupMemberJoinedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter`)

**Notification *(Stream)*: `GroupMemberJoinedNotification`**
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)



### GroupMemberLeft
**Subscription: `SubscribeToGroupMemberLeftNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter`)

**Notification *(Stream)*: `GroupMemberLeftNotification`**
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)



### GroupOwnPermissionsUpdated
**Subscription: `SubscribeToGroupOwnPermissionsUpdatedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter`)
* `previous_permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter`)

**Notification *(Stream)*: `GroupOwnPermissionsUpdatedNotification`**
* `group` ({ref}`datatype-group`)
* `permissions` ({ref}`datatype-groupmemberpermissions`)
* `previous_permissions` ({ref}`datatype-groupmemberpermissions`)



### GroupMemberPermissionsUpdated
**Subscription: `SubscribeToGroupMemberPermissionsUpdatedNotification`**
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter`)
* `previous_permission_filter` (**optional** {ref}`datatype-groupmemberfilter`)

**Notification *(Stream)*: `GroupMemberPermissionsUpdatedNotification`**
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)
* `previous_permissions` ({ref}`datatype-groupmemberpermissions`)



---

(service-invitationnotificationservice)=
## InvitationNotificationService

> **Associated Datatype:** {ref}`datatype-invitation`

### InvitationReceived
**Subscription: `SubscribeToInvitationReceivedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Notification *(Stream)*: `InvitationReceivedNotification`**
* `invitation` ({ref}`datatype-invitation`)



### InvitationSent
**Subscription: `SubscribeToInvitationSentNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Notification *(Stream)*: `InvitationSentNotification`**
* `invitation` ({ref}`datatype-invitation`)



### InvitationDeleted
**Subscription: `SubscribeToInvitationDeletedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)
* `invitation_ids` (**repeated** uint64)

**Notification *(Stream)*: `InvitationDeletedNotification`**
* `invitation` ({ref}`datatype-invitation`)



### InvitationUpdated
**Subscription: `SubscribeToInvitationUpdatedNotification`**
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)
* `invitation_ids` (**repeated** uint64)

**Notification *(Stream)*: `InvitationUpdatedNotification`**
* `invitation` ({ref}`datatype-invitation`)
* `previous_invitation_status` ({ref}`datatype-status`)



---

(service-callnotificationservice)=
## CallNotificationService

> **Associated Datatype:** {ref}`datatype-call`

### CallIncomingCall
**Subscription: `SubscribeToCallIncomingCallNotification`**
* `count` (**optional** uint64)

**Notification *(Stream)*: `CallIncomingCallNotification`**
* `call_identifier` (string)
* `discussion_id` (uint64 - *set to group discussion if calling a group, else to contact's discussion, even if there are multiple participants*)
* `participant_id` ({ref}`datatype-callparticipantid` - *obviously contains a contact id*)
* `caller_display_name` (string)
* `participant_count` (uint32)



### CallRinging
**Subscription: `SubscribeToCallRingingNotification`**
* `count` (**optional** uint64)

**Notification *(Stream)*: `CallRingingNotification`**
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)



### CallAccepted
**Subscription: `SubscribeToCallAcceptedNotification`**
* `count` (**optional** uint64)

**Notification *(Stream)*: `CallAcceptedNotification`**
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)



### CallDeclined
**Subscription: `SubscribeToCallDeclinedNotification`**
* `count` (**optional** uint64)

**Notification *(Stream)*: `CallDeclinedNotification`**
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)



### CallBusy
**Subscription: `SubscribeToCallBusyNotification`**
* `count` (**optional** uint64)

**Notification *(Stream)*: `CallBusyNotification`**
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)



### CallEnded
**Subscription: `SubscribeToCallEndedNotification`**
* `count` (**optional** uint64)

**Notification *(Stream)*: `CallEndedNotification`**
* `call_identifier` (string)



---
