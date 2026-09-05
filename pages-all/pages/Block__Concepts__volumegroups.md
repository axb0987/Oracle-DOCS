# Working with Volume Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm
- Fetched: 2026-09-05 01:44 CDT

# Working with Volume Groups

The Oracle Cloud Infrastructure Block Volume service provides you with the capability to group together many volumes in a volume group. A volume group can include both types of volumes, boot volumes, which are the system disks for your compute instances, and block volumes for your data storage. You can use volume groups to create volume group backups and clones that are point-in-time and crash-consistent.

## Tasks

This section includes the following tasks:
- [Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm)
- [Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm)
- [Cloning a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm)
- [Getting a Volume Group's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/get-volume-group.htm)
- [Replicating Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
- [Updating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm)
- [Managing Assigned Backup Policies for Volume Groups (Policy-Based Volume Group Backups)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups_topic-Scheduled_Backups.htm)
- [Moving a Volume Group to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/change-compartment-volume-group.htm)
- [Deleting a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/delete-volume-group.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes, backups, and volume groups.

See the following policy examples for working with volume groups:
- [Let users create a volume group](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-creators-create-volume-groups)lets the specified group create a volume group from a set of volumes.
- [Let users clone a volume group](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-cloners-clone-volume-groups)lets the specified group clone a volume group from an existing volume group.
- [Let users create a volume group backup](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#backup-volume-groups)lets the specified group create a volume group backup.
- [Let users restore a volume group backup](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#restore-volume-group-backup)lets the specified group create a volume group by restoring a volume group backup.

Tip  
  
When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same compartment . However, users must have access to both compartments.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## About Volume Groups

Volume groups simplify the process to create time-consistent backups of running enterprise applications that span several storage volumes across several instances. You can then restore an entire group of volumes from a volume group backup.

Similarly, you can also clone an entire volume group in a time-consistent and crash-consistent manner. A deep disk-to-disk and fully isolated clone of a volume group, with all the volumes associated in it, becomes available for use within a matter of seconds. This speeds up the process of creating new environments for development, quality assurance, user acceptance testing, and troubleshooting.

For more information about Block Volume-backed system disks, see[Working with Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm). For more information about Block Volume backups see[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm). See[Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/cloningavolume.htm)for more information about Block Volume clones.

This capability is available using the Console, CLI, SDKs, or REST APIs.

Volume groups and volume group backups are high-level constructs that allow you to group together several volumes. When working with volume groups and volume group backups, keep the following in mind:
- 

You can only add a volume to a volume group when the volume status is available.
- 

You can add up to 32 volumes in a volume group, up to a maximum size limit of 128 TB. For example, if you wanted to add 32 volumes of equal size to a volume group, the maximum size for each volume would be 4 TB. Or you could add volumes that vary in size, however the overall combined size of all the block and boot volumes in the volume group must be 128 TB or less. Ensure you account for the size of any boot volumes in your volume group when considering volume group size limits.
- 

Each volume can only be in one volume group.
- 

When you clone a volume group, a new group with new volumes is created. For example, if you clone a volume group containing three volumes, then at completion of the operation, you have two separate volume groups and six different volumes with nothing shared between the volume groups.
- 

When you update a volume group using the CLI, SDKs, or REST APIs, you need to specify all the volumes to include in the volume group each time you use the update operation. If you don't include a volume ID in the update call, that volume is removed from the volume group.
- 

When you delete a volume group, the individual volumes in the group aren't deleted, only the volume group is deleted.
- 

When you delete a volume that's part of a volume group, you must first remove it from the volume group before you can delete it.
- 

When you delete a volume group backup, all the volume backups in the volume group backup are deleted.

## Volume Group Replication

The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of volume groups to other regions. This feature supports the following scenarios without requiring volume group backups:
- Disaster recovery
- Migration
- Business expansion

For more information, see[Block Volume Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm). For specific details about volume groups, including step-by-step procedures using the Console and CLI, see[Replicating Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
