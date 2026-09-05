# Connecting to a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm
- Fetched: 2026-09-05 01:45 CDT

# Connecting to a Block Volume

Connect to a block volume that's attached to a compute instance.

To connect to a volume, you must first attach the volume to the instance. See[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm). The steps to connect depend on the volume attachment type, paravirtualized or iSCSI. For more information about attachment type options, see[Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#attachtype).

## Paravirtualized-Attached Volumes
For volumes attached with[Paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#Paravirtualized)as the volume attachment type, you don't need to perform any additional steps after attaching the volumes; they're connected automatically. However, for Linux-based images, if you want to mount these volumes when the instance starts, you need to perform additional configuration steps:
- If you specified a device path when you attached the volume, see[/etc/fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptionsconsistentdevicepaths.htm).
- If you didn't specify a device path or if the instance was created from an image that doesn't support device paths, see[Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptions.htm)

## iSCSI-Attached Volumes

For volumes attached with[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI)as the volume attachment type, you need to connect and mount the volume from the instance for the volume to be usable. See[Connecting to iSCSI-Attached Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume_topic-Connecting_to_iSCSIAttached_Volumes.htm).
Important  
  
When you attach a volume using an iSCSI attachment type, you can optionally specify that the Block Volume Management plugin should run the iSCSI commands to connect to the volume. See step 9 in[Attaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm#console)
