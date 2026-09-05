# Enabling Performance-Based Autotuning for an Existing Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-bv-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Enabling Performance-Based Autotuning for an Existing Boot Volume

Learn how to enable performance-based autotuning to automatically adjust an existing boot volume's performance between levels you specify.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-bv-boot-volume.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Edit .
- In the Volume size and performance section, select the Performanced based auto-tune slider so that it changes from Off to On .
- Specify a value for Default VPUs/GB . This is the minimum performance setting the volume will be adjusted to. The value must be a multiple of 10. The minimum value is 10 and the maximum value is 110. You can also use the VPUs/GB slider to specify the value.
- Specify a value for Maximum VPUs/GB . This is the maximum performance setting the volume will be adjusted to. The value must be a multiple of 10, and must be at least 10 VPUs/GB higher than Default VPUs/GB . The maximum value is 120 VPUs/GB. You can also use the VPUs/GB slider to specify the value.
- 

Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)oci bv boot-volume update`command and specify the`--volume-id`,`--compartment-id`and`--autotune-policies`parameters to enable performance-based autotuning for an existing volume:

```

```

For example:

```

```

- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)UpdateBootVolume`operation and specify the`autotunePolicies`attribute in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateBootVolumeDetails)UpdateBootVolumeDetails`
