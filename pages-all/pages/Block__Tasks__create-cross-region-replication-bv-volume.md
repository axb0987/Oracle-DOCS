# Enabling Cross-Region Replication When Creating a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume.htm
- Fetched: 2026-09-05 01:45 CDT

# Enabling Cross-Region Replication When Creating a Block Volume

Learn how to enable cross-region replication when you create a new block volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume.htm#)
- 

See[Creating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#console).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)oci bv volume create`command and specify the`--compartment-id`,`--block-volume-replicas`,`"availabilityDomain"`and`"xrrKmsKeyId"`parameters to create a block volume with cross-region replication enabled:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`CreateVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)operation and specify the`blockVolumeReplicas`attribute in the[`CreateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails)
