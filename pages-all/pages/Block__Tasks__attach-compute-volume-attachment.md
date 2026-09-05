# Attaching a Block Volume to an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm
- Fetched: 2026-09-05 01:45 CDT

# Attaching a Block Volume to an Instance

Learn how to attach a block volume to a compute instance to expand the available storage on the instance.

If you specify[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI)as the volume attachment type, you must also connect and mount the volume from the instance for the volume to be usable. For more information, see[Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#attachtype)and[Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm).

You can attach volumes to more than one instance at a time. For more information, see[Attaching a Volume to Multiple Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm). To prevent data corruption from uncontrolled read/write operations with multiple instance volume attachments you must install and configure a clustered file system before you can use the volume. For more information, see[Configuring Multiple Instance Volume Attachments with Read/Write Access](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm#configcluster).
Note  
  
When you change the performance for a volume, the volume's lifecycle state changes to Provisioning while the settings are being updated. During this process, you can't attach the volume to an instance. You must wait until the volume's lifecycle state transitions back to Available before you attach the volume to an instance.

## Attaching Ultra High Performance Volumes

When you attach a volume configured for the Ultra High Performance level, the volume attachment must be enabled for multipath to optimize the volume's performance.

The Block Volume service attempts to configure the attachment as multipath-enabled during the attachment process. After you attach a volume, you can confirm if the volume attachment was successfully enabled for multipath. See[Checking If a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-multipath-enable-check-compute-volume-attachment.htm).

Whether an attachment is enabled for multipath is determined based the attached instance's shape, along with whether all the applicable prerequisites are met and configured correctly. For more information about prerequisites and requirements for multipath-enabled attachments, see[Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm).

For more information about the Ultra High Performance level, see[Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeperformance.htm)and[Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeultrahighperformance.htm).

## Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect your ability to attach block volumes to compute instances.
- 

All block volumes attached to a compute instance in a security zone must be in the same security zone.
- 

Block volumes in a security zone can't be attached to a compute instance that is not in the same security zone.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm#)
- 

- 

On the Instances list page, select the name of the instance that you want to attach a volume to. If you need help finding the list page or the instance, see[Listing Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/list-instances.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- Select Storage and then scroll down to Attached block volumes .
- Select Attached Block Volumes .
- 

Select Attach block volume .
- 
Specify the volume that you want to attach to the instance.
- To use the volume name, select Select volume and then select the volume from the Volume list. If the volume is in a different compartment from the instance, select Change compartment and select the compartment that contains the volume.
- To specify the volume OCID, select Enter volume OCID and then enter the OCID into the Volume OCID field
- 

If the instance supports consistent device paths, and the volume that you're attaching isn't a boot volume, select a path from the Device path list.

Use this feature to specify a device path for the volume attachment that remains consistent between instance reboots. For more information about this feature and the instances that support it, see[Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/consistentdevicepaths.htm)
- 

Select the volume attachment type. See[Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#attachtype).
- 

For iSCSI volume attachments, optionally require CHAP credentials by selecting the Require CHAP credentials checkbox.

For iSCSI attachments to Linux-based instances, you can also optionally configure the attachment to use the Block Volume Management plugin to run the iSCSI commands to automatically connect to the volume. To do this, select the Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes checkbox.
Important  
  
To automatically connect to the volume, the Block Volume Management plugin must be enabled on the instance. See[Enabling the Block Volume Management Plugin](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm)for more information. When enabling the Block Volume Management plugin, ensure that the instance is running version 1.23.0 or newer of the Oracle Cloud Agent software.
- 

For paravirtualized attachments on virtual machine (VM) instances, optionally encrypt data that's transferred between the instance and the Block Volume service storage servers by selecting the Use in-transit encryption checkbox.

If you configured the volume to use an encryption key that you manage through the Vault service, this key is used for paravirtualized in-transit encryption. Otherwise, the Oracle-provided encryption key is used. When you attach the volume to a[bare metal instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#BlockVolumeEncryption)that supports in-transit encryption, in-transit encryption is enabled by default and isn't configurable. For more information about in-transit encryption, see[Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#BlockVolumeEncryption).
- 

Select the access type. For more information, see[Volume Access Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#accesstype).
- 

Select Attach .

When the volume's state is Attached , if the attachment type is[Paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#Paravirtualized), the volume is connected automatically and you can use it. If the attachment type is[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI), you need to connect to the volume first. For more information, see[Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm).

On Linux-based instances, to automatically mount volumes when the instance starts, you must set some specific options in the`/etc/fstab`file, or the instance might fail to start. This applies to both iSCSI and paravirtualized attachment types. For volumes that use consistent device paths, see[/etc/fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptionsconsistentdevicepaths.htm). For all other volumes, see[Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptions.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/attach.html)oci compute volume-attachment attach`command and required parameters to attach a block volume to an instance:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/AttachVolume)AttachVolume`operation and specify the`instanceId`,`type`, and`volumeId`parameters in the[`AttachVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/AttachVolumeDetails)
