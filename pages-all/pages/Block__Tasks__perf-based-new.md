# Enabling Performance-based Autotuning for a New Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-new.htm
- Fetched: 2026-09-05 01:47 CDT

# Enabling Performance-based Autotuning for a New Block Volume

Learn how to enable performance-based autotuning when creating a new block volume to automatically adjust its performance between levels you specify.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-new.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-new.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based-new.htm#)
- 

This task can't be performed using the Console.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)oci bv volume create`command and specify the`--compartment-id`and`--autotune-policies`parameters to enable performance-based autotune for a new block volume:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)CreateVolume`operation and specify the`autotunePolicies`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails)CreateVolumeDetails`
