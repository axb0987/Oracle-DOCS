# Online Resizing a Block or Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Online Resizing a Block or Boot Volume

With online resizing, you can expand the volume size without detaching the volume from an instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm#)
- 

- On the Block Volumes or Boot Volumes list page, find the volume that you want to resize. If you need help finding the list page or the volume, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm)or[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- From the Actions menu (three dots) , select Edit .
- In the edit panel, for Volume size (in GB) , enter the new volume size.

You must specify a larger value than the block volume's current size.
- Select Save changes .
If you resized a volume attached to a Linux-based instance, a dialog opens that lists the commands you need to run after the volume is provisioned.
- (Optional) Run the listed commands to ensure that the operating system correctly identifies the increased volume size.

- Select Copy to copy the commands.
- Select Close to close the dialogue.
- See[Next Steps](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm#next_steps)for information on rescanning the disk and extending the partition.
- 

#### Block Volumes

Use the[`oci bv volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)command and specify the`--volume-id`and`--size-in-gbs`parameters to resize a block volume:

```

```

#### Boot Volumes

Use the[`oci bv boot-volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)command and specify the`--volume-id`and`--size-in-gbs`parameters to resize a block volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

#### Block Volumes

Run the[`UpdateVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)operation and specify the`volumeId`attribute in the request body and the`sizeInGBs`attribute in the[`UpdateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)resource to resize a block volume.

#### Boot Volumes

Run the[`UpdateBootVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)operation and specify the`volumeId`attribute in the request body and the`sizeInGBs`attribute in the`UpdateBootVolumeDetails`resource to resize a boot volume.

## Next Steps

- Rescan the disk. See[Rescanning the Disk for Volumes Attached to Windows Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanni2).
- Extend the partition. See[Extending the Partition for a Block Volume on a Windows-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#exBlockWindows)
