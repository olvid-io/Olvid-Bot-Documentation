# Commands

List all the actions you can perform with your Olvid identity, using daemon APi.

:::{contents} Commands
:depth: 1
:local:
:::
(service-messagecommandservice)=
## Message Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-message`
:::
(rpc-messagelist)=
### MessageList
::::::{card}
> List messages for current identity.  
> Pass a filter to select only messages that match specific criteria.  
> You can list unread only messages with _unread_ parameter. This is useful to list unread messages on start if you want to process messages that arrived when you were down.  
> Messages are mark as read when you list them with MessageList or if a MessageReceived notification was sent to any client when it arrived.

(message-messagelistrequest)=
**Request**: *MessageListRequest*
* `filter` (**optional** {ref}`message-messagefilter`)
* `unread` (**optional** bool - *only list unread messages (messages that have never been listed or sent in a MessageReceived notification)*)

(message-messagelistresponse)=
**Response *(Stream)***: *MessageListResponse*
* `messages` (**repeated** {ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INVALID_ARGUMENT`: filter is invalid
 - `INTERNAL`
::::::

(rpc-messageget)=
### MessageGet
::::::{card}
> get a specific message by id.

(message-messagegetrequest)=
**Request**: *MessageGetRequest*
* `message_id` ({ref}`message-messageid`)

(message-messagegetresponse)=
**Response**: *MessageGetResponse*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
::::::

(rpc-messagesend)=
### MessageSend
::::::{card}
> Post a text message in a discussion.  
> A message must have a non-blank body.

(message-messagesendrequest)=
**Request**: *MessageSendRequest*
* `discussion_id` (uint64 - *the discussion to post the message into*)
* `body` (string - *text body for the message*)
* `reply_id` (**optional** {ref}`message-messageid` - *the id of a message to quote*)
* `ephemerality` (**optional** {ref}`message-messageephemerality` - *set an ephemerality for this message*)
* `disable_link_preview` (**optional** bool - *do not download link preview if a link is detected in the message body (make send process faster)*)

(message-messagesendresponse)=
**Response**: *MessageSendResponse*
* `message` ({ref}`message-message` - *sent message*)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion / replied message not found.
 - `INVALID_ARGUMENT`: message body is empty or blank.
 - `INTERNAL`
::::::

(rpc-messagesendwithattachments)=
### MessageSendWithAttachments
::::::{card}
> Post a message with attachments in a given discussion.  
> A message must have a non empty body or at least one attachment.  
> To allow sending multiple files with no size limitations this entry point is a client stream.  
> First send a MessageSendWithAttachmentsRequest filling metadata field.  
> Then send each file separately by chunks of any size.  
> Always send an empty MessageSendWithAttachmentsRequest with only file_delimiter set to true at the end of each file upload.  
> Once attachments uploaded finished daemon will answer with a {ref}`response <message-MessageSendWithAttachmentsResponse>` and close stream.

(message-messagesendwithattachmentsrequest)=
**Request *(Stream)***: *MessageSendWithAttachmentsRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`message-messagesendwithattachmentsrequestmetadata`)
  * `payload` (bytes)
  * `file_delimiter` (bool)

(message-messagesendwithattachmentsresponse)=
**Response**: *MessageSendWithAttachmentsResponse*
* `message` ({ref}`message-message` - *sent message*)
* `attachments` (**repeated** {ref}`message-attachment` - *sent attachments*)

:::::{card}
(message-messagesendwithattachmentsrequestmetadata)=
##### MessageSendWithAttachmentsRequestMetadata

**Fields:**
* `discussion_id` (uint64 - *the discussion to post the message into*)
* `body` (**optional** string - *text body, mandatory if there are no attached files*)
* `reply_id` (**optional** {ref}`message-messageid` - *the id of a message to quote*)
* `ephemerality` (**optional** {ref}`message-messageephemerality` - *set an ephemerality for message and attachments*)
* `disable_link_preview` (**optional** bool - *do not download link preview if a link is detected in the message body (make send process faster)*)
* `files` (**repeated** {ref}`message-messagesendwithattachmentsrequestmetadata.file` - *a list of files to attach to the message*)
:::::
:::::{card}
(message-messagesendwithattachmentsrequestmetadata.file)=
##### MessageSendWithAttachmentsRequestMetadata.File

> describe a file you want to attach to a message

**Fields:**
* `filename` (string)
* `file_size` (uint64 - *file size in bytes*)
:::::
**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion / replied message not found.
 - `INVALID_ARGUMENT`: message body is empty or blank with no attached file / attached the same file twice.
 - `INTERNAL`
::::::

(rpc-messagereact)=
### MessageReact
::::::{card}
> Add, update or remove a reaction from a message.  
> If _reaction_ is set this will add a new reaction or update your previous reaction on this message.  
> If _reaction_ is an empty string your previous reaction will be removed if you had one.

(message-messagereactrequest)=
**Request**: *MessageReactRequest*
* `message_id` ({ref}`message-messageid` - *the message to react*)
* `reaction` (**optional** string - *an emoji string*)

(message-messagereactresponse)=
**Response**: *MessageReactResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INTERNAL`
::::::

(rpc-messageupdatebody)=
### MessageUpdateBody
::::::{card}
> Update one of your message body.  
> Body cannot be empty or blank.

(message-messageupdatebodyrequest)=
**Request**: *MessageUpdateBodyRequest*
* `message_id` ({ref}`message-messageid` - *the message to update*)
* `updated_body` (string - *the new body*)

(message-messageupdatebodyresponse)=
**Response**: *MessageUpdateBodyResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INVALID_ARGUMENT`: you can only edit your own messages / new body cannot be empty or blank.
 - `INTERNAL`
::::::

(rpc-messagedelete)=
### MessageDelete
::::::{card}
> Delete a message giving its id.  
> TODO delete everywhere ?

(message-messagedeleterequest)=
**Request**: *MessageDeleteRequest*
* `message_id` ({ref}`message-messageid`)
* `delete_everywhere` (**optional** bool)

(message-messagedeleteresponse)=
**Response**: *MessageDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INTERNAL`
::::::

(rpc-messagesendlocation)=
### MessageSendLocation
::::::{card}
> Post a location message in a discussion.  
> A location message represents a specific location, and is different from a location sharing that can be updated later.

(message-messagesendlocationrequest)=
**Request**: *MessageSendLocationRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)
* `address` (**optional** string)
* `preview_filename` (**optional** string - *attach an option preview as a picture, specify filename to use*)
* `preview_payload` (**optional** bytes - *attach an option preview as a picture, specify payload (must be smaller than grpc max message size)*)
* `ephemerality` (**optional** {ref}`message-messageephemerality` - *make your location message ephemeral*)

(message-messagesendlocationresponse)=
**Response**: *MessageSendLocationResponse*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion not found.
 - `INVALID_ARGUMENT`: latitude and longitude are both equal to zero / preview_filename and preview_payload must be set together.
 - `INTERNAL`
::::::

(rpc-messagestartlocationsharing)=
### MessageStartLocationSharing
::::::{card}
> Start sharing a location in a discussion.

(message-messagestartlocationsharingrequest)=
**Request**: *MessageStartLocationSharingRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

(message-messagestartlocationsharingresponse)=
**Response**: *MessageStartLocationSharingResponse*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: discussion not found.
 - `INVALID_ARGUMENT`: latitude and longitude are both equal to zero.
 - `INTERNAL`
::::::

(rpc-messageupdatelocationsharing)=
### MessageUpdateLocationSharing
::::::{card}
> Update one of your sharing location message with a new location.

(message-messageupdatelocationsharingrequest)=
**Request**: *MessageUpdateLocationSharingRequest*
* `message_id` ({ref}`message-messageid`)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

(message-messageupdatelocationsharingresponse)=
**Response**: *MessageUpdateLocationSharingResponse*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INVALID_ARGUMENT`: you can only update your location sharing messages / sharing is no longer active.
 - `INTERNAL`
::::::

(rpc-messageendlocationsharing)=
### MessageEndLocationSharing
::::::{card}
(message-messageendlocationsharingrequest)=
**Request**: *MessageEndLocationSharingRequest*
* `message_id` ({ref}`message-messageid`)

(message-messageendlocationsharingresponse)=
**Response**: *MessageEndLocationSharingResponse*
* `message` ({ref}`message-message`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `NOT_FOUND`: message not found.
 - `INVALID_ARGUMENT`: you can only end your location sharing messages / sharing is no longer active.
 - `INTERNAL`
::::::

(rpc-messagerefresh)=
### MessageRefresh
::::::{card}
> Manually refresh messages available on server.

(message-messagerefreshrequest)=
**Request**: *MessageRefreshRequest*
* *Empty payload.*

(message-messagerefreshresponse)=
**Response**: *MessageRefreshResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-attachmentcommandservice)=
## Attachment Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-attachment`
:::
(rpc-attachmentlist)=
### AttachmentList
::::::{card}
> List attachments for current identity.  
> Pass a filter to select only attachments that match specific criteria.

(message-attachmentlistrequest)=
**Request**: *AttachmentListRequest*
* `filter` (**optional** {ref}`message-attachmentfilter`)

(message-attachmentlistresponse)=
**Response *(Stream)***: *AttachmentListResponse*
* `attachments` (**repeated** {ref}`message-attachment`)

**Error Codes**:
- `NOT_FOUND` ("Message not found"): filter.messageId does not belong to an identity message.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-attachmentget)=
### AttachmentGet
::::::{card}
> Get an attachment by id.

(message-attachmentgetrequest)=
**Request**: *AttachmentGetRequest*
* `attachment_id` ({ref}`message-attachmentid`)

(message-attachmentgetresponse)=
**Response**: *AttachmentGetResponse*
* `attachment` ({ref}`message-attachment`)

**Error Codes**:
- `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-attachmentdelete)=
### AttachmentDelete
::::::{card}
> Delete an attachment by id.

(message-attachmentdeleterequest)=
**Request**: *AttachmentDeleteRequest*
* `attachment_id` ({ref}`message-attachmentid`)
* `delete_everywhere` (**optional** bool)

(message-attachmentdeleteresponse)=
**Response**: *AttachmentDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-attachmentdownload)=
### AttachmentDownload
::::::{card}
> Download the file associated to an attachment.  
> This returns one or more chunks of bytes.

(message-attachmentdownloadrequest)=
**Request**: *AttachmentDownloadRequest*
* `attachment_id` ({ref}`message-attachmentid`)

(message-attachmentdownloadresponse)=
**Response *(Stream)***: *AttachmentDownloadResponse*
* `chunk` (bytes)

**Error Codes**:
- `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-discussioncommandservice)=
## Discussion Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-discussion`
:::
(rpc-discussionlist)=
### DiscussionList
::::::{card}
> List discussions for current identity.  
> Pass a filter to select only discussions that match specific criteria.

(message-discussionlistrequest)=
**Request**: *DiscussionListRequest*
* `filter` (**optional** {ref}`message-discussionfilter`)

(message-discussionlistresponse)=
**Response *(Stream)***: *DiscussionListResponse*
* `discussions` (**repeated** {ref}`message-discussion`)

**Error Codes**:
- `INVALID_ARGUMENT`: invalid filter.
 - `NOT_FOUND`: filter contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-discussionget)=
### DiscussionGet
::::::{card}
> Get discussion by id.

(message-discussiongetrequest)=
**Request**: *DiscussionGetRequest*
* `discussion_id` (uint64)

(message-discussiongetresponse)=
**Response**: *DiscussionGetResponse*
* `discussion` ({ref}`message-discussion`)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussiongetbytesidentifier)=
### DiscussionGetBytesIdentifier
::::::{card}
> Get a discussion identifier as bytes.  
> This is useful to have a long term identifier for a discussion, backup-proof, and common to any device.

(message-discussiongetbytesidentifierrequest)=
**Request**: *DiscussionGetBytesIdentifierRequest*
* `discussion_id` (uint64)

(message-discussiongetbytesidentifierresponse)=
**Response**: *DiscussionGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussiongetbycontact)=
### DiscussionGetByContact
::::::{card}
> Get discussion by contact id.

(message-discussiongetbycontactrequest)=
**Request**: *DiscussionGetByContactRequest*
* `contact_id` (uint64)

(message-discussiongetbycontactresponse)=
**Response**: *DiscussionGetByContactResponse*
* `discussion` ({ref}`message-discussion`)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussiongetbygroup)=
### DiscussionGetByGroup
::::::{card}
> Get discussion by group id.

(message-discussiongetbygrouprequest)=
**Request**: *DiscussionGetByGroupRequest*
* `group_id` (uint64)

(message-discussiongetbygroupresponse)=
**Response**: *DiscussionGetByGroupResponse*
* `discussion` ({ref}`message-discussion`)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussionempty)=
### DiscussionEmpty
::::::{card}
> Delete all messages and attachments in a discussion.

(message-discussionemptyrequest)=
**Request**: *DiscussionEmptyRequest*
* `discussion_id` (uint64)

(message-discussionemptyresponse)=
**Response**: *DiscussionEmptyResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-discussiondownloadphoto)=
### DiscussionDownloadPhoto
::::::{card}
> Download a discussion photo.  
> The photo can be the contact photo, the group photo, or a generated image for the discussion if a specific image was not set.  
> Photos are always jpeg files with a maximum of 1080x1080 resolution.

(message-discussiondownloadphotorequest)=
**Request**: *DiscussionDownloadPhotoRequest*
* `discussion_id` (uint64)

(message-discussiondownloadphotoresponse)=
**Response**: *DiscussionDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-discussionlockedlist)=
### DiscussionLockedList
::::::{card}
> locked discussions

(message-discussionlockedlistrequest)=
**Request**: *DiscussionLockedListRequest*
DiscussionLockedList
List locked discussions.
Locked discussions are discussions associated to a deleted contact or a group you left.
Messages in those discussions are still accessible, but you cannot post new messages in those discussions.

**Error codes**:
`UNAUTHENTICATED`: client key is invalid.
`INTERNAL`

* *Empty payload.*

(message-discussionlockedlistresponse)=
**Response *(Stream)***: *DiscussionLockedListResponse*
* `discussions` (**repeated** {ref}`message-discussion`)

::::::

(rpc-discussionlockeddelete)=
### DiscussionLockedDelete
::::::{card}
> Delete a locked discussion by id.  
> This will delete discussion and its content, including messages and attached files.

(message-discussionlockeddeleterequest)=
**Request**: *DiscussionLockedDeleteRequest*
* `discussion_id` (uint64)

(message-discussionlockeddeleteresponse)=
**Response**: *DiscussionLockedDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-contactcommandservice)=
## Contact Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-contact`
:::
(rpc-contactlist)=
### ContactList
::::::{card}
> List contacts for current identity.  
> Pass a filter to select only contacts that match specific criteria.

(message-contactlistrequest)=
**Request**: *ContactListRequest*
* `filter` (**optional** {ref}`message-contactfilter`)

(message-contactlistresponse)=
**Response *(Stream)***: *ContactListResponse*
* `contacts` (**repeated** {ref}`message-contact`)

**Error Codes**:
- `INVALID_ARGUMENT`: invalid filter.
 - `UNAUTHENTICATED`: client key is invalid
 - `INTERNAL`
::::::

(rpc-contactget)=
### ContactGet
::::::{card}
> Get a contact by id.

(message-contactgetrequest)=
**Request**: *ContactGetRequest*
* `contact_id` (uint64)

(message-contactgetresponse)=
**Response**: *ContactGetResponse*
* `contact` ({ref}`message-contact`)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactgetbytesidentifier)=
### ContactGetBytesIdentifier
::::::{card}
> Get a contact identity as bytes.  
> This is useful to have a long term identifier for a contact, backup-proof, and common to any device.

(message-contactgetbytesidentifierrequest)=
**Request**: *ContactGetBytesIdentifierRequest*
* `contact_id` (uint64)

(message-contactgetbytesidentifierresponse)=
**Response**: *ContactGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactgetinvitationlink)=
### ContactGetInvitationLink
::::::{card}
> Get a contact invitation link.

(message-contactgetinvitationlinkrequest)=
**Request**: *ContactGetInvitationLinkRequest*
* `contact_id` (uint64)

(message-contactgetinvitationlinkresponse)=
**Response**: *ContactGetInvitationLinkResponse*
* `invitation_link` (string)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactdelete)=
### ContactDelete
::::::{card}
> Delete a contact by id.

(message-contactdeleterequest)=
**Request**: *ContactDeleteRequest*
* `contact_id` (uint64)

(message-contactdeleteresponse)=
**Response**: *ContactDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `INVALID_ARGUMENT`: contact is still in a group.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-contactintroduction)=
### ContactIntroduction
::::::{card}
> Introduce two of your contacts together.  
> They will both receive an invitation to accept.  
> If each of the two accepts, they will be added to each other's contact book and can exchange.

(message-contactintroductionrequest)=
**Request**: *ContactIntroductionRequest*
* `first_contact_id` (uint64)
* `second_contact_id` (uint64)

(message-contactintroductionresponse)=
**Response**: *ContactIntroductionResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: first or second contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-contactdownloadphoto)=
### ContactDownloadPhoto
::::::{card}
> Download the contact profile picture as bytes, or the group picture, or the generated image for this discussion.  
> Pictures are always jpeg files with a maximum of 1080x1080 resolution.

(message-contactdownloadphotorequest)=
**Request**: *ContactDownloadPhotoRequest*
* `contact_id` (uint64)

(message-contactdownloadphotoresponse)=
**Response**: *ContactDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-contactrecreatechannels)=
### ContactRecreateChannels
::::::{card}
> Reset cryptographic channels with a contact.  
> USE CAREFULLY: this might fix some issues but every non sent / received messages will be lost.

(message-contactrecreatechannelsrequest)=
**Request**: *ContactRecreateChannelsRequest*
* `contact_id` (uint64)

(message-contactrecreatechannelsresponse)=
**Response**: *ContactRecreateChannelsResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-contactinvitetoonetoonediscussion)=
### ContactInviteToOneToOneDiscussion
::::::{card}
> collected contacts

(message-contactinvitetoonetoonediscussionrequest)=
**Request**: *ContactInviteToOneToOneDiscussionRequest*
ContactInviteToOneToOneDiscussion
Invite a non one-to-one contact to have a one-to-one discussion.

**Error codes**:
`NOT_FOUND`: contact not found.
`INVALID_ARGUMENT`: contact already has a one to one discussion.
`UNAUTHENTICATED`: client key is invalid.
`INTERNAL`

* `contact_id` (uint64)

(message-contactinvitetoonetoonediscussionresponse)=
**Response**: *ContactInviteToOneToOneDiscussionResponse*
* `invitation` ({ref}`message-invitation`)

::::::

(rpc-contactdowngradeonetoonediscussion)=
### ContactDowngradeOneToOneDiscussion
::::::{card}
> ContactDowngradeOneToOne  
> Downgrade a one-to-one contact to a non one-to-one contact.  
> This will lock current discussion with this contact.  
> The contact will always be in your contact book and common groups but you will no longer be able to exchange direct message.

(message-contactdowngradeonetoonediscussionrequest)=
**Request**: *ContactDowngradeOneToOneDiscussionRequest*
* `contact_id` (uint64)

(message-contactdowngradeonetoonediscussionresponse)=
**Response**: *ContactDowngradeOneToOneDiscussionResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: contact not found.
 - `INVALID_ARGUMENT`: contact is not one to one, does not have established channel or does not support one to one downgrade.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

---

(service-groupcommandservice)=
## Group Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-group`
:::
(rpc-grouplist)=
### GroupList
::::::{card}
> List groups for current identity.  
> Pass a filter to select only groups that match specific criteria.

(message-grouplistrequest)=
**Request**: *GroupListRequest*
* `filter` (**optional** {ref}`message-groupfilter`)

(message-grouplistresponse)=
**Response *(Stream)***: *GroupListResponse*
* `groups` (**repeated** {ref}`message-group`)

**Error Codes**:
- `INVALID_ARGUMENT`: invalid filter.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupget)=
### GroupGet
::::::{card}
> Get group by id.

(message-groupgetrequest)=
**Request**: *GroupGetRequest*
* `group_id` (uint64)

(message-groupgetresponse)=
**Response**: *GroupGetResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupgetbytesidentifier)=
### GroupGetBytesIdentifier
::::::{card}
> Get a group identifier as bytes.  
> This is useful to have a long term identifier for a group, backup-proof, and common to any device.

(message-groupgetbytesidentifierrequest)=
**Request**: *GroupGetBytesIdentifierRequest*
* `group_id` (uint64)

(message-groupgetbytesidentifierresponse)=
**Response**: *GroupGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-groupnewstandardgroup)=
### GroupNewStandardGroup
::::::{card}
> Create a new standard group.  
> In a standard group all members are administrators, everyone can edit group details and manage group members.

(message-groupnewstandardgrouprequest)=
**Request**: *GroupNewStandardGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)

(message-groupnewstandardgroupresponse)=
**Response**: *GroupNewStandardGroupResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupnewcontrolledgroup)=
### GroupNewControlledGroup
::::::{card}
> Create a new controlled group.  
> In a controlled group Administrators are specifically designated and they can edit group details and manage group members.  
> Simple members cannot manage the group but they can post messages, attachments and reactions.

(message-groupnewcontrolledgrouprequest)=
**Request**: *GroupNewControlledGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

(message-groupnewcontrolledgroupresponse)=
**Response**: *GroupNewControlledGroupResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: a contact cannot be in admins and members at the same time / at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupnewreadonlygroup)=
### GroupNewReadOnlyGroup
::::::{card}
> Create a new read-only group.  
> In read only groups only group administrators can manage the group and post messages.  
> Other users can only react to messages.

(message-groupnewreadonlygrouprequest)=
**Request**: *GroupNewReadOnlyGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

(message-groupnewreadonlygroupresponse)=
**Response**: *GroupNewReadOnlyGroupResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: a contact cannot be in admins and members at the same time / at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupnewadvancedgroup)=
### GroupNewAdvancedGroup
::::::{card}
> Create a new advanced group.  
> An advanced group allows to manually assign permissions to all members.

(message-groupnewadvancedgrouprequest)=
**Request**: *GroupNewAdvancedGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `advanced_configuration` (**optional** {ref}`message-group.advancedconfiguration`)
* `members` (**repeated** {ref}`message-groupmember`)

(message-groupnewadvancedgroupresponse)=
**Response**: *GroupNewAdvancedGroupResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: contacts not found.
 - `INVALID_ARGUMENT`: a contact cannot be in admins and members at the same time / at least one contact does not support group v2.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupdisband)=
### GroupDisband
::::::{card}
> Close a group, every member will leave the group and the discussion will be locked for everyone.  
> Only administrators are allowed to disband a group.

(message-groupdisbandrequest)=
**Request**: *GroupDisbandRequest*
* `group_id` (uint64)

(message-groupdisbandresponse)=
**Response**: *GroupDisbandResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `INVALID_ARGUMENT`: impossible to disband a keycloak group.
 - `PERMISSION_DENIED`: you are not admin in this group.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupleave)=
### GroupLeave
::::::{card}
> Leave a group, the discussion will still exists for other group members.  
> Any group member can leave a group at any time, except if you are the last administrator in this group (a group must always have an administrator).

(message-groupleaverequest)=
**Request**: *GroupLeaveRequest*
* `group_id` (uint64)

(message-groupleaveresponse)=
**Response**: *GroupLeaveResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `INVALID_ARGUMENT`: impossible to disband a keycloak group / you cannot leave a group if you are the only group administrator.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupupdate)=
### GroupUpdate
::::::{card}
> Update a group by modifying a Group object retrieved from groupList of groupGet.  
> Supported modifications:  
> - Add a member: create a new GroupMember and add it to members field  
> - Remove a member: remove associated GroupMember from members field  
> - Remove a pending member: remove associated GroupPendingMember from pendingMembers field  
> - Update (pending) member permissions: update permissions in permissions field in GroupMember or GroupPendingMember  
> - Update group name: modify name field  
> - Update group description: modify description field  
> Every other modifications will be ignored. You must keep groupId field properly set.

(message-groupupdaterequest)=
**Request**: *GroupUpdateRequest*
* `group` ({ref}`message-group`)

(message-groupupdateresponse)=
**Response**: *GroupUpdateResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `PERMISSION_DENIED`: you are not admin in this group.
 - `INVALID_ARGUMENT`: the new group version has not been updated / new group member not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupsetphoto)=
### GroupSetPhoto
::::::{card}
(message-groupsetphotorequest)=
**Request *(Stream)***: *GroupSetPhotoRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`message-groupsetphotorequestmetadata`)
  * `payload` (bytes)

(message-groupsetphotoresponse)=
**Response**: *GroupSetPhotoResponse*
* `group` ({ref}`message-group`)

:::::{card}
(message-groupsetphotorequestmetadata)=
##### GroupSetPhotoRequestMetadata

> GroupSetPhoto  
> Set a new photo for a group.  
> The photo can be jpeg or png but will be converted to jpeg and resolution will be limited to 1080x1080.  
>   
> **Error codes**:  
> `NOT_FOUND`: group not found.  
> `PERMISSION_DENIED`: you are not admin in this group.  
> `UNAUTHENTICATED`: client key is invalid.  
> `INTERNAL`

**Fields:**
* `group_id` (uint64)
* `filename` (string)
* `file_size` (uint64)
:::::
::::::

(rpc-groupdownloadphoto)=
### GroupDownloadPhoto
::::::{card}
> Download the group picture as bytes, or the generated image for this group.  
> Pictures are always jpeg files with a maximum of 1080x1080 resolution.

(message-groupdownloadphotorequest)=
**Request**: *GroupDownloadPhotoRequest*
* `group_id` (uint64)

(message-groupdownloadphotoresponse)=
**Response**: *GroupDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-groupunsetphoto)=
### GroupUnsetPhoto
::::::{card}
> Unset the current group picture if there is one.

(message-groupunsetphotorequest)=
**Request**: *GroupUnsetPhotoRequest*
* `group_id` (uint64)

(message-groupunsetphotoresponse)=
**Response**: *GroupUnsetPhotoResponse*
* `group` ({ref}`message-group`)

**Error Codes**:
- `NOT_FOUND`: group not found.
 - `INVALID_ARGUMENT`: group does not have a photo.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

---

(service-identitycommandservice)=
## Identity Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-identity`
:::
(rpc-identityget)=
### IdentityGet
::::::{card}
> Get your identity details.

(message-identitygetrequest)=
**Request**: *IdentityGetRequest*
* *Empty payload.*

(message-identitygetresponse)=
**Response**: *IdentityGetResponse*
* `identity` ({ref}`message-identity`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-identitygetbytesidentifier)=
### IdentityGetBytesIdentifier
::::::{card}
> Get your Olvid identity as bytes.  
> This is useful to have a long term identifier for an identity, backup-proof, and common to any device.

(message-identitygetbytesidentifierrequest)=
**Request**: *IdentityGetBytesIdentifierRequest*
* *Empty payload.*

(message-identitygetbytesidentifierresponse)=
**Response**: *IdentityGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-identitygetinvitationlink)=
### IdentityGetInvitationLink
::::::{card}
> Get your invitation link. This link can be sent to other Olvid users to let them send you an invitation.  
> Invitation links can be opened with any Olvid application or opened in a web browser to show a QR code to scan.

(message-identitygetinvitationlinkrequest)=
**Request**: *IdentityGetInvitationLinkRequest*
* *Empty payload.*

(message-identitygetinvitationlinkresponse)=
**Response**: *IdentityGetInvitationLinkResponse*
* `invitation_link` (string)

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-identityupdatedetails)=
### IdentityUpdateDetails
::::::{card}
> Update your Olvid identity details (first name, last name, company and position).  
> At least one field in first and last name must be non empty.  
> Your details will be visible by your contacts, and your display name is computed from these details.  
> Details for a keycloak managed identity cannot be updated.

(message-identityupdatedetailsrequest)=
**Request**: *IdentityUpdateDetailsRequest*
* `new_details` ({ref}`message-identitydetails` - *your new identity details*)

(message-identityupdatedetailsresponse)=
**Response**: *IdentityUpdateDetailsResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `INVALID_ARGUMENT`: at least one of first name and last name must be non empty / cannot update a keycloak managed identity.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identitysetphoto)=
### IdentitySetPhoto
::::::{card}
(message-identitysetphotorequest)=
**Request *(Stream)***: *IdentitySetPhotoRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`message-identitysetphotorequestmetadata`)
  * `payload` (bytes)

(message-identitysetphotoresponse)=
**Response**: *IdentitySetPhotoResponse*
* *Empty payload.*

:::::{card}
(message-identitysetphotorequestmetadata)=
##### IdentitySetPhotoRequestMetadata

> IdentitySetPhoto  
> Set a profile picture for your identity.  
> This picture will be visible by your contacts.  
> The photo can be jpeg or png but will be converted to jpeg and resolution will be limited to 1080x1080.  
>   
> **Error codes**:  
> `NOT_FOUND`: identity not found.  
> `UNAUTHENTICATED`: client key is invalid.  
> `INTERNAL`

**Fields:**
* `filename` (string)
* `file_size` (uint64)
:::::
::::::

(rpc-identitydownloadphoto)=
### IdentityDownloadPhoto
::::::{card}
> Download your current identity picture.  
> Pictures are always jpeg files with a maximum of 1080x1080 resolution.

(message-identitydownloadphotorequest)=
**Request**: *IdentityDownloadPhotoRequest*
* *Empty payload.*

(message-identitydownloadphotoresponse)=
**Response**: *IdentityDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-identityremovephoto)=
### IdentityRemovePhoto
::::::{card}
> Remove your current identity picture.  
> The automatically generated identity image will be used instead.

(message-identityremovephotorequest)=
**Request**: *IdentityRemovePhotoRequest*
* *Empty payload.*

(message-identityremovephotoresponse)=
**Response**: *IdentityRemovePhotoResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-identitygetapikeystatus)=
### IdentityGetApiKeyStatus
::::::{card}
> Check your current Olvid API key status.  
> API keys allow an identity to initiate calls or to use multi device.

(message-identitygetapikeystatusrequest)=
**Request**: *IdentityGetApiKeyStatusRequest*
* *Empty payload.*

(message-identitygetapikeystatusresponse)=
**Response**: *IdentityGetApiKeyStatusResponse*
* `api_key` ({ref}`message-identity.apikey`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identitysetapikey)=
### IdentitySetApiKey
::::::{card}
> Manually set an Olvid api key.  
> Olvid api keys are standard uuids.

(message-identitysetapikeyrequest)=
**Request**: *IdentitySetApiKeyRequest*
* `api_key` (string)

(message-identitysetapikeyresponse)=
**Response**: *IdentitySetApiKeyResponse*
* `api_key` ({ref}`message-identity.apikey`)

**Error Codes**:
- `INVALID_ARGUMENT`: api key format is not valid.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identitysetconfigurationlink)=
### IdentitySetConfigurationLink
::::::{card}
> Set an Olvid configuration link with an api key.

(message-identitysetconfigurationlinkrequest)=
**Request**: *IdentitySetConfigurationLinkRequest*
* `configuration_link` (string)

(message-identitysetconfigurationlinkresponse)=
**Response**: *IdentitySetConfigurationLinkResponse*
* `api_key` ({ref}`message-identity.apikey`)

**Error Codes**:
- `INVALID_ARGUMENT`: configuration link is invalid / configuration link is for another server.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-invitationcommandservice)=
## Invitation Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-invitation`
:::
(rpc-invitationlist)=
### InvitationList
::::::{card}
> List invitations for current identity.  
> Pass a filter to select only invitations that match specific criteria.

(message-invitationlistrequest)=
**Request**: *InvitationListRequest*
* `filter` (**optional** {ref}`message-invitationfilter`)

(message-invitationlistresponse)=
**Response *(Stream)***: *InvitationListResponse*
* `invitations` (**repeated** {ref}`message-invitation`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
 - `INVALID_ARGUMENT`: invalid filter.
 - `INTERNAL`
::::::

(rpc-invitationget)=
### InvitationGet
::::::{card}
> Get invitation by id.

(message-invitationgetrequest)=
**Request**: *InvitationGetRequest*
* `invitation_id` (uint64)

(message-invitationgetresponse)=
**Response**: *InvitationGetResponse*
* `invitation` ({ref}`message-invitation`)

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-invitationnew)=
### InvitationNew
::::::{card}
> Send an invitation to another Olvid user using its invitation link.  
> Invitation links start with https://invitation.olvid.io#.  
> Sending an invitation will initiate an invitation protocol and create a new Invitation.

(message-invitationnewrequest)=
**Request**: *InvitationNewRequest*
* `invitation_url` (string)

(message-invitationnewresponse)=
**Response**: *InvitationNewResponse*
* `invitation` ({ref}`message-invitation`)

**Error Codes**:
- `INVALID_ARGUMENT`: you cannot invite yourself / invitation link is invalid.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-invitationaccept)=
### InvitationAccept
::::::{card}
> Accept a pending invitation. This will allow protocol to continue.  
> This command is only possible if `invitation.status` is one of the following:  
> - STATUS_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT  
> - STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT

(message-invitationacceptrequest)=
**Request**: *InvitationAcceptRequest*
* `invitation_id` (uint64)

(message-invitationacceptresponse)=
**Response**: *InvitationAcceptResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `INVALID_ARGUMENT`: cannot accept an invitation with this status.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-invitationdecline)=
### InvitationDecline
::::::{card}
> Decline a pending invitation. This will abort protocol.  
> For invitation, introduction and one to one invitation the other user is not notified you declined the invitation.  
> This command is only possible if `invitation.status` is one of the following:  
> - STATUS_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_INTRODUCTION_WAIT_YOU_TO_ACCEPT  
> - STATUS_ONE_TO_ONE_INVITATION_WAIT_YOU_TO_ACCEPT  
> - STATUS_GROUP_INVITATION_WAIT_YOU_TO_ACCEPT

(message-invitationdeclinerequest)=
**Request**: *InvitationDeclineRequest*
* `invitation_id` (uint64)

(message-invitationdeclineresponse)=
**Response**: *InvitationDeclineResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-invitationsas)=
### InvitationSas
::::::{card}
> Only possible if `invitation.status` is equal to STATUS_INVITATION_WAIT_YOU_FOR_SAS_EXCHANGE.  
> Set the 4 digit code shown on your partner device.

(message-invitationsasrequest)=
**Request**: *InvitationSasRequest*
* `invitation_id` (uint64)
* `sas` (string - *4 digit pin code shown on your partner device*)

(message-invitationsasresponse)=
**Response**: *InvitationSasResponse*
* *Empty payload.*

**Error Codes**:
- `NOT_FOUND`: invitation not found.
 - `INVALID_ARGUMENT`: unexpected invitation status.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-invitationdelete)=
### InvitationDelete
::::::{card}
> Abort the protocol associated to any invitation and delete this invitation.

(message-invitationdeleterequest)=
**Request**: *InvitationDeleteRequest*
* `invitation_id` (uint64)

(message-invitationdeleteresponse)=
**Response**: *InvitationDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-settingscommandservice)=
## Settings Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-settings`
:::
(rpc-settingsidentityget)=
### SettingsIdentityGet
::::::{card}
> Get current settings for your identity.

(message-settingsidentitygetrequest)=
**Request**: *SettingsIdentityGetRequest*
* *Empty payload.*

(message-settingsidentitygetresponse)=
**Response**: *SettingsIdentityGetResponse*
* `identity_settings` ({ref}`message-identitysettings`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-settingsidentityset)=
### SettingsIdentitySet
::::::{card}
> Update your identity settings.  
> ⚠️ Update erases the WHOLE settings.  
> To update current settings use SettingsIdentityGet to get current config, and only edit fields you want to update.

(message-settingsidentitysetrequest)=
**Request**: *SettingsIdentitySetRequest*
* `identity_settings` ({ref}`message-identitysettings`)

(message-settingsidentitysetresponse)=
**Response**: *SettingsIdentitySetResponse*
* `identity_settings` ({ref}`message-identitysettings`)

**Error Codes**:
- `INVALID_ARGUMENT`: cannot set keycloak settings if your identity is not keycloak managed.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-settingsdiscussionget)=
### SettingsDiscussionGet
::::::{card}
> Get a discussion settings.  
> Those settings are shared with other members of this discussion.  
> For example, a parameter for ephemeral message parameters concerning a discussion would affect all future messages posted in this discussion, from any member.

(message-settingsdiscussiongetrequest)=
**Request**: *SettingsDiscussionGetRequest*
* `discussion_id` (uint64)

(message-settingsdiscussiongetresponse)=
**Response**: *SettingsDiscussionGetResponse*
* `discussion_settings` ({ref}`message-discussionsettings`)

**Error Codes**:
- `NOT_FOUND`: discussion not found
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-settingsdiscussionset)=
### SettingsDiscussionSet
::::::{card}
> Update a discussion settings.  
> ⚠️ Update erases the WHOLE settings.  
> To update current settings use SettingsDiscussionGet to get current config, and only edit fields you want to update.

(message-settingsdiscussionsetrequest)=
**Request**: *SettingsDiscussionSetRequest*
* `discussion_settings` ({ref}`message-discussionsettings`)

(message-settingsdiscussionsetresponse)=
**Response**: *SettingsDiscussionSetResponse*
* `discussion_settings` ({ref}`message-discussionsettings`)

**Error Codes**:
- `NOT_FOUND`: discussion not found
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-storagecommandservice)=
## Storage Command Service

:::{admonition} Info
Each client key has its own independent storage space, with a simple key-value system.  
_Storage_ can be seen as a global storage space, compared to _Discussion Storage_ that offers a space associated with a specific discussion.  
  
Both mechanisms are backup resilient, and will be restored with their associated client key in a backup restoration process.  
  
Mind that temporary client keys (specified in daemon environment or as command line arguments) do not have an allocated storage space.  
You must create a client in database to use storage commands.


**Associated Datatype:** {ref}`file-storage`
:::
(rpc-storagelist)=
### StorageList
::::::{card}
> List stored elements in global storage scope, for current client key.  
> Pass a filter to select only elements that match specific criteria.  
>   
> Mind that temporary client keys (specified in daemon environment or as command line arguments) does not have an allocated storage space.  
> You must create a client in database to use storage commands.

(message-storagelistrequest)=
**Request**: *StorageListRequest*
* `filter` (**optional** {ref}`message-storageelementfilter`)

(message-storagelistresponse)=
**Response *(Stream)***: *StorageListResponse*
* `elements` (**repeated** {ref}`message-storageelement`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: invalid filter
 - `INTERNAL`
::::::

(rpc-storageget)=
### StorageGet
::::::{card}
> Request the value associated to a key in your global storage.  
> If the key does not already exist, return an empty string.

(message-storagegetrequest)=
**Request**: *StorageGetRequest*
* `key` (string)

(message-storagegetresponse)=
**Response**: *StorageGetResponse*
* `value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
::::::

(rpc-storageset)=
### StorageSet
::::::{card}
> Set the value for a key in your global storage.  
> If the key was already set the value is updated and it returns the *previous_value* in response.

(message-storagesetrequest)=
**Request**: *StorageSetRequest*
* `key` (string)
* `value` (string)

(message-storagesetresponse)=
**Response**: *StorageSetResponse*
* `previous_value` (string - *if the key already exists, this contains the erased value.*)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INTERNAL`
::::::

(rpc-storageunset)=
### StorageUnset
::::::{card}
> Unset a key in your global storage.

(message-storageunsetrequest)=
**Request**: *StorageUnsetRequest*
* `key` (string)

(message-storageunsetresponse)=
**Response**: *StorageUnsetResponse*
* `previous_value` (string - *the value previously associated to this key*)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
::::::

---

(service-discussionstoragecommandservice)=
## Discussion Storage Command Service

:::{admonition} Info
Each client key has its own independent storage space, with a simple key-value system.  
_Storage_ can be seen as a global storage space, compared to _Discussion Storage_ that offers a space associated with a specific discussion.  
  
Both mechanisms are backup resilient, and will be restored with their associated client key in a backup restoration process.  
  
Mind that temporary client keys (specified in daemon environment or as command line arguments) do not have an allocated storage space.  
You must create a client in database to use storage commands.


**Associated Datatype:** {ref}`file-storage`
:::
(rpc-discussionstoragelist)=
### DiscussionStorageList
::::::{card}
> List stored elements in a specific discussion storage scope, for current client key.  
> Pass a filter to select only elements that match specific criteria.

(message-discussionstoragelistrequest)=
**Request**: *DiscussionStorageListRequest*
* `discussion_id` (uint64)
* `filter` (**optional** {ref}`message-storageelementfilter`)

(message-discussionstoragelistresponse)=
**Response *(Stream)***: *DiscussionStorageListResponse*
* `elements` (**repeated** {ref}`message-storageelement`)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key / invalid filter.
 - `NOT_FOUND`: discussion not found.
 - `INTERNAL`
::::::

(rpc-discussionstorageget)=
### DiscussionStorageGet
::::::{card}
> Request the value associated to a key in the specified discussion storage.  
> If the key does not already exist, return an empty string.

(message-discussionstoragegetrequest)=
**Request**: *DiscussionStorageGetRequest*
* `discussion_id` (uint64)
* `key` (string)

(message-discussionstoragegetresponse)=
**Response**: *DiscussionStorageGetResponse*
* `value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key.
 - `NOT_FOUND`: discussion not found.
::::::

(rpc-discussionstorageset)=
### DiscussionStorageSet
::::::{card}
> Set the value for a key in the specified discussion storage.  
> If the key was already set the value is updated and it returns the *previous_value* in response.

(message-discussionstoragesetrequest)=
**Request**: *DiscussionStorageSetRequest*
* `discussion_id` (uint64)
* `key` (string)
* `value` (string)

(message-discussionstoragesetresponse)=
**Response**: *DiscussionStorageSetResponse*
* `previous_value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key.
 - `NOT_FOUND`: discussion not found.
 - `INTERNAL`
::::::

(rpc-discussionstorageunset)=
### DiscussionStorageUnset
::::::{card}
> Unset a key in the specified discussion storage.

(message-discussionstorageunsetrequest)=
**Request**: *DiscussionStorageUnsetRequest*
* `discussion_id` (uint64)
* `key` (string)

(message-discussionstorageunsetresponse)=
**Response**: *DiscussionStorageUnsetResponse*
* `previous_value` (string)

**Error Codes**:
- `UNAUTHENTICATED`: client key is invalid or a temporary client key.
 - `INVALID_ARGUMENT`: discussion storage is not available with an admin client key.
 - `NOT_FOUND`: discussion not found.
::::::

---

(service-keycloakcommandservice)=
## Keycloak Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-keycloak`
:::
(rpc-keycloakbindidentity)=
### KeycloakBindIdentity
::::::{card}
> Register your identity in a keycloak directory.  
> Your identity should not already be registered in a keycloak directory (`identity.keycloak_managed`).  
> When registered your directory might add you to some managed groups, and you will be granted access to other directory users.  
> Other directory users can be added as contacts with no further confirmation (see *KeycloakUserList* and *KeycloakAddUserAsContact*).

(message-keycloakbindidentityrequest)=
**Request**: *KeycloakBindIdentityRequest*
* `configuration_link` (string)

(message-keycloakbindidentityresponse)=
**Response**: *KeycloakBindIdentityResponse*
* *Empty payload.*

**Error Codes**:
- `INVALID_ARGUMENT`: identity is already keycloak managed.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-keycloakunbindidentity)=
### KeycloakUnbindIdentity
::::::{card}
> Unregister from a keycloak directory.  
> Your identity should already be keycloak managed.  
> You will lose access to keycloak user directory and you will leave keycloak managed groups.  
> Your keycloak managed contacts will remain contacts but won't be keycloak managed anymore.

(message-keycloakunbindidentityrequest)=
**Request**: *KeycloakUnbindIdentityRequest*
* *Empty payload.*

(message-keycloakunbindidentityresponse)=
**Response**: *KeycloakUnbindIdentityResponse*
* *Empty payload.*

**Error Codes**:
- `INVALID_ARGUMENT`: identity is not keycloak managed.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-keycloakuserlist)=
### KeycloakUserList
::::::{card}
> List other users registered on your keycloak directory.  
> Pass a filter to select only users that match specific criteria.

(message-keycloakuserlistrequest)=
**Request**: *KeycloakUserListRequest*
* `filter` (**optional** {ref}`message-keycloakuserfilter`)
* `last_list_timestamp` (**optional** uint64 - *only users that registered on keycloak since this timestamp, set to 0 to list all users.*)

(message-keycloakuserlistresponse)=
**Response *(Stream)***: *KeycloakUserListResponse*
* `users` (**repeated** {ref}`message-keycloakuser`)
* `last_list_timestamp` (uint64 - *set this timestamp in request.last_list_timestamp if you want to list only new users.*)

**Error Codes**:
- `INVALID_ARGUMENT`: identity is not keycloak managed / invalid filter.
 - `UNAUTHENTICATED`: client key is invalid.
 - `INTERNAL`
::::::

(rpc-keycloakadduserascontact)=
### KeycloakAddUserAsContact
::::::{card}
> Add a user from keycloak directory as a contact.  
> This will not trigger any invitation protocol.  
> Directory is considered as a trusted third party so no further confirmation is required.  
> Contact and discussion will be created as soon as one of the other user's device is online and automatically answer "invitation".

(message-keycloakadduserascontactrequest)=
**Request**: *KeycloakAddUserAsContactRequest*
* `keycloak_id` (string)

(message-keycloakadduserascontactresponse)=
**Response**: *KeycloakAddUserAsContactResponse*
* *Empty payload.*

**Error Codes**:
- `INVALID_ARGUMENT`: identity is not keycloak managed.
 - `NOT_FOUND`: keycloak user not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-callcommandservice)=
## Call Command Service

:::{admonition} Info
Currently daemon cannot handle Olvid calls properly.  
You can be notified on incoming calls, and you can initiate call within discussions or with any contact.  
But we cannot manage audio or video streams, that's why a daemon will always answer any incoming call with a "busy" response.


**Associated Datatype:** {ref}`file-call`
:::
(rpc-callstartdiscussioncall)=
### CallStartDiscussionCall
::::::{card}
> Start a call with one discussion member(s).  
> This will start a one to one call or a group call depending on discussion type.  
> You can use *call_identifier* to filter later call notifications.

(message-callstartdiscussioncallrequest)=
**Request**: *CallStartDiscussionCallRequest*
* `discussion_id` (uint64)

(message-callstartdiscussioncallresponse)=
**Response**: *CallStartDiscussionCallResponse*
* `call_identifier` (string)

**Error Codes**:
- `NOT_FOUND`: discussion not found.
 - `INVALID_ARGUMENT`: cannot start a call in an empty group.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-callstartcustomcall)=
### CallStartCustomCall
::::::{card}
> Start a call with any contacts, even if they do not belong to the same discussion.  
> You can use *call_identifier* to filter later call notifications.

(message-callstartcustomcallrequest)=
**Request**: *CallStartCustomCallRequest*
* `contact_ids` (**repeated** uint64)
* `discussion_id` (**optional** uint64 - *specify in which discussion other contacts will log call*)

(message-callstartcustomcallresponse)=
**Response**: *CallStartCustomCallResponse*
* `call_identifier` (string)

**Error Codes**:
- `NOT_FOUND`: discussion or contact not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-toolcommandservice)=
## Tool Command Service

:::{admonition} Info
A set of utility entrypoint to test debug and your configuration.


:::
(rpc-ping)=
### Ping
::::::{card}
> Unauthenticated method.  
> Just check if daemon is reachable.

(message-pingrequest)=
**Request**: *PingRequest*
* *Empty payload.*

(message-pingresponse)=
**Response**: *PingResponse*
* *Empty payload.*

::::::

(rpc-daemonversion)=
### DaemonVersion
::::::{card}
> Authenticated method.  
> Ask daemon its version.

(message-daemonversionrequest)=
**Request**: *DaemonVersionRequest*
* *Empty payload.*

(message-daemonversionresponse)=
**Response**: *DaemonVersionResponse*
* `version` (string)

::::::

(rpc-authenticationtest)=
### AuthenticationTest
::::::{card}
> Authenticated rpc.  
> Check that sent credentials are valid user credentials, else it returns an error.

(message-authenticationtestrequest)=
**Request**: *AuthenticationTestRequest*
* *Empty payload.*

(message-authenticationtestresponse)=
**Response**: *AuthenticationTestResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: invalid client key.
::::::

(rpc-authenticationadmintest)=
### AuthenticationAdminTest
::::::{card}
> Authenticated rpc (admin key only).  
> Check that sent credentials are valid admin credentials, else it returns an error.

(message-authenticationadmintestrequest)=
**Request**: *AuthenticationAdminTestRequest*
* *Empty payload.*

(message-authenticationadmintestresponse)=
**Response**: *AuthenticationAdminTestResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: client key is not an admin client key.
::::::
