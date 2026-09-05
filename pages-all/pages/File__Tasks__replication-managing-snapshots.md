# Replication and Snapshots
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-managing-snapshots.htm
- Fetched: 2026-09-05 02:04 CDT

# Replication and Snapshots

Learn how File Storage snapshots are used in replication.

## Types of Snapshots

Several types of snapshots are used in File Storage. You might come across any type when you use replication. It's helpful to understand the difference between them, how to identify them, and how they're treated during replication:

User-created snapshots: You create these snapshots when you want to preserve a point-in-time view of the file system. File systems can have one or many user-created snapshots. See[Managing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm).

Policy-based snapshots: The system automatically creates these snapshots according to snapshot policies and schedules. See[Policy-Based Snapshots and Scheduling](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm).

Replication snapshots: Automatically created by a replication resource. Replication snapshots are used to transmit data from the source file system to the target file system. Replication snapshots follow the naming pattern`replication-snapshot- <replication_number> - <creation_time_UTC>`. You can't modify a replication snapshot. Only one replication snapshot is preserved for disaster recovery at a time.

Replicated snapshots: A replicated snapshot is a snapshot of any type that has been copied from a source file system into a target file system.

## Identifying Snapshots

Each snapshot has the following identifiers:
- Snapshot OCID: The unique OCID (Oracle Cloud Identifier) for the snapshot.
- Provenance OCID: An OCID (Oracle Cloud Identifier) identifying the parent file system from which this snapshot was cloned, if any. If the snapshot wasn't the result of cloning, this value is the same as the snapshot OCID.

You can identify the type and history of a snapshot by comparing its snapshot OCID and Provenance OCID values.
- When you manually create a snapshot in a file system, the snapshot's OCID and Provenance OCID value are the same .
- When you clone a file system, all its snapshots are also cloned. When a snapshot is created by cloning, the cloned snapshot's OCID and Provenance OCID values are different . The Provenance OCID is the OCID of the clone's parent file system .
- When you replicate a file system, all of its snapshots are also replicated by default. When a snapshot is created by replication, the replication snapshot's Provenance OCID is the same as the Provenance OCID of the original snapshot.

Method of creation Snapshot OCID Provenance OCID
Manual, or by a snapshot policy New Snapshot's OCID (Oracle Cloud Identifier) New Snapshot's OCID (Oracle Cloud Identifier)
Cloned New Snapshot's OCID (Oracle Cloud Identifier) Parent File System OCID (Oracle Cloud Identifier)
Replicated New Snapshot's OCID (Oracle Cloud Identifier) Copied Snapshot's OCID (Oracle Cloud Identifier)

## Replicated Snapshots

By default, all snapshots that exist in the source file system are replicated in the target file system, including policy-based snapshots. If you have many snapshots in the file system, it can impact how long replication takes. If you don't want to replicate all snapshots, you can take the following steps before you set up your disaster recovery replication.

For example, suppose you want to replicate File System A, but only replicate five of its snapshots:
- [Create a clone of File System A (Clone A)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm).
- [Delete snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-snapshot.htm)that you don't want to replicate from Clone A.
- [Create a new unexported file system (File System B)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm).
- [Create a replication from Clone A to File System B](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm). Since it only has five snapshots, replication will be faster than it would be if you kept all the original snapshots.
- Wait until the first replication cycle is complete.
- [Delete the replication from Clone A to File System B.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
- [Create a new replication from File System A to File System B.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm)No older snapshots are copied; only new data updates are transferred.
- [Delete Clone A.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-file-system.htm)
