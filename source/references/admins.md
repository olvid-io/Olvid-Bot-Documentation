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
:::{card}
```text
List all identities on this daemon.
```

**Request: `IdentityListRequest`**
* `filter` (**optional** {ref}`datatype-identityfilter`)

**Response *(Stream)*: `IdentityListResponse`**
* `identities` (**repeated** {ref}`datatype-identity`)

:::

### IdentityAdminGet
:::{card}
```text
Get a specific identity, identified by it's id.
```

**Request: `IdentityAdminGetRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminGetResponse`**
* `identity` ({ref}`datatype-identity`)

:::

### IdentityAdminGetBytesIdentifier
:::{card}
```text
Get identity long term identifier.
```

**Request: `IdentityAdminGetBytesIdentifierRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminGetBytesIdentifierResponse`**
* `identifier` (bytes)

:::

### IdentityAdminGetInvitationLink
:::{card}
```text
Get identity invitation link.
This link allows other identities to send invitations.
```

**Request: `IdentityAdminGetInvitationLinkRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminGetInvitationLinkResponse`**
* `invitation_link` (string)

:::

### IdentityAdminDownloadPhoto
:::{card}
```text
Download profile photo of an identity.
```

**Request: `IdentityAdminDownloadPhotoRequest`**
* `identity_id` (uint64)

**Response: `IdentityAdminDownloadPhotoResponse`**
* `photo` (bytes)

:::

### IdentityDelete
:::{card}
```text
Delete an identity on this daemon, identified by it's id.
```

**Request: `IdentityDeleteRequest`**
* `identity_id` (uint64)
* `delete_everywhere` (**optional** bool - *delete from every device and notify your contacts for deletion*)

**Response: `IdentityDeleteResponse`**
* *Empty payload.*

:::

### IdentityNew
:::{card}
```text
Create a new identity on this daemon.
You must specify at least a non blank firstname or lastname in identity_details.
You can specify a server_url to create identity on, by default it use Olvid main distribution server.
```

**Request: `IdentityNewRequest`**
* `identity_details` ({ref}`datatype-identitydetails`)
* `server_url` (**optional** string)

**Response: `IdentityNewResponse`**
* `identity` ({ref}`datatype-identity`)

:::

### IdentityKeycloakNew
:::{card}
```text
Create a new keycloak managed identity on this daemon.
Pass the configuration link you created in the keycloak management console.
```

**Request: `IdentityKeycloakNewRequest`**
* `configuration_link` (string)

**Response: `IdentityKeycloakNewResponse`**
* `identity` ({ref}`datatype-identity`)

:::

---

(service-backupadminservice)=
## BackupAdminService

> **Associated Datatype:** {ref}`datatype-backup`

### BackupKeyGet
:::{card}
```text
Get your current backup key
⚠️ Store it in a safe place.
This key allows to restore this daemon identities on another device/daemon.
```

**Request: `BackupKeyGetRequest`**
* *Empty payload.*

**Response: `BackupKeyGetResponse`**
* `backup_key` (string)

:::

### BackupKeyRenew
:::{card}
```text
Discard previous backup key and create a new one.
```

**Request: `BackupKeyRenewRequest`**
* *Empty payload.*

**Response: `BackupKeyRenewResponse`**
* `backup_key` (string)

:::

### BackupGet
:::{card}
```text
Show the backup associated with a backup key.
It contains an admin backup with admin client key and associated storage,
and snapshots for each identity.
```

**Request: `BackupGetRequest`**
* `backup_key` (string)

**Response: `BackupGetResponse`**
* `backup` ({ref}`datatype-backup`)

:::

### BackupNow
:::{card}
```text
Force to backup now
```

**Request: `BackupNowRequest`**
* *Empty payload.*

**Response: `BackupNowResponse`**
* *Empty payload.*

:::

### BackupRestoreDaemon
:::{card}
```text
Restore a complete daemon instance. This is only possible on a blank daemon instance.
```

**Request: `BackupRestoreDaemonRequest`**
* `backup_key` (string)
* `new_device_name` (**optional** string - *specify a name for this new daemon*)

**Response: `BackupRestoreDaemonResponse`**
* `restored_identities` (**repeated** {ref}`datatype-identity`)
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)

:::

### BackupRestoreAdminBackup
:::{card}
```text
Restore admin data of a backup (admin client keys and associated storage)
```

**Request: `BackupRestoreAdminBackupRequest`**
* `backup_key` (string)

**Response: `BackupRestoreAdminBackupResponse`**
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)

:::

### BackupRestoreProfileSnapshot
:::{card}
```text
Restore a identity from a backup.
Pass the identity snapshot id you want to restore.
```

**Request: `BackupRestoreProfileSnapshotRequest`**
* `backup_key` (string)
* `id` (string)
* `new_device_name` (**optional** string - *specify a name for this new daemon*)

**Response: `BackupRestoreProfileSnapshotResponse`**
* `restored_identity` ({ref}`datatype-identity`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)

:::

---

(service-clientkeyadminservice)=
## ClientKeyAdminService

> **Associated Datatype:** {ref}`datatype-clientkey`

### ClientKeyList
:::{card}
```text
List all client keys of this daemon.
This does not return temporary client keys passed in environment or as command line arguments.
```

**Request: `ClientKeyListRequest`**
* `filter` (**optional** {ref}`datatype-clientkeyfilter`)

**Response *(Stream)*: `ClientKeyListResponse`**
* `client_keys` (**repeated** {ref}`datatype-clientkey`)

:::

### ClientKeyGet
:::{card}
```text
Get a specific client key details, identified by it's value.
```

**Request: `ClientKeyGetRequest`**
* `client_key` (string)

**Response: `ClientKeyGetResponse`**
* `client_key` ({ref}`datatype-clientkey`)

:::

### ClientKeyNew
:::{card}
```text
Create a new api key associated with a given identity
Pass 0 as identity id to create and admin api key.
```

**Request: `ClientKeyNewRequest`**
* `name` (string)
* `identity_id` (uint64)

**Response: `ClientKeyNewResponse`**
* `client_key` ({ref}`datatype-clientkey`)

:::

### ClientKeyDelete
:::{card}
```text
Delete a specific client key, identified by it's value.
```

**Request: `ClientKeyDeleteRequest`**
* `client_key` (string)

**Response: `ClientKeyDeleteResponse`**
* *Empty payload.*

:::
