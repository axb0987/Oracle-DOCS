# Deleting a Backup Policy Assigned to a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-for-volume-group-bv-volume-backup-policy-assignment.htm
- Fetched: 2026-09-05 01:44 CDT

# Deleting a Backup Policy Assigned to a Volume Group

Learn how to delete a backup policy assigned to a volume group.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-for-volume-group-bv-volume-backup-policy-assignment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-for-volume-group-bv-volume-backup-policy-assignment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-for-volume-group-bv-volume-backup-policy-assignment.htm#)
- 

- On the Volume Groups list page, select the volume group you want to remove the backup policy from. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- On the details page, select Edit .
- Select Next until the Backup policy section is displayed.
- 

In the Backup policies section, select None from the list.
- 

Select Next , then Save changes .
- 

Use the[`oci bv volume-backup-policy-assignment delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy-assignment/delete.html)command and specify the`--policy-id`parameter to delete a backup policy assigned to a volume group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteVolumeBackupAssignment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/DeleteVolumeBackupPolicyAssignment)
