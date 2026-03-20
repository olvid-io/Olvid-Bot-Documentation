# Admin Commands

Privileged commands requiring a valid admin client key.

:::{contents} Admin Commands
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
```
delete everywhere: delete from every device and notify your contacts for deletion
```

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
```
get your current backup key (to store in a safe place to restore your identities)
```

**Request: `BackupKeyGetRequest`**
* *Empty payload.*

**Response: `BackupKeyGetResponse`**
* `backup_key` (string)



### BackupKeyRenew
```
discard previous backup key and create a new one
```

**Request: `BackupKeyRenewRequest`**
* *Empty payload.*

**Response: `BackupKeyRenewResponse`**
* `backup_key` (string)



### BackupGet
```
show backup associated with a backup key.
It contains an admin backup with admin client key and associated storage,
and snapshots for each profile (identity).
```

**Request: `BackupGetRequest`**
* `backup_key` (string)

**Response: `BackupGetResponse`**
* `backup` ({ref}`datatype-backup`)



### BackupNow
```
force to backup now
```

**Request: `BackupNowRequest`**
* *Empty payload.*

**Response: `BackupNowResponse`**
* *Empty payload.*



### BackupRestoreDaemon
```
restore a complete daemon instance, only possible on a blank daemon instance
```

**Request: `BackupRestoreDaemonRequest`**
* `backup_key` (string)
* `new_device_name` (**optional** string - *specify a name for this new daemon*)

**Response: `BackupRestoreDaemonResponse`**
* `restored_identities` (**repeated** {ref}`datatype-identity`)
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)



### BackupRestoreAdminBackup
```
restore a backup admin data (admin client keys and associated storage)
```

**Request: `BackupRestoreAdminBackupRequest`**
* `backup_key` (string)

**Response: `BackupRestoreAdminBackupResponse`**
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)



### BackupRestoreProfileSnapshot
```
restore a specific profile snapshot
```

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
```
create a new api key associated with a given identity
```

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


