# Disabling Cross-Region Replication for a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Disabling Cross-Region Replication for a Boot Volume

Learn how to disable cross-region replication for an existing boot volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-boot-volume.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Edit .
- In the Cross region replication section, move the slider to the left to disable cross-region replication.
- 

Select Confirm to acknowledge the replica deletion.
- 

Select Save changes .
- 

Use the[`oci bv boot-volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)command and specify the`boot-volume-id`parameter and`'[]'`for the`--boot-volume-replicas`parameter to disable cross-region replication for a boot volume:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify`[]`for the`bootVolumeReplicas`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`
