# Changing the Performance of an Existing Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-block-bv-volume.htm
- Fetched: 2026-09-05 01:44 CDT

# Changing the Performance of an Existing Block Volume

Learn how to dynamically configure the performance level for a block volume.

You can change the default setting when you create a new block volume. For more information, see[Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/creatingavolume.htm). The default volume performance setting for existing and new block volumes is Balanced .

When you create an instance, the volume performance setting for the instance's boot volume is set to Balanced . You can change this setting to Higher Performance or UHP (Ultra High Performance) after the instance has been launched.

See also[Enabling Performance-based Autotuning for an Existing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/perf-based-existing.htm)and[Enabling Detached Volume Autotuning for an Existing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/detached-perf-existing.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-block-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-block-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-block-bv-volume.htm#)
- 

- On the Block Volumes list page, find the volume that you want to work with. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/listingvolumes.htm).
- From the Actions menu (three dots) for the volume, select Edit .
- In the Edit block volume (or Edit volume ) panel, for VPUs type , select the performance setting that you want.
You can also specify the VPUs/GB value for the performance setting in Default VPUs/GB .
- Select Save changes .
- 

Run the[`oci bv volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)command and specify one of the following volume performance unit (VPU) amounts in the`vpus-per-gb`parameter to update a block volume's elastic performance setting:
- `0`: Represents the Lower Cost setting. Applies to block volumes only.
- `10`: Represents the Balanced setting. Applies to both block volumes and boot volumes.
- `20`: Represents the Higher Performance setting. Applies to both block volumes and boot volumes.
- `30`to`120`: Represents the Ultra High Performance . Applies to both block volumes and boot volumes.

For example:

```

```

- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)UpdateVolume`operation and specify one of the following volume performance unit (VPU) amounts in the`vpusPerGB`attribute for the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)UpdateVolumeDetails`resource to update a block volume's elastic performance setting:
- `0`: Represents the Lower Cost setting, applies to block volumes only.
- `10`: Represents the Balanced setting, applies to both block volumes and boot volumes.
- `20`: Represents the Higher Performance setting, applies to both block volumes and boot volumes.
- `30`to`120`
