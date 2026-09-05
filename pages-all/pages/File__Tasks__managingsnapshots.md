# Managing Snapshots
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm
- Fetched: 2026-09-05 02:04 CDT

# Managing Snapshots

The File Storage service supports snapshots for data protection of your file system. Snapshots are a consistent, point-in-time view of your file systems. Snapshots are copy-on-write, and scoped to the entire file system. The File Storage service encrypts all file system and snapshot data at rest.

You can take as many snapshots as you need, and you can use[policy-based snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm)to create snapshots automatically according to set schedules.

Data usage is metered against differentiated snapshot data. If nothing has changed within the file system since the last snapshot was taken, the new snapshot does not consume more storage. For more information, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm).

Snapshots are accessible under the root directory of the file system at`.snapshot/ name`. When you use an NFSv3 client to perform operations such as`ls`,`du`, or`find`on the snapshot directory, the service automatically exports the directory. The client uses`nfs_d_automount()`to detect and mount the directory. After the directory is detected and mounted the first time, the client mounts the directory automatically.

For data protection, you can use[file system replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm)to copy data in one file system to another file system in the same region or a different region. You can also use a tool that supports NFSv3 to copy data to a different[availability domain, region,](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filestorageoverview.htm#Regions)file system,[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm), or remote location. See[Backing Up Snapshots to Object Storage Using rclone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/backing-up-snapshots-to-object-storage.htm)for an example.

For best performance, we recommend that you use the parallel tar (`partar`) and parallel copy (`parcp`) tools provided in the File Storage Parallel File Toolkit for this purpose. These tools work best with parallel workloads and requests. The Parallel File Toolkit is available for Oracle Linux, Red Hat Enterprise Linux, and CentOS. You can use`rsync`or regular`tar`for other operating system types. See[Installing the Parallel File Tools](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#install_par_tools)for more information.
Tip  
  
Watch a[video](https://www.youtube.com/watch?v=JRu5_8sBBos&t=0s&list=PLvlciYga5j3x-i-cJGudmpGuUupUliIck&index=4)about protecting data with snapshots in File Storage.

You can perform the following snapshot management tasks:
- [Creating a Snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot.htm)
- [Creating a Snapshot from a Unix-style Instance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot-unix-instance.htm)
- [Creating a Snapshot Policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm)
- [Listing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-snapshots.htm)
- [Getting a Snapshot's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-snapshot-details.htm)
- [Tagging a Snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-snapshot.htm)
- [Changing Snapshot Expiration Time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm)
- [Locking a Snapshot Using Resource Lock](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-snapshot.htm)
- [Deleting a Snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-snapshot.htm)
- [Restoring from a Snapshot on a Unix-style Instance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/restore-from-snapshot.htm)
- [Backing Up Snapshots to Object Storage Using rclone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/backing-up-snapshots-to-object-storage.htm)

## Snapshot Types

User-created snapshots: You create these snapshots when you want to preserve a point-in-time view of the file system. File systems can have one or many user-created snapshots.

Policy-based snapshots: The system automatically creates these snapshots according to snapshot policies and schedules. A policy-based snapshot uses the following naming pattern:

`<policy_prefix> ​_ <schedule_prefix> ​_ <creation_timestamp> ​_ <schedule_type> ​_ <retention_in_ISO-8601_duration>`

For example:`Policy1_SchedulePrefix_20220201181313_Hourly_P1DT1H`

If the snapshot policy and schedules don't include a prefix, snapshots use a default prefix of`FSS_ <policy_name>`. For more information, see[Policy-Based Snapshots and Scheduling](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm).

Replication snapshots: Automatically created by a replication resource. Replication snapshots are used to send data from the source file system to the target file system. A replication snapshot uses the following naming pattern:`replication-snapshot​- <replication_number> ​- <creation_time_UTC>`

You can't modify a replication snapshot. Only one replication snapshot is preserved for disaster recovery at a time. Older replication snapshots are deleted. See[File System Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm).

## Managing Clone and Replication Snapshots

Cloning and replicating file systems also clone and replicate the file system's snapshots. This section describes how to avoid replicating snapshots you don't need, how to identify snapshots to clone for replication, and how to identify snapshots you can safely discard.

### Identifying Snapshots

Each snapshot has the following identifiers:
- Snapshot OCID: The unique OCID (Oracle Cloud Identifier) for the snapshot.
- Provenance OCID: An OCID (Oracle Cloud Identifier) identifying the parent file system from which this snapshot was cloned, if any. If the snapshot was not the result of cloning, this value is the same as the snapshot OCID.

You can identify the type and history of a snapshot by comparing its snapshot OCID and Provenance OCID values.
- When you manually create a snapshot in a file system, the snapshot's OCID and Provenance OCID value are the same .
- When you clone a file system, all its snapshots are also cloned. When a snapshot is created by cloning, the cloned snapshot's OCID and Provenance OCID values are different . The Provenance OCID is the OCID of the clone's parent file system .
- When you replicate a file system, all its snapshots are also replicated by default. When a snapshot is created by replication, the replication snapshot's Provenance OCID is the same as the Provenance OCID of the original snapshot.

Method of creation Snapshot OCID Provenance OCID
Manual New Snapshot's OCID (Oracle Cloud Identifier) New Snapshot's OCID (Oracle Cloud Identifier)
Cloned New Snapshot's OCID (Oracle Cloud Identifier) Parent File System OCID (Oracle Cloud Identifier)
Replicated New Snapshot's OCID (Oracle Cloud Identifier) Copied Snapshot's OCID (Oracle Cloud Identifier)

## Monitoring Snapshots

[Policy-based snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm)enable automatic snapshot creation and deletion. Because the File Storage service handles these operations for you after the snapshot policy and schedules are created, we recommend using[Events](https://docs.oracle.com/iaas/Content/Events/home.htm)to monitor policy-based snapshots.

You can monitor for the following[snapshot events](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#file-events):
- Manual snapshot creation
- Policy-based snapshot creation
- Attempts to create a policy-based snapshot that are rejected
- Attempts to create a policy-based snapshot that are skipped
- Attempts to create a policy-based snapshot that are throttled
- Manual deletion of snapshots
- Deletion of snapshots with an expiration date
- Attempts to delete a policy-based snapshot that are throttled

An event's`additionalDetails`property contains more information you can use to understand the event. For more information, see[Contents of an Event Message](https://docs.oracle.com/iaas/Content/Events/Reference/eventenvelopereference.htm).
Note  
  
If a high number of policy-based snapshots are scheduled to be created or deleted for a file system at the same time, the File Storage may temporarily throttle the request and create or delete the snapshot at the next available opportunity.

For more information, see[Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm).

## Details About Your Snapshot

The Details page provides the following information about your snapshot: SNAPSHOT OCID Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). You need your snapshot's OCID to use the Command Line Interface (CLI) or the API. You also need the OCID when contacting support. See[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). CREATED The date and time that the snapshot was created. SNAPSHOT TIME The date and time the snapshot was taken. This value might differ from the date and time that the snapshot was created if it was cloned or replicated. DESCENDANTS Indicates whether the this snapshot has been used to create a clone. See[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm). PROVENANCE OCID An OCID (Oracle Cloud Identifier) identifying the parent file system from which this snapshot was cloned, if any. If the snapshot was not the result of cloning, this value is the same as the snapshot OCID. For more information, see[Managing Clone and Replication Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#fsreplication-managing-replication-snapshots). TYPE Indicates whether the snapshot was created by a user, according to a[snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm), or by[Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm). SNAPSHOT POLICY The[snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm)used to create the snapshot. EXPIRATION TIME Each policy-based snapshot is created with a retention period and expiration time. At the end of the retention period, the snapshot expires and the system deletes it. You can[modify or remove](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm)an existing expiration time, or add an expiration time to a user-created or policy-based snapshot. EXCLUSIVE BYTES Amount of storage unique to this snapshot and reclaimed when it's deleted.

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to create and delete snapshots.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
