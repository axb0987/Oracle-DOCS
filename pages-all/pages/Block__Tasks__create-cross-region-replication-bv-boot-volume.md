# Enabling Cross-Region Replication When Creating a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-boot-volume.htm
- Fetched: 2026-09-05 01:45 CDT

# Enabling Cross-Region Replication When Creating a Boot Volume

Learn how to enable cross-region replication when you create a new boot volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-boot-volume.htm#)
- 

This task can't be performed using the Console.
- 

Use the[`oci bv boot-volume create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/create.html)command and specify the`--source-boot-volume-id`,`--compartment-id`,`"displayName"`,`"availabilityDomain"`and`"xrrKmsKeyId"`parameters to create boot volume with cross-region replication enabled:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`CreateVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)operation and specify the`bootVolumeReplicas`attribute in the[`CreateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails)
