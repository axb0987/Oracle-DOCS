# Deleting a User-defined Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:46 CDT

# Deleting a User-defined Backup Policy

Delete a user-defined (custom) backup policy in Block Volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-volume-backup-policy.htm#)
- 

- On the Backup Policies list page, find the backup policy that you want to work with. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- From the Actions menu (three dots) , select Delete .
- In the Delete backup policy dialog box, enter the name of the backup policy that you want to delete.
- Select Delete .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/delete.html)oci bv volume-backup-policy delete`command and specify the`--policy-id`parameter to delete the policy:
```

```

Note  
  
You can only delete a user-defined backup policy if it is not assigned to any volumes. You cannot delete Oracle-defined backup policies.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/DeleteVolumeBackupPolicy)DeleteVolumeBackupPolicy`operation and specify the`policyId`
