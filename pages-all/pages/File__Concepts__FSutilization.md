# File System Usage and Metering
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm
- Fetched: 2026-09-05 02:02 CDT

# File System Usage and Metering

Learn about how usage and metering are calculated for your file systems, to help you understand and manage your service costs. Understand different ways to see your file system, clone, and snapshot utilization and the differences in reporting that can occur depending on which method you use.

## Overview

File Storage service provisioning is fully managed and automatic as your utilization scales. For more information, see[Space Allocation](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm#Space).

Here are the methods you can use to view a file system, clone, and snapshot usage:
- The File Storage service reports metered file system utilization and updates hourly. The metered file system utilization comes from the`meteredBytes`value in the API, and represents the authoritative utilization value that's used to count your service cost. You can access the reported utilization for each of your file systems using the[Console, the Command Line Interface (CLI), or the API](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingfilesystems.htm). For more information, see the following section[File System Metered Utilization](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm#Metering_and_Service_Cost__Metered).
- [file system quotas](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/file-system-quotas.htm)set soft or hard limits on file system utilization or utilization by specific users and groups. Administrators can[list quotas](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/quotas-list.htm)or use metrics and events to monitor requests that exceed quotas. Quotas only reflect live data usage, not metadata or snapshots.
- The File Storage service supports Network File System (NFS) protocol, so you can use the`df`or`du`command from your instance command line tool to see usage for mounted file systems. However, the usage reported by`du`can differ from both the`meteredBytes`value and the`df`value. For more information, see[Using DF and DU Commands](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm#Using).

## Space Allocation

The File Storage service allocates space in blocks of variable size in a way that minimizes total customer cost and optimizes performance. Other storage systems might allocate blocks differently than Oracle Cloud Infrastructure File Storage. If you copy files from another storage device to your Oracle Cloud Infrastructure file system, you might see minor differences when you compare the physical file size before and after copying.

## Metering and Service Cost

This section describes aspects of file system usage and how they affect your overall service costs.

### File System Metered Utilization

The File Storage service reports metered utilization size for each file system. The metered utilization size is updated on an hourly cycle. You can see the metered Utilization size in the Console on the Details page of the file system. This value comes from the File Storage service API`meteredBytes`property which is the total number of bytes consumed by the file system. If the file system is a clone of another file system, the clone is only metered for the differentiated data unique to the clone.

The`meteredBytes`value is updated asynchronously with respect to updates to the file system. Your usage charges are calculated based on the`meteredBytes`value.

You can also use the CLI or API to obtain this information. See[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingfilesystems.htm)for instructions about how to view your file system utilization.
Important  
  
When you add or remove files from your file system, it can take the File Storage service up to one hour to report the change in metered size.

### Snapshot Metered Utilization

A snapshot is a point-in-time view of your file system. Snapshots initially consume no additional usage in the file system, because they reference the original data instead of duplicating it, limiting usage cost. A snapshot doesn't change which blocks it references after it's taken.

Snapshot data usage is metered against differentiated data only. If nothing has changed within the file system since the last snapshot was taken, a new snapshot does not consume more storage. The metered size of snapshots is included in the reported`meteredBytes`value of the file system it belongs to.

For example:
- Let's say you create a file system called MyFileSystem and add File1. The new file system now contains 1 GB including metadata. After the hourly update cycle is complete, the total`meteredBytes`shown by the File Storage service is 1 GB.
- 

Next, you create a snapshot of MyFileSystem named Snapshot1. After the hourly update cycle is complete, the total`meteredBytes`shown by the File Storage service remains at 1 GB, because there's no differentiated data yet.
- 

You then overwrite the first 0.5 GB of File1. Now, MyFileSystem has a file that is different than the version previously captured in Snapshot1. The`meteredBytes`value is 1.5 GB, because the differentiated data between the live file system and the snapshot is 0.5 GB.

1 GB (snapshot) + 0.5 GB (differentiated data) = 1.5 GB
- If you then delete File1. MyFileSystem now has a`meteredBytes`value of 1 GB, which represents just the usage for Snapshot1.
- Finally, delete Snapshot1. Deleting the snapshot removes its references to the file data. Provided no other snapshots reference the file data , the space is relinquished and utilization returns to zero.

### Clone Metered Utilization

The initial metered cost of a file system clone is based on its metadata only, because clones reference the parent file system's data instead of duplicating it.

A clone's parent file system is metered for all the data shared with its descendant clones. A clone is metered for all its metadata and incremental changes made to its data. When a clone is deleted, all blocks that are referenced solely by that clone are reclaimed. If another clone is hydrating from the deleted clone, the referenced metadata blocks are reclaimed after hydration is complete.

If you delete a parent clone, any data blocks shared by descendant clones cannot be released. Allocated blocks referenced by descendant clones are transferred to the new clone parent (the parent's parent) for metering purposes. You are not metered more than once for data shared between multiple file systems.

For example:
- Let's say you create a clone of FileSystemA called Clone1. At the time of creation, and before any data is altered:
- FileSystemA (parent) is metered for its data and metadata.
- Clone1 is metered only for its metadata.
- Then, you create a new 1GB file in Clone1 called File1:
- FileSystemA (parent) is metered for the data it shares with Clone1 (clone).
- Clone1 is metered for its metadata plus the 1GB of changed data incurred by File1.
- FileSystemA's parent is OriginalRoot. It is the root of the clone tree. Let's say you delete FileSystemA:
- OriginalRoot becomes the new parent of Clone1.
- OriginalRoot is metered for the data it shares with Clone1.
- Clone1 is metered for its metadata plus the 1GB of changed data incurred by File1.

### Replication Metered Utilization

After you enable replication for a file system, the file system is replicated to a target file system in the specified region and availability domain. File Storage is metered for your total capacity stored on disk for both the source and target file systems. Source and target file systems are priced at the same rate.

Your bill includes any applicable network costs for the replication process between regions. As part of the replication process, all data being updated on the source file system is transferred to the file system replica, so file systems with continual updates incur higher network costs. There is no additional charge for cross-availability domain bandwidth within the same region or inbound data transfer.

Many replication failback scenarios use a clone of an original source file system. Cloning the source from the last completely applied snapshot ensures that the source and target are compatible. You can also choose to use a new file system for failback. However, using a clone of the original source file system tends to be both faster and more cost effective than using a new file system. For example:
- Let's say you create a source file system, File System A, and a target file system, File System B. You set up replication from File System A (source) to File System B (target). File System A is mounted and data is written to it from instances or applications. The replication process duplicates data updates from File System A on File System B.
- File System A (source) is metered for its data and metadata. As data is updated, increased cost may be incurred.
- User-created snapshots for File System A are metered against differentiated data in File System A only.
- File System B (target) data is identical to File System A, and is metered for its data and metadata.
- User-created snapshots for File System B are identical to File System A and metered against differentiated data only.
- Replication-created snapshots are metered against differentiated data only, and are deleted after a replication cycle is complete.
Note  
  
Until a replication cycle is complete, the data and metatada usage for File System B may be different for File System A.
- Then, at some point the availability domain that contains File System A fails, and you fail over to File System B. File System B is mounted to application instances, and data is written to it.
- File System A is metered for its existing data and metadata. Since no data is updated, there are no cost changes.
- User-created snapshots for File System A continue to be metered against the existing differentiated data in File System A only.
- File System B data is metered for its data and metadata. As data is updated, increased cost may be incurred.
- User-created snapshots for File System B are metered against differentiated data in File System B only.
- No replication snapshots are created.
- After the availability domain that contains File System A is restored, you reverse replication to copy updated data from File System B back to File System A and bring them back into sync. You create a clone of File System A called Clone1. At the time of creation, and before any data is altered:
- File System A (original replication source, clone parent) is metered for its data and metadata.
- Clone1 is metered only for its metadata.
- As the replication from File System B to Clone1 progresses, data is copied from File System B To Clone1.
- File System A (old replication source, clone parent) is metered for its data and metadata. Since no data is updated, there are no cost changes.
- User-created snapshots for File System A continue to be metered against the existing differentiated data in File System A only.
- Clone1 (new target) is metered for the differentiated data between it and File System A. As data is replicated to Clone1 from File System B, increased cost is incurred.
- File System B (new source) is metered for its data and metadata.
- User-created snapshots for File System B are metered against differentiated data in File System B only.
- Replication-created snapshots are metered against differentiated data between Clone1 and File System B only, and are deleted after a replication cycle is complete.

For more information, see[File System Replication](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/FSreplication.htm).

### Metadata Metered Utilization

Files in the file system require space to be allocated for metadata.`512`bytes are required for each directory entry, and`8192`bytes are required for each symlink. Multiple hardlinks to a file create multiple directory entries for the file, and increases the metadata utilization. This utilization is included in the`meteredBytes`value of the file system to which it belongs.

## Using DF and DU Commands

You can use`df`or`du`commands from your instance command-line application to view usage information about your file system. To use these commands to view file system usage, the file system must first be mounted to the instance. See[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/mountingfilesystems.htm)for instructions on mounting your file system.

### How the Commands Work
- `df`provides the amount of storage metered for your file system. The metered storage includes live usage, snapshots, attached clones. The result can be up to an hour out of date. When quota enforcement is enabled on the file system,`df-total`reflects the file system quota limit as set and`df-used`reports file system quota usage.
- `du`provides the storage used by a directory hierarchy. The`du`command walks the directory tree, and if your hierarchy is large, it can take a long time to run and return results. When quota enforcement is enabled on the file system,`_du --exclude=.snapshot <FSS_mountpoint>_`reflects the`df-used`, which in turn reflects the file system quota usage.

### How Results can Differ

The following sections explain how and why`df`and`du`results differ:
- [DF and DU report snapshot and clone utilization differently](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm#Using__snapshots-clones)
- [DF and DU count hard links differently](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm#Using__hard-links)
- [DF and DU count symlinks and metadata differently](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm#Using__symlinks)

### DF and DU report snapshot and clone utilization differently

A snapshot is a point-in-time view of a file system. Snapshots reference unchanged file system data instead of duplicating it. The file system blocks that the snapshot references don't count towards the snapshot utilization. Only differentiated data increases the snapshot utilization.

The same behavior is true for file system clones. Clones reference the data they share with their parent file system. The file system blocks that the clone references don't count toward the clone's utilization. Only differentiated data increases clone utilization.
- 

The`df`command retrieves information provided by the File Storage service using the NFS FSSTAT call. The NFS FSSTAT call accounts correctly for the way that snapshots and clones reference file system data. Only utilization caused by differentiated data is reported.

Snapshots are accessible under the root directory of the file system at`.snapshot/ name`. When you use an NFSv3 client to perform operations such as`ls`,`du`, or`find`on the snapshot directory, the service automatically exports the directory. The client uses`nfs_d_automount()`to detect and mount the directory. After the directory is detected and mounted the first time, the client mounts the directory automatically.
Note  
  
If you've purged a file system, but the file system has snapshots or clones, the`df`command still reports the underlying blocks. Purging a file system without deleting snapshots or clones doesn't remove those blocks.
- The`du`command descends the file system tree and uses each file's size attribute to total up the space used. When you create a snapshot or a clone, it copies the original size attribute for each file. So, if you run the`du`command, the snapshot reports the file system's size at the time the snapshot was taken not necessarily the snapshot's actual current utilization. Clones initially report the parent file system's size at the time the source snapshot was taken. When changes are made to clone data,`du`begins to report new size attributes for updated files only.

For example,
- 

Let's say you create file system called "MyFileSystem". You then add a 1 GB file called "FileA" to the file system. Here's how each command would report size.

For.. du reports...

df reports...
FileA 1 GB 1 GB
MyFileSystem 1 GB 1 GB
- 

You then create "Snapshot1". The snapshot is placed in the`/.snapshot`folder of MyFileSystem. Here's how each command would report size:

For... du reports...

df reports...
FileA 1 GB 1 GB
Snapshot1 1 GB 1 GB

MyFileSystem 2 GB 1 GB
- `du`reports 1 GB for Snapshot1 because it reports the copied file size attribute of FileA, which is 1 GB.
- 

You then use "Snapshot1" to create a clone called "Clone1". Here's how each command would report size:

For... du reports...

df reports...
FileA 1 GB 1 GB
Snapshot1 1 GB 1 GB

MyFileSystem 2 GB 1 GB
Clone1 2 GB 0 GB
- `df`reports 0 GB for Clone1 because the data hasn't changed yet, so there is no space allocated for differentiated data.
- `du`reports 2 GB for Clone1 because it reports the copied file size attribute of FileA, which is 1 GB, and the size of Snapshot1, which is another 1 GB.
- 

You add a 1 GB file called "FileB" to the cloned file system. Here's how each command would report size:

For... du reports...

df reports...
FileA 1 GB 1 GB
Snapshot1 1 GB 1 GB

MyFileSystem 2 GB 1 GB
Clone1 3 GB 1 GB
FileB 1 GB 1 GB
- `df`reports 1 GB for Clone1 for the differentiated data added in FileB.
- `du`reports 3 GB for Clone1 because it reports the sum of the copied file size attributes of FileA, FileB, and Snapshot1.
Important  
  
Charges are calculated using the`meteredBytes`value. The utilization size reported by`du`can be much larger than`meteredBytes`value.`df`reports the same value as`meteredBytes`, so you can use it to accurately view the file system size.

### DF and DU count hard links differently
- `df`counts each file only once.
- `du`may count files with hard links more than once.

### DF and DU count symlinks and metadata differently
- `df`reports the utilization of bytes required by File Storage for metadata and symlinks, even on empty files.
- `du`
