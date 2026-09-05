# Working with Block Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/blockvolumes.htm
- Fetched: 2026-09-05 01:47 CDT

# Working with Block Volumes

Oracle Cloud Infrastructure Block Volume lets you dynamically provision and manage block storage volumes. You can create, attach, connect, and move volumes, as well as change volume performance, as needed, to meet your storage, performance, and application requirements. After you create a volume, you can attach and connect a volume to an instance, and then you can use the volume like a regular hard drive. You can also disconnect a volume and attach it to another instance without the loss of data.

## Tasks

- [Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/listingvolumes.htm)
- [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm)
- [Getting a Block Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm)
- [Updating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-block-volume.htm)
- [Changing the Performance of an Existing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-performance-block-bv-volume.htm)
- [Editing a Block Volume's Settings](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/editvolume.htm)
- [Managing Backup Policy Assignments for Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/block-volume-policy-assignments.htm)
- [Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
- [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm)
- [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm)
- [Listing Attachments for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-volume-attachment.htm)
- [Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-bv-backup.htm)
- [Moving a Block Volume to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm)
- [Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm)
- [Replicating Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/replicating-block-volumes.htm)
- [Disconnecting From a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm)
- [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm)
- [Deleting a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm)

## IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Monitoring Resources

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
