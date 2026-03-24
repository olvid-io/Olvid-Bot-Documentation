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
**Subscription**: *SubscribeToMessageReceivedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageReceivedNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageSent
:::{card}
**Subscription**: *SubscribeToMessageSentNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageSentNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageDeleted
:::{card}
**Subscription**: *SubscribeToMessageDeletedNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageDeletedNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageBodyUpdated
:::{card}
> datatypes.v1.Message updates

**Subscription**: *SubscribeToMessageBodyUpdatedNotification*
MessageBodyUpdated

* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageBodyUpdatedNotification*
* `message` ({ref}`datatype-message`)
* `previous_body` (string)

:::

### MessageUploaded
:::{card}
> You cannot guarantee this notification will arrive when working with ephemeral message  
>   
>   
> MessageUploaded

**Subscription**: *SubscribeToMessageUploadedNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageUploadedNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageDelivered
:::{card}
> You cannot guarantee this notification will arrive when working with ephemeral message  
>   
>   
> MessageDelivered

**Subscription**: *SubscribeToMessageDeliveredNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageDeliveredNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageRead
:::{card}
> You cannot guarantee this notification will arrive when working with ephemeral message  
>   
>   
> MessageRead

**Subscription**: *SubscribeToMessageReadNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageReadNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageLocationReceived
:::{card}
> location message

**Subscription**: *SubscribeToMessageLocationReceivedNotification*
MessageLocationReceived
triggered by inbound messages

* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageLocationReceivedNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageLocationSent
:::{card}
> triggered by outbound messages

**Subscription**: *SubscribeToMessageLocationSentNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageLocationSentNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageLocationSharingStart
:::{card}
> triggered by inbound AND outbound messages

**Subscription**: *SubscribeToMessageLocationSharingStartNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageLocationSharingStartNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageLocationSharingUpdate
:::{card}
> triggered by inbound AND outbound messages

**Subscription**: *SubscribeToMessageLocationSharingUpdateNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageLocationSharingUpdateNotification*
* `message` ({ref}`datatype-message`)
* `previous_location` ({ref}`datatype-messagelocation`)

:::

### MessageLocationSharingEnd
:::{card}
> triggered by inbound AND outbound messages

**Subscription**: *SubscribeToMessageLocationSharingEndNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)

**Notification *(Stream)***: *MessageLocationSharingEndNotification*
* `message` ({ref}`datatype-message`)

:::

### MessageReactionAdded
:::{card}
> datatypes.v1.Message reactions

**Subscription**: *SubscribeToMessageReactionAddedNotification*
MessageReactionAdded

* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter`)

**Notification *(Stream)***: *MessageReactionAddedNotification*
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)

:::

### MessageReactionUpdated
:::{card}
**Subscription**: *SubscribeToMessageReactionUpdatedNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `message_filter` (**optional** {ref}`datatype-messagefilter`)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter`)
* `previous_reaction_filter` (**optional** {ref}`datatype-reactionfilter`)

**Notification *(Stream)***: *MessageReactionUpdatedNotification*
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)
* `previous_reaction` ({ref}`datatype-messagereaction`)

:::

### MessageReactionRemoved
:::{card}
**Subscription**: *SubscribeToMessageReactionRemovedNotification*
* `count` (**optional** uint64)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `reaction_filter` (**optional** {ref}`datatype-reactionfilter`)

**Notification *(Stream)***: *MessageReactionRemovedNotification*
* `message` ({ref}`datatype-message`)
* `reaction` ({ref}`datatype-messagereaction`)

:::

---

(service-attachmentnotificationservice)=
## Attachment Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-attachment`
:::
### AttachmentReceived
:::{card}
**Subscription**: *SubscribeToAttachmentReceivedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-attachmentfilter`)

**Notification *(Stream)***: *AttachmentReceivedNotification*
* `attachment` ({ref}`datatype-attachment`)

:::

### AttachmentUploaded
:::{card}
**Subscription**: *SubscribeToAttachmentUploadedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-attachmentfilter`)
* `message_ids` (**repeated** {ref}`datatype-messageid`)
* `attachment_ids` (**repeated** {ref}`datatype-attachmentid`)

**Notification *(Stream)***: *AttachmentUploadedNotification*
* `attachment` ({ref}`datatype-attachment`)

:::

---

(service-discussionnotificationservice)=
## Discussion Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-discussion`
:::
### DiscussionNew
:::{card}
**Subscription**: *SubscribeToDiscussionNewNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)

**Notification *(Stream)***: *DiscussionNewNotification*
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionLocked
:::{card}
**Subscription**: *SubscribeToDiscussionLockedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)
* `discussion_ids` (**repeated** uint64)

**Notification *(Stream)***: *DiscussionLockedNotification*
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionTitleUpdated
:::{card}
**Subscription**: *SubscribeToDiscussionTitleUpdatedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)
* `discussion_ids` (**repeated** uint64)

**Notification *(Stream)***: *DiscussionTitleUpdatedNotification*
* `discussion` ({ref}`datatype-discussion`)
* `previous_title` (string)

:::

### DiscussionSettingsUpdated
:::{card}
**Subscription**: *SubscribeToDiscussionSettingsUpdatedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-discussionfilter`)
* `discussion_ids` (**repeated** uint64)

**Notification *(Stream)***: *DiscussionSettingsUpdatedNotification*
* `discussion` ({ref}`datatype-discussion`)
* `new_settings` ({ref}`datatype-discussionsettings`)
* `previous_settings` ({ref}`datatype-discussionsettings`)

:::

---

(service-contactnotificationservice)=
## Contact Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-contact`
:::
### ContactNew
:::{card}
**Subscription**: *SubscribeToContactNewNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)

**Notification *(Stream)***: *ContactNewNotification*
* `contact` ({ref}`datatype-contact`)

:::

### ContactDeleted
:::{card}
**Subscription**: *SubscribeToContactDeletedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)
* `contact_ids` (**repeated** uint64)

**Notification *(Stream)***: *ContactDeletedNotification*
* `contact` ({ref}`datatype-contact`)

:::

### ContactDetailsUpdated
:::{card}
**Subscription**: *SubscribeToContactDetailsUpdatedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)
* `contact_ids` (**repeated** uint64)

**Notification *(Stream)***: *ContactDetailsUpdatedNotification*
* `contact` ({ref}`datatype-contact`)
* `previous_details` ({ref}`datatype-identitydetails`)

:::

### ContactPhotoUpdated
:::{card}
**Subscription**: *SubscribeToContactPhotoUpdatedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-contactfilter`)
* `contact_ids` (**repeated** uint64)

**Notification *(Stream)***: *ContactPhotoUpdatedNotification*
* `contact` ({ref}`datatype-contact`)

:::

---

(service-groupnotificationservice)=
## Group Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-group`
:::
### GroupNew
:::{card}
**Subscription**: *SubscribeToGroupNewNotification*
* `count` (**optional** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)

**Notification *(Stream)***: *GroupNewNotification*
* `group` ({ref}`datatype-group`)

:::

### GroupDeleted
:::{card}
**Subscription**: *SubscribeToGroupDeletedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)

**Notification *(Stream)***: *GroupDeletedNotification*
* `group` ({ref}`datatype-group`)

:::

### GroupNameUpdated
:::{card}
**Subscription**: *SubscribeToGroupNameUpdatedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `previous_name_search` (**optional** string)

**Notification *(Stream)***: *GroupNameUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `previous_name` (string)

:::

### GroupPhotoUpdated
:::{card}
**Subscription**: *SubscribeToGroupPhotoUpdatedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)

**Notification *(Stream)***: *GroupPhotoUpdatedNotification*
* `group` ({ref}`datatype-group`)

:::

### GroupDescriptionUpdated
:::{card}
**Subscription**: *SubscribeToGroupDescriptionUpdatedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `previous_description_search` (**optional** string)

**Notification *(Stream)***: *GroupDescriptionUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `previous_description` (string)

:::

### GroupPendingMemberAdded
:::{card}
**Subscription**: *SubscribeToGroupPendingMemberAddedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `pending_member_filter` (**optional** {ref}`datatype-pendinggroupmemberfilter`)

**Notification *(Stream)***: *GroupPendingMemberAddedNotification*
* `group` ({ref}`datatype-group`)
* `pending_member` ({ref}`datatype-pendinggroupmember`)

:::

### GroupPendingMemberRemoved
:::{card}
**Subscription**: *SubscribeToGroupPendingMemberRemovedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `pending_member_filter` (**optional** {ref}`datatype-pendinggroupmemberfilter`)

**Notification *(Stream)***: *GroupPendingMemberRemovedNotification*
* `group` ({ref}`datatype-group`)
* `pending_member` ({ref}`datatype-pendinggroupmember`)

:::

### GroupMemberJoined
:::{card}
**Subscription**: *SubscribeToGroupMemberJoinedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter`)

**Notification *(Stream)***: *GroupMemberJoinedNotification*
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)

:::

### GroupMemberLeft
:::{card}
**Subscription**: *SubscribeToGroupMemberLeftNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter`)

**Notification *(Stream)***: *GroupMemberLeftNotification*
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)

:::

### GroupOwnPermissionsUpdated
:::{card}
> triggered when your permissions are updated

**Subscription**: *SubscribeToGroupOwnPermissionsUpdatedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter`)
* `previous_permissions_filter` (**optional** {ref}`datatype-grouppermissionfilter`)

**Notification *(Stream)***: *GroupOwnPermissionsUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `permissions` ({ref}`datatype-groupmemberpermissions`)
* `previous_permissions` ({ref}`datatype-groupmemberpermissions`)

:::

### GroupMemberPermissionsUpdated
:::{card}
> triggered when permissions of a group member are updated

**Subscription**: *SubscribeToGroupMemberPermissionsUpdatedNotification*
* `count` (**optional** uint64)
* `group_ids` (**repeated** uint64)
* `group_filter` (**optional** {ref}`datatype-groupfilter`)
* `member_filter` (**optional** {ref}`datatype-groupmemberfilter`)
* `previous_permission_filter` (**optional** {ref}`datatype-groupmemberfilter`)

**Notification *(Stream)***: *GroupMemberPermissionsUpdatedNotification*
* `group` ({ref}`datatype-group`)
* `member` ({ref}`datatype-groupmember`)
* `previous_permissions` ({ref}`datatype-groupmemberpermissions`)

:::

---

(service-invitationnotificationservice)=
## Invitation Notification Service

:::{admonition} Info
must be for admin only  
// Identity  
service IdentityNotificationService {  
rpc IdentityCreated(notification.v1.SubscribeToIdentityCreatedNotification) returns (stream notification.v1.IdentityCreatedNotification) {}  
rpc IdentityDeleted(notification.v1.SubscribeToIdentityDeletedNotification) returns (stream notification.v1.IdentityDeletedNotification) {}  
rpc IdentityDetailsUpdated(notification.v1.SubscribeToIdentityDetailsUpdatedNotification) returns (stream notification.v1.IdentityDetailsUpdatedNotification) {}  
}  
  
Invitation


**Associated Datatype:** {ref}`datatype-invitation`
:::
### InvitationReceived
:::{card}
**Subscription**: *SubscribeToInvitationReceivedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Notification *(Stream)***: *InvitationReceivedNotification*
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationSent
:::{card}
**Subscription**: *SubscribeToInvitationSentNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Notification *(Stream)***: *InvitationSentNotification*
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationDeleted
:::{card}
**Subscription**: *SubscribeToInvitationDeletedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)
* `invitation_ids` (**repeated** uint64)

**Notification *(Stream)***: *InvitationDeletedNotification*
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationUpdated
:::{card}
**Subscription**: *SubscribeToInvitationUpdatedNotification*
* `count` (**optional** uint64)
* `filter` (**optional** {ref}`datatype-invitationfilter`)
* `invitation_ids` (**repeated** uint64)

**Notification *(Stream)***: *InvitationUpdatedNotification*
* `invitation` ({ref}`datatype-invitation`)
* `previous_invitation_status` ({ref}`datatype-status`)

:::

---

(service-callnotificationservice)=
## Call Notification Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-call`
:::
### CallIncomingCall
:::{card}
> PUBLIC API  
>   
>   
> CallIncomingCall (Inbound call)

**Subscription**: *SubscribeToCallIncomingCallNotification*
* `count` (**optional** uint64)

**Notification *(Stream)***: *CallIncomingCallNotification*
* `call_identifier` (string)
* `discussion_id` (uint64 - *set to group discussion if calling a group, else to contact's discussion, even if there are multiple participants*)
* `participant_id` ({ref}`datatype-callparticipantid` - *obviously contains a contact id*)
* `caller_display_name` (string)
* `participant_count` (uint32)

:::

### CallRinging
:::{card}
> (Outbound call)

**Subscription**: *SubscribeToCallRingingNotification*
* `count` (**optional** uint64)

**Notification *(Stream)***: *CallRingingNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

:::

### CallAccepted
:::{card}
> (Outbound call)

**Subscription**: *SubscribeToCallAcceptedNotification*
* `count` (**optional** uint64)

**Notification *(Stream)***: *CallAcceptedNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

:::

### CallDeclined
:::{card}
> (Outbound call)

**Subscription**: *SubscribeToCallDeclinedNotification*
* `count` (**optional** uint64)

**Notification *(Stream)***: *CallDeclinedNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

:::

### CallBusy
:::{card}
> (Outbound call)

**Subscription**: *SubscribeToCallBusyNotification*
* `count` (**optional** uint64)

**Notification *(Stream)***: *CallBusyNotification*
* `call_identifier` (string)
* `participant_id` ({ref}`datatype-callparticipantid`)

:::

### CallEnded
:::{card}
> : everyone declined or left call

**Subscription**: *SubscribeToCallEndedNotification*
* `count` (**optional** uint64)

**Notification *(Stream)***: *CallEndedNotification*
* `call_identifier` (string)

:::
