# Resizing a Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm
- Fetched: 2026-09-05 01:47 CDT

# Resizing a Volume

The Oracle Cloud Infrastructure Block Volume service lets you expand the size of block volumes and boot volumes. You have several options to increase the size of your volumes.

Options to resize a volume:
- 

Expand an existing volume in place with online resizing. See[Online Resizing a Block or Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm).
- 

Restore from a volume backup to a larger volume. See[Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-to-new-volume-bv-volume-backup.htm)and[Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-restore-bv-boot-volume-backup.htm).
- 

Clone an existing volume to a new, larger volume. See[Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm)and[Cloning a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-clone-bv-boot-volume.htm).
- 

Expand an existing volume in place with offline resizing. See[Offline Resizing a Block or Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-offline-resize-block-boot-volume.htm)for the steps to do this.

For more information about the Block Volume service, see the[Block Volume FAQ](https://cloud.oracle.com/infrastructure/storage/block-volume/faq).

You can only increase the size of the volume. You cannot decrease the size.
Note  
  
If cross-region replication is enabled for the volume you want to resize, before you resize the volume, you must disable cross-region replication. Once the volume is resized, you can renable cross-region replication for the volume. For more information about this feature, see[Block Volume Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/volumereplication.htm).
Note  
  

Resizing IDE type boot volumes is not supported. This applies to both offline and online resizing. To workaround this limitation, you can do one of the following:
- 

Terminate the VM instance, ensuring that you keep the boot volume when you terminate the instance. Resize the boot volume that you have kept, and then launch a new VM instance, using the resized boot volume as the image source.
- 

Create a clone of the boot volume, resize the boot volume clone, and then launch a new VM instance using the resized boot volume clone as the image source.
Caution  
  
Before you resize a boot or block volume, you should create a backup of the volume.
Note  
  
After a volume has been resized, the first backup on the resized volume will be a full backup. See[Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backuptype)for more information about full versus incremental volume backups.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to attach/detach existing block volumes. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm)
