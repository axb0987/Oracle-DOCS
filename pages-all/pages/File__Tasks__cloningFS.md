# Cloning File Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm
- Fetched: 2026-09-05 02:02 CDT

# Cloning File Systems

A clone is a new file system that's created based on a snapshot of an existing file system. Snapshots preserve the state of the data of a file system at a particular point in time. If you take snapshots of a file system regularly, you can create clones of the file system as it existed at many points in its lifetime.

A snapshot provides the initial blueprint for a clone. You can clone a parent file system, or you can clone a clone, as long as at least one snapshot is available. At the point of creation, the data included in the clone is identical to the data in the snapshot. After creation, data changes in the clone aren't included in the original file system. Conversely, any data changes to the original file system aren't included in the clone. All file systems operate independently of each other, regardless of whether they're parent file systems, clones, or clones of clones.

Clones are space and time efficient because creating a clone doesn't replicate or move any data from the parent file system to the clone. Instead, the clone references the parent file system for any data they share. A file system that's a clone of a clone also references the original parent file system for any shared data. If you[detach a clone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm), it becomes an entirely independent file system. Any shared data is copied or moved to the file system as it's detached.

When you create a clone, initially only the metadata incurs storage costs. Clone data usage is metered only against differentiated data. Data that the clone references from the parent file system isn't metered against the clone, only the parent. Detaching a clone results in an independent file system that's metered normally. For more information, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm).
Note  
  
Clones count against a tenancy's service limits the same way regular file systems do. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

You can use clones for testing, patching, and faster application provisioning. If failed testing or patching causes the data to become unrecoverable, create a new clone from the original file system snapshot, delete the old clone, and restart the operation.

You can perform the following cloning tasks:
- [Cloning a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-clone.htm)
- [Finding and Listing Clones](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/find-clones.htm)
- [Detaching a Clone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm)

## Cloning Concepts
PARENT FILE SYSTEM

A parent file system is a file system that contains data referenced by one or many clones. When you create a clone, you must specify which file system snapshot is used as the blueprint for the clone directory hierarchy and file data. The file system that contains this snapshot is the initial parent of the clone. The clone continues to reference the parent file system for any data they share in common unless the clone is detached.

A clone's parent file system can change after the clone is created. For example, if you delete a clone's parent file system, the file system parent's parent (the clone's grandparent) becomes the clone's new parent. The clone's data references are transferred to the new parent.

A cloned file system can be[detached from a parent file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm)to become an independent file system. SOURCE SNAPSHOT The snapshot used as a blueprint to create a clone. A snapshot is a point-in-time reference of a file system. You can take as many snapshots of a file system as you need, as often as you want. A parent file system can have snapshots available for many points along its lifetime. You can create a clone of a file system as it exists today, or as it existed in the past, as long as snapshots were taken of the file system at those times. For more information, see[Managing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm). FILE SYSTEM CLONE A clone is a new file system that's created based on a snapshot of existing file system. A clone automatically inherits the directory hierarchy and file data of the file system. All snapshots that exist in the parent file system are inherited by the clone, up to and including the snapshot that's used as the source of the clone. The`timeCreated`field of inherited snapshots are set to the time the clone operation was initiated. You can choose to keep or delete these snapshots. File system properties such as compartment, tags, display name, keys, and mount target export information aren't copied over from the parent. These properties must be specified manually.[File System Quotas](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm)are copied from the parent, but they're disabled and must be enabled manually. You can access the clone by creating an export for it and mounting it to an instance in the same manner as any other file system. See[Creating an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)and[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm). When a clone is created, it's assigned a unique OCID. A clone also contains the following information on its details page to let you track its relationships to other file systems and snapshots:
- Hydration: Indicates whether the clone is currently copying metadata from the source.
- Source snapshot: A link to the snapshot used to create the clone.
- Parent file system: A link to the parent file system of the clone.
- Clone root: Indicates whether this file system is the root of a clone tree.
- Descendants: Indicates whether this file system has been cloned.
- Clone attached status : Indicates whether this file system is attached to its parent file system.
- Clone count : The number of clones attached to the file system.

Cloned file systems are managed in the same way that any other file system is managed. See[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm)for information on how view the clone's details page, edit its properties, or delete the clone. CLONE TREE A clone tree is a group of clones that all descend from the same root file system. There is a transitive relationship between the root and the descendant clones. To delete the root of a clone tree, all its descendants must first be deleted. In this diagram, B, C, D, E, F, G are all clones. A→ B→ C→D and A→ B→ E→ F→ G are all part of a clone tree. File system A is the root of this clone tree, and it's the parent of file system B.
[BRANCH A clone tree branch is a set of clones whose data diverges from a common ancestor in the clone tree. In the preceding example, C and D are one branch of the clone tree, and E, F, and G are a second branch of the clone tree. Depth is a term used to describe how many clones are between one file system and another in a clone tree. In the preceding example, the depth from G to E is 2, and the depth from G to A is 4. Size is a term used to describe how many clones descend from a single parent. In the preceding example, the size of the clone tree from clone A is 6, but the size of the clone tree from F is only 1. HYDRATION Hydration is the process of copying metadata from the source to the clone. Hydration is an asynchronous process that starts when the clone is created. The clone is immediately available on creation and can be used for regular operations while hydration is in progress. You can see whether a clone is still in the process of hydration by visiting its details page. For more information, see[Getting a File System's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-file-system-details.htm).

## Limitations and Considerations

### Logical Organization

You can only create a clone in the same availability domain as its parent file system. See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for more information.

### Clone Hydration

Performance

Creating a clone is instantaneous and you can immediately access the clone for both READ and WRITE operations. However, there's a minor performance impact on both the parent and clone when accessing shared data while hydration is in progress. Performance impact is more significant on the clone than the parent. The duration of impact depends on the size of the source. Maximum throughput for[high performance mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm)isn't available until the clone is fully hydrated.

If the clone and parent are concurrently hydrating, hydration can affect the performance of the clone tree root. When creating clones, we recommend that you don't have more than 10 clones hydrating within a clone tree concurrently.

In this diagram, file system A is the root of the clone tree. File systems B, C, D, E, F, and G are all concurrently hydrating, so the performance of file system A might be impacted.

[

After hydration is complete, there's no further impact to the parent file system or clone tree root. You can see if hydration is in progress on a clone by viewing its details page. See[Getting a File System's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-file-system-details.htm)for more information.

Clone Tree Size and Depth

The number of clones in a clone tree that can hydrate concurrently is limited based on the following two values:
- Maximum Size: 10 This value represents the maximum allowed number of clones in a clone tree concurrently hydrating from a single parent file system.
- Maximum Depth: 5 This value represents the maximum number of unhydrated clones on a clone tree branch between the clone you're creating and its last hydrated ancestor.

Exceeding these limits causes the cloning operation to fail. Wait until enough clones complete hydration, and then try the operation again.

### Deleting Resources

File Systems

You can delete a file system if it is not the root of a clone tree. If a file system is the root of a clone tree, all descendant clones must first be deleted or detached.

If a file system is a parent to only a single clone, you can delete the parent file system and the cloned file system becomes an independent file system.

If a clone parent is deleted while any of its descendants are still hydrating, the parent remains in the DELETING state until hydration is complete. Metered space associated with the clone parent remains in use until all hydration is complete for all descendant clones. While a file system is still in a DELETING state, its parent, children, and siblings can't be deleted. A file system in a DELETING state can't be cloned. However, you can still clone its siblings or children.

After deletion is complete, the parent of the deleted file system becomes the new parent of the descendant clones.

Source Snapshot

You can delete the source snapshot of a clone. If the source snapshot is deleted while a clone of it's being hydrated, the source snapshot remains in the DELETING state until hydration is complete.

Parent Snapshots

A clone inherits all snapshots from the parent. If you delete a snapshot within a parent file system while hydration is in progress, the snapshot remains in the DELETING state until hydration is complete. After hydration is complete, you can delete any snapshot in the parent or clone file system at any time.

See instructions for deleting file systems in[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm).

See instructions for deleting snapshots in[Managing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm).

### Detaching Clones

A cloned file system can be detached from its parent file system. You might want to detach a clone if the parent was used as a template, or if a clone was used for[Disaster Recovery](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm).

To be eligible for detachment, the cloned file system must not be the parent of further clones in a clone tree. You can detach a clone in several ways:
- A clone can be detached when[it's created](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-clone.htm).
- A clone can be[detached](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm)at any point after the clone was created, if eligible.
- A clone can be detached when[deleting the parent file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-file-system.htm), if the parent file system has only a single clone.

While a clone is detaching, it can't be used to create another clone until the detachment is complete.
Note  
  
Detaching a clone is an asynchronous operation. Use the file system's Clone attached status to monitor the status of the detach operation.

## Metering and Billing

A parent file system is metered for all the data shared with its descendant clones. A clone is metered for its metadata and incremental changes made to its data. When a clone is deleted, all blocks that are referenced solely by that clone are reclaimed. If another clone is hydrating from the deleted clone, the referenced blocks are reclaimed after hydration is complete.

If you delete a parent clone, any data blocks shared by descendant clones can't be released. Allocated blocks referenced by descendant clones are transferred to the new clone parent (the clone parent's parent) for metering purposes. You are not metered more than once for data shared between multiple file systems.

If you[detach a clone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm), shared data blocks are copied to the cloned file system, resulting in an independent file system that's metered and billed as such.

For more information, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm).

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: Cloning a file system uses the`CreateFileSystem`API operation and requires the FILE_SYSTEM_CLONE permission. The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to clone file systems.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
