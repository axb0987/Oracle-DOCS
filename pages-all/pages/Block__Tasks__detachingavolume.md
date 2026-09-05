# Detaching a Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm
- Fetched: 2026-09-05 01:46 CDT

# Detaching a Volume

Detach a block volume from an instance.

When an instance no longer needs access to a volume, you can detach the volume from the instance without affecting the volume's data.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#)
- 

Caution  
  
For volumes attached using[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI), we recommend that you unmount and disconnect the volume from the instance using`iscsiadm`before you detach the volume. Failure to do so might lead to loss of data. See[Disconnecting From a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm)for more information.
- On the Instances list page, select the instance you want to detach a volume from. If you need help finding the list page or the instance, see[Listing Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/list-instances.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- Select Storage and then scroll down to Attached block volumes .
- Select Attached Block Volumes .
- From the Actions menu (three dots) for the block volume you want to detach, select Detach .
- Select Detach volume .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/detach.html)oci compute volume-attachment detach`command and required parameters to detach a block volume from an instance:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[`DetachVolume`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/DetachVolume)operation and specify the`volumeAttachmentId`
