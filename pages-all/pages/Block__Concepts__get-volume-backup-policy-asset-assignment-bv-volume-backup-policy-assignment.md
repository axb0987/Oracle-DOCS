# Getting a Volume Group's Backup Assignment Policy Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-backup-policy-asset-assignment-bv-volume-backup-policy-assignment.htm
- Fetched: 2026-09-05 01:44 CDT

# Getting a Volume Group's Backup Assignment Policy Details

Learn how to get a the backup assignment policy details for a volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-backup-policy-asset-assignment-bv-volume-backup-policy-assignment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-backup-policy-asset-assignment-bv-volume-backup-policy-assignment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-backup-policy-asset-assignment-bv-volume-backup-policy-assignment.htm#)
- 

On the Volume Groups list page, the backup policy for a volume group is listed in the Backup policy column. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- 

Use the[`oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy-assignment/get-volume-backup-policy-asset-assignment.html)command and specify the`--asset-id`parameter to get the backup assignment policy details for a volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`GetVolumeBackupPolicyAssetAssignment`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssetAssignment)operation and specify the`assetId`
