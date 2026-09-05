# Backing Up and Restoring Vaults and Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm
- Fetched: 2026-09-05 02:31 CDT

# Backing Up and Restoring Vaults and Keys

Learn about backing up and restoring virtual private vaults and master encryption keys in a Hardware Security Module (HSM).

You can create backups of virtual private vaults and master encryption keys in an Object Storage bucket, or back them up in storage outside of OCI.

The only type of vault you can back up is a virtual private vault. Similarly, the only type of encryption key that you can back up is a master encryption key protected by a hardware security module (HSM). You can't back up master encryption keys protected by software. You also can't back up secrets.

You might want to back up a vault or encryption key before deleting either if you don't need them now, but think you might need to use the key for decryption later. Deleting a vault and key otherwise means losing the ability to decrypt any resource or data that the key was used to encrypt. Restoring a key from a backup lets you resume using a resource that was encrypted by the key if the original key material was deleted.

You might also create a backup of a vault to use in a disaster recovery scenario. You can restore a backup in any region within the realm you use, making it possible to access encrypted resources even in disaster recovery scenarios where the region of the backed-up resource is no longer available.
Note  
  
By default, a key backup includes metadata about the key's vault. A vault backup might optionally include key metadata, but will not include metadata about secrets because you can't back up secrets, whether independently or as part of a vault backup.

The following topics provide instructions for vault backup operations:
- [Backing up a vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_vault.htm)
- [Backing up a vault key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_key.htm)
- [Restoring vault from a backup](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_vault.htm)
- [Restoring a key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_key.htm)

For information about creating and managing keys, see[Managing Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys.htm). For information about managing vaults see[Managing Vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults.htm). For information about creating and managing secrets in the Secret Management Service, see[Managing Secrets](https://docs.oracle.com/iaas/Content/secret-management/Concepts/manage-secrets.htm).

## How It Works

Keys are always associated with the vault where you created them. This relationship persists even as the key is backed up and restored. As a result, restoring a key always requires you to already have the vault associated with the key. You also need the vault because the vault hosts the management and cryptographic endpoints against which you manage and use the key. This might mean that you need to first restore the vault, and then restore the key, if both were backed up and subsequently deleted.

You back up a vault or key by exporting identifying information about the vault or key and what it contains. (The service encrypts the backups, and only the service can restore them.) Vault backups can optionally include keys, assuming the vault has keys and the keys are in a supported lifecycle state when you perform the backup. You can only back up active, enabled, or disabled keys. Backups exclude keys that are deleted or in a transitional state (for example, "Creating" or "Pending Deletion"). Key backups always include vault metadata, in addition to key metadata. Having vault metadata makes it possible to restore the key at all. You can only back up active vaults.

You can back up only one vault or one key at a time. (The exception is when you backup keys as part of a vault backup.) When you perform a key backup, the file includes all associated key versions in an enabled state. Backups exclude key versions in a deleted or pending deletion state.

Backup operations require you to specify where to download the backup. Downloads can be stored in a new or existing Object Storage bucket or a temporary URL that's created specifically for pre-authenticated requests. For more information about pre-authenticated requests, see[Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm). Backups must be stored in buckets in the same region, but you can copy the backup to a different region by using Object Storage.

Backup and restore operations generate work requests to help you track their progress.

You restore a vault or key by importing the backup from storage to where you want it, as long as you restore the vault to the same tenancy and compartment where you originally created the backup. The key also can only be restored to its original tenancy and compartment, which might be a different compartment from the vault. You can, however, restore vaults and keys to a different region if your tenancy spans multiple regions.

You can restore a vault or a key individually. If you included keys in a vault backup, then restoring the vault restores all the keys included in the backup. Restoring a key restores all the key versions included in the backup.

You can restore a vault or key even when the vault or key already exists in the region. Also, at any time, you can take a newer backup of a vault or key if you want to capture changes to the vault, such as a new name or tags, or the keys, such as new key versions. Updating an already restored vault or key reflects those changes. Updates from a backup are always additive. This means that updates can only append new information. For example, any new key versions created in a reference vault are added to its restored key when you update the restored key. But, if you delete a key from a reference vault, and then you update a restored vault from a backup of the reference vault, the update does not result in a corresponding key deletion in the restored vault. Similarly, any keys that you create for a restored vault are independent of any keys associated with the reference vault that you created the backup from. You manage them independently, too.

Most other operations are not allowed while a backup or restore operation is in progress. This prevents you from deleting a key while it's being backed up, for example. Prohibited operations include attempts to perform simultaneous backup or restore operations on the same resource.

To make it easier to reuse any policies that you created to allow management and use of vaults and keys, when you restore a vault and key, they maintain the same unique Oracle Cloud Identifier (OCID) if they're restored to the region where they were originally backed up. When you restore a vault or key to a different region, you must review and update policies to correspond to new OCIDs.

When you restore a vault or key, especially a key with a lot of key versions, tenancy service limits do apply.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: for typical policies that give access to vaults, keys, and secrets, see[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#sec-admins-manage-vaults-keys). For more information about permissions or if you need to write more restrictive policies, see[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

Depending on where you want to store backups and retrieve them from, you might also need access to an Object Storage bucket. For administrators: for typical policies that gives access to buckets, see[Let users write objects to Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm#write-objects-to-buckets)and[Let users download objects from Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm#download-objects-from-buckets).

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm)
