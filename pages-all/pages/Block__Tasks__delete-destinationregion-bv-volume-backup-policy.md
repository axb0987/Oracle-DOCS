# Disabling Cross-region Copy for a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-destinationregion-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:46 CDT

# Disabling Cross-region Copy for a User-defined Backup Policy

Stop copying backups between regions. Update a user-defined (custom) backup policy in Block Volume to disable cross-region copy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-destinationregion-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-destinationregion-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-destinationregion-bv-volume-backup-policy.htm#)
- 

- On the Backup Policies list page, find the backup policy that you want to work with. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- From the Actions menu (three dots) , select Edit .
- On the Edit backup policy panel, for Cross region copy target , select None .
- Select the checkbox to acknowledge the warning.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/create.html)oci bv volume-backup-policy create`command and specify the`--compartment id`parameter and set the`--destinationregion`parameter as`none`to disable backups for a paired region.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`UpdateVolumeBackupPolicy`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/UpdateVolumeBackupPolicy)operation and specify the`policyId`attribute in the request body and the`destinationRegion`as`none`in the[`UpdateVolumeBackupPolicyDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeBackupPolicyDetails)
