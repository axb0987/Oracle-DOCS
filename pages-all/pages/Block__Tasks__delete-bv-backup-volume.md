# Deleting a Block Volume Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-backup-volume.htm
- Fetched: 2026-09-05 01:46 CDT

# Deleting a Block Volume Backup

Learn how to delete a block volume backup from a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-backup-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-backup-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/delete-bv-backup-volume.htm#)
- 

- On the Block Volume Backups list page, locate the volume you want to work with. If you need help finding the list page, see[Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-backup.htm).
- Select the the Actions menu (three dots) , and then select Terminate .
- Confirm when prompted.
- 

Use the[`oci bv backup delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/backup/delete.html)command and specify the`--volume-backup-id`parameter to list block volume backups:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`DeleteVolumeBackup`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/DeleteVolumeBackup)operation to delete a block volume backups.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
