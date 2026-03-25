# Admin Commands

Privileged commands requiring a valid admin client key.

:::{contents} Admin Commands
:depth: 1
:local:
:::
(service-identityadminservice)=
## Identity Admin Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-identity`
:::
### IdentityList
:::{card}
> List all identities on this daemon.

**Request**: *IdentityListRequest*
* `filter` (**optional** {ref}`datatype-identityfilter`)

**Response *(Stream)***: *IdentityListResponse*
* `identities` (**repeated** {ref}`datatype-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: invalid filter.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityAdminGet
:::{card}
> Get a specific identity, identified by its id.

**Request**: *IdentityAdminGetRequest*
* `identity_id` (uint64)

**Response**: *IdentityAdminGetResponse*
* `identity` ({ref}`datatype-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityAdminGetBytesIdentifier
:::{card}
> Get identity long term identifier.

**Request**: *IdentityAdminGetBytesIdentifierRequest*
* `identity_id` (uint64)

**Response**: *IdentityAdminGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityAdminGetInvitationLink
:::{card}
> Get identity invitation link.  
> This link allows other identities to send invitations.

**Request**: *IdentityAdminGetInvitationLinkRequest*
* `identity_id` (uint64)

**Response**: *IdentityAdminGetInvitationLinkResponse*
* `invitation_link` (string)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityAdminDownloadPhoto
:::{card}
> Download profile photo of an identity.

**Request**: *IdentityAdminDownloadPhotoRequest*
* `identity_id` (uint64)

**Response**: *IdentityAdminDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityDelete
:::{card}
> Delete an identity on this daemon, identified by its id.

**Request**: *IdentityDeleteRequest*
* `identity_id` (uint64)
* `delete_everywhere` (**optional** bool - *delete from every device and notify your contacts for deletion*)

**Response**: *IdentityDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityNew
:::{card}
> Create a new identity on this daemon.  
> You must specify at least a non blank firstname or lastname in identity_details.  
> You can specify a server_url to create identity on, by default it uses Olvid main distribution server.

**Request**: *IdentityNewRequest*
* `identity_details` ({ref}`datatype-identitydetails`)
* `server_url` (**optional** string)

**Response**: *IdentityNewResponse*
* `identity` ({ref}`datatype-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: one of first name or last name must be non empty.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### IdentityKeycloakNew
:::{card}
> Create a new keycloak managed identity on this daemon.  
> Pass the configuration link you created in the keycloak management console.

**Request**: *IdentityKeycloakNewRequest*
* `configuration_link` (string)

**Response**: *IdentityKeycloakNewResponse*
* `identity` ({ref}`datatype-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-backupadminservice)=
## Backup Admin Service

:::{admonition} Info
Olvid Backups are accessible using a simple key. They contain data necessary to restore or to transfer an identity from a device (a daemon) to another.  
Note: Backups do not contain any messages or attachments; they are only designed to re-create secure channels with your contacts, restore your discussions and your daemon configuration (client keys, settings, ...)


**Associated Datatype:** {ref}`datatype-backup`
:::
### BackupKeyGet
:::{card}
> Get your current backup key.  
> ⚠️ Store it in a safe place, this key allows to restore this daemon identities on another device/daemon.

**Request**: *BackupKeyGetRequest*
* *Empty payload.*

**Response**: *BackupKeyGetResponse*
* `backup_key` (string)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### BackupKeyRenew
:::{card}
> Discard previous backup key and create a new one.

**Request**: *BackupKeyRenewRequest*
* *Empty payload.*

**Response**: *BackupKeyRenewResponse*
* `backup_key` (string)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### BackupGet
:::{card}
> Show the backup associated with a backup key.  
> It contains an admin backup with admin client key and associated storage,  
> and snapshots for each identity.

**Request**: *BackupGetRequest*
* `backup_key` (string)

**Response**: *BackupGetResponse*
* `backup` ({ref}`datatype-backup`)

**Error Codes**:
- `INVALID_ARGUMENT`: cannot access backup.
 - `PERMISSION_DENIED`: an admin client key is necessary.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### BackupNow
:::{card}
> Force a new backup.

**Request**: *BackupNowRequest*
* *Empty payload.*

**Response**: *BackupNowResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### BackupRestoreDaemon
:::{card}
> Restore a complete daemon instance.  
> This is only possible on a blank daemon instance.

**Request**: *BackupRestoreDaemonRequest*
* `backup_key` (string - *key of the backup to restore*)
* `new_device_name` (**optional** string - *specify a name for this new device (*daemon* is set as default)*)

**Response**: *BackupRestoreDaemonResponse*
* `restored_identities` (**repeated** {ref}`datatype-identity`)
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: your daemon database is not empty.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### BackupRestoreAdminBackup
:::{card}
> Restore admin data of a backup (admin client keys and associated storage).

**Request**: *BackupRestoreAdminBackupRequest*
* `backup_key` (string - *key of the backup to restore*)

**Response**: *BackupRestoreAdminBackupResponse*
* `restored_admin_client_keys` (**repeated** {ref}`datatype-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### BackupRestoreProfileSnapshot
:::{card}
> Restore an identity from a backup.  
> Pass the identity snapshot id you want to restore.

**Request**: *BackupRestoreProfileSnapshotRequest*
* `backup_key` (string - *key of the backup to restore*)
* `id` (string - *id of the snapshot to restore*)
* `new_device_name` (**optional** string - *specify a name for this new device (*daemon* is set as default)*)

**Response**: *BackupRestoreProfileSnapshotResponse*
* `restored_identity` ({ref}`datatype-identity`)
* `restored_client_keys` (**repeated** {ref}`datatype-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: snapshot not found.
 - `INVALID_ARGUMENT`: identity already exists locally.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

---

(service-clientkeyadminservice)=
## Client Key Admin Service

:::{admonition} Info

**Associated Datatype:** {ref}`datatype-clientkey`
:::
### ClientKeyList
:::{card}
> List all client keys of this daemon (admin and non admin).  
> This does not return temporary client keys passed in environment or as command line arguments.

**Request**: *ClientKeyListRequest*
* `filter` (**optional** {ref}`datatype-clientkeyfilter`)

**Response *(Stream)***: *ClientKeyListResponse*
* `client_keys` (**repeated** {ref}`datatype-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: filter is invalid.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ClientKeyGet
:::{card}
> Get a specific client key details, identified by its value.  
> This does not return temporary client keys passed in environment or as command line arguments.

**Request**: *ClientKeyGetRequest*
* `client_key` (string)

**Response**: *ClientKeyGetResponse*
* `client_key` ({ref}`datatype-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: client key not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ClientKeyNew
:::{card}
> Create a new client key associated with a given identity.  
> Pass 0 as identity id to create an admin client key.

**Request**: *ClientKeyNewRequest*
* `name` (string)
* `identity_id` (uint64)

**Response**: *ClientKeyNewResponse*
* `client_key` ({ref}`datatype-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
:::

### ClientKeyDelete
:::{card}
> Delete a specific client key, identified by its value.

**Request**: *ClientKeyDeleteRequest*
* `client_key` (string)

**Response**: *ClientKeyDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: client key not found.
 - `UNAUTHENTICATED`: client key is invalid.
:::
