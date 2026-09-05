# Creating a Snapshot on a Replication's Target File System Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/troubleshooting-replication_create-snapshot-fails.htm
- Fetched: 2026-09-05 02:06 CDT

# Creating a Snapshot on a Replication's Target File System Fails

Creating a snapshot on the replication target file system fails with the message, "This file system is part of an ongoing Replication," and returns Status Code 409.

Users can't create snapshots on a target file system.

If there is a need to create a snapshot of the target file system, create the snapshot on the source file system. The snapshot will get transferred to the target during the next replication cycle.

Alternatively, you can[delete the replication](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-replication.htm)
