# Commands



:::{contents} Commands
:depth: 1
:local:
:::
(service-messagecommandservice)=
## MessageCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-message`
```

:::{card}
### MessageList
> Return all messages for current identity

**Request**: *MessageListRequest*
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `unread` (**optional** bool - *only list unread messages (messages that have never been listed or sent in a MessageReceived notification)*)

**Response *(Stream)***: *MessageListResponse*
* `messages` (**repeated** {ref}`datatype-message`)

:::

:::{card}
### MessageGet
**Request**: *MessageGetRequest*
* `message_id` ({ref}`datatype-messageid`)

**Response**: *MessageGetResponse*
* `message` ({ref}`datatype-message`)

:::

:::{card}
### MessageSend
> Post a message in a given discussion.  
> A message must have a non empty body.

**Request**: *MessageSendRequest*
* `discussion_id` (uint64)
* `body` (string)
* `reply_id` (**optional** {ref}`datatype-messageid`)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality`)
* `disable_link_preview` (**optional** bool)

**Response**: *MessageSendResponse*
* `message` ({ref}`datatype-message`)

:::

:::{card}
### MessageSendWithAttachments
> Post a message with attachments in a given discussion.  
> A message must have a non empty body or at least one attachment.

**Request *(Stream)***: *MessageSendWithAttachmentsRequest*
* `metadata` ({ref}`datatype-messagesendwithattachmentsrequestmetadata`)
* `payload` (bytes)
* `file_delimiter` (bool)

**Response**: *MessageSendWithAttachmentsResponse*
* `message` ({ref}`datatype-message`)
* `attachments` (**repeated** {ref}`datatype-attachment`)

:::

:::{card}
### MessageReact
> if reaction is not set delete current reaction if there is one

**Request**: *MessageReactRequest*
* `message_id` ({ref}`datatype-messageid`)
* `reaction` (**optional** string)

**Response**: *MessageReactResponse*
* *Empty payload.*

:::

:::{card}
### MessageUpdateBody
**Request**: *MessageUpdateBodyRequest*
* `message_id` ({ref}`datatype-messageid`)
* `updated_body` (string)

**Response**: *MessageUpdateBodyResponse*
* *Empty payload.*

:::

:::{card}
### MessageDelete
**Request**: *MessageDeleteRequest*
* `message_id` ({ref}`datatype-messageid`)
* `delete_everywhere` (**optional** bool)

**Response**: *MessageDeleteResponse*
* *Empty payload.*

:::

:::{card}
### MessageSendLocation
> Post a location message in a discussion.

**Request**: *MessageSendLocationRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)
* `address` (**optional** string)
* `preview_filename` (**optional** string - *preview filename and payload must be set together. Payload might not exceed protobuf max message size.*)
* `preview_payload` (**optional** bytes)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality`)

**Response**: *MessageSendLocationResponse*
* `message` ({ref}`datatype-message`)

:::

:::{card}
### MessageStartLocationSharing
**Request**: *MessageStartLocationSharingRequest*
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response**: *MessageStartLocationSharingResponse*
* `message` ({ref}`datatype-message`)

:::

:::{card}
### MessageUpdateLocationSharing
**Request**: *MessageUpdateLocationSharingRequest*
* `message_id` ({ref}`datatype-messageid`)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response**: *MessageUpdateLocationSharingResponse*
* `message` ({ref}`datatype-message`)

:::

:::{card}
### MessageEndLocationSharing
**Request**: *MessageEndLocationSharingRequest*
* `message_id` ({ref}`datatype-messageid`)

**Response**: *MessageEndLocationSharingResponse*
* `message` ({ref}`datatype-message`)

:::

:::{card}
### MessageRefresh
> force download message on server

**Request**: *MessageRefreshRequest*
* *Empty payload.*

**Response**: *MessageRefreshResponse*
* *Empty payload.*

:::

---

(service-attachmentcommandservice)=
## AttachmentCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-attachment`
```

:::{card}
### AttachmentList
> return all attachments for current identity

**Request**: *AttachmentListRequest*
* `filter` (**optional** {ref}`datatype-attachmentfilter`)

**Response *(Stream)***: *AttachmentListResponse*
* `attachments` (**repeated** {ref}`datatype-attachment`)

:::

:::{card}
### AttachmentGet
**Request**: *AttachmentGetRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response**: *AttachmentGetResponse*
* `attachment` ({ref}`datatype-attachment`)

:::

:::{card}
### AttachmentDelete
**Request**: *AttachmentDeleteRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)
* `delete_everywhere` (**optional** bool)

**Response**: *AttachmentDeleteResponse*
* *Empty payload.*

:::

:::{card}
### AttachmentDownload
**Request**: *AttachmentDownloadRequest*
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response *(Stream)***: *AttachmentDownloadResponse*
* `chunk` (bytes)

:::

---

(service-discussioncommandservice)=
## DiscussionCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-discussion`
```

:::{card}
### DiscussionList
**Request**: *DiscussionListRequest*
* `filter` (**optional** {ref}`datatype-discussionfilter`)

**Response *(Stream)***: *DiscussionListResponse*
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

:::{card}
### DiscussionGet
**Request**: *DiscussionGetRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionGetResponse*
* `discussion` ({ref}`datatype-discussion`)

:::

:::{card}
### DiscussionGetBytesIdentifier
**Request**: *DiscussionGetBytesIdentifierRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

:::{card}
### DiscussionGetByContact
**Request**: *DiscussionGetByContactRequest*
* `contact_id` (uint64)

**Response**: *DiscussionGetByContactResponse*
* `discussion` ({ref}`datatype-discussion`)

:::

:::{card}
### DiscussionGetByGroup
**Request**: *DiscussionGetByGroupRequest*
* `group_id` (uint64)

**Response**: *DiscussionGetByGroupResponse*
* `discussion` ({ref}`datatype-discussion`)

:::

:::{card}
### DiscussionEmpty
**Request**: *DiscussionEmptyRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionEmptyResponse*
* *Empty payload.*

:::

:::{card}
### DiscussionDownloadPhoto
**Request**: *DiscussionDownloadPhotoRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionDownloadPhotoResponse*
* `photo` (bytes)

:::

:::{card}
### DiscussionLockedList
> locked discussions

**Request**: *DiscussionLockedListRequest*
DiscussionLockedList

* *Empty payload.*

**Response *(Stream)***: *DiscussionLockedListResponse*
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

:::{card}
### DiscussionLockedDelete
**Request**: *DiscussionLockedDeleteRequest*
* `discussion_id` (uint64)

**Response**: *DiscussionLockedDeleteResponse*
* *Empty payload.*

:::

---

(service-discussionstoragecommandservice)=
## DiscussionStorageCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-discussionstorage`
```

:::{card}
### DiscussionStorageList
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

:::{card}
### DiscussionStorageGet
**Request**: *DiscussionStorageGetRequest*
* `discussion_id` (uint64)
* `key` (string)

**Response**: *DiscussionStorageGetResponse*
* `value` (string)

:::

:::{card}
### DiscussionStorageSet
**Request**: *DiscussionStorageSetRequest*
* `discussion_id` (uint64)
* `key` (string)
* `value` (string)

**Response**: *DiscussionStorageSetResponse*
* `previous_value` (string)

:::

:::{card}
### DiscussionStorageUnset
**Request**: *DiscussionStorageUnsetRequest*
* `discussion_id` (uint64)
* `key` (string)

**Response**: *DiscussionStorageUnsetResponse*
* `previous_value` (string)

:::

---

(service-contactcommandservice)=
## ContactCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-contact`
```

:::{card}
### ContactList
**Request**: *ContactListRequest*
* `filter` (**optional** {ref}`datatype-contactfilter`)

**Response *(Stream)***: *ContactListResponse*
* `contacts` (**repeated** {ref}`datatype-contact`)

:::

:::{card}
### ContactGet
**Request**: *ContactGetRequest*
* `contact_id` (uint64)

**Response**: *ContactGetResponse*
* `contact` ({ref}`datatype-contact`)

:::

:::{card}
### ContactGetBytesIdentifier
**Request**: *ContactGetBytesIdentifierRequest*
* `contact_id` (uint64)

**Response**: *ContactGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

:::{card}
### ContactGetInvitationLink
**Request**: *ContactGetInvitationLinkRequest*
* `contact_id` (uint64)

**Response**: *ContactGetInvitationLinkResponse*
* `invitation_link` (string)

:::

:::{card}
### ContactDelete
**Request**: *ContactDeleteRequest*
* `contact_id` (uint64)

**Response**: *ContactDeleteResponse*
* *Empty payload.*

:::

:::{card}
### ContactIntroduction
**Request**: *ContactIntroductionRequest*
* `first_contact_id` (uint64)
* `second_contact_id` (uint64)

**Response**: *ContactIntroductionResponse*
* *Empty payload.*

:::

:::{card}
### ContactDownloadPhoto
**Request**: *ContactDownloadPhotoRequest*
* `contact_id` (uint64)

**Response**: *ContactDownloadPhotoResponse*
* `photo` (bytes)

:::

:::{card}
### ContactRecreateChannels
> USE CAREFULLY: this might fix some issues but every non sent / received messages will be lost.

**Request**: *ContactRecreateChannelsRequest*
* `contact_id` (uint64)

**Response**: *ContactRecreateChannelsResponse*
* *Empty payload.*

:::

:::{card}
### ContactInviteToOneToOneDiscussion
> collected contacts

**Request**: *ContactInviteToOneToOneDiscussionRequest*
ContactInviteToOneToOneDiscussion

* `contact_id` (uint64)

**Response**: *ContactInviteToOneToOneDiscussionResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

:::{card}
### ContactDowngradeOneToOneDiscussion
> ContactDowngradeOneToOne

**Request**: *ContactDowngradeOneToOneDiscussionRequest*
* `contact_id` (uint64)

**Response**: *ContactDowngradeOneToOneDiscussionResponse*
* *Empty payload.*

:::

---

(service-groupcommandservice)=
## GroupCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-group`
```

:::{card}
### GroupList
> return all groups for current identity

**Request**: *GroupListRequest*
* `filter` (**optional** {ref}`datatype-groupfilter`)

**Response *(Stream)***: *GroupListResponse*
* `groups` (**repeated** {ref}`datatype-group`)

:::

:::{card}
### GroupGet
**Request**: *GroupGetRequest*
* `group_id` (uint64)

**Response**: *GroupGetResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupGetBytesIdentifier
**Request**: *GroupGetBytesIdentifierRequest*
* `group_id` (uint64)

**Response**: *GroupGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

:::{card}
### GroupNewStandardGroup
**Request**: *GroupNewStandardGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)

**Response**: *GroupNewStandardGroupResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupNewControlledGroup
**Request**: *GroupNewControlledGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response**: *GroupNewControlledGroupResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupNewReadOnlyGroup
**Request**: *GroupNewReadOnlyGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response**: *GroupNewReadOnlyGroupResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupNewAdvancedGroup
**Request**: *GroupNewAdvancedGroupRequest*
* `name` (**optional** string)
* `description` (**optional** string)
* `advanced_configuration` (**optional** {ref}`datatype-advancedconfiguration`)
* `members` (**repeated** {ref}`datatype-groupmember`)

**Response**: *GroupNewAdvancedGroupResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupDisband
**Request**: *GroupDisbandRequest*
* `group_id` (uint64)

**Response**: *GroupDisbandResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupLeave
**Request**: *GroupLeaveRequest*
* `group_id` (uint64)

**Response**: *GroupLeaveResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupUpdate
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

:::{card}
### GroupUnsetPhoto
**Request**: *GroupUnsetPhotoRequest*
* `group_id` (uint64)

**Response**: *GroupUnsetPhotoResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupSetPhoto
**Request *(Stream)***: *GroupSetPhotoRequest*
* `metadata` ({ref}`datatype-groupsetphotorequestmetadata`)
* `payload` (bytes)

**Response**: *GroupSetPhotoResponse*
* `group` ({ref}`datatype-group`)

:::

:::{card}
### GroupDownloadPhoto
**Request**: *GroupDownloadPhotoRequest*
* `group_id` (uint64)

**Response**: *GroupDownloadPhotoResponse*
* `photo` (bytes)

:::

---

(service-identitycommandservice)=
## IdentityCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-identity`
```

:::{card}
### IdentityGet
**Request**: *IdentityGetRequest*
* *Empty payload.*

**Response**: *IdentityGetResponse*
* `identity` ({ref}`datatype-identity`)

:::

:::{card}
### IdentityGetBytesIdentifier
**Request**: *IdentityGetBytesIdentifierRequest*
* *Empty payload.*

**Response**: *IdentityGetBytesIdentifierResponse*
* `identifier` (bytes)

:::

:::{card}
### IdentityGetInvitationLink
**Request**: *IdentityGetInvitationLinkRequest*
* *Empty payload.*

**Response**: *IdentityGetInvitationLinkResponse*
* `invitation_link` (string)

:::

:::{card}
### IdentityUpdateDetails
**Request**: *IdentityUpdateDetailsRequest*
* `new_details` ({ref}`datatype-identitydetails`)

**Response**: *IdentityUpdateDetailsResponse*
* *Empty payload.*

:::

:::{card}
### IdentityRemovePhoto
**Request**: *IdentityRemovePhotoRequest*
* *Empty payload.*

**Response**: *IdentityRemovePhotoResponse*
* *Empty payload.*

:::

:::{card}
### IdentitySetPhoto
**Request *(Stream)***: *IdentitySetPhotoRequest*
* `metadata` ({ref}`datatype-identitysetphotorequestmetadata`)
* `payload` (bytes)

**Response**: *IdentitySetPhotoResponse*
* *Empty payload.*

:::

:::{card}
### IdentityDownloadPhoto
**Request**: *IdentityDownloadPhotoRequest*
* *Empty payload.*

**Response**: *IdentityDownloadPhotoResponse*
* `photo` (bytes)

:::

:::{card}
### IdentityGetApiKeyStatus
**Request**: *IdentityGetApiKeyStatusRequest*
* *Empty payload.*

**Response**: *IdentityGetApiKeyStatusResponse*
* `api_key` ({ref}`datatype-apikey`)

:::

:::{card}
### IdentitySetApiKey
**Request**: *IdentitySetApiKeyRequest*
* `api_key` (string)

**Response**: *IdentitySetApiKeyResponse*
* `api_key` ({ref}`datatype-apikey`)

:::

:::{card}
### IdentitySetConfigurationLink
**Request**: *IdentitySetConfigurationLinkRequest*
* `configuration_link` (string)

**Response**: *IdentitySetConfigurationLinkResponse*
* `api_key` ({ref}`datatype-apikey`)

:::

---

(service-invitationcommandservice)=
## InvitationCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-invitation`
```

:::{card}
### InvitationList
> return all discussions for current identity

**Request**: *InvitationListRequest*
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Response *(Stream)***: *InvitationListResponse*
* `invitations` (**repeated** {ref}`datatype-invitation`)

:::

:::{card}
### InvitationGet
**Request**: *InvitationGetRequest*
* `invitation_id` (uint64)

**Response**: *InvitationGetResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

:::{card}
### InvitationNew
**Request**: *InvitationNewRequest*
* `invitation_url` (string)

**Response**: *InvitationNewResponse*
* `invitation` ({ref}`datatype-invitation`)

:::

:::{card}
### InvitationAccept
**Request**: *InvitationAcceptRequest*
* `invitation_id` (uint64)

**Response**: *InvitationAcceptResponse*
* *Empty payload.*

:::

:::{card}
### InvitationDecline
**Request**: *InvitationDeclineRequest*
* `invitation_id` (uint64)

**Response**: *InvitationDeclineResponse*
* *Empty payload.*

:::

:::{card}
### InvitationSas
**Request**: *InvitationSasRequest*
* `invitation_id` (uint64)
* `sas` (string)

**Response**: *InvitationSasResponse*
* *Empty payload.*

:::

:::{card}
### InvitationDelete
**Request**: *InvitationDeleteRequest*
* `invitation_id` (uint64)

**Response**: *InvitationDeleteResponse*
* *Empty payload.*

:::

---

(service-settingscommandservice)=
## SettingsCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-settings`
```

:::{card}
### SettingsIdentityGet
**Request**: *SettingsIdentityGetRequest*
* *Empty payload.*

**Response**: *SettingsIdentityGetResponse*
* `identity_settings` ({ref}`datatype-identitysettings`)

:::

:::{card}
### SettingsIdentitySet
> WARN: this entrypoint erase WHOLE settings. To update identity settings use SettingsIdentityGet to get current config  
> and only edit fields you want to update.

**Request**: *SettingsIdentitySetRequest*
* `identity_settings` ({ref}`datatype-identitysettings`)

**Response**: *SettingsIdentitySetResponse*
* `identity_settings` ({ref}`datatype-identitysettings`)

:::

:::{card}
### SettingsDiscussionGet
**Request**: *SettingsDiscussionGetRequest*
* `discussion_id` (uint64)

**Response**: *SettingsDiscussionGetResponse*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

:::

:::{card}
### SettingsDiscussionSet
**Request**: *SettingsDiscussionSetRequest*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

**Response**: *SettingsDiscussionSetResponse*
* `discussion_settings` ({ref}`datatype-discussionsettings`)

:::

---

(service-storagecommandservice)=
## StorageCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-storage`
```

:::{card}
### StorageList
> Global storage api: store key value elements in storage. They will be restored as is during backup restoration.  
>   
>   
> StorageList

**Request**: *StorageListRequest*
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)***: *StorageListResponse*
* `elements` (**repeated** {ref}`datatype-storageelement`)

:::

:::{card}
### StorageGet
**Request**: *StorageGetRequest*
* `key` (string)

**Response**: *StorageGetResponse*
* `value` (string)

:::

:::{card}
### StorageSet
**Request**: *StorageSetRequest*
* `key` (string)
* `value` (string)

**Response**: *StorageSetResponse*
* `previous_value` (string)

:::

:::{card}
### StorageUnset
**Request**: *StorageUnsetRequest*
* `key` (string)

**Response**: *StorageUnsetResponse*
* `previous_value` (string)

:::

---

(service-keycloakcommandservice)=
## KeycloakCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-keycloak`
```

:::{card}
### KeycloakBindIdentity
**Request**: *KeycloakBindIdentityRequest*
* `configuration_link` (string)

**Response**: *KeycloakBindIdentityResponse*
* *Empty payload.*

:::

:::{card}
### KeycloakUnbindIdentity
**Request**: *KeycloakUnbindIdentityRequest*
* *Empty payload.*

**Response**: *KeycloakUnbindIdentityResponse*
* *Empty payload.*

:::

:::{card}
### KeycloakUserList
**Request**: *KeycloakUserListRequest*
* `filter` (**optional** {ref}`datatype-keycloakuserfilter`)
* `last_list_timestamp` (**optional** uint64)

**Response *(Stream)***: *KeycloakUserListResponse*
* `users` (**repeated** {ref}`datatype-keycloakuser`)
* `last_list_timestamp` (uint64)

:::

:::{card}
### KeycloakAddUserAsContact
**Request**: *KeycloakAddUserAsContactRequest*
* `keycloak_id` (string)

**Response**: *KeycloakAddUserAsContactResponse*
* *Empty payload.*

:::

---

(service-callcommandservice)=
## CallCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-call`
```

:::{card}
### CallStartDiscussionCall
**Request**: *CallStartDiscussionCallRequest*
* `discussion_id` (uint64)

**Response**: *CallStartDiscussionCallResponse*
* `call_identifier` (string)

:::

:::{card}
### CallStartCustomCall
**Request**: *CallStartCustomCallRequest*
* `contact_ids` (**repeated** uint64)
* `discussion_id` (**optional** uint64)

**Response**: *CallStartCustomCallResponse*
* `call_identifier` (string)

:::

---

(service-toolcommandservice)=
## ToolCommandService

```{admonition} Info
**Associated Datatype:** {ref}`datatype-tool`
```

:::{card}
### Ping
> unauthenticated rpc to check daemon is up and accessible

**Request**: *PingRequest*
* *Empty payload.*

**Response**: *PingResponse*
* *Empty payload.*

:::

:::{card}
### DaemonVersion
> authenticated rpc to get current daemon version

**Request**: *DaemonVersionRequest*
* *Empty payload.*

**Response**: *DaemonVersionResponse*
* `version` (string)

:::

:::{card}
### AuthenticationTest
> check that sent credentials are valid user credentials, else it returns an error

**Request**: *AuthenticationTestRequest*
* *Empty payload.*

**Response**: *AuthenticationTestResponse*
* *Empty payload.*

:::

:::{card}
### AuthenticationAdminTest
> check that sent credentials are valid admin credentials, else it returns an error

**Request**: *AuthenticationAdminTestRequest*
* *Empty payload.*

**Response**: *AuthenticationAdminTestResponse*
* *Empty payload.*

:::
