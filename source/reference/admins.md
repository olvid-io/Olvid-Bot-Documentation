# Admin Commands

List all privileged commands an admin can execute to manage the daemon. Those commands require a valid admin client key.

:::{contents} Admin Commands
:depth: 1
:local:
:::
(service-identityadminservice)=
## Identity Admin Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-identity`
:::
(rpc-identitylist)=
### IdentityList
::::::{card}
> List all identities on this daemon.

(message-identitylistrequest)=
**Request**: *IdentityListRequest*
* `filter` (**optional** {ref}`message-identityfilter`)

(message-identitylistresponse)=
**Response *(Stream)***: *IdentityListResponse*
* `identities` (**repeated** {ref}`message-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: invalid filter.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identityadminget)=
### IdentityAdminGet
::::::{card}
> Get a specific identity, identified by its id.

(message-identityadmingetrequest)=
**Request**: *IdentityAdminGetRequest*
* `identity_id` (uint64)

(message-identityadmingetresponse)=
**Response**: *IdentityAdminGetResponse*
* `identity` ({ref}`message-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identityadmingetbytesidentifier)=
### IdentityAdminGetBytesIdentifier
::::::{card}
> Get identity long term identifier.

(message-identityadmingetbytesidentifierrequest)=
**Request**: *IdentityAdminGetBytesIdentifierRequest*
* `identity_id` (uint64)

(message-identityadmingetbytesidentifierresponse)=
**Response**: *IdentityAdminGetBytesIdentifierResponse*
* `identifier` (bytes)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identityadmingetinvitationlink)=
### IdentityAdminGetInvitationLink
::::::{card}
> Get identity invitation link.  
> This link allows other identities to send invitations.

(message-identityadmingetinvitationlinkrequest)=
**Request**: *IdentityAdminGetInvitationLinkRequest*
* `identity_id` (uint64)

(message-identityadmingetinvitationlinkresponse)=
**Response**: *IdentityAdminGetInvitationLinkResponse*
* `invitation_link` (string)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identityadmindownloadphoto)=
### IdentityAdminDownloadPhoto
::::::{card}
> Download profile photo of an identity.

(message-identityadmindownloadphotorequest)=
**Request**: *IdentityAdminDownloadPhotoRequest*
* `identity_id` (uint64)

(message-identityadmindownloadphotoresponse)=
**Response**: *IdentityAdminDownloadPhotoResponse*
* `photo` (bytes)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identitydelete)=
### IdentityDelete
::::::{card}
> Delete an identity on this daemon, identified by its id.

(message-identitydeleterequest)=
**Request**: *IdentityDeleteRequest*
* `identity_id` (uint64)
* `delete_everywhere` (**optional** bool - *delete from every device and notify your contacts for deletion*)

(message-identitydeleteresponse)=
**Response**: *IdentityDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identitynew)=
### IdentityNew
::::::{card}
> Create a new identity on this daemon.  
> You must specify at least a non blank firstname or lastname in identity_details.  
> You can specify a server_url to create identity on, by default it uses Olvid main distribution server.

(message-identitynewrequest)=
**Request**: *IdentityNewRequest*
* `identity_details` ({ref}`message-identitydetails`)
* `server_url` (**optional** string)

(message-identitynewresponse)=
**Response**: *IdentityNewResponse*
* `identity` ({ref}`message-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: one of first name or last name must be non empty.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-identitykeycloaknew)=
### IdentityKeycloakNew
::::::{card}
> Create a new keycloak managed identity on this daemon.  
> Pass the configuration link you created in the keycloak management console.

(message-identitykeycloaknewrequest)=
**Request**: *IdentityKeycloakNewRequest*
* `configuration_link` (string)

(message-identitykeycloaknewresponse)=
**Response**: *IdentityKeycloakNewResponse*
* `identity` ({ref}`message-identity`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-backupadminservice)=
## Backup Admin Service

:::{admonition} Info
Olvid Backups are accessible using a simple key. They contain data necessary to restore or to transfer an identity from a device (a daemon) to another.  
Note: Backups do not contain any messages or attachments; they are only designed to re-create secure channels with your contacts, restore your discussions and your daemon configuration (client keys, settings, ...)


**Associated Datatype:** {ref}`file-backup`
:::
(rpc-backupkeyget)=
### BackupKeyGet
::::::{card}
> Get your current backup key.  
> ⚠️ Store it in a safe place, this key allows to restore this daemon identities on another device/daemon.

(message-backupkeygetrequest)=
**Request**: *BackupKeyGetRequest*
* *Empty payload.*

(message-backupkeygetresponse)=
**Response**: *BackupKeyGetResponse*
* `backup_key` (string)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-backupkeyrenew)=
### BackupKeyRenew
::::::{card}
> Discard previous backup key and create a new one.

(message-backupkeyrenewrequest)=
**Request**: *BackupKeyRenewRequest*
* *Empty payload.*

(message-backupkeyrenewresponse)=
**Response**: *BackupKeyRenewResponse*
* `backup_key` (string)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-backupget)=
### BackupGet
::::::{card}
> Show the backup associated with a backup key.  
> It contains an admin backup with admin client key and associated storage,  
> and snapshots for each identity.

(message-backupgetrequest)=
**Request**: *BackupGetRequest*
* `backup_key` (string)

(message-backupgetresponse)=
**Response**: *BackupGetResponse*
* `backup` ({ref}`message-backup`)

**Error Codes**:
- `INVALID_ARGUMENT`: cannot access backup.
 - `PERMISSION_DENIED`: an admin client key is necessary.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-backupnow)=
### BackupNow
::::::{card}
> Force a new backup.

(message-backupnowrequest)=
**Request**: *BackupNowRequest*
* *Empty payload.*

(message-backupnowresponse)=
**Response**: *BackupNowResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-backuprestoredaemon)=
### BackupRestoreDaemon
::::::{card}
> Restore a complete daemon instance.  
> This is only possible on a blank daemon instance.

(message-backuprestoredaemonrequest)=
**Request**: *BackupRestoreDaemonRequest*
* `backup_key` (string - *key of the backup to restore*)
* `new_device_name` (**optional** string - *specify a name for this new device (*daemon* is set as default)*)

(message-backuprestoredaemonresponse)=
**Response**: *BackupRestoreDaemonResponse*
* `restored_identities` (**repeated** {ref}`message-identity`)
* `restored_admin_client_keys` (**repeated** {ref}`message-clientkey`)
* `restored_client_keys` (**repeated** {ref}`message-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: your daemon database is not empty.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-backuprestoreadminbackup)=
### BackupRestoreAdminBackup
::::::{card}
> Restore admin data of a backup (admin client keys and associated storage).

(message-backuprestoreadminbackuprequest)=
**Request**: *BackupRestoreAdminBackupRequest*
* `backup_key` (string - *key of the backup to restore*)

(message-backuprestoreadminbackupresponse)=
**Response**: *BackupRestoreAdminBackupResponse*
* `restored_admin_client_keys` (**repeated** {ref}`message-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-backuprestoreprofilesnapshot)=
### BackupRestoreProfileSnapshot
::::::{card}
> Restore an identity from a backup.  
> Pass the identity snapshot id you want to restore.

(message-backuprestoreprofilesnapshotrequest)=
**Request**: *BackupRestoreProfileSnapshotRequest*
* `backup_key` (string - *key of the backup to restore*)
* `id` (string - *id of the snapshot to restore*)
* `new_device_name` (**optional** string - *specify a name for this new device (*daemon* is set as default)*)

(message-backuprestoreprofilesnapshotresponse)=
**Response**: *BackupRestoreProfileSnapshotResponse*
* `restored_identity` ({ref}`message-identity`)
* `restored_client_keys` (**repeated** {ref}`message-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: snapshot not found.
 - `INVALID_ARGUMENT`: identity already exists locally.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

---

(service-clientkeyadminservice)=
## Client Key Admin Service

:::{admonition} Info

**Associated Datatype:** {ref}`file-identity`
:::
(rpc-clientkeylist)=
### ClientKeyList
::::::{card}
> List all client keys of this daemon (admin and non admin).  
> This does not return temporary client keys passed in environment or as command line arguments.

(message-clientkeylistrequest)=
**Request**: *ClientKeyListRequest*
* `filter` (**optional** {ref}`message-clientkeyfilter`)

(message-clientkeylistresponse)=
**Response *(Stream)***: *ClientKeyListResponse*
* `client_keys` (**repeated** {ref}`message-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `INVALID_ARGUMENT`: filter is invalid.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-clientkeyget)=
### ClientKeyGet
::::::{card}
> Get a specific client key details, identified by its value.  
> This does not return temporary client keys passed in environment or as command line arguments.

(message-clientkeygetrequest)=
**Request**: *ClientKeyGetRequest*
* `client_key` (string)

(message-clientkeygetresponse)=
**Response**: *ClientKeyGetResponse*
* `client_key` ({ref}`message-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: client key not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-clientkeynew)=
### ClientKeyNew
::::::{card}
> Create a new client key associated with a given identity.  
> Pass 0 as identity id to create an admin client key.

(message-clientkeynewrequest)=
**Request**: *ClientKeyNewRequest*
* `name` (string)
* `identity_id` (uint64)

(message-clientkeynewresponse)=
**Response**: *ClientKeyNewResponse*
* `client_key` ({ref}`message-clientkey`)

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: identity not found.
 - `INTERNAL`
 - `UNAUTHENTICATED`: client key is invalid.
::::::

(rpc-clientkeydelete)=
### ClientKeyDelete
::::::{card}
> Delete a specific client key, identified by its value.

(message-clientkeydeleterequest)=
**Request**: *ClientKeyDeleteRequest*
* `client_key` (string)

(message-clientkeydeleteresponse)=
**Response**: *ClientKeyDeleteResponse*
* *Empty payload.*

**Error Codes**:
- `PERMISSION_DENIED`: an admin client key is necessary.
 - `NOT_FOUND`: client key not found.
 - `UNAUTHENTICATED`: client key is invalid.
::::::
