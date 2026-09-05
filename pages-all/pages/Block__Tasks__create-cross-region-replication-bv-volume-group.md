# Enabling Cross-Region Replication When Creating a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume-group.htm
- Fetched: 2026-09-05 01:45 CDT

# Enabling Cross-Region Replication When Creating a Volume Group

Learn how to enable cross-region replication when you create a new boot volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-cross-region-replication-bv-volume-group.htm#)
- 

See[Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/create-volume-group.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html)oci bv volume-group create`command and specify the`--compartment-id`,`--volume-group-replicas'[{"displayName":"`,`"availabilityDomain"`and`"xrrKmsKeyId"`parameters to enable cross-region replication when creating a volume group:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)CreateVolumeGroup`operation and specify the`volumeGroupReplicas`attribute in the[`CreateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeGroupDetails)
