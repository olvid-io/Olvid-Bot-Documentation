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
>   
> **Error codes**:  
> `INVALID_ARGUMENT`: filter is invalid  
> `INTERNAL`

**Request**: *MessageListRequest*
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `unread` (**optional** bool - *only list unread messages (messages that have never been listed or sent in a MessageReceived notification)*)

**Response *(Stream)***: *MessageListResponse*
* `messages` (**repeated** {ref}`datatype-message`)

:::

### MessageGet
:::{card}
> get a specific message by id.  
>   
> **Error codes**:  
> `NOT_FOUND`: message not found.

**Request**: *MessageGetRequest*
* `message_id` ({ref}`datatype-messageid`)

**Response**: *MessageGetResponse*
* `message` ({ref}`datatype-message`)

:::

### MessageSend
:::{card}
> Post a text message in a discussion.  
> A message must have a non-blank body.  
>   
> **Error codes**:  
> `NOT_FOUND`: discussion / replied message not found.  
> `INVALID_ARGUMENT`: message body is empty or blank.  
> `INTERNAL`

**Request**: *MessageSendRequest*
* `discussion_id` (uint64)
* `body` (string)
* `reply_id` (**optional** {ref}`datatype-messageid`)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality`)
* `disable_link_preview` (**optional** bool)

**Response**: *MessageSendResponse*
* `message` ({ref}`datatype-message`)

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
>   
> **Error codes**:  
> `NOT_FOUND`: discussion / replied message not found.  
> `INVALID_ARGUMENT`: message body is empty or blank with no attached file / attached the same file twice.  
> `INTERNAL`

**Request *(Stream)***: *MessageSendWithAttachmentsRequest*
* **Oneof `request`**:
  * `metadata` ({ref}`datatype-messagesendwithattachmentsrequestmetadata`)
  * `payload` (bytes)
  * `file_delimiter` (bool)

**Response**: *MessageSendWithAttachmentsResponse*
* `message` ({ref}`datatype-message`)
* `attachments` (**repeated** {ref}`datatype-attachment`)

:::

### MessageReact
:::{card}
> Add, update or remove a reaction from a message.  
> If reaction is an empty string your previous reaction will be removed if there were any.  
>   
> **Error codes**:  
> `NOT_FOUND`: message not found.  
> `INTERNAL`

**Request**: *MessageReactRequest*
* `message_id` ({ref}`datatype-messageid`)
* `reaction` (**optional** string)

**Response**: *MessageReactResponse*
* *Empty payload.*

:::

### MessageUpdateBody
:::{card}
> Update one of your message body.  
> Body cannot be empty or blank.  
>   
> **Error codes**:  
> `NOT_FOUND`: message not found.  
> `INVALID_ARGUMENT`: you can only edit your own messages / new body cannot be empty or blank.  
> `INTERNAL`

**Request**: *MessageUpdateBodyRequest*
* `message_id` ({ref}`datatype-messageid`)
* `updated_body` (string)

**Response**: *MessageUpdateBodyResponse*
* *Empty payload.*

:::

### MessageDelete
:::{card}
> Delete a message giving it's id.  
> TODO delete everywhere ?  
>   
> **Error codes**:  
> `NOT_FOUND`: message not found.  
> `INTERNAL`

**Request**: *MessageDeleteRequest*
* `message_id` ({ref}`datatype-messageid`)
* `delete_everywhere` (**optional** bool)

**Response**: *MessageDeleteResponse*
* *Empty payload.*

:::

### MessageSendLocation
:::{card}
> Post a location message in a discussion.  
> A location message represent a specific location, and is different of a location sharing that can be updated.  
>   
> **Error codes**:  
> `NOT_FOUND`: discussion not found.  
> `INVALID_ARGUMENT: latitude and longitude are both equal to zero / preview_filename and preview_payload must be set together.  
> `INTERNAL`

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

:::

### MessageStartLocationSharing
:::{card}
> Start sharing a location in a discussion.  
>   
> **Error codes**:  
> `NOT_FOUND`: discussion not found.  
> `INVALID_ARGUMENT: latitude and longitude are both equal to zero.  
> `INTERNAL`

**Request**: *MessageStartLocationSharingRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response**: *MessageStartLocationSharingResponse*
* `message` ({ref}`datatype-message`)

:::

### MessageUpdateLocationSharing
:::{card}
> Update one of your sharing location message with a new location.  
>   
> **Error codes**:  
> `NOT_FOUND`: message not found.  
> `INVALID_ARGUMENT: you can only update your location sharing messages / sharing is no longer active.  
> `INTERNAL`

**Request**: *MessageUpdateLocationSharingRequest*
* `message_id` ({ref}`datatype-messageid`)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response**: *MessageUpdateLocationSharingResponse*
* `message` ({ref}`datatype-message`)

:::

### MessageEndLocationSharing
:::{card}
> **Error codes**:  
> `NOT_FOUND`: message not found.  
> `INVALID_ARGUMENT: you can only end your location sharing messages / sharing is no longer active.  
> `INTERNAL`

**Request**: *MessageEndLocationSharingRequest*
* `message_id` ({ref}`datatype-messageid`)

**Response**: *MessageEndLocationSharingResponse*
* `message` ({ref}`datatype-message`)

:::

### MessageRefresh
:::{card}
> Manually refresh messages available on server.

**Request**: *MessageRefreshRequest*
* *Empty payload.*

**Response**: *MessageRefreshResponse*
* *Empty payload.*

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
>   
> **Error codes**:  
> `NOT_FOUND` ("Message not found"): filter.messageId does not belong to an identity message.

**Request**: *AttachmentListRequest*
* `filter` (**optional** {ref}`datatype-attachmentfilter`)

**Response *(Stream)***: *AttachmentListResponse*
* `attachments` (**repeated** {ref}`datatype-attachment`)

:::

### AttachmentGet
:::{card}
> Get an attachment by id.  
>   
> **Error codes**:  
> `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.

**Request**: *AttachmentGetRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response**: *AttachmentGetResponse*
* `attachment` ({ref}`datatype-attachment`)

:::

### AttachmentDelete
:::{card}
> Delete an attachment by id.  
>   
> **Error codes**:  
> `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.

**Request**: *AttachmentDeleteRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)
* `delete_everywhere` (**optional** bool)

**Response**: *AttachmentDeleteResponse*
* *Empty payload.*

:::

### AttachmentDownload
:::{card}
> Download the file associated to an attachment.  
> This returns one or more chunks of bytes.  
>   
> **Error codes**:  
> `NOT_FOUND` (*Attachment not found*): attachment_id does not belong to an identity attachment.  
> `INTERNAL`

**Request**: *AttachmentDownloadRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response *(Stream)***: *AttachmentDownloadResponse*
* `chunk` (bytes)

:::

---

(service-discussioncommandservice)=
## Discussion Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-discussion`
:::
### DiscussionList
:::{card}
**Request**: *DiscussionListRequest*
* `filter` (**optional** {ref}`datatype-discussionfilter`)

**Response *(Stream)***: *DiscussionListResponse*
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

### DiscussionGet
:::{card}
**Request**: *DiscussionGetRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionGetResponse*
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionGetBytesIdentifier
:::{card}
**Request**: *DiscussionGetBytesIdentifierRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

### DiscussionGetByContact
:::{card}
**Request**: *DiscussionGetByContactRequest*
* `contact_id` (uint64)

**Response**: *DiscussionGetByContactResponse*
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionGetByGroup
:::{card}
**Request**: *DiscussionGetByGroupRequest*
* `group_id` (uint64)

**Response**: *DiscussionGetByGroupResponse*
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionEmpty
:::{card}
**Request**: *DiscussionEmptyRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionEmptyResponse*
* *Empty payload.*

:::

### DiscussionDownloadPhoto
:::{card}
**Request**: *DiscussionDownloadPhotoRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionDownloadPhotoResponse*
* `photo` (bytes)

:::

### DiscussionLockedList
:::{card}
> locked discussions

**Request**: *DiscussionLockedListRequest*
DiscussionLockedList

* *Empty payload.*

**Response *(Stream)***: *DiscussionLockedListResponse*
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

### DiscussionLockedDelete
:::{card}
**Request**: *DiscussionLockedDeleteRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionLockedDeleteResponse*
* *Empty payload.*

:::

---

(service-discussionstoragecommandservice)=
## Discussion Storage Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-discussionstorage`
:::
### DiscussionStorageList
:::{card}
> Discussion storage api: store elements in daemon database, associated with a discussion id. They will remain associated to this discussion if you restore a backup.  
>   
>   
> DiscussionStorageList

**Request**: *DiscussionStorageListRequest*
* `discussion_id` (uint64)
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)***: *DiscussionStorageListResponse*
* `elements` (**repeated** {ref}`datatype-storageelement`)

:::

### DiscussionStorageGet
:::{card}
**Request**: *DiscussionStorageGetRequest*
* `discussion_id` (uint64)
* `key` (string)

**Response**: *DiscussionStorageGetResponse*
* `value` (string)

:::

### DiscussionStorageSet
:::{card}
**Request**: *DiscussionStorageSetRequest*
* `discussion_id` (uint64)
* `key` (string)
* `value` (string)

**Response**: *DiscussionStorageSetResponse*
* `previous_value` (string)

:::

### DiscussionStorageUnset
:::{card}
**Request**: *DiscussionStorageUnsetRequest*
* `discussion_id` (uint64)
* `key` (string)

**Response**: *DiscussionStorageUnsetResponse*
* `previous_value` (string)

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

:::

### ContactGet
:::{card}
> Get a contact specifying it's id.

**Request**: *ContactGetRequest*
* `contact_id` (uint64)

**Response**: *ContactGetResponse*
* `contact` ({ref}`datatype-contact`)

:::

### ContactGetBytesIdentifier
:::{card}
> Get a contact identity as bytes.  
> This is useful to have a long term identifier for a contact, backup-proof, and common to any device.

**Request**: *ContactGetBytesIdentifierRequest*
* `contact_id` (uint64)

**Response**: *ContactGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

### ContactGetInvitationLink
:::{card}
> Get invitation link for a contact.

**Request**: *ContactGetInvitationLinkRequest*
* `contact_id` (uint64)

**Response**: *ContactGetInvitationLinkResponse*
* `invitation_link` (string)

:::

### ContactDelete
:::{card}
> Delete a contact giving it's id.

**Request**: *ContactDeleteRequest*
* `contact_id` (uint64)

**Response**: *ContactDeleteResponse*
* *Empty payload.*

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

:::

### ContactDownloadPhoto
:::{card}
**Request**: *ContactDownloadPhotoRequest*
* `contact_id` (uint64)

**Response**: *ContactDownloadPhotoResponse*
* `photo` (bytes)

:::

### ContactRecreateChannels
:::{card}
> USE CAREFULLY: this might fix some issues but every non sent / received messages will be lost.

**Request**: *ContactRecreateChannelsRequest*
* `contact_id` (uint64)

**Response**: *ContactRecreateChannelsResponse*
* *Empty payload.*

:::

### ContactInviteToOneToOneDiscussion
:::{card}
> collected contacts

**Request**: *ContactInviteToOneToOneDiscussionRequest*
ContactInviteToOneToOneDiscussion
Invite a non one-to-one contact to have a one-to-one discussion.
If *contact.

* `contact_id` (uint64)

**Response**: *ContactInviteToOneToOneDiscussionResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

### ContactDowngradeOneToOneDiscussion
:::{card}
> ContactDowngradeOneToOne

**Request**: *ContactDowngradeOneToOneDiscussionRequest*
* `contact_id` (uint64)

**Response**: *ContactDowngradeOneToOneDiscussionResponse*
* *Empty payload.*

:::

---

(service-groupcommandservice)=
## Group Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-group`
:::
### GroupList
:::{card}
> return all groups for current identity

**Request**: *GroupListRequest*
* `filter` (**optional** {ref}`datatype-groupfilter`)

**Response *(Stream)***: *GroupListResponse*
* `groups` (**repeated** {ref}`datatype-group`)

:::

### GroupGet
:::{card}
**Request**: *GroupGetRequest*
* `group_id` (uint64)

**Response**: *GroupGetResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupGetBytesIdentifier
:::{card}
**Request**: *GroupGetBytesIdentifierRequest*
* `group_id` (uint64)

**Response**: *GroupGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

### GroupNewStandardGroup
:::{card}
**Request**: *GroupNewStandardGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)

**Response**: *GroupNewStandardGroupResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupNewControlledGroup
:::{card}
**Request**: *GroupNewControlledGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response**: *GroupNewControlledGroupResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupNewReadOnlyGroup
:::{card}
**Request**: *GroupNewReadOnlyGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response**: *GroupNewReadOnlyGroupResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupNewAdvancedGroup
:::{card}
**Request**: *GroupNewAdvancedGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `advanced_configuration` (**optional** {ref}`datatype-advancedconfiguration`)
* `members` (**repeated** {ref}`datatype-groupmember`)

**Response**: *GroupNewAdvancedGroupResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupDisband
:::{card}
**Request**: *GroupDisbandRequest*
* `group_id` (uint64)

**Response**: *GroupDisbandResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupLeave
:::{card}
**Request**: *GroupLeaveRequest*
* `group_id` (uint64)

**Response**: *GroupLeaveResponse*
* `group` ({ref}`datatype-group`)

:::

### GroupUpdate
:::{card}
> : update a group by modifying a Group object retrieved from groupList of groupGet.  
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

:::

### GroupUnsetPhoto
:::{card}
**Request**: *GroupUnsetPhotoRequest*
* `group_id` (uint64)

**Response**: *GroupUnsetPhotoResponse*
* `group` ({ref}`datatype-group`)

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
**Request**: *GroupDownloadPhotoRequest*
* `group_id` (uint64)

**Response**: *GroupDownloadPhotoResponse*
* `photo` (bytes)

:::

---

(service-identitycommandservice)=
## Identity Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-identity`
:::
### IdentityGet
:::{card}
**Request**: *IdentityGetRequest*
* *Empty payload.*

**Response**: *IdentityGetResponse*
* `identity` ({ref}`datatype-identity`)

:::

### IdentityGetBytesIdentifier
:::{card}
**Request**: *IdentityGetBytesIdentifierRequest*
* *Empty payload.*

**Response**: *IdentityGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

### IdentityGetInvitationLink
:::{card}
**Request**: *IdentityGetInvitationLinkRequest*
* *Empty payload.*

**Response**: *IdentityGetInvitationLinkResponse*
* `invitation_link` (string)

:::

### IdentityUpdateDetails
:::{card}
**Request**: *IdentityUpdateDetailsRequest*
* `new_details` ({ref}`datatype-identitydetails`)

**Response**: *IdentityUpdateDetailsResponse*
* *Empty payload.*

:::

### IdentityRemovePhoto
:::{card}
**Request**: *IdentityRemovePhotoRequest*
* *Empty payload.*

**Response**: *IdentityRemovePhotoResponse*
* *Empty payload.*

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
**Request**: *IdentityDownloadPhotoRequest*
* *Empty payload.*

**Response**: *IdentityDownloadPhotoResponse*
* `photo` (bytes)

:::

### IdentityGetApiKeyStatus
:::{card}
**Request**: *IdentityGetApiKeyStatusRequest*
* *Empty payload.*

**Response**: *IdentityGetApiKeyStatusResponse*
* `api_key` ({ref}`datatype-apikey`)

:::

### IdentitySetApiKey
:::{card}
**Request**: *IdentitySetApiKeyRequest*
* `api_key` (string)

**Response**: *IdentitySetApiKeyResponse*
* `api_key` ({ref}`datatype-apikey`)

:::

### IdentitySetConfigurationLink
:::{card}
**Request**: *IdentitySetConfigurationLinkRequest*
* `configuration_link` (string)

**Response**: *IdentitySetConfigurationLinkResponse*
* `api_key` ({ref}`datatype-apikey`)

:::

---

(service-invitationcommandservice)=
## Invitation Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-invitation`
:::
### InvitationList
:::{card}
> return all discussions for current identity

**Request**: *InvitationListRequest*
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Response *(Stream)***: *InvitationListResponse*
* `invitations` (**repeated** {ref}`datatype-invitation`)

:::

### InvitationGet
:::{card}
**Request**: *InvitationGetRequest*
* `invitation_id` (uint64)

**Response**: *InvitationGetResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationNew
:::{card}
**Request**: *InvitationNewRequest*
* `invitation_url` (string)

**Response**: *InvitationNewResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationAccept
:::{card}
**Request**: *InvitationAcceptRequest*
* `invitation_id` (uint64)

**Response**: *InvitationAcceptResponse*
* *Empty payload.*

:::

### InvitationDecline
:::{card}
**Request**: *InvitationDeclineRequest*
* `invitation_id` (uint64)

**Response**: *InvitationDeclineResponse*
* *Empty payload.*

:::

### InvitationSas
:::{card}
**Request**: *InvitationSasRequest*
* `invitation_id` (uint64)
* `sas` (string)

**Response**: *InvitationSasResponse*
* *Empty payload.*

:::

### InvitationDelete
:::{card}
**Request**: *InvitationDeleteRequest*
* `invitation_id` (uint64)

**Response**: *InvitationDeleteResponse*
* *Empty payload.*

:::

---

(service-settingscommandservice)=
## Settings Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-settings`
:::
### SettingsIdentityGet
:::{card}
**Request**: *SettingsIdentityGetRequest*
* *Empty payload.*

**Response**: *SettingsIdentityGetResponse*
* `identity_settings` ({ref}`datatype-identitysettings`)

:::

### SettingsIdentitySet
:::{card}
> WARN: this entrypoint erase WHOLE settings. To update identity settings use SettingsIdentityGet to get current config  
> and only edit fields you want to update.

**Request**: *SettingsIdentitySetRequest*
* `identity_settings` ({ref}`datatype-identitysettings`)

**Response**: *SettingsIdentitySetResponse*
* `identity_settings` ({ref}`datatype-identitysettings`)

:::

### SettingsDiscussionGet
:::{card}
**Request**: *SettingsDiscussionGetRequest*
* `discussion_id` (uint64)

**Response**: *SettingsDiscussionGetResponse*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

:::

### SettingsDiscussionSet
:::{card}
**Request**: *SettingsDiscussionSetRequest*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

**Response**: *SettingsDiscussionSetResponse*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

:::

---

(service-storagecommandservice)=
## Storage Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-storage`
:::
### StorageList
:::{card}
> Global storage api: store key value elements in storage. They will be restored as is during backup restoration.  
>   
>   
> StorageList

**Request**: *StorageListRequest*
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)***: *StorageListResponse*
* `elements` (**repeated** {ref}`datatype-storageelement`)

:::

### StorageGet
:::{card}
**Request**: *StorageGetRequest*
* `key` (string)

**Response**: *StorageGetResponse*
* `value` (string)

:::

### StorageSet
:::{card}
**Request**: *StorageSetRequest*
* `key` (string)
* `value` (string)

**Response**: *StorageSetResponse*
* `previous_value` (string)

:::

### StorageUnset
:::{card}
**Request**: *StorageUnsetRequest*
* `key` (string)

**Response**: *StorageUnsetResponse*
* `previous_value` (string)

:::

---

(service-keycloakcommandservice)=
## Keycloak Command Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-keycloak`
:::
### KeycloakBindIdentity
:::{card}
**Request**: *KeycloakBindIdentityRequest*
* `configuration_link` (string)

**Response**: *KeycloakBindIdentityResponse*
* *Empty payload.*

:::

### KeycloakUnbindIdentity
:::{card}
**Request**: *KeycloakUnbindIdentityRequest*
* *Empty payload.*

**Response**: *KeycloakUnbindIdentityResponse*
* *Empty payload.*

:::

### KeycloakUserList
:::{card}
**Request**: *KeycloakUserListRequest*
* `filter` (**optional** {ref}`datatype-keycloakuserfilter`)
* `last_list_timestamp` (**optional** uint64)

**Response *(Stream)***: *KeycloakUserListResponse*
* `users` (**repeated** {ref}`datatype-keycloakuser`)
* `last_list_timestamp` (uint64)

:::

### KeycloakAddUserAsContact
:::{card}
**Request**: *KeycloakAddUserAsContactRequest*
* `keycloak_id` (string)

**Response**: *KeycloakAddUserAsContactResponse*
* *Empty payload.*

:::

---

(service-callcommandservice)=
## Call Command Service

:::{admonition} Info
Currently daemon cannot handle Olvid calls properly.  
You can be notified on incoming calls, and you can initiate call within discussions or with any contact.  
But, you we cannot manage audio or video stream, that's why a daemon will always answer any incoming call with a "busy" response.


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
> unauthenticated rpc to check daemon is up and accessible

**Request**: *PingRequest*
* *Empty payload.*

**Response**: *PingResponse*
* *Empty payload.*

:::

### DaemonVersion
:::{card}
> authenticated rpc to get current daemon version

**Request**: *DaemonVersionRequest*
* *Empty payload.*

**Response**: *DaemonVersionResponse*
* `version` (string)

:::

### AuthenticationTest
:::{card}
> check that sent credentials are valid user credentials, else it returns an error

**Request**: *AuthenticationTestRequest*
* *Empty payload.*

**Response**: *AuthenticationTestResponse*
* *Empty payload.*

:::

### AuthenticationAdminTest
:::{card}
> check that sent credentials are valid admin credentials, else it returns an error

**Request**: *AuthenticationAdminTestRequest*
* *Empty payload.*

**Response**: *AuthenticationAdminTestResponse*
* *Empty payload.*

:::
