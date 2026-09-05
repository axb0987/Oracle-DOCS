# Disaster Recovery
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm
- Fetched: 2026-09-05 02:04 CDT

# Disaster Recovery

Learn about using File Storage replication for disaster recovery.

Important  
  
When making disaster recovery plans, ensure that you have enough available resources to create the clones, file systems, and mount targets necessary for unplanned failovers. Common disaster recovery scenarios require creation of at least one extra file system for each unavailable source file system. At least one mount target is required to provide access to file systems created during failovers. See[File Storage Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#File_Storage_Limits)for more information.

The following table shows the basic steps of recovery using File Storage replication:

Step Primary Availability Domain Condition Action
[1](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm#replication-disaster-recovery__failover)Failed[Failover to target file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm#replication-disaster-recovery__failover)
[2](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm#replication-disaster-recovery__prepare)Restored[Prepare to failback to source](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm#replication-disaster-recovery__prepare): Use reverse replication to sync data in source
[3](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm#replication-disaster-recovery__reestablish)Restored[Re-establish replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm#replication-disaster-recovery__reestablish)from source to target
Important  
  

Disaster recovery requires that you use clones of the source and target file systems. When creating file systems, you must remain within[File Storage service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#File_Storage_Limits). Clones are required because you can't use a file system that has been exported as a target file system. Cloning the file system creates a copy of the file system with no history of being exported.
- Creating a clone is instantaneous and you can immediately access the clone for both READ and WRITE operations. While hydration is in progress, a minor performance impact might be observed on both the parent and clone when accessing shared data.
- You can't delete a clone's parent file system unless the clone is[detached](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm). See[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm)and[Detaching a Clone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/detach-clone.htm)for more information.

## 1. Failover to Target

If the region containing the source file system (File System A) is inaccessible, clone the last applied replication snapshot on the target file system (File System B) to a new file system (File System C):
- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- 

Select the Replication Target name link.
- 

On the replication target's details page, select the Last Snapshot .
Important  
  
Note the Provenance OCID of the last applied snapshot. This identifies the snapshot on the source file system needed when you failback to the source. For more information, see[Identifying Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-managing-snapshots.htm#replication-managing-snapshots__identifying-snapshots).
- On the snapshot's details page, select Clone to use the snapshot to create a new file system (File System C). See[Cloning a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-clone.htm)for more information.
- [Delete the replication target resource from the target file system Details page (File System B).](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm)
Caution  
  
Deleting the replication target resource stops the replication process, but any in-progress replications might finish after the source is restored. If you don't delete the replication target, replication will resume when the source file system is restored, which can delete the snapshot needed in a planned failback to the source.
Tip  
  
If you're testing : The source availability domain is still available, so you can delete the replication resource from the source file system. Deleting the replication resource automatically deletes the replication target resource.
- [Create an export in the new file system (File System C).](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)
- [Mount the new file system (File System C).](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)

## 2. Prepare to Failback to Source

When the primary region is restored, prepare to failback to the source. Depending on your requirements, you may failback to a new, empty file system, or failback to a clone of the source file system. Use reverse replication to sync the data and bring it up-to-date.
Note  
  
Failback to a new file system requires a full base copy. You can use the[replication estimator](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-estimating-replication-time.htm)to decide if this scenario would be fast enough during disaster recovery.
- [Delete the`FAILED`replication resource in File System A.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
Tip  
  
If you're testing: You already[deleted the replication resource from the source file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm), so you can skip this step.
Note  
  
When the replication is deleted, the replication snapshot is converted to a user snapshot.
- Identify the snapshot common to the source file system (File System A) and the file system that you created when you failed over to the target (File System C). The snapshot you use should be in both the source and clone of the target.
- On the source file system (File System A), you can use the Provenance OCID you made note of earlier to identify this snapshot.
Caution  
  
The Last Snapshot could identify a snapshot that completed after the initial failover to target, not the snapshot used to create File System C.
- On File System C, you can find the last snapshot with a name such as`replication-snapshot- <replication_number> - <creation_time_UTC>`but a type of User . When you cloned the replication snapshot to create the file system, the snapshot type changed from Replication to User .
- 
- If you're using a clone of the original source file system for failback,[on the source file system (File System A), clone the snapshot identified in the previous step to create a new file system (File System D).](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm)
- If you're using a new, empty file system and a full base copy for failback, you can[create a new file system (File System D) without cloning](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm).
- 
- If you're using a clone of the original source file system for failback,[create a new replication where the clone of the original target file system (File System C) becomes the new source, and File System D becomes the new target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm). Wait for the replication cycle to complete and bring the File System D up-to-date with File System C. You can verify that the file systems are in sync by creating a snapshot on File System C and waiting for it to appear on File System D.
- If you're using a new, empty file system for failback,[create a replication using File System C as the source and your new, empty file system (File System D) as the target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm). Wait for the replication cycle to complete and bring the File System D up-to-date with File System C. You can verify that the file systems are in sync by creating a snapshot on File System C and waiting for it to appear on File System D.

## 3. Re-Establish Replication from Source to Target

Reestablish the original replication configuration. Migrate applications from File System C to File System D and stop writing to File System C. Then, create a replication from your source (File System D) to a new target clone (File System E).
- [Unmount the clone of the original target (File System C).](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm#mountingunixstyleos_topic_unmount)
- [Delete the replication resource from File System C.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
- [Create an export for File System D.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)
- [Mount File System D so that applications can access it.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)
- [Clone the last completely applied replication snapshot on File System D to create a new target file system (File System E).](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm)To determine the last completely applied snapshot, compare the name and timestamp of last replication snapshot listed in the source with the name and timestamp of the last replication snapshot in the target. The snapshot you use should be in both the source and target.
- [Create a new replication where the File System D is the source file system and File System E is the target file system.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm)
