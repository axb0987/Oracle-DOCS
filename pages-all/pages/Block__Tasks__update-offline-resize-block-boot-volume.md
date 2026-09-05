# Offline Resizing a Block or Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-offline-resize-block-boot-volume.htm
- Fetched: 2026-09-05 01:47 CDT

# Offline Resizing a Block or Boot Volume

You can use offline resizing to detach the volume from an instance before you expand the volume size. Once the volume is resized and reattached, you must extend the partition, but you do not need to rescan the disk.

## Considerations When Resizing an Offline Volume

Whenever you detach and reattach volumes, there are complexities and risks for both Linux-based and Windows-based instances. This applies to both paravirtualized and iSCSI attachment types. You should keep the following in mind when resizing volumes:
- 

When you reattach a volume to an instance after resizing, if you are not using consistent device paths, or the instance does not support consistent device paths, device order and path may change. If you are using a tool such as Logical Volume Manager (LVM), you may need to fix the device mappings. For more information about consistent device paths, see[Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/consistentdevicepaths.htm).
- 

When you detach and then reattach an iSCSI-attached volume to an instance, the volume's IP address will increment.
- 

Before you resize a volume, you should create a full backup of the volume.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-offline-resize-block-boot-volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-offline-resize-block-boot-volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-offline-resize-block-boot-volume.htm#)
- 

- [Detach the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm).
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
- [Detach the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#detach-compute-volume-attachment-cli).
- 

Use the[`oci bv volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html)command and specify the`--volume-id`and`--size-in-gbs`parameters to resize a block volume:

```

```

#### Boot Volumes

- [Detach the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#detach-compute-volume-attachment-cli).
- 

Use the[`oci bv boot-volume update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html)command and specify the`--volume-id`and`--size-in-gbs`parameters to resize a block volume:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

#### Block Volumes
- 

Run the[`DetachVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/DetachVolume)operation and specify the`volumeAttachmentId`attribute to detach a block volume from an instance.
- 

Run the[`UpdateVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)operation and specify the`volumeId`attribute in the request body and the`sizeInGBs`attribute in the[`UpdateVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails)resource to resize the block volume.

#### Boot Volumes
- 

Run the[`DetachVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/DetachVolume)operation and specify the`volumeAttachmentId`attribute to detach a block volume from an instance.
- 

Run the[`UpdateBootVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)operation and specify the`volumeId`attribute in the request body and the`sizeInGBs`attribute in the`UpdateBootVolumeDetails`resource to resize the boot volume.

## Next Steps

- Rescan the disk. See[Rescanning the Disk for Volumes Attached to Windows Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanni2).
- Extend the partition. See[Extending the Partition for a Block Volume on a Windows-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#exBlockWindows)
