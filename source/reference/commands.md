# Commands



:::{contents} Commands
:depth: 1
:local:
:::
(service-messagecommandservice)=
## Message Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-message`
:::
### MessageList
:::{card}
> List messages for current identity.  
> Pass a filter to select only messages that match specific criteria.  
> You can list unread only messages with _unread_ parameter. This is useful to list unread messages on start if you want to process messages that arrived when you were down.  
> Messages are mark as read when you list them with MessageList or if a MessageReceived notification was sent to any client when it arrived.

**Request**: *MessageListRequest*
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `unread` (**optional** bool - *only list unread messages (messages that have never been listed or sent in a MessageReceived notification)*)

**Response *(Stream)***: *MessageListResponse*
* `messages` (**repeated** {ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INVALID_ARGUMENT`: filter is invalid
 - `INTERNAL`
:::

### MessageGet
:::{card}
> get a specific message by id.

**Request**: *MessageGetRequest*
* `message_id` ({ref}`datatype-messageid`)

**Response**: *MessageGetResponse*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
:::

### MessageSend
:::{card}
> Post a text message in a discussion.  
> A message must have a non-blank body.

**Request**: *MessageSendRequest*
* `discussion_id` (uint64)
* `body` (string)
* `reply_id` (**optional** {ref}`datatype-messageid`)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality`)
* `disable_link_preview` (**optional** bool)

**Response**: *MessageSendResponse*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion / replied message not found.
 - `INVALID_ARGUMENT`: message body is empty or blank.
 - `INTERNAL`
:::

### MessageSendWithAttachments
:::{card}
> Post a message with attachments in a given discussion.  
> A message must have a non empty body or at least one attachment.  
> To allow sending multiple files with no size limitations this entry point is a client stream.  
> First send a MessageSendWithAttachmentsRequest filling metadata field.  
> Then send each file separately by chunks of any size.  
> Always send an empty MessageSendWithAttachmentsRequest with only file_delimiter set to true at the end of each file upload.  
> When all attachments are uploaded server will answer with a MessageSendWithAttachmentsResponse and close stream.

**Request *(Stream)***: *MessageSendWithAttachmentsRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`datatype-messagesendwithattachmentsrequestmetadata`)
  * `payload` (bytes)
  * `file_delimiter` (bool)

**Response**: *MessageSendWithAttachmentsResponse*
* `message` ({ref}`datatype-message`)
* `attachments` (**repeated** {ref}`datatype-attachment`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion / replied message not found.
 - `INVALID_ARGUMENT`: message body is empty or blank with no attached file / attached the same file twice.
 - `INTERNAL`
:::

### MessageReact
:::{card}
> Add, update or remove a reaction from a message.  
> If _reaction_ is set this will add a new reaction or update your previous reaction on this message.  
> If _reaction_ is an empty string your previous reaction will be removed if you had one.

**Request**: *MessageReactRequest*
* `message_id` ({ref}`datatype-messageid`)
* `reaction` (**optional** string)

**Response**: *MessageReactResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INTERNAL`
:::

### MessageUpdateBody
:::{card}
> Update one of your message body.  
> Body cannot be empty or blank.

**Request**: *MessageUpdateBodyRequest*
* `message_id` ({ref}`datatype-messageid`)
* `updated_body` (string)

**Response**: *MessageUpdateBodyResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INVALID_ARGUMENT`: you can only edit your own messages / new body cannot be empty or blank.
 - `INTERNAL`
:::

### MessageDelete
:::{card}
> Delete a message giving its id.  
> TODO delete everywhere ?

**Request**: *MessageDeleteRequest*
* `message_id` ({ref}`datatype-messageid`)
* `delete_everywhere` (**optional** bool)

**Response**: *MessageDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INTERNAL`
:::

### MessageSendLocation
:::{card}
> Post a location message in a discussion.  
> A location message represents a specific location, and is different from a location sharing that can be updated later.

**Request**: *MessageSendLocationRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)
* `address` (**optional** string)
* `preview_filename` (**optional** string - *attach an option preview as a picture, specify filename to use*)
* `preview_payload` (**optional** bytes - *attach an option preview as a picture, specify payload (must be smaller than grpc max message size)*)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality` - *make your location message ephemeral*)

**Response**: *MessageSendLocationResponse*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion not found.
 - `INVALID_ARGUMENT`: latitude and longitude are both equal to zero / preview_filename and preview_payload must be set together.
 - `INTERNAL`
:::

### MessageStartLocationSharing
:::{card}
> Start sharing a location in a discussion.

**Request**: *MessageStartLocationSharingRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response**: *MessageStartLocationSharingResponse*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion not found.
 - `INVALID_ARGUMENT`: latitude and longitude are both equal to zero.
 - `INTERNAL`
:::

### MessageUpdateLocationSharing
:::{card}
> Update one of your sharing location message with a new location.

**Request**: *MessageUpdateLocationSharingRequest*
* `message_id` ({ref}`datatype-messageid`)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response**: *MessageUpdateLocationSharingResponse*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INVALID_ARGUMENT`: you can only update your location sharing messages / sharing is no longer active.
 - `INTERNAL`
:::

### MessageEndLocationSharing
:::{card}
**Request**: *MessageEndLocationSharingRequest*
* `message_id` ({ref}`datatype-messageid`)

**Response**: *MessageEndLocationSharingResponse*
* `message` ({ref}`datatype-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INVALID_ARGUMENT`: you can only end your location sharing messages / sharing is no longer active.
 - `INTERNAL`
:::

### MessageRefresh
:::{card}
> Manually refresh messages available on server.

**Request**: *MessageRefreshRequest*
* *Empty payload.*

**Response**: *MessageRefreshResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-attachmentcommandservice)=
## Attachment Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-attachment`
:::
### AttachmentList
:::{card}
> List attachments for current identity.  
> Pass a filter to select only attachments that match specific criteria.

**Request**: *AttachmentListRequest*
* `filter` (**optional** {ref}`datatype-attachmentfilter`)

**Response *(Stream)***: *AttachmentListResponse*
* `attachments` (**repeated** {ref}`datatype-attachment`)

**Error Codes**:
- `NOT_FOUND` ("Message not found"): filter.messageId does not belong to an identity message.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### AttachmentGet
:::{card}
> Get an attachment by id.

**Request**: *AttachmentGetRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response**: *AttachmentGetResponse*
* `attachment` ({ref}`datatype-attachment`)

**Error Codes**:
- `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### AttachmentDelete
:::{card}
> Delete an attachment by id.

**Request**: *AttachmentDeleteRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)
* `delete_everywhere` (**optional** bool)

**Response**: *AttachmentDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### AttachmentDownload
:::{card}
> Download the file associated to an attachment.  
> This returns one or more chunks of bytes.

**Request**: *AttachmentDownloadRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response *(Stream)***: *AttachmentDownloadResponse*
* `chunk` (bytes)

**Error Codes**:
- `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-discussioncommandservice)=
## Discussion Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-discussion`
:::
### DiscussionList
:::{card}
> List discussions for current identity.  
> Pass a filter to select only discussions that match specific criteria.

**Request**: *DiscussionListRequest*
* `filter` (**optional** {ref}`datatype-discussionfilter`)

**Response *(Stream)***: *DiscussionListResponse*
* `discussions` (**repeated** {ref}`datatype-discussion`)

**Error Codes**:
- `INVALID_ARGUMENT`: invalid filter.
 - `NOT_FOUND`: filter contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### DiscussionGet
:::{card}
> Get discussion by id.

**Request**: *DiscussionGetRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionGetResponse*
* `discussion` ({ref}`datatype-discussion`)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionGetBytesIdentifier
:::{card}
> Get a discussion identifier as bytes.  
> This is useful to have a long term identifier for a discussion, backup-proof, and common to any device.

**Request**: *DiscussionGetBytesIdentifierRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionGetByContact
:::{card}
> Get discussion by contact id.

**Request**: *DiscussionGetByContactRequest*
* `contact_id` (uint64)

**Response**: *DiscussionGetByContactResponse*
* `discussion` ({ref}`datatype-discussion`)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionGetByGroup
:::{card}
> Get discussion by group id.

**Request**: *DiscussionGetByGroupRequest*
* `group_id` (uint64)

**Response**: *DiscussionGetByGroupResponse*
* `discussion` ({ref}`datatype-discussion`)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionEmpty
:::{card}
> Delete all messages and attachments in a discussion.

**Request**: *DiscussionEmptyRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionEmptyResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### DiscussionDownloadPhoto
:::{card}
> Download a discussion photo.  
> The photo can be the contact photo, the group photo, or a generated image for the discussion if a specific image was not set.  
> Photos are always jpeg files with a maximum of 1080x1080 resolution.

**Request**: *DiscussionDownloadPhotoRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### DiscussionLockedList
:::{card}
> locked discussions

**Request**: *DiscussionLockedListRequest*
DiscussionLockedList
List locked discussions.
Locked discussions are discussions associated to a deleted contact or a group you left.
Messages in those discussions are still accessible, but you cannot post new messages in those discussions.

**Error codes**:
`UNAUTHENTICATED`: client key is invalid.
`INTERNAL`

* *Empty payload.*

**Response *(Stream)***: *DiscussionLockedListResponse*
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

### DiscussionLockedDelete
:::{card}
> Delete a locked discussion by id.  
> This will delete discussion and its content, including messages and attached files.

**Request**: *DiscussionLockedDeleteRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionLockedDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-contactcommandservice)=
## Contact Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-contact`
:::
### ContactList
:::{card}
> List contacts for current identity.  
> Pass a filter to select only contacts that match specific criteria.

**Request**: *ContactListRequest*
* `filter` (**optional** {ref}`datatype-contactfilter`)

**Response *(Stream)***: *ContactListResponse*
* `contacts` (**repeated** {ref}`datatype-contact`)

**Error Codes**:
- `INVALID_ARGUMENT`: invalid filter.
 - `UNAUTHENTICATED`: client key is invalid
 - `INTERNAL`
:::

### ContactGet
:::{card}
> Get a contact by id.

**Request**: *ContactGetRequest*
* `contact_id` (uint64)

**Response**: *ContactGetResponse*
* `contact` ({ref}`datatype-contact`)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ContactGetBytesIdentifier
:::{card}
> Get a contact identity as bytes.  
> This is useful to have a long term identifier for a contact, backup-proof, and common to any device.

**Request**: *ContactGetBytesIdentifierRequest*
* `contact_id` (uint64)

**Response**: *ContactGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ContactGetInvitationLink
:::{card}
> Get a contact invitation link.

**Request**: *ContactGetInvitationLinkRequest*
* `contact_id` (uint64)

**Response**: *ContactGetInvitationLinkResponse*
* `invitation_link` (string)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ContactDelete
:::{card}
> Delete a contact by id.

**Request**: *ContactDeleteRequest*
* `contact_id` (uint64)

**Response**: *ContactDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `INVALID_ARGUMENT`: contact is still in a group.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### ContactIntroduction
:::{card}
> Introduce two of your contacts together.  
> They will both receive an invitation to accept.  
> If each of the two accepts, they will be added to each other's contact book and can exchange.

**Request**: *ContactIntroductionRequest*
* `first_contact_id` (uint64)
* `second_contact_id` (uint64)

**Response**: *ContactIntroductionResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: first or second contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### ContactDownloadPhoto
:::{card}
> Download the contact profile picture as bytes, or the group picture, or the generated image for this discussion.  
> Pictures are always jpeg files with a maximum of 1080x1080 resolution.

**Request**: *ContactDownloadPhotoRequest*
* `contact_id` (uint64)

**Response**: *ContactDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ContactRecreateChannels
:::{card}
> Reset cryptographic channels with a contact.  
> USE CAREFULLY: this might fix some issues but every non sent / received messages will be lost.

**Request**: *ContactRecreateChannelsRequest*
* `contact_id` (uint64)

**Response**: *ContactRecreateChannelsResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### ContactInviteToOneToOneDiscussion
:::{card}
> collected contacts

**Request**: *ContactInviteToOneToOneDiscussionRequest*
ContactInviteToOneToOneDiscussion
Invite a non one-to-one contact to have a one-to-one discussion.

**Error codes**:
`NOT_FOUND`: contact not found.
`INVALID_ARGUMENT`: contact already has a one to one discussion.
`UNAUTHENTICATED`: client key is invalid.
`INTERNAL`

* `contact_id` (uint64)

**Response**: *ContactInviteToOneToOneDiscussionResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

### ContactDowngradeOneToOneDiscussion
:::{card}
> ContactDowngradeOneToOne  
> Downgrade a one-to-one contact to a non one-to-one contact.  
> This will lock current discussion with this contact.  
> The contact will always be in your contact book and common groups but you will no longer be able to exchange direct message.

**Request**: *ContactDowngradeOneToOneDiscussionRequest*
* `contact_id` (uint64)

**Response**: *ContactDowngradeOneToOneDiscussionResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `INVALID_ARGUMENT`: contact is not one to one, does not have established channel or does not support one to one downgrade.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

---

(service-groupcommandservice)=
## Group Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-group`
:::
### GroupList
:::{card}
> List groups for current identity.  
> Pass a filter to select only groups that match specific criteria.

**Request**: *GroupListRequest*
* `filter` (**optional** {ref}`datatype-groupfilter`)

**Response *(Stream)***: *GroupListResponse*
* `groups` (**repeated** {ref}`datatype-group`)

**Error Codes**:
- `INVALID_ARGUMENT`: invalid filter.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupGet
:::{card}
> Get group by id.

**Request**: *GroupGetRequest*
* `group_id` (uint64)

**Response**: *GroupGetResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupGetBytesIdentifier
:::{card}
> Get a group identifier as bytes.  
> This is useful to have a long term identifier for a group, backup-proof, and common to any device.

**Request**: *GroupGetBytesIdentifierRequest*
* `group_id` (uint64)

**Response**: *GroupGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### GroupNewStandardGroup
:::{card}
> Create a new standard group.  
> In a standard group all members are administrators, everyone can edit group details and manage group members.

**Request**: *GroupNewStandardGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)

**Response**: *GroupNewStandardGroupResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupNewControlledGroup
:::{card}
> Create a new controlled group.  
> In a controlled group Administrators are specifically designated and they can edit group details and manage group members.  
> Simple members cannot manage the group but they can post messages, attachments and reactions.

**Request**: *GroupNewControlledGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response**: *GroupNewControlledGroupResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: a contact cannot be in admins and members at the same time / at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupNewReadOnlyGroup
:::{card}
> Create a new read-only group.  
> In read only groups only group administrators can manage the group and post messages.  
> Other users can only react to messages.

**Request**: *GroupNewReadOnlyGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response**: *GroupNewReadOnlyGroupResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: a contact cannot be in admins and members at the same time / at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupNewAdvancedGroup
:::{card}
> Create a new advanced group.  
> An advanced group allows to manually assign permissions to all members.

**Request**: *GroupNewAdvancedGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `advanced_configuration` (**optional** {ref}`datatype-advancedconfiguration`)
* `members` (**repeated** {ref}`datatype-groupmember`)

**Response**: *GroupNewAdvancedGroupResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: a contact cannot be in admins and members at the same time / at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupDisband
:::{card}
> Close a group, every member will leave the group and the discussion will be locked for everyone.  
> Only administrators are allowed to disband a group.

**Request**: *GroupDisbandRequest*
* `group_id` (uint64)

**Response**: *GroupDisbandResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `INVALID_ARGUMENT`: impossible to disband a keycloak group.
 - `PERMISSION_DENIED`: you are not admin in this group.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupLeave
:::{card}
> Leave a group, the discussion will still exists for other group members.  
> Any group member can leave a group at any time, except if you are the last administrator in this group (a group must always have an administrator).

**Request**: *GroupLeaveRequest*
* `group_id` (uint64)

**Response**: *GroupLeaveResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `INVALID_ARGUMENT`: impossible to disband a keycloak group / you cannot leave a group if you are the only group administrator.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupUpdate
:::{card}
> Update a group by modifying a Group object retrieved from groupList of groupGet.  
> Supported modifications:  
> - Add a member: create a new GroupMember and add it to members field  
> - Remove a member: remove associated GroupMember from members field  
> - Remove a pending member: remove associated GroupPendingMember from pendingMembers field  
> - Update (pending) member permissions: update permissions in permissions field in GroupMember or GroupPendingMember  
> - Update group name: modify name field  
> - Update group description: modify description field  
> Every other modifications will be ignored. You must keep groupId field properly set.

**Request**: *GroupUpdateRequest*
* `group` ({ref}`datatype-group`)

**Response**: *GroupUpdateResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `PERMISSION_DENIED`: you are not admin in this group.
 - `INVALID_ARGUMENT`: the new group version has not been updated / new group member not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupSetPhoto
:::{card}
**Request *(Stream)***: *GroupSetPhotoRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`datatype-groupsetphotorequestmetadata`)
  * `payload` (bytes)

**Response**: *GroupSetPhotoResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupDownloadPhoto
:::{card}
> Download the group picture as bytes, or the generated image for this group.  
> Pictures are always jpeg files with a maximum of 1080x1080 resolution.

**Request**: *GroupDownloadPhotoRequest*
* `group_id` (uint64)

**Response**: *GroupDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### GroupUnsetPhoto
:::{card}
> Unset the current group picture if there is one.

**Request**: *GroupUnsetPhotoRequest*
* `group_id` (uint64)

**Response**: *GroupUnsetPhotoResponse*
* `group` ({ref}`datatype-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `INVALID_ARGUMENT`: group does not have a photo.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

---

(service-identitycommandservice)=
## Identity Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-identity`
:::
### IdentityGet
:::{card}
> Get your identity details.

**Request**: *IdentityGetRequest*
* *Empty payload.*

**Response**: *IdentityGetResponse*
* `identity` ({ref}`datatype-identity`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### IdentityGetBytesIdentifier
:::{card}
> Get your Olvid identity as bytes.  
> This is useful to have a long term identifier for an identity, backup-proof, and common to any device.

**Request**: *IdentityGetBytesIdentifierRequest*
* *Empty payload.*

**Response**: *IdentityGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### IdentityGetInvitationLink
:::{card}
> Get your invitation link. This link can be sent to other Olvid users to let them send you an invitation.  
> Invitation links can be opened with any Olvid application or opened in a web browser to show a QR code to scan.

**Request**: *IdentityGetInvitationLinkRequest*
* *Empty payload.*

**Response**: *IdentityGetInvitationLinkResponse*
* `invitation_link` (string)

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### IdentityUpdateDetails
:::{card}
> Update your Olvid identity details (first name, last name, company and position).  
> At least one field in first and last name must be non empty.  
> Your details will be visible by your contacts, and your display name is computed from these details.  
> Details for a keycloak managed identity cannot be updated.

**Request**: *IdentityUpdateDetailsRequest*
* `new_details` ({ref}`datatype-identitydetails` - *your new identity details*)

**Response**: *IdentityUpdateDetailsResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `INVALID_ARGUMENT`: at least one of first name and last name must be non empty / cannot update a keycloak managed identity.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentitySetPhoto
:::{card}
**Request *(Stream)***: *IdentitySetPhotoRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`datatype-identitysetphotorequestmetadata`)
  * `payload` (bytes)

**Response**: *IdentitySetPhotoResponse*
* *Empty payload.*

:::

### IdentityDownloadPhoto
:::{card}
> Download your current identity picture.  
> Pictures are always jpeg files with a maximum of 1080x1080 resolution.

**Request**: *IdentityDownloadPhotoRequest*
* *Empty payload.*

**Response**: *IdentityDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### IdentityRemovePhoto
:::{card}
> Remove your current identity picture.  
> The automatically generated identity image will be used instead.

**Request**: *IdentityRemovePhotoRequest*
* *Empty payload.*

**Response**: *IdentityRemovePhotoResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### IdentityGetApiKeyStatus
:::{card}
> Check your current Olvid API key status.  
> API keys allow an identity to initiate calls or to use multi device.

**Request**: *IdentityGetApiKeyStatusRequest*
* *Empty payload.*

**Response**: *IdentityGetApiKeyStatusResponse*
* `api_key` ({ref}`datatype-apikey`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### IdentitySetApiKey
:::{card}
> Manually set an Olvid api key.  
> Olvid api keys are standard uuids.

**Request**: *IdentitySetApiKeyRequest*
* `api_key` (string)

**Response**: *IdentitySetApiKeyResponse*
* `api_key` ({ref}`datatype-apikey`)

**Error Codes**:
- `INVALID_ARGUMENT`: api key format is not valid.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentitySetConfigurationLink
:::{card}
> Set an Olvid configuration link with an api key.

**Request**: *IdentitySetConfigurationLinkRequest*
* `configuration_link` (string)

**Response**: *IdentitySetConfigurationLinkResponse*
* `api_key` ({ref}`datatype-apikey`)

**Error Codes**:
- `INVALID_ARGUMENT`: configuration link is invalid / configuration link is for another server.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-invitationcommandservice)=
## Invitation Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-invitation`
:::
### InvitationList
:::{card}
> List invitations for current identity.  
> Pass a filter to select only invitations that match specific criteria.

**Request**: *InvitationListRequest*
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Response *(Stream)***: *InvitationListResponse*
* `invitations` (**repeated** {ref}`datatype-invitation`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INVALID_ARGUMENT`: invalid filter.
 - `INTERNAL`
:::

### InvitationGet
:::{card}
> Get invitation by id.

**Request**: *InvitationGetRequest*
* `invitation_id` (uint64)

**Response**: *InvitationGetResponse*
* `invitation` ({ref}`datatype-invitation`)

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### InvitationNew
:::{card}
> Send an invitation to another Olvid user using its invitation link.  
> Invitation links start with https://invitation.olvid.io#.  
> Sending an invitation will initiate an invitation protocol and create a new Invitation.

**Request**: *InvitationNewRequest*
* `invitation_url` (string)

**Response**: *InvitationNewResponse*
* `invitation` ({ref}`datatype-invitation`)

**Error Codes**:
- `INVALID_ARGUMENT`: you cannot invite yourself / invitation link is invalid.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### InvitationAccept
:::{card}
> Accept a pending invitation. This will allow protocol to continue.  
> This command is only possible if `invitation.status` is one of the following:  
> - STATUS_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT  
> - STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT

**Request**: *InvitationAcceptRequest*
* `invitation_id` (uint64)

**Response**: *InvitationAcceptResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `INVALID_ARGUMENT`: cannot accept an invitation with this status.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### InvitationDecline
:::{card}
> Decline a pending invitation. This will abort protocol.  
> For invitation, introduction and one to one invitation the other user is not notified you declined the invitation.  
> This command is only possible if `invitation.status` is one of the following:  
> - STATUS_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT  
> - STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT

**Request**: *InvitationDeclineRequest*
* `invitation_id` (uint64)

**Response**: *InvitationDeclineResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### InvitationSas
:::{card}
> Only possible if `invitation.status` is equal to STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE.  
> Set the 4 digit code shown on your partner device.

**Request**: *InvitationSasRequest*
* `invitation_id` (uint64)
* `sas` (string - *4 digit pin code shown on your partner device*)

**Response**: *InvitationSasResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `INVALID_ARGUMENT`: unexpected invitation status.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### InvitationDelete
:::{card}
> Abort the protocol associated to any invitation and delete this invitation.

**Request**: *InvitationDeleteRequest*
* `invitation_id` (uint64)

**Response**: *InvitationDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-settingscommandservice)=
## Settings Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-settings`
:::
### SettingsIdentityGet
:::{card}
> Get current settings for your identity.

**Request**: *SettingsIdentityGetRequest*
* *Empty payload.*

**Response**: *SettingsIdentityGetResponse*
* `identity_settings` ({ref}`datatype-identitysettings`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
:::

### SettingsIdentitySet
:::{card}
> Update your identity settings.  
> ⚠️ Update erases the WHOLE settings.  
> To update current settings use SettingsIdentityGet to get current config, and only edit fields you want to update.

**Request**: *SettingsIdentitySetRequest*
* `identity_settings` ({ref}`datatype-identitysettings`)

**Response**: *SettingsIdentitySetResponse*
* `identity_settings` ({ref}`datatype-identitysettings`)

**Error Codes**:
- `INVALID_ARGUMENT`: cannot set keycloak settings if your identity is not keycloak managed.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### SettingsDiscussionGet
:::{card}
> Get a discussion settings.  
> Those settings are shared with other members of this discussion.  
> For example, a parameter for ephemeral message parameters concerning a discussion would affect all future messages posted in this discussion, from any member.

**Request**: *SettingsDiscussionGetRequest*
* `discussion_id` (uint64)

**Response**: *SettingsDiscussionGetResponse*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

**Error Codes**:
- `NOT_FOUND`: discussion not found
 - `UNAUTHENTICATED`: client key is invalid.
:::

### SettingsDiscussionSet
:::{card}
> Update a discussion settings.  
> ⚠️ Update erases the WHOLE settings.  
> To update current settings use SettingsDiscussionGet to get current config, and only edit fields you want to update.

**Request**: *SettingsDiscussionSetRequest*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

**Response**: *SettingsDiscussionSetResponse*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

**Error Codes**:
- `NOT_FOUND`: discussion not found
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-storagecommandservice)=
## Storage Command Service

:::{admonition} Info
Each client key has its own independent storage space, with a simple key-value system.  
_Storage_ can be seen as a global storage space, compared to _Discussion Storage_ that offers a space associated with a specific discussion.  
  
Both mechanisms are backup resilient, and will be restored with their associated client key in a backup restoration process.  
  
Mind that temporary client keys (specified in daemon environment or as command line arguments) do not have an allocated storage space.  
You must create a client in database to use storage commands.


**Associated Datatype:** {ref}`datatype-storage`
:::
### StorageList
:::{card}
> List stored elements in global storage scope, for current client key.  
> Pass a filter to select only elements that match specific criteria.  
>   
> Mind that temporary client keys (specified in daemon environment or as command line arguments) does not have an allocated storage space.  
> You must create a client in database to use storage commands.

**Request**: *StorageListRequest*
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)***: *StorageListResponse*
* `elements` (**repeated** {ref}`datatype-storageelement`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: invalid filter
 - `INTERNAL`
:::

### StorageGet
:::{card}
> Request the value associated to a key in your global storage.  
> If the key does not already exist, return an empty string.

**Request**: *StorageGetRequest*
* `key` (string)

**Response**: *StorageGetResponse*
* `value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
:::

### StorageSet
:::{card}
> Set the value for a key in your global storage.  
> If the key was already set the value is updated and it returns the *previous_value* in response.

**Request**: *StorageSetRequest*
* `key` (string)
* `value` (string)

**Response**: *StorageSetResponse*
* `previous_value` (string - *if the key already exists, this contains the erased value.*)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INTERNAL`
:::

### StorageUnset
:::{card}
> Unset a key in your global storage.

**Request**: *StorageUnsetRequest*
* `key` (string)

**Response**: *StorageUnsetResponse*
* `previous_value` (string - *the value previously associated to this key*)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
:::

---

(service-discussionstoragecommandservice)=
## Discussion Storage Command Service

:::{admonition} Info
Each client key has its own independent storage space, with a simple key-value system.  
_Storage_ can be seen as a global storage space, compared to _Discussion Storage_ that offers a space associated with a specific discussion.  
  
Both mechanisms are backup resilient, and will be restored with their associated client key in a backup restoration process.  
  
Mind that temporary client keys (specified in daemon environment or as command line arguments) do not have an allocated storage space.  
You must create a client in database to use storage commands.


**Associated Datatype:** {ref}`datatype-discussionstorage`
:::
### DiscussionStorageList
:::{card}
> List stored elements in a specific discussion storage scope, for current client key.  
> Pass a filter to select only elements that match specific criteria.

**Request**: *DiscussionStorageListRequest*
* `discussion_id` (uint64)
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)***: *DiscussionStorageListResponse*
* `elements` (**repeated** {ref}`datatype-storageelement`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key / invalid filter.
 - `NOT_FOUND`: discussion not found.
 - `INTERNAL`
:::

### DiscussionStorageGet
:::{card}
> Request the value associated to a key in the specified discussion storage.  
> If the key does not already exist, return an empty string.

**Request**: *DiscussionStorageGetRequest*
* `discussion_id` (uint64)
* `key` (string)

**Response**: *DiscussionStorageGetResponse*
* `value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key.
 - `NOT_FOUND`: discussion not found.
:::

### DiscussionStorageSet
:::{card}
> Set the value for a key in the specified discussion storage.  
> If the key was already set the value is updated and it returns the *previous_value* in response.

**Request**: *DiscussionStorageSetRequest*
* `discussion_id` (uint64)
* `key` (string)
* `value` (string)

**Response**: *DiscussionStorageSetResponse*
* `previous_value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key.
 - `NOT_FOUND`: discussion not found.
 - `INTERNAL`
:::

### DiscussionStorageUnset
:::{card}
> Unset a key in the specified discussion storage.

**Request**: *DiscussionStorageUnsetRequest*
* `discussion_id` (uint64)
* `key` (string)

**Response**: *DiscussionStorageUnsetResponse*
* `previous_value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key.
 - `NOT_FOUND`: discussion not found.
:::

---

(service-keycloakcommandservice)=
## Keycloak Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-keycloak`
:::
### KeycloakBindIdentity
:::{card}
> Register your identity in a keycloak directory.  
> Your identity should not already be registered in a keycloak directory (`identity.keycloak_managed`).  
> When registered your directory might add you to some managed groups, and you will be granted access to other directory users.  
> Other directory users can be added as contacts with no further confirmation (see *KeycloakUserList* and *KeycloakAddUserAsContact*).

**Request**: *KeycloakBindIdentityRequest*
* `configuration_link` (string)

**Response**: *KeycloakBindIdentityResponse*
* *Empty payload.*

**Error Codes**:
- `INVALID_ARGUMENT`: identity is already keycloak managed.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### KeycloakUnbindIdentity
:::{card}
> Unregister from a keycloak directory.  
> Your identity should already be keycloak managed.  
> You will lose access to keycloak user directory and you will leave keycloak managed groups.  
> Your keycloak managed contacts will remain contacts but won't be keycloak managed anymore.

**Request**: *KeycloakUnbindIdentityRequest*
* *Empty payload.*

**Response**: *KeycloakUnbindIdentityResponse*
* *Empty payload.*

**Error Codes**:
- `INVALID_ARGUMENT`: identity is not keycloak managed.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### KeycloakUserList
:::{card}
> List other users registered on your keycloak directory.  
> Pass a filter to select only users that match specific criteria.

**Request**: *KeycloakUserListRequest*
* `filter` (**optional** {ref}`datatype-keycloakuserfilter`)
* `last_list_timestamp` (**optional** uint64 - *only users that registered on keycloak since this timestamp, set to 0 to list all users.*)

**Response *(Stream)***: *KeycloakUserListResponse*
* `users` (**repeated** {ref}`datatype-keycloakuser`)
* `last_list_timestamp` (uint64 - *set this timestamp in request.last_list_timestamp if you want to list only new users.*)

**Error Codes**:
- `INVALID_ARGUMENT`: identity is not keycloak managed / invalid filter.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
:::

### KeycloakAddUserAsContact
:::{card}
> Add a user from keycloak directory as a contact.  
> This will not trigger any invitation protocol.  
> Directory is considered as a trusted third party so no further confirmation is required.  
> Contact and discussion will be created as soon as one of the other user's device is online and automatically answer "invitation".

**Request**: *KeycloakAddUserAsContactRequest*
* `keycloak_id` (string)

**Response**: *KeycloakAddUserAsContactResponse*
* *Empty payload.*

**Error Codes**:
- `INVALID_ARGUMENT`: identity is not keycloak managed.
 - `NOT_FOUND`: keycloak user not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-callcommandservice)=
## Call Command Service

:::{admonition} Info
Currently daemon cannot handle Olvid calls properly.  
You can be notified on incoming calls, and you can initiate call within discussions or with any contact.  
But we cannot manage audio or video streams, that's why a daemon will always answer any incoming call with a "busy" response.


**Associated Datatype:** {ref}`datatype-call`
:::
### CallStartDiscussionCall
:::{card}
> Start a call with one discussion member(s).  
> This will start a one to one call or a group call depending on discussion type.  
> You can use *call_identifier* to filter later call notifications.

**Request**: *CallStartDiscussionCallRequest*
* `discussion_id` (uint64)

**Response**: *CallStartDiscussionCallResponse*
* `call_identifier` (string)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `INVALID_ARGUMENT`: cannot start a call in an empty group.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### CallStartCustomCall
:::{card}
> Start a call with any contacts, even if they do not belong to the same discussion.  
> You can use *call_identifier* to filter later call notifications.

**Request**: *CallStartCustomCallRequest*
* `contact_ids` (**repeated** uint64)
* `discussion_id` (**optional** uint64 - *specify in which discussion other contacts will log call*)

**Response**: *CallStartCustomCallResponse*
* `call_identifier` (string)

**Error Codes**:
- `NOT_FOUND`: discussion or contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-toolcommandservice)=
## Tool Command Service

:::{admonition} Info
s


**Associated Datatype:** {ref}`datatype-tool`
:::
### Ping
:::{card}
> Unauthenticated method.  
> Just check if daemon is reachable.

**Request**: *PingRequest*
* *Empty payload.*

**Response**: *PingResponse*
* *Empty payload.*

:::

### DaemonVersion
:::{card}
> Authenticated method.  
> Ask daemon its version.

**Request**: *DaemonVersionRequest*
* *Empty payload.*

**Response**: *DaemonVersionResponse*
* `version` (string)

:::

### AuthenticationTest
:::{card}
> Authenticated rpc.  
> Check that sent credentials are valid user credentials, else it returns an error.

**Request**: *AuthenticationTestRequest*
* *Empty payload.*

**Response**: *AuthenticationTestResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: invalid client key.
:::

### AuthenticationAdminTest
:::{card}
> Authenticated rpc (admin key only).  
> Check that sent credentials are valid admin credentials, else it returns an error.

**Request**: *AuthenticationAdminTestRequest*
* *Empty payload.*

**Response**: *AuthenticationAdminTestResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: client key is not an admin client key.
:::
