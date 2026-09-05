# Enabling Detached Volume Autotuning for a New Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-new.htm
- Fetched: 2026-09-05 01:46 CDT

# Enabling Detached Volume Autotuning for a New Block Volume

Learn how to enable detached volume autotuning when creating a new block volume to automatically adjust its performance based on attachment to or detachment from an instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-new.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-new.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-new.htm#)
- 

This task can't be performed using the Console.
- 

Use the[`oci bv volume create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)command and specify the`--compartment-id`,`--autotune-policies`parameters to enable detached volume autotuning:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)CreateVolume`operation and specify the`autotunePolicies`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails)CreateVolumeDetails`
