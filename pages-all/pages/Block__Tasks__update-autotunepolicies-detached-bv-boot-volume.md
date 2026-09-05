# Enabling Detached Volume Autotuning for an Existing Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-detached-bv-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Enabling Detached Volume Autotuning for an Existing Boot Volume

Learn how to enable detached autotuning to automatically adjust an existing boot volume's performance based on its attachment to or detachment from an instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-detached-bv-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-detached-bv-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-autotunepolicies-detached-bv-boot-volume.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Edit .
- In the Volume Size and Performance section, select the Detached volume auto-tune slider so that it changes from Off to On .
- Select Save Changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)oci bv boot-volume update`command and specify the`--volume-id`,`--compartment-id`and`--autotune-policies`parameters to enable detached volume autotuning for an existing volume:

```

```

For example:

```

```

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)UpdateBootVolume`operation and specify the`autotunePolicies`and`DetachedVolumeAutotunePolicy`attributes in the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateBootVolumeDetails)UpdateBootVolumeDetails`
