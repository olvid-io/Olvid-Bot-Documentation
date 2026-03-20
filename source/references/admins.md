# Admin Commands

Privileged commands requiring a valid admin client key.

:::{contents}
:depth: 1
:local:
:::
(service-identityadminservice)=
## IdentityAdminService

> **Associated Datatype:** {ref}`datatype-identity`

### IdentityList
**Request: `IdentityListRequest`**
* `filter` (**optional** {ref}`datatype-identityfilter`)

**Response *(Stream)*: `IdentityListResponse`**
* `identities` (**repeated** {ref}`datatype-identity`)



### IdentityAdminGet
**Request: `IdentityAdminGetRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminGetResponse`**
* `identity` ({ref}`datatype-identity`)



### IdentityAdminGetBytesIdentifier
**Request: `IdentityAdminGetBytesIdentifierRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminGetBytesIdentifierResponse`**
* `identifier` (bytes)



### IdentityAdminGetInvitationLink
**Request: `IdentityAdminGetInvitationLinkRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminGetInvitationLinkResponse`**
* `invitation_link` (string)



### IdentityAdminDownloadPhoto
**Request: `IdentityAdminDownloadPhotoRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminDownloadPhotoResponse`**
* `photo` (bytes)



### IdentityDelete
**Request: `IdentityDeleteRequest`**
* `identity_id` (uint64)
* `delete_everywhere` (**optional** bool)

**Response: `IdentityDeleteResponse`**
* *Empty payload.*



### IdentityNew
**Request: `IdentityNewRequest`**
* `identity_details` ({ref}`datatype-identitydetails`)
* `server_url` (**optional** string)

**Response: `IdentityNewResponse`**
* `identity` ({ref}`datatype-identity`)



### IdentityKeycloakNew
**Request: `IdentityKeycloakNewRequest`**
* `configuration_link` (string)

**Response: `IdentityKeycloakNewResponse`**
* `identity` ({ref}`datatype-identity`)



---

(service-backupadminservice)=
## BackupAdminService

> **Associated Datatype:** {ref}`datatype-backup`

### BackupKeyGet
**Request: `BackupKeyGetRequest`**
* *Empty payload.*

**Response: `BackupKeyGetResponse`**
* `backup_key` (string)



### BackupKeyRenew
**Request: `BackupKeyRenewRequest`**
* *Empty payload.*

**Response: `BackupKeyRenewResponse`**
* `backup_key` (string)



### BackupGet
**Request: `BackupGetRequest`**
* `backup_key` (string)

**Response: `BackupGetResponse`**
* `backup` ({ref}`datatype-backup`)



### BackupNow
**Request: `BackupNowRequest`**
* *Empty payload.*

**Response: `BackupNowResponse`**
* *Empty payload.*



### BackupRestoreDaemon
**Request: `BackupRestoreDaemonRequest`**
* `backup_key` (string)
* `new_device_name` (**optional** string - *specify a name for this new daemon*)

**Response: `BackupRestoreDaemonResponse`**
* `restored_identities` (**repeated** {ref}`datatype-identity`)
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)



### BackupRestoreAdminBackup
**Request: `BackupRestoreAdminBackupRequest`**
* `backup_key` (string)

**Response: `BackupRestoreAdminBackupResponse`**
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)



### BackupRestoreProfileSnapshot
**Request: `BackupRestoreProfileSnapshotRequest`**
* `backup_key` (string)
* `id` (string)
* `new_device_name` (**optional** string - *specify a name for this new daemon*)

**Response: `BackupRestoreProfileSnapshotResponse`**
* `restored_identity` ({ref}`datatype-identity`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)



---

(service-clientkeyadminservice)=
## ClientKeyAdminService

> **Associated Datatype:** {ref}`datatype-clientkey`

### ClientKeyList
**Request: `ClientKeyListRequest`**
* `filter` (**optional** {ref}`datatype-clientkeyfilter`)

**Response *(Stream)*: `ClientKeyListResponse`**
* `client_keys` (**repeated** {ref}`datatype-clientkey`)



### ClientKeyGet
**Request: `ClientKeyGetRequest`**
* `client_key` (string)

**Response: `ClientKeyGetResponse`**
* `client_key` ({ref}`datatype-clientkey`)



### ClientKeyNew
**Request: `ClientKeyNewRequest`**
* `name` (string)
* `identity_id` (uint64 - *specify 0 to create an admin api key*)

**Response: `ClientKeyNewResponse`**
* `client_key` ({ref}`datatype-clientkey`)



### ClientKeyDelete
**Request: `ClientKeyDeleteRequest`**
* `client_key` (string)

**Response: `ClientKeyDeleteResponse`**
* *Empty payload.*



---
