# Enabling Cross-region Copy for a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-destinationregion-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:46 CDT

# Enabling Cross-region Copy for a User-defined Backup Policy

Copy backups between regions for disaster recovery, business continuity, migration, or expansion. Update a user-defined (custom) backup policy in Block Volume to enable cross-region copy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-destinationregion-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-destinationregion-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-destinationregion-bv-volume-backup-policy.htm#)
- 

- On the Backup Policies list page, find the backup policy that you want to work with. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- From the Actions menu (three dots) , select Edit .
- On the Edit backup policy panel, for Cross region copy target , select the region you want the volume backup to be copied to.
- Select the checkbox to acknowledge the warning.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/create.html)oci bv volume-backup-policy create`command and specify the`--compartment id`,`--destinationregion`parameters to set a paired region for copying scheduled backups to.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/CreateVolumeBackupPolicy)CreateVolumeBackup`operation and specify the`compartmentId`and`destinationRegion`attributes for the[`CreateVolumeBackupPolicyDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeBackupPolicyDetails)
