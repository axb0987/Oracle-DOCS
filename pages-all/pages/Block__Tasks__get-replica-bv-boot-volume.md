# Getting Details for a Boot Volume Replica
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-boot-volume.htm
- Fetched: 2026-09-05 01:46 CDT

# Getting Details for a Boot Volume Replica

Learn how to view details for a specific boot volume replica.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-replica-bv-boot-volume.htm#)
- 

On the Boot Volume Replicas list page, select the boot volume replica you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volume Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume-replica.htm)
- 

Use the[`oci bv boot-volume-replica get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume-replica/get.html)command and specify the`--boot-volume-replica-id`parameter to get details for a boot volume replica:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeReplica/GetBootVolumeReplica)GetBootVolumeReplica`operation and specify the`bootVolumeId`
