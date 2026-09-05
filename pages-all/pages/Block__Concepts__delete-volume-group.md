# Deleting a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Deleting a Volume Group

Delete a volume group in the Block Volume service.

Note  
  
When you delete a volume group, the individual volumes in the group are not deleted. Only the volume group is deleted.

See also[Deleting a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/delete-bv-volume-group-backup.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm#)
- 

- On the Volume Groups list page, select the volume group you want to delete. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- From the Actions menu for the volume group, select Terminate .
- On the Terminate volume group dialog, select Terminate .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/delete.html)oci bv volume-group delete`command and required parameters to delete a volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/DeleteVolumeGroup)DeleteVolumeGroup`operation and specify the`volumeGroupId`
