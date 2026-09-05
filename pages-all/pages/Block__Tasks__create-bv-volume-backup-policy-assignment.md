# Assigning a Backup Policy to a Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy-assignment.htm
- Fetched: 2026-09-05 01:45 CDT

# Assigning a Backup Policy to a Volume

Learn how to assign a backup policy to an existing user- or Oracle-defined volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy-assignment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy-assignment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy-assignment.htm#)
- 

- On the Block Volumes list page, find the volume that you want to work with. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) for the volume, select Edit .
- In the Edit block volume panel, under Backup Policies , select the compartment containing the backup policies, and then select the backup policy that meets your requirements.
Optionally, if you select a backup policy enabled for cross region backup copies, you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting Encrypt using customer-managed keys for Cross region backup copy encryption . If you select this option, you must specify the OCID for a valid encryption key in the destination region, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#cust-key-xrr)for more information.
- Select Save changes .
- 

Use the[`oci bv volume-backup-policy-assignment create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy-assignment/create.html)command and specify the`--asset-id`,`--policy-id`and`--xrc-kms-key-id`parameters to assign a user- or Oracle-defined backup policy to a volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/CreateVolumeBackupPolicyAssignment)CreateVolumeBackupPolicyAssignment`operation and specify the`assetId`and`policyId`attributes in a`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeBackupPolicyAssignmentDetails)CreateVolumeBackupPolicyAssignmentDetails`
