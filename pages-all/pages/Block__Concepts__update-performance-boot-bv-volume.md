# Changing the Performance of an Existing Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-boot-bv-volume.htm
- Fetched: 2026-09-05 01:44 CDT

# Changing the Performance of an Existing Boot Volume

Learn how to dynamically configure the performance level for a boot volume.

If you're changing the boot volume's performance to the Ultra High Performance level, see[Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot)for more details.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-boot-bv-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-boot-bv-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-boot-bv-volume.htm#)
- 

- On the Boot Volumes list page, find the boot volume that you want to work with. If you need help finding the list page or the boot volumes, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-bv-boot-volume.htm).
- From the Actions menu (three dots) for the boot volume, select Edit .
- In the Edit boot volume panel, for VPUs type , select the performance setting that you want.
You can also specify the VPUs/GB value for the performance setting in Default VPUs/GB .
- Select Save changes .
- 

Run the[oci bv boot-volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)command and specify one of the following volume performance unit (VPU) amounts in the`vpus-per-gb`parameter to update a block volume's elastic performance setting:
- `0`: Represents the Lower Cost setting. Applies to block volumes only.
- `10`: Represents the Balanced setting. Applies to both block volumes and boot volumes.
- `20`: Represents the Higher Performance setting. Applies to both block volumes and boot volumes.
- `30`to`120`: Represents the Ultra High Performance . Applies to both block volumes and boot volumes.

If you're changing a boot volume's performance to the Ultra High Performance level, see also[Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot).

For example:

```

```

- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)UpdateBootVolume`operation and specify one of the following volume performance unit (VPU) amounts in the`vpusPerGB`attribute for the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateBootVolumeDetails)UpdateBootVolumeDetails`resource to update a boot volume's elastic performance setting:
- `0`: Represents the Lower Cost setting, applies to block volumes only.
- `10`: Represents the Balanced setting, applies to both block volumes and boot volumes.
- `20`: Represents the Higher Performance setting, applies to both block volumes and boot volumes.
- `30`to`120`: Represents the Ultra High Performance setting, applies to both block volumes and boot volumes.

If you are changing the boot volume's performance to the Ultra High Performance level, see[Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot)
