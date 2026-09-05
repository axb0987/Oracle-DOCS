# Deleting a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm
- Fetched: 2026-09-05 01:46 CDT

# Deleting a Block Volume

Delete a block volume from the Block Volume service when it's no longer needed.

Caution  
  

- You can't undo this operation. When you delete a volume, any data on the volume is permanently deleted.
- All policy-based backups eventually expire, so if you want to keep a backup of the volume indefinitely, create a manual backup of the volume before you delete it. See[Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm)and[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm#)
- 

- 

On the Block Volumes list page, find the block volume that you want to delete. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) , select Terminate .
- In the confirmation dialog box, select Terminate .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/delete.html)oci bv volume delete`command and required parameters to delete a block volume:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/DeleteVolume)DeleteVolume`operation and specify the`volumeId`
