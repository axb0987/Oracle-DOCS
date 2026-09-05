# Changing the Assigned Master Encryption Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm
- Fetched: 2026-09-05 01:45 CDT

# Changing the Assigned Master Encryption Key

Change the assigned key for a Block Volume resource, such as a volume or volume backup. You can assign a customer-managed key or an Oracle-managed key. When you change the key, the data key is re-encrypted. (The content of the resource isn't re-encrypted for a key change.)

See also[Update a Key to a Block Volume](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm).

## Requirements

- [Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr)
- [Cross-Region Backup Copies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#xrr-backup)

### Customer-Managed Encryption Keys for Cross-Region Operations

Vault encryption keys for volumes aren't copied to the destination region for scheduled volume and volume group backups enabled for cross-region copy. Instead, you can specify a Vault encryption key for the backup copied to the destination region when you assign the backup policy. When you assign the backup policy, if it's enabled for cross region backup copies, select Encrypt using customer-managed keys for Cross region backup copy encryption to encrypt the volume or volume group backup in the destination region. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see for more information.

When you specify a customer-managed encryption key for cross-region operations, ensure the following:
- The OCID is a valid OCID for the encryption key, in a format similar to the following:
```

```

- The OCID is for an encryption key that exists in the destination region for the cross-region operation.
- You have the required permissions configured in the destination region to use encryption keys with Block Volume. For more information, see the following:
- [Assigning Master Encryption Keys - Required IAM Policy](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys.htm#permissions)
- [Create a policy to enable encryption keys](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key)
- [Let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id)

If you don't specify a customer-managed encryption key for cross-region operations, an Oracle-managed encryption is used by default. These requirements don't apply to Oracle-managed encryption keys.

### Cross-Region Backup Copies

When you[manually copy a volume backup between regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm)you can use the Oracle-managed key or your own encryption key. When you assign a backup policy with[cross-region backup copies enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy)to a volume or volume group, or[perform a manual backup cross region copy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-backup.htm), you can optionally select Encrypt using customer-managed keys for Cross region backup copy encryption to encrypt the volume backup in the destination region. If you select this option, you must specify the OCID for a valid encryption key in the destination region.

See also[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#)
- 

- Find the resource that you want to work with.
For example, for a block volume backup, go to the Block Volume Backups list page. If you need help finding the list page or the block volume backups, see[Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-backup.htm).
- From the Actions menu (three dots) for the resource, select Assign master encryption key .
This option is available for volumes and volume backups.
The Assign master encryption key panel opens.
- Select the vault compartment, vault, key compartment, and key.
- When you're finished, select Assign or Update , as appropriate.
- 

Use the relevant resource-specific command and required parameters to assign a master encryption key.

For example, for a block volume backup, use[oci bv backup update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/update.html).
- Example 1: Customer-managed key:

```

```

- Example 2: Oracle-managed key (empty string for the key ID):

```

```

For a volume, use[oci bv volume-kms-key update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-kms-key/update.html).

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the relevant resource-specific operation to assign a master encryption key.

For example, for a block volume backup, run the[UpdateVolumeBackup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/UpdateVolumeBackup)operation and specify the encryption key OCID in the`kmsKeyId`attribute.

For a volume, run the[UpdateVolumeKmsKey](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeKmsKey/UpdateVolumeKmsKey)operation and specify the encryption key OCID in the`kmsKeyId`
