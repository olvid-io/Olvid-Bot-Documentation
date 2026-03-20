# Commands



:::{contents} Commands
:depth: 1
:local:
:::
(service-messagecommandservice)=
## MessageCommandService

> **Associated Datatype:** {ref}`datatype-message`

### MessageList
:::{card}
```text
return all messages for current identity
```

**Request: `MessageListRequest`**
* `filter` (**optional** {ref}`datatype-messagefilter`)
* `unread` (**optional** bool - *only list unread messages (messages that have never been listed or sent in a MessageReceived notification)*)

**Response *(Stream)*: `MessageListResponse`**
* `messages` (**repeated** {ref}`datatype-message`)

:::

### MessageGet
:::{card}
**Request: `MessageGetRequest`**
* `message_id` ({ref}`datatype-messageid`)

**Response: `MessageGetResponse`**
* `message` ({ref}`datatype-message`)

:::

### MessageSend
:::{card}
```text
Post a message in a given discussion.
A message must have a non empty body.
```

**Request: `MessageSendRequest`**
* `discussion_id` (uint64)
* `body` (string)
* `reply_id` (**optional** {ref}`datatype-messageid`)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality`)
* `disable_link_preview` (**optional** bool)

**Response: `MessageSendResponse`**
* `message` ({ref}`datatype-message`)

:::

### MessageSendWithAttachments
:::{card}
```text
Post a message with attachments in a given discussion.
A message must have a non empty body or at least one attachment.
```

**Request *(Stream)*: `MessageSendWithAttachmentsRequest`**
* `metadata` ({ref}`datatype-messagesendwithattachmentsrequestmetadata`)
* `payload` (bytes)
* `file_delimiter` (bool)

**Response: `MessageSendWithAttachmentsResponse`**
* `message` ({ref}`datatype-message`)
* `attachments` (**repeated** {ref}`datatype-attachment`)

:::

### MessageReact
:::{card}
```text
if reaction is not set delete current reaction if there is one
```

**Request: `MessageReactRequest`**
* `message_id` ({ref}`datatype-messageid`)
* `reaction` (**optional** string)

**Response: `MessageReactResponse`**
* *Empty payload.*

:::

### MessageUpdateBody
:::{card}
**Request: `MessageUpdateBodyRequest`**
* `message_id` ({ref}`datatype-messageid`)
* `updated_body` (string)

**Response: `MessageUpdateBodyResponse`**
* *Empty payload.*

:::

### MessageDelete
:::{card}
**Request: `MessageDeleteRequest`**
* `message_id` ({ref}`datatype-messageid`)
* `delete_everywhere` (**optional** bool)

**Response: `MessageDeleteResponse`**
* *Empty payload.*

:::

### MessageSendLocation
:::{card}
```text
Post a location message in a discussion.
```

**Request: `MessageSendLocationRequest`**
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)
* `address` (**optional** string)
* `preview_filename` (**optional** string - *preview filename and payload must be set together. Payload might not exceed protobuf max message size.*)
* `preview_payload` (**optional** bytes)
* `ephemerality` (**optional** {ref}`datatype-messageephemerality`)

**Response: `MessageSendLocationResponse`**
* `message` ({ref}`datatype-message`)

:::

### MessageStartLocationSharing
:::{card}
**Request: `MessageStartLocationSharingRequest`**
* `discussion_id` (uint64)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response: `MessageStartLocationSharingResponse`**
* `message` ({ref}`datatype-message`)

:::

### MessageUpdateLocationSharing
:::{card}
**Request: `MessageUpdateLocationSharingRequest`**
* `message_id` ({ref}`datatype-messageid`)
* `latitude` (double)
* `longitude` (double)
* `altitude` (**optional** double)
* `precision` (**optional** float)

**Response: `MessageUpdateLocationSharingResponse`**
* `message` ({ref}`datatype-message`)

:::

### MessageEndLocationSharing
:::{card}
**Request: `MessageEndLocationSharingRequest`**
* `message_id` ({ref}`datatype-messageid`)

**Response: `MessageEndLocationSharingResponse`**
* `message` ({ref}`datatype-message`)

:::

### MessageRefresh
:::{card}
```text
force download message on server
```

**Request: `MessageRefreshRequest`**
* *Empty payload.*

**Response: `MessageRefreshResponse`**
* *Empty payload.*

:::

---

(service-attachmentcommandservice)=
## AttachmentCommandService

> **Associated Datatype:** {ref}`datatype-attachment`

### AttachmentList
:::{card}
```text
return all attachments for current identity
```

**Request: `AttachmentListRequest`**
* `filter` (**optional** {ref}`datatype-attachmentfilter`)

**Response *(Stream)*: `AttachmentListResponse`**
* `attachments` (**repeated** {ref}`datatype-attachment`)

:::

### AttachmentGet
:::{card}
**Request: `AttachmentGetRequest`**
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response: `AttachmentGetResponse`**
* `attachment` ({ref}`datatype-attachment`)

:::

### AttachmentDelete
:::{card}
**Request: `AttachmentDeleteRequest`**
* `attachment_id` ({ref}`datatype-attachmentid`)
* `delete_everywhere` (**optional** bool)

**Response: `AttachmentDeleteResponse`**
* *Empty payload.*

:::

### AttachmentDownload
:::{card}
**Request: `AttachmentDownloadRequest`**
* `attachment_id` ({ref}`datatype-attachmentid`)

**Response *(Stream)*: `AttachmentDownloadResponse`**
* `chunk` (bytes)

:::

---

(service-discussioncommandservice)=
## DiscussionCommandService

> **Associated Datatype:** {ref}`datatype-discussion`

### DiscussionList
:::{card}
**Request: `DiscussionListRequest`**
* `filter` (**optional** {ref}`datatype-discussionfilter`)

**Response *(Stream)*: `DiscussionListResponse`**
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

### DiscussionGet
:::{card}
**Request: `DiscussionGetRequest`**
* `discussion_id` (uint64)

**Response: `DiscussionGetResponse`**
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionGetBytesIdentifier
:::{card}
**Request: `DiscussionGetBytesIdentifierRequest`**
* `discussion_id` (uint64)

**Response: `DiscussionGetBytesIdentifierResponse`**
* `identifier` (bytes)

:::

### DiscussionGetByContact
:::{card}
**Request: `DiscussionGetByContactRequest`**
* `contact_id` (uint64)

**Response: `DiscussionGetByContactResponse`**
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionGetByGroup
:::{card}
**Request: `DiscussionGetByGroupRequest`**
* `group_id` (uint64)

**Response: `DiscussionGetByGroupResponse`**
* `discussion` ({ref}`datatype-discussion`)

:::

### DiscussionEmpty
:::{card}
**Request: `DiscussionEmptyRequest`**
* `discussion_id` (uint64)

**Response: `DiscussionEmptyResponse`**
* *Empty payload.*

:::

### DiscussionDownloadPhoto
:::{card}
**Request: `DiscussionDownloadPhotoRequest`**
* `discussion_id` (uint64)

**Response: `DiscussionDownloadPhotoResponse`**
* `photo` (bytes)

:::

### DiscussionLockedList
:::{card}
```text
locked discussions
```

**Request: `DiscussionLockedListRequest`**
DiscussionLockedList

* *Empty payload.*

**Response *(Stream)*: `DiscussionLockedListResponse`**
* `discussions` (**repeated** {ref}`datatype-discussion`)

:::

### DiscussionLockedDelete
:::{card}
**Request: `DiscussionLockedDeleteRequest`**
* `discussion_id` (uint64)

**Response: `DiscussionLockedDeleteResponse`**
* *Empty payload.*

:::

---

(service-discussionstoragecommandservice)=
## DiscussionStorageCommandService

> **Associated Datatype:** {ref}`datatype-discussionstorage`

### DiscussionStorageList
:::{card}
```text
Discussion storage api: store elements in daemon database, associated with a discussion id. They will remain associated to this discussion if you restore a backup.


DiscussionStorageList
```

**Request: `DiscussionStorageListRequest`**
* `discussion_id` (uint64)
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)*: `DiscussionStorageListResponse`**
* `elements` (**repeated** {ref}`datatype-storageelement`)

:::

### DiscussionStorageGet
:::{card}
**Request: `DiscussionStorageGetRequest`**
* `discussion_id` (uint64)
* `key` (string)

**Response: `DiscussionStorageGetResponse`**
* `value` (string)

:::

### DiscussionStorageSet
:::{card}
**Request: `DiscussionStorageSetRequest`**
* `discussion_id` (uint64)
* `key` (string)
* `value` (string)

**Response: `DiscussionStorageSetResponse`**
* `previous_value` (string)

:::

### DiscussionStorageUnset
:::{card}
**Request: `DiscussionStorageUnsetRequest`**
* `discussion_id` (uint64)
* `key` (string)

**Response: `DiscussionStorageUnsetResponse`**
* `previous_value` (string)

:::

---

(service-contactcommandservice)=
## ContactCommandService

> **Associated Datatype:** {ref}`datatype-contact`

### ContactList
:::{card}
**Request: `ContactListRequest`**
* `filter` (**optional** {ref}`datatype-contactfilter`)

**Response *(Stream)*: `ContactListResponse`**
* `contacts` (**repeated** {ref}`datatype-contact`)

:::

### ContactGet
:::{card}
**Request: `ContactGetRequest`**
* `contact_id` (uint64)

**Response: `ContactGetResponse`**
* `contact` ({ref}`datatype-contact`)

:::

### ContactGetBytesIdentifier
:::{card}
**Request: `ContactGetBytesIdentifierRequest`**
* `contact_id` (uint64)

**Response: `ContactGetBytesIdentifierResponse`**
* `identifier` (bytes)

:::

### ContactGetInvitationLink
:::{card}
**Request: `ContactGetInvitationLinkRequest`**
* `contact_id` (uint64)

**Response: `ContactGetInvitationLinkResponse`**
* `invitation_link` (string)

:::

### ContactDelete
:::{card}
**Request: `ContactDeleteRequest`**
* `contact_id` (uint64)

**Response: `ContactDeleteResponse`**
* *Empty payload.*

:::

### ContactIntroduction
:::{card}
**Request: `ContactIntroductionRequest`**
* `first_contact_id` (uint64)
* `second_contact_id` (uint64)

**Response: `ContactIntroductionResponse`**
* *Empty payload.*

:::

### ContactDownloadPhoto
:::{card}
**Request: `ContactDownloadPhotoRequest`**
* `contact_id` (uint64)

**Response: `ContactDownloadPhotoResponse`**
* `photo` (bytes)

:::

### ContactRecreateChannels
:::{card}
```text
USE CAREFULLY: this might fix some issues but every non sent / received messages will be lost.
```

**Request: `ContactRecreateChannelsRequest`**
* `contact_id` (uint64)

**Response: `ContactRecreateChannelsResponse`**
* *Empty payload.*

:::

### ContactInviteToOneToOneDiscussion
:::{card}
```text
collected contacts
```

**Request: `ContactInviteToOneToOneDiscussionRequest`**
ContactInviteToOneToOneDiscussion

* `contact_id` (uint64)

**Response: `ContactInviteToOneToOneDiscussionResponse`**
* `invitation` ({ref}`datatype-invitation`)

:::

### ContactDowngradeOneToOneDiscussion
:::{card}
```text
ContactDowngradeOneToOne
```

**Request: `ContactDowngradeOneToOneDiscussionRequest`**
* `contact_id` (uint64)

**Response: `ContactDowngradeOneToOneDiscussionResponse`**
* *Empty payload.*

:::

---

(service-groupcommandservice)=
## GroupCommandService

> **Associated Datatype:** {ref}`datatype-group`

### GroupList
:::{card}
```text
return all groups for current identity
```

**Request: `GroupListRequest`**
* `filter` (**optional** {ref}`datatype-groupfilter`)

**Response *(Stream)*: `GroupListResponse`**
* `groups` (**repeated** {ref}`datatype-group`)

:::

### GroupGet
:::{card}
**Request: `GroupGetRequest`**
* `group_id` (uint64)

**Response: `GroupGetResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupGetBytesIdentifier
:::{card}
**Request: `GroupGetBytesIdentifierRequest`**
* `group_id` (uint64)

**Response: `GroupGetBytesIdentifierResponse`**
* `identifier` (bytes)

:::

### GroupNewStandardGroup
:::{card}
**Request: `GroupNewStandardGroupRequest`**
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)

**Response: `GroupNewStandardGroupResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupNewControlledGroup
:::{card}
**Request: `GroupNewControlledGroupRequest`**
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response: `GroupNewControlledGroupResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupNewReadOnlyGroup
:::{card}
**Request: `GroupNewReadOnlyGroupRequest`**
* `name` (**optional** string)
* `description` (**optional** string)
* `admin_contact_ids` (**repeated** uint64)
* `contact_ids` (**repeated** uint64)

**Response: `GroupNewReadOnlyGroupResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupNewAdvancedGroup
:::{card}
**Request: `GroupNewAdvancedGroupRequest`**
* `name` (**optional** string)
* `description` (**optional** string)
* `advanced_configuration` (**optional** {ref}`datatype-advancedconfiguration`)
* `members` (**repeated** {ref}`datatype-groupmember`)

**Response: `GroupNewAdvancedGroupResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupDisband
:::{card}
**Request: `GroupDisbandRequest`**
* `group_id` (uint64)

**Response: `GroupDisbandResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupLeave
:::{card}
**Request: `GroupLeaveRequest`**
* `group_id` (uint64)

**Response: `GroupLeaveResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupUpdate
:::{card}
```text
: update a group by modifying a Group object retrieved from groupList of groupGet.
Supported modifications:
- Add a member: create a new GroupMember and add it to members field
- Remove a member: remove associated GroupMember from members field
- Remove a pending member: remove associated GroupPendingMember from pendingMembers field
- Update (pending) member permissions: update permissions in permissions field in GroupMember or GroupPendingMember
- Update group name: modify name field
- Update group description: modify description field
Every other modifications will be ignored. You must keep groupId field properly set.
```

**Request: `GroupUpdateRequest`**
* `group` ({ref}`datatype-group`)

**Response: `GroupUpdateResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupUnsetPhoto
:::{card}
**Request: `GroupUnsetPhotoRequest`**
* `group_id` (uint64)

**Response: `GroupUnsetPhotoResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupSetPhoto
:::{card}
**Request *(Stream)*: `GroupSetPhotoRequest`**
* `metadata` ({ref}`datatype-groupsetphotorequestmetadata`)
* `payload` (bytes)

**Response: `GroupSetPhotoResponse`**
* `group` ({ref}`datatype-group`)

:::

### GroupDownloadPhoto
:::{card}
**Request: `GroupDownloadPhotoRequest`**
* `group_id` (uint64)

**Response: `GroupDownloadPhotoResponse`**
* `photo` (bytes)

:::

---

(service-identitycommandservice)=
## IdentityCommandService

> **Associated Datatype:** {ref}`datatype-identity`

### IdentityGet
:::{card}
**Request: `IdentityGetRequest`**
* *Empty payload.*

**Response: `IdentityGetResponse`**
* `identity` ({ref}`datatype-identity`)

:::

### IdentityGetBytesIdentifier
:::{card}
**Request: `IdentityGetBytesIdentifierRequest`**
* *Empty payload.*

**Response: `IdentityGetBytesIdentifierResponse`**
* `identifier` (bytes)

:::

### IdentityGetInvitationLink
:::{card}
**Request: `IdentityGetInvitationLinkRequest`**
* *Empty payload.*

**Response: `IdentityGetInvitationLinkResponse`**
* `invitation_link` (string)

:::

### IdentityUpdateDetails
:::{card}
**Request: `IdentityUpdateDetailsRequest`**
* `new_details` ({ref}`datatype-identitydetails`)

**Response: `IdentityUpdateDetailsResponse`**
* *Empty payload.*

:::

### IdentityRemovePhoto
:::{card}
**Request: `IdentityRemovePhotoRequest`**
* *Empty payload.*

**Response: `IdentityRemovePhotoResponse`**
* *Empty payload.*

:::

### IdentitySetPhoto
:::{card}
**Request *(Stream)*: `IdentitySetPhotoRequest`**
* `metadata` ({ref}`datatype-identitysetphotorequestmetadata`)
* `payload` (bytes)

**Response: `IdentitySetPhotoResponse`**
* *Empty payload.*

:::

### IdentityDownloadPhoto
:::{card}
**Request: `IdentityDownloadPhotoRequest`**
* *Empty payload.*

**Response: `IdentityDownloadPhotoResponse`**
* `photo` (bytes)

:::

### IdentityGetApiKeyStatus
:::{card}
**Request: `IdentityGetApiKeyStatusRequest`**
* *Empty payload.*

**Response: `IdentityGetApiKeyStatusResponse`**
* `api_key` ({ref}`datatype-apikey`)

:::

### IdentitySetApiKey
:::{card}
**Request: `IdentitySetApiKeyRequest`**
* `api_key` (string)

**Response: `IdentitySetApiKeyResponse`**
* `api_key` ({ref}`datatype-apikey`)

:::

### IdentitySetConfigurationLink
:::{card}
**Request: `IdentitySetConfigurationLinkRequest`**
* `configuration_link` (string)

**Response: `IdentitySetConfigurationLinkResponse`**
* `api_key` ({ref}`datatype-apikey`)

:::

---

(service-invitationcommandservice)=
## InvitationCommandService

> **Associated Datatype:** {ref}`datatype-invitation`

### InvitationList
:::{card}
```text
return all discussions for current identity
```

**Request: `InvitationListRequest`**
* `filter` (**optional** {ref}`datatype-invitationfilter`)

**Response *(Stream)*: `InvitationListResponse`**
* `invitations` (**repeated** {ref}`datatype-invitation`)

:::

### InvitationGet
:::{card}
**Request: `InvitationGetRequest`**
* `invitation_id` (uint64)

**Response: `InvitationGetResponse`**
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationNew
:::{card}
**Request: `InvitationNewRequest`**
* `invitation_url` (string)

**Response: `InvitationNewResponse`**
* `invitation` ({ref}`datatype-invitation`)

:::

### InvitationAccept
:::{card}
**Request: `InvitationAcceptRequest`**
* `invitation_id` (uint64)

**Response: `InvitationAcceptResponse`**
* *Empty payload.*

:::

### InvitationDecline
:::{card}
**Request: `InvitationDeclineRequest`**
* `invitation_id` (uint64)

**Response: `InvitationDeclineResponse`**
* *Empty payload.*

:::

### InvitationSas
:::{card}
**Request: `InvitationSasRequest`**
* `invitation_id` (uint64)
* `sas` (string)

**Response: `InvitationSasResponse`**
* *Empty payload.*

:::

### InvitationDelete
:::{card}
**Request: `InvitationDeleteRequest`**
* `invitation_id` (uint64)

**Response: `InvitationDeleteResponse`**
* *Empty payload.*

:::

---

(service-settingscommandservice)=
## SettingsCommandService

> **Associated Datatype:** {ref}`datatype-settings`

### SettingsIdentityGet
:::{card}
**Request: `SettingsIdentityGetRequest`**
* *Empty payload.*

**Response: `SettingsIdentityGetResponse`**
* `identity_settings` ({ref}`datatype-identitysettings`)

:::

### SettingsIdentitySet
:::{card}
```text
WARN: this entrypoint erase WHOLE settings. To update identity settings use SettingsIdentityGet to get current config
and only edit fields you want to update.
```

**Request: `SettingsIdentitySetRequest`**
* `identity_settings` ({ref}`datatype-identitysettings`)

**Response: `SettingsIdentitySetResponse`**
* `identity_settings` ({ref}`datatype-identitysettings`)

:::

### SettingsDiscussionGet
:::{card}
**Request: `SettingsDiscussionGetRequest`**
* `discussion_id` (uint64)

**Response: `SettingsDiscussionGetResponse`**
* `discussion_settings` ({ref}`datatype-discussionsettings`)

:::

### SettingsDiscussionSet
:::{card}
**Request: `SettingsDiscussionSetRequest`**
* `discussion_settings` ({ref}`datatype-discussionsettings`)

**Response: `SettingsDiscussionSetResponse`**
* `discussion_settings` ({ref}`datatype-discussionsettings`)

:::

---

(service-storagecommandservice)=
## StorageCommandService

> **Associated Datatype:** {ref}`datatype-storage`

### StorageList
:::{card}
```text
Global storage api: store key value elements in storage. They will be restored as is during backup restoration.


StorageList
```

**Request: `StorageListRequest`**
* `filter` (**optional** {ref}`datatype-storageelementfilter`)

**Response *(Stream)*: `StorageListResponse`**
* `elements` (**repeated** {ref}`datatype-storageelement`)

:::

### StorageGet
:::{card}
**Request: `StorageGetRequest`**
* `key` (string)

**Response: `StorageGetResponse`**
* `value` (string)

:::

### StorageSet
:::{card}
**Request: `StorageSetRequest`**
* `key` (string)
* `value` (string)

**Response: `StorageSetResponse`**
* `previous_value` (string)

:::

### StorageUnset
:::{card}
**Request: `StorageUnsetRequest`**
* `key` (string)

**Response: `StorageUnsetResponse`**
* `previous_value` (string)

:::

---

(service-callcommandservice)=
## CallCommandService

> **Associated Datatype:** {ref}`datatype-call`

### CallStartDiscussionCall
:::{card}
**Request: `CallStartDiscussionCallRequest`**
* `discussion_id` (uint64)

**Response: `CallStartDiscussionCallResponse`**
* `call_identifier` (string)

:::

### CallStartCustomCall
:::{card}
**Request: `CallStartCustomCallRequest`**
* `contact_ids` (**repeated** uint64)
* `discussion_id` (**optional** uint64)

**Response: `CallStartCustomCallResponse`**
* `call_identifier` (string)

:::

---

(service-keycloakcommandservice)=
## KeycloakCommandService

> **Associated Datatype:** {ref}`datatype-keycloak`

### KeycloakBindIdentity
:::{card}
**Request: `KeycloakBindIdentityRequest`**
* `configuration_link` (string)

**Response: `KeycloakBindIdentityResponse`**
* *Empty payload.*

:::

### KeycloakUnbindIdentity
:::{card}
**Request: `KeycloakUnbindIdentityRequest`**
* *Empty payload.*

**Response: `KeycloakUnbindIdentityResponse`**
* *Empty payload.*

:::

### KeycloakUserList
:::{card}
**Request: `KeycloakUserListRequest`**
* `filter` (**optional** {ref}`datatype-keycloakuserfilter`)
* `last_list_timestamp` (**optional** uint64)

**Response *(Stream)*: `KeycloakUserListResponse`**
* `users` (**repeated** {ref}`datatype-keycloakuser`)
* `last_list_timestamp` (uint64)

:::

### KeycloakAddUserAsContact
:::{card}
**Request: `KeycloakAddUserAsContactRequest`**
* `keycloak_id` (string)

**Response: `KeycloakAddUserAsContactResponse`**
* *Empty payload.*

:::

---

(service-toolcommandservice)=
## ToolCommandService

> **Associated Datatype:** {ref}`datatype-tool`

### Ping
:::{card}
```text
unauthenticated rpc to check daemon is up and accessible
```

**Request: `PingRequest`**
* *Empty payload.*

**Response: `PingResponse`**
* *Empty payload.*

:::

### DaemonVersion
:::{card}
```text
authenticated rpc to get current daemon version
```

**Request: `DaemonVersionRequest`**
* *Empty payload.*

**Response: `DaemonVersionResponse`**
* `version` (string)

:::

### AuthenticationTest
:::{card}
```text
check that sent credentials are valid user credentials, else it returns an error
```

**Request: `AuthenticationTestRequest`**
* *Empty payload.*

**Response: `AuthenticationTestResponse`**
* *Empty payload.*

:::

### AuthenticationAdminTest
:::{card}
```text
check that sent credentials are valid admin credentials, else it returns an error
```

**Request: `AuthenticationAdminTestRequest`**
* *Empty payload.*

**Response: `AuthenticationAdminTestResponse`**
* *Empty payload.*

:::
