# Disabling Cross-Region Replication for a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume-group.htm
- Fetched: 2026-09-05 01:47 CDT

# Disabling Cross-Region Replication for a Volume Group

Learn how to disable cross-region replication for an existing boot volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume-group.htm#)
- 

- On the Volume Groups list page, select the volume group you want to work with. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/list-volume-group.htm).
- On the details page, select Edit .
- Select Next twice to display the Cross region replication section.
- In the Cross region replication section, move the Enable cross ad/region replication slider to the left to disable cross-region replication.
- Select Check here to confirm to acknowledge the that volume group replica will be deleted.
- (Optional) To turn off individual volume replication for each volume in the group, select Volume replication off .
- Select Next twice to display the Summary section.
- 

Select Save changes .
- 

Use the[`oci bv volume-group update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html)command and specify`'[]'`for the`--volume-group-replicas`parameter to disable cross-region replication for a volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`UpdateVolumeGroup`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup)operation and specify`'[]'`for the`volumeGroupReplicas`attribute in the[`UpdateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/datatypes/UpdateVolumeGroupDetails)
