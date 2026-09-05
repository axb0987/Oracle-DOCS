# Enabling Detached Volume Autotuning for an Existing Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-existing.htm
- Fetched: 2026-09-05 01:46 CDT

# Enabling Detached Volume Autotuning for an Existing Block Volume

Learn how to enable detached volume autotuning to automatically adjust an existing block volume's performance based on attachment to or detachment from an instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-existing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-existing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf-existing.htm#)
- 

- On the Block Volumes list page, find the volume that you want to work with. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) for the volume, select Edit .
- In the Edit block volume (or Edit volume ) panel, under Target volume performance , turn on Detached volume auto-tune .
- Select Save changes .
- 

Use the[`oci bv volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)command specify the`--volume-id`,`compartment-id`, and`--autotune-policies`parameters to enable detached volume autotuning:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify the`autotunePolicies`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`
