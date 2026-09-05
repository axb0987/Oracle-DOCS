# Assigning a Backup Policy to a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-assign-to-group-bv-volume-backup-policy-assignment.htm
- Fetched: 2026-09-05 01:44 CDT

# Assigning a Backup Policy to a Volume Group

Learn how to assign a backup policy to a volume group.

If a volume group has an assigned backup policy, you must remove any backup policy assignments from volumes before you can add them to the volume group.

Before you can assign a backup policy to an existing volume group containing one or more volumes with assigned backup policies, you must remove those policy assignments from the individual volumes.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-assign-to-group-bv-volume-backup-policy-assignment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-assign-to-group-bv-volume-backup-policy-assignment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-assign-to-group-bv-volume-backup-policy-assignment.htm#)
- 

- On the Volume Groups list page, select the volume group you want to assign a backup policy to. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- On the details page, select Edit .
- Select Next until the Backup Policies section is displayed.
- 

In the Backup Policies section, select the compartment containing the backup policies.
- 

Select the appropriate backup policy for your requirements.
- Optionally, if you select a backup policy enabled for cross region backup copies, you can encrypt the backup copy in the destination region with your own Vault encryption key by selecting Encrypt using customer-managed keys for Cross region backup copy encryption . If you select this option, you must specify the OCID for a valid encryption key in the destination region, see[Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm#cust-key-xrr).
- 

Select Next , and then Save changes .
- 

Use the[`oci bv volume-backup-policy-assignment create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy-assignment/create.html)command and specify the`--asset-id`and`--policy-id`parameters to assign the policy to the volume backup group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateVolumeBackupPolicyAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/CreateVolumeBackupPolicyAssignment)operation and specify the assetId and policyId attributes in the[CreateVolumeBackupPolicyAssignmentDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeBackupPolicyAssignmentDetails)
