# Attaching a Volume to Multiple Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm
- Fetched: 2026-09-05 01:45 CDT

# Attaching a Volume to Multiple Instances

Learn how to attach a block volume to multiple compute instances.

Note  
  
See also the Compute Cloud@Customer instructions:[Attaching a Volume to Multiple Instances](https://docs.oracle.com/iaas/compute-cloud-at-customer/cmn/block/attaching-a-volume-to-multiple-instances.htm).

## Limits and Considerations

- 

The Block Volume service does not provide coordination for concurrent write operations to block volumes attached to multiple instances, so if you configure the block volume as read/write and shareable you must deploy a cluster aware system or solution on top of the shared storage, see[Configuring Multiple Instance Volume Attachments with Read/Write Access](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm#configcluster).
- 

Once you attach a block volume to an instance as read-only, it can only be attached to other instances as read-only. If you want to attach the block volume to an instance as read/write, you need to detach the block volume from all instances and then you can reattach the block volume to instances as read/write.
- 

If the block volume is already attached to an instance as read/write non-shareable you can't attach it to another instance until you detach it from the first instance. You can then reattach it to both the first and second instances as read/write shareable.
- 

You can't delete a block volume until it has been detached from all instances it was attached to. When viewing the instances attached to the block volume from the Resources section of the Volume Details page, you should note that only instances in the selected compartment will be displayed. You may need to change the compartment to list additional instances that are attached to the volume.
- 

You can attach up to 32 instances to a shared volume if the volume is not configured for the Ultra High Performance level
- 

Volumes configured for the Ultra High Performance level require multipath-enabled attachments. You can attach up to 25 instances with multipath-enabled attachments to a shared volume configured for Ultra High Performance . If you try to attach additional multipath-enabled attachments beyond 25, the attachment process will fail.
- 

Block volumes attached as read-only are configured as shareable by default.
- 

Performance characteristics described in[Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeperformance.htm)are per volume, so when a block volume is attached to multiple instances the performance is shared across all the attached instances.
- Volumes configured for the Ultra High Performance level can also be attached to multiple instances, however the total IOPS and throughput of all attachments combined, including those configured for Ultra High Performance and non- Ultra High Performance are capped at the limits for a volume. For more information, see[Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeultrahighperformance.htm)and[Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm).

## Configuring Multiple Instance Volume Attachments with Read/Write Access

The Block Volume service does not provide coordination for concurrent write operations to volumes attached to multiple instances. To prevent data corruption from uncontrolled read/write operations you must install and configure a cluster aware system or solution such as Oracle Cluster File System version 2 (OCFS2) on top of the shared storage before you can use the volume.

You can see an sample walkthrough of scenario using OCFS2 described in[Using the Multiple-Instance Attach Block Volume Feature to Create a Shared File System on Oracle Cloud Infrastructure](https://blogs.oracle.com/cloud-infrastructure/using-the-multi-attach-block-volume-feature-to-create-a-shared-file-system-on-oracle-cloud-infrastructure). The summary of the required steps for this scenario are:
- 

Attach the block volume to an instance as Read/Write-Shareable using the Console, CLI, or API.
- 

Set up your OCFS2/O2CB cluster nodes.
- 

Create your OCFS2 file system and mount point.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to attach/detach existing block volumes. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm#)
- 

- On the Block Volumes list page, select the block volume that you want to attach to an instance. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- On the details page, select Attached Instances , and then select Attach to Instance .
- In the Attach to instance panel , enter the following information.

- Attachment type : Select iSCSI or Paravirtualized .

For more information, see[Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#attachtype).
- Access type : Select the[volume access type](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#accesstype):
- Read/Write : Enable read/write attachment, not shareable with other instances.
- Read/Write-Shareable : Enable read/write attachments to multiple instances.
- Read-only-Shareable : Enable read-only attachments to multiple instances.
- Instance : Either select an instance from the specified compartment or enter the instance's OCID.
- Require CHAP credentials : Select to use iSCSI security protocol CHAP for authentication between the instance and volume.
- Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes : Select to run iSCSI commands automatically when connecting an iSCSI volume to Linux-based instances.
- Device Path : If supported by the specified instance, select a[consistent device path](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/consistentdevicepaths.htm).
Tip  
  
You must select a device path when you attach a volume from the Console. Specifying a device path is only optional when you attach a volume using the CLI, REST APIs, or SDK.
- Use in-transit encryption (paravirtualized volume attachments on virtual machine (VM) instances): (Optional) Select to encrypt data that's transferred between the instance and the Block Volume service storage servers.

If you configured the volume to use an encryption key that you manage using the Vault service, this key is used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.

For iSCSI attachments on[bare metal instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#BlockVolumeEncryption)that support in-transit encryption, in-transit encryption is enabled by default and isn't configurable.

See[Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#BlockVolumeEncryption)for more information about in-transit encryption.
- Select Attach .
The volume's icon changes to Attaching while it attaches to the instance.

For a[paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#Paravirtualized)attachment type, you can use the volume when the volume's icon is no longer Attaching .

For a[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI)attachment type, you must[connect to the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm)first.

On Linux-based instances, to automatically mount volumes on instance boot, you must set specific options in the`/etc/fstab`file, or the instance might fail to launch. This requirement applies to both iSCSI and paravirtualized attachment types.

For volumes using consistent device paths, see[/etc/fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptionsconsistentdevicepaths.htm). For all other volumes, see[Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptions.htm).

[To attach a volume to multiple instances from the Instance details page](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-to-multiple-instances-compute-volume-attachment.htm#)

## To attach a volume to multiple instances from the Instance details page

- On the Instances list page, select the name of the instance that you want to attach a volume to. If you need help finding the list page or the instance, see[Listing Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/list-instances.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- Select Storage and then scroll down to Attached block volumes .
- Select Attached Block Volumes .
- 

Select Attach Block Volume .
- 

In the Attach block volume panel, for Attachment type , select the volume attachment type, iSCSI or Paravirtualized . (Select Custom to see options.)

For more information, see[Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#attachtype).
- 

Select the volume access type. Select Read/Write-Shareable if you want to enable read/write attachments to multiple instances or Read-only-Shareable for read-only attachments to multiple instances.

For more information, see[Volume Access Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#accesstype).
- 

In the Block Volume Compartment drop-down list, select the compartment.
- 

Specify the volume you want to attach to. To use the volume name, choose SELECT VOLUME and then select the volume from the Block Volume drop-down list. To specify the volume OCID, choose ENTER VOLUME OCID and then enter the OCID into the Block Volume OCID field.
- 

If the instance supports consistent device paths select a path from the Device Path drop-down list when attaching. This is required and enables you to specify a device path for the volume attachment that remains consistent between instance reboots.

For more information about this feature and the instances that support it, see[Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/consistentdevicepaths.htm)
Tip  
  
You must select a device path when you attach a volume from the Console, it is not optional. Specifying a device path is optional when you attach a volume using the CLI, REST APIs, or SDK.
- 

For paravirtualized volume attachments on virtual machine (VM) instances you can optionally encrypt data that is transferred between the instance and the Block Volume service storage servers. To do this, select the Use in-transit encryption check box. If you configured the volume to use an encryption key that you manage using the Vault service, this key is used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.

For iSCSI attachments on[bare metal instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#BlockVolumeEncryption)that support in-transit encryption, in-transit encryption is enabled by default and is not configurable.

See[Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#BlockVolumeEncryption)for more information about in-transit encryption.
- 

Select Attach .

When the volume's icon no longer lists it as Attaching , if the attachment type is[Paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#Paravirtualized), you can use the volume. If the attachment type is[iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/overview.htm#iSCSI), you need to connect to the volume first. For more information, see[Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm).

On Linux-based instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the`/etc/fstab`file, or the instance may fail to launch. This applies to both iSCSI and paravirtualized attachment types. For volumes using consistent device paths, see[/etc/fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptionsconsistentdevicepaths.htm). For all other volumes, see[Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../References/fstaboptions.htm).
- 

Use the`oci compute volume-attachment attach`command and specify the`--instance-id`,`--type`,`--volume-id`,`read-only`and`--is-shareable`parameters to attach a volume to an instance as shareable with read/write permissions:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/AttachVolume)AttachVolume`operation and specify the`isShareable`attribute for the[`AttachVolumeDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/AttachVolumeDetails)resource.

## Additional Resources

See the following links for example deployments of shared file systems on Oracle Cloud Infrastructure.
- 

GitHub project for automated terraform deployment of[BeeGFS](https://www.beegfs.io/content/):[oci-beegfs](https://github.com/oracle-quickstart/oci-beegfs)
- 

GitHub project for automated terraform deployment of[Lustre](http://lustre.org/):[oci-lustre](https://github.com/oracle-quickstart/oci-lustre)
- 

GitHub project for automated terraform deployments of IBM Spectrum Scale (GPFS) distributed parallel file system on Oracle Cloud Infrastructure:[oci-ibm-spectrum-scale](https://github.com/oracle-quickstart/oci-ibm-spectrum-scale)
