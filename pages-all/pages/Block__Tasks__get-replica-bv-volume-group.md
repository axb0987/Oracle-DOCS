# Getting Details for a Volume Group Replica
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-volume-group.htm
- Fetched: 2026-09-05 01:46 CDT

# Getting Details for a Volume Group Replica

Learn how to view details for a specific volume group replica.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-volume-group.htm#)
- 

On the Volume Groups list page, select the volume group you want to work with. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/list-volume-group.htm).
- 

Use the[`oci bv volume-group-replica get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group-replica/get.html)command and specify the`--volume-group-replica-id`parameter to get details for a volume group replica:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`GetVolumeGroupReplica`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupReplica/GetVolumeGroupReplica)operation and specify the`volumeGroupReplicaId`
