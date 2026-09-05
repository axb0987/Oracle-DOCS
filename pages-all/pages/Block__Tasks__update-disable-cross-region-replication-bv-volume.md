# Disabling Cross-Region Replication for a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Disabling Cross-Region Replication for a Block Volume

Learn how to disable cross-region replication for an existing block volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-disable-cross-region-replication-bv-volume.htm#)
- 

- 

On the Block Volumes list page, find the block volume that you want to edit. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) , select Edit .
- In the Edit block volume panel, turn off Enable cross ad/region replication (might be labeled Cross ad/region replication ).
- 

Select Confirm to acknowledge the replica deletion.
- 

Select Save changes .
- 

Use the`oci bv volume update`command and specify the`--volume-id`parameter and`'[]'`for the`--block-volume-replicas`parameter to disable cross-region replication for a block volume:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify`[]`for the`blockVolumeReplicas`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`
