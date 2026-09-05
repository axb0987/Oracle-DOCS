# Updating the Display Name for a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-display-name-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:47 CDT

# Updating the Display Name for a User-defined Backup Policy

Change the display name for a user-defined (custom) backup policy in Block Volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-display-name-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-display-name-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-display-name-bv-volume-backup-policy.htm#)
- 

- On the Backup Policies list page, find the backup policy that you want to work with. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- From the Actions menu (three dots) , select Edit .
- In the Edit backup policy panel, enter a new name.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/update.html)oci bv volume-backup-policy update`command and specify the`--policy-id`and`--display-name`parameters to update a volume backup policy display name:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/UpdateVolumeBackupPolicy)UpdateVolumeBackupPolicy`operation and provide the updated values in the`policyId`and`displayName`attributes of the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeBackupPolicyDetails)UpdateVolumeBackupPolicyDetails`
