# Details for Vault, Key Management, and Secret Management Service
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm
- Fetched: 2026-09-05 02:26 CDT

# Details for Vault, Key Management, and Secret Management Service

This topic covers details for writing policies to control access to vaults, keys, and secrets.

## Individual Resource-Types

`vaults`

`keys`

`key-delegate`

`hsm-cluster`

`secrets`

`secret-versions`

`secret-bundles`

## Aggregate Resource-Type

`secret-family`

A policy that uses`<verb> secret-family`is equivalent to writing one with a separate`<verb> <individual resource-type>`statement for each of the individual secret resource-types. (Secret resource-types include only`secrets`,`secret-versions`, and`secret-bundles`.

See the table in[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#Details)for details of the API operations covered by each verb, for each individual resource-type included in`secret-family`.

## Supported Variables

Vault supports all the general variables, plus the ones listed here. For more information about general variables supported by Oracle Cloud Infrastructure services, see[General Variables](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm).

Variable Variable Type Comments
`request.includePlainTextKey`String Use this variable to control whether to return the plaintext key, in addition to the encrypted key, in response to a request to generate a data encryption key.
`request.kms-key.id`String Use this variable to control whether block volumes or buckets can be created without a Vault master encryption key.
`target.boot-volume.kms-key.id`String Use this variable to control whether Compute instances can be launched with boot volumes that were created without a Vault master encryption key.
`target.key.id`Entity (OCID) Use this variable to control access to specific keys by OCID.
`target.vault.id`Entity (OCID) Use this variable to control access to specific vaults by OCID.
`target.secret.name`String Use this variable to control access to specific secrets, secret versions, and secret bundles by name.
`target.secret.id`Entity (OCID) Use this variable to control access to specific secrets, secret versions, and secret bundles by OCID.

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

For example, the`use`verb for the`keys`resource-type includes the same permissions and API operations as the`read`verb, plus the KEY_ENCRYPT and KEY_DECRYPT permissions and a number of API operations (`Encrypt`,`Decrypt`, and`GenerateDataEncryptionKey`). The`manage`verb allows even more permissions and API operations when compared to the`use`verb.

[vaults](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

VAULT_INSPECT`ListVaults`

none
read

INSPECT +

VAULT_READ

INSPECT +

`GetVault`

`GetVaultUsage`

none
use

READ +

VAULT_CREATE_KEY

VAULT_IMPORT_KEY

VAULT_CREATE_SECRET

no extra

`CreateKey`(also needs`manage keys`)

`ImportKey`(also needs`manage keys`)

`CreateSecret`(also needs`manage secrets`)
manage

USE +

VAULT_CREATE

VAULT_UPDATE

VAULT_DELETE

VAULT_MOVE

VAULT_BACKUP

VAULT_RESTORE

VAULT_REPLICATE

USE +

`CreateVault`

`UpdateVault`

`ScheduleVaultDeletion`

`CancelVaultDeletion`

`ChangeVaultCompartment`

`BackupVault`

`RestoreVaultFromFile`

`RestoreVaultFromObjectStore`

`CreateVaultReplica`

`DeleteVaultReplica`

none

[keys](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

KEY_INSPECT

`ListKeys`

`ListKeyVersions`

none
read

INSPECT +

KEY_READ

INSPECT +

`GetKey`

`GetKeyVersion`

none
use

READ +

KEY_ENCRYPT

KEY_DECRYPT

KEY_EXPORT

KEY_SIGN

KEY_VERIFY

READ +

`Encrypt`

`Decrypt`

`ExportKey`

`Sign`

`Verify`

none
manage

USE +

KEY_CREATE

KEY_UPDATE

KEY_ROTATE

KEY_DELETE

KEY_MOVE

KEY_IMPORT

KEY_BACKUP

KEY_RESTORE

USE +

`UpdateKey`

`CreateKeyVersion`

`CancelKeyDeletion`

`ChangeKeyCompartment`

`ImportKeyVersion`

`BackupKey`

`RestoreKeyFromFile`

`RestoreKeyFromObjectStore`

`CreateKey`(also needs`use vaults`)

`ImportKey`(also needs`use vaults`)

[key-delegate](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Note  
  

key-delegate permissions are used to allow integrated OCI services to use a specific key in a specific compartment. For example, you can use this permission type to enable the Object Storage service to create or update an encrypted bucket, and to let the service encrypt or decrypt data in the bucket. Users granted delegate permissions don't have permission to use the specified key itself, but rather have permission to let specified services use the key. See the following common policies for details:
- [Let a user group delegate key usage in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../Concepts/commonpolicies.htm#os-bv-admins-use-key-id)
- [Let a dynamic group delegate key usage in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../Concepts/commonpolicies.htm#bvdelegatekey)
- [Let Block Volume, Object Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, Kubernetes secrets, and stream pools](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../Concepts/commonpolicies.htm#services-use-key)

Verbs Permissions APIs Fully Covered APIs Partially Covered
use

KEY_ASSOCIATE

KEY_DISASSOCIATE

`Encrypt`

`GenerateDataEncryptionKey`

`Decrypt`

none

[hsm-cluster](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Verbs Permissions API Fully Covered API Partially Covered
Inspect

HSM_CLUSTER_INSPECT

ListHsmClusters

ListHsmPartitions

None

read

INSPECT +

HSM_CLUSTER_READ

GetHsmCluster

GetHsmPartition

None

use

READ +

HSM_CLUSTER_UPDATE

GetPreCoUserCredentials

DownloadCertificateSigningRequest

UpdateHsmCluster

UploadPartitionCertificates

None

manage

USE +

HSM_CLUSTER_DELETE

HSM_CLUSTER_CREATE

HSM_CLUSTER_MOVE

CreateHsmCluster

ChangeHsmClusterCompartment

ScheduleHsmClusterDeletion

CancelHsmClusterDeletion

None

[secrets](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

SECRET_INSPECT`ListSecrets`

none
read

INSPECT +

SECRET_READ

INSPECT +

`GetSecret`

none
use

READ +

SECRET_UPDATE

SECRET_ROTATE

READ +

`CancelRotation`

READ +

`UpdateSecret`(for cross-region secret replication feature only, also needs`manage secrets`or the`SECRET_REPLICATE_CONFIGURE`permission)

`ChangeSecretCompartment`(also needs`manage secrets)`

`ScheduleSecretVersionDeletion`(also needs`manage secret-versions`)

`CancelSecretVersionDeletion`(also needs`manage secret-versions`)
manage

USE +

SECRET_CREATE

SECRET_DELETE

SECRET_MOVE

SECRET_ROTATE

SECRET_REPLICATE_CONFIGURE

USE +

`ScheduleSecretDeletion`

`CancelSecretDeletion`

`RotateSecret`

USE +

`CreateSecret`(also needs`use vaults`)

`ChangeSecretCompartment`(also needs`use secrets`)

[secret-versions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

SECRET_VERSION_INSPECT`ListSecretVersions`

none
read

INSPECT +

SECRET_VERSION_READ

INSPECT +

`GetKeyVersion`

none
manage

READ +

SECRET_VERSION_DELETE

no extra

`ScheduleSecretVersionDeletion`(also needs`use secrets`)

`CancelSecretVersionDeletion`(also needs`use secrets`)

[secret-bundles](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

SECRET_BUNDLE_INSPECT`ListSecretBundles`

none
read

INSPECT +

SECRET_BUNDLE_READ

INSPECT +

`GetSecretBundle`

none

## Permissions Required for Each API Operation

Permission for Vault API operations.

The following table lists the API operations in a logical order, grouped by resource type.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/../policies/permissions.htm).

API Operation Permissions Required to Use the Operation
`ListVaults`VAULT_INSPECT
`GetVault`VAULT_READ
`CreateVault`VAULT_CREATE
`UpdateVault`VAULT_UPDATE
`ScheduleVaultDeletion`VAULT_DELETE
`CancelVaultDeletion`VAULT_DELETE
`ChangeVaultCompartment`VAULT_MOVE
`BackupVault`VAULT_BACKUP
`RestoreVaultFromFile`VAULT_RESTORE
`RestoreVaultFromObjectStore`VAULT_RESTORE
`ListVaultReplicas`VAULT_INSPECT
`CreateVaultReplica`VAULT_REPLICATE
`DeleteVaultReplica`VAULT_REPLICATE
`GetVaultUsage`VAULT_READ
`ListKeys`KEY_INSPECT
`ListKeyVersions`KEY_INSPECT
`GetKey`KEY_READ
`CreateKey`KEY_CREATE and VAULT_CREATE_KEY
`EnableKey`KEY_UPDATE
`DisableKey`KEY_UPDATE
`UpdateKey`KEY_UPDATE
`ScheduleKeyDeletion`KEY_DELETE
`CancelKeyDeletion`KEY_DELETE
`ChangeKeyCompartment`KEY_MOVE
`BackupKey`KEY_BACKUP
`RestoreKeyFromFile`KEY_RESTORE
`RestoreKeyFromObjectStore`KEY_RESTORE
`GetKeyVersion`KEY_READ
`CreateKeyVersion`KEY_ROTATE
`ImportKey`KEY_IMPORT and VAULT_IMPORT_KEY
`ImportKeyVersion`KEY_IMPORT
`ExportKey`KEY_EXPORT
`GenerateDataEncryptionKey`KEY_ENCRYPT (Use KEY_ASSOCIATE when[delegating permission](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#keydelegate)to an integrated service)
`Encrypt`KEY_ENCRYPT (Use KEY_ASSOCIATE when[delegating permission](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#keydelegate)to an integrated service)
`Decrypt`KEY_DECRYPT (Use KEY_ASSOCIATE when[delegating permission](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/keypolicyreference.htm#keydelegate)to an integrated service)
`Sign`KEY_SIGN
`Verify`KEY_VERIFY
`CreateSecret`KEY_ENCRYPT, KEY_DECRYPT, SECRET_CREATE , and VAULT_CREATE_SECRET (add SECRET_REPLICATE_CONFIGURE to allow configuration of cross-region replication in the region of the source secret)
`UpdateSecret`SECRET_UPDATE (add SECRET_REPLICATE_CONFIGURE to allow configuration of cross-region replication in the region of the source secret)
`ListSecrets`SECRET_INSPECT
`GetSecret`SECRET_READ
`RotateSecret`SECRET_ROTATE
`ScheduleSecretDeletion`SECRET_DELETE
`ChangeSecretCompartment`SECRET_MOVE and SECRET_UPDATE
`ListSecretVersions`SECRET_VERSION_INSPECT
`GetSecretVersion`SECRET_VERSION_READ
`ScheduleSecretVersionDeletion`SECRET_VERSION_DELETE and SECRET_UPDATE
`CancelSecretVersionDeletion`SECRET_VERSION_DELETE and SECRET_UPDATE
`ListSecretBundles`SECRET_BUNDLE_INSPECT
`GetSecretBundle`SECRET_BUNDLE_READ
`GetSecretBundleByName`SECRET_BUNDLE_READ
`ScheduleSecretVersionDeletion`SECRET_VERSION_DELETE and SECRET_UPDATE
`CancelSecretVersionDeletion`SECRET_VERSION_DELETE and SECRET_UPDATE
`ListSecretBundles`SECRET_BUNDLE_INSPECT
`GetSecretBundle`SECRET_BUNDLE_READ
`GetSecretBundleByName`SECRET_BUNDLE_READ
`CreateHsmCluster`HSM_CLUSTER_CREATE
`GetHsmCluster`HSM_CLUSTER_READ
`GetHsmPartition`HSM_CLUSTER_READ
`GetPreCoUserCredentials`HSM_CLUSTER_UPDATE
`DownloadCertificateSigningRequest`HSM_CLUSTER_UPDATE
`UpdateHsmCluster`HSM_CLUSTER_UPDATE
`ChangeHsmClusterCompartment`HSM_CLUSTER_MOVE
`UploadPartitionOwnerCertificate`HSM_CLUSTER_UPDATE
`ScheduleHsmClusterDeletion`HSM_CLUSTER_DELETE
`CancelDeletion`HSM_CLUSTER_DELETE
`ListHsmClusters`HSM_CLUSTER_INSPECT
`ListHsmPartitions`
