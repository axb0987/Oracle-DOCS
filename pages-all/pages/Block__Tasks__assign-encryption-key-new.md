# Assigning a New Master Encryption Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm
- Fetched: 2026-09-05 01:45 CDT

# Assigning a New Master Encryption Key

Assign a new key to a Block Volume resource, such as when restoring a backup, cloning a volume, activating a replica, or enabling replication. You can assign a customer-managed key or an Oracle-managed key.

## Requirements

- [Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm#cust-key-xrr)
- [Cross-Region Backup Copies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm#xrr-backup)

### Customer-Managed Encryption Keys for Cross-Region Operations

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

See also[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm#cust-key-xrr).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key-new.htm#)
- 

- [Restoring a backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm),[cloning a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm), or[activating a replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume.htm#console):

Under Encryption , select Encrypt using customer-managed keys , and then select the Vault encryption key you want to use.
- Enabling replication: You can optionally specify your own key to encrypt the volume replica in the destination region. The customer-managed key can be one of the following types of key:
- A replicated key that exists in the destination region
- Any key in the target region that you own and is different than the one in the source region

You can encrypt the volume replica with a customer-managed encryption key in the destination region when you enable replication for a volume or volume group.

Select Encrypt using customer-managed keys for Cross region replication encryption , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume or volume group to.

If you don't specify a customer-managed key, an Oracle-managed encryption key is used instead.
- 

- [Restoring a backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm),[cloning a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm), or[activating a replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume.htm#console):

Use the relevant[Block Volume CLI command](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv.html). Include the`--kms-key-id`attribute unless, for restoring a volume, you want to use the Oracle-managed key.
- Enabling replication: You can optionally specify your own key to encrypt the volume replica in the destination region. The customer-managed key can either be:
- a replicated key that exists in the destination region.
- any key in target region that you own and is different than the one in the source region.

You can encrypt the volume replica with a customer-managed encryption key in the destination region when you enable replication for a volume or volume group.

Select Encrypt using customer-managed keys for Cross region replication encryption , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume or volume group to.

If you don't specify a customer-managed key, an Oracle-managed encryption key is used instead.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

- [Restoring a backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm),[cloning a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm), or[activating a replica](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-activate-replica-bv-volume.htm#console):

Run the relevant[Core Services API](https://docs.oracle.com/iaas/api/#/en/iaas/)operation to assign a master encryption key. Include the`kmsKeyId`attribute.
- Enabling replication: You can optionally specify your own key to encrypt the volume replica in the destination region. The customer-managed key can either be:
- a replicated key that exists in the destination region.
- any key in target region that you own and is different than the one in the source region.

You can encrypt the volume replica with a customer-managed encryption key in the destination region when you enable replication for a volume or volume group.

Select Encrypt using customer-managed keys for Cross region replication encryption , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume or volume group to.
