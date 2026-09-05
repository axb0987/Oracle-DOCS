# Working with Boot Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm
- Fetched: 2026-09-05 01:44 CDT

# Working with Boot Volumes

A boot volume is created when you create an instance.

## Tasks

- [Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-bv-boot-volume.htm)
- [Getting a Boot Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/get-bv-boot-volume.htm)
- [Updating a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-boot-volume.htm)
- [Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/extendingbootpartition.htm)
- [Changing the Performance of an Existing Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-boot-bv-volume.htm)
- [Enabling Performance-Based Autotuning for an Existing Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-autotunepolicies-bv-boot-volume.htm)
- [Enabling Detached Volume Autotuning for an Existing Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-autotunepolicies-detached-bv-boot-volume.htm)
- [Managing Backup Policy Assignments for Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/boot-volume-policy-assignments.htm)
- [Listing Attachments for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-compute-boot-volume-attachment.htm)
- [Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/attach-compute-boot-volume-attachment.htm)
- [Creating a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-boot-volume-backup.htm)
- [Moving a Boot Volume to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/change-boot-volume-compartment-bv-boot-volume.htm)
- [Cloning a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-clone-bv-boot-volume.htm)
- [Replicating Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/boot_volume_replicas.htm)
- [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/detach-compute-boot-volume-attachment.htm)
- [Deleting a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/delete-bv-boot-volume.htm)
- [Linux: Recovering a Corrupted Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/recoveringlinuxbootvolume.htm)
- [Windows: Recovering a Corrupted Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/recoveringwindowsbootvolume.htm)

## About Boot Volumes

When you launch a virtual machine (VM) or bare metal instance based on a[platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)or[custom image](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm), a new boot volume for the instance is created in the same compartment. That boot volume is associated with that instance until you terminate the instance. When you[terminate the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm), you can preserve the boot volume and its data. This feature gives you more control and management options for your compute instance boot volumes, and enables:
- Instance scaling: When you terminate your instance, you can keep the associated boot volume and use it to launch a new instance using a different instance type or shape. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)for steps to launch an instance based on a boot volume. This allows you to switch easily from a bare metal instance to a VM instance and vice versa, or scale up or down the number of cores for an instance.
- Troubleshooting and repair: If you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume. Then you can attach it to another instance as a data volume to troubleshoot it. After resolving the issue, you can then reattach it to the original instance or use it to launch a new instance.

Boot volumes are encrypted by default, the same as other block storage volumes. For more information, see[Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption).
Important  
  
In-transit encryption for boot and block volumes is only available for virtual machine (VM) instances launched from platform images, along with bare metal instances that use the following shapes: BM.Standard.E3.128, BM.Standard.E4.128, BM.DenseIO.E4.128. It is not supported on other bare metal instances. To confirm support for certain Linux-based custom images and for more information,[contact Oracle support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

You can group boot volumes with block volumes into the same volume group, making it easy to create a group volume backup or a clone of your entire instance, including both the system disk and storage disks at the same time. See[Working with Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)for more information.

You can move Block Volume resources such as boot volumes and boot volume backups between compartments. For more information, see[Moving Block Volume Resources Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/moveblockresourcecompartments.htm).

For more information about the Block Volume service and boot volumes, see the[Block Volume FAQ](https://www.oracle.com/cloud/storage/block-volumes/faq/).

## Custom Boot Volume Sizes

When you launch an instance, you can use the selected image's default boot volume size or specify a custom size up to 32 TB. This capability is available for the following image source options:
- Platform image
- Custom image
- Image OCID

See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)for more information.

For Linux and Windows images, the custom boot volume size must be larger than the image's default boot volume size or 50 GB, whichever is higher.
Note  
  
For Windows Server 2012 R2 Datacenter images and Windows platform images published before October 2021, the custom boot volume size must be larger than the image's default boot volume size or 256 GB, whichever is higher.

If you specify a custom boot volume size, you need to extend the volume to take advantage of the larger size. For steps, see[Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/extendingbootpartition.htm).

## Boot Volume Performance

Boot volume performance varies with volume size, see[Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm)for more information.

The Block Volume service's elastic performance enables you to dynamically change the volume performance for boot volumes. Once an instance has been created, you can change the volume performance of the boot volume to one of the following performance levels:
- 

Balanced
- 

Higher Performance
- 

Ultra High Performance (See[Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot).)

For how to change the performance for a boot volume, see[Changing the Performance of a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/changingvolumeperformance.htm)

## Cross-Region Boot Volume Replication

The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of boot volumes to other regions. This feature supports disaster recovery, migration, and business expansion scenarios, without requiring boot volume backups. See[Block Volume Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)for more information.

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to list boot volumes. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes, boot volumes, and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
