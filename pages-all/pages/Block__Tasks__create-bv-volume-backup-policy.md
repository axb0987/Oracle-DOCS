# Creating a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:45 CDT

# Creating a User-defined Backup Policy

Create a user-defined (custom) backup policy in Block Volume. A user-defined backup policy includes configurable frequency, retention, optional cross-region copy, and optional schedules.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-volume-backup-policy.htm#)
- 

- On the Backup Policies list page, select Create backup policy . If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- On the Create backup policy page, enter the following information.

- Name : Enter a name for the backup policy. Avoid entering confidential information.
- Compartment : Select the compartment to create the backup policy in.

While you select a compartment for the backup policy, it's accessible across your tenancy.
- Cross region copy target : (Optional) Select a target region to enable cross region copy. This function automates the copying of the volume backup to the selected region after each backup is created. For more information, see[Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).

Select the checkbox to acknowledge the warning.

When you assign a backup policy with cross region copy enabled to a volume, you can optionally select Encrypt using customer-managed keys for Cross region backup copy encryption to encrypt the volume backup with a Vault key from the destination region. See[Cross-Region Backup Copies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#xrr-backup)for more information.
- Tags : (Optional) Select Tags to add tags to the backup policy. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create backup policy .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/create.html)oci bv volume backup policy create`command and specify the`--compartment-id`and`--schedules`parameters to create a volume backup policy:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/CreateVolumeBackupPolicy)CreateVolumeBackupPolicy`operation and specify the`compartmentId`attribute for the[`CreateVolumeBackupPolicyDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeBackupPolicyDetails)
