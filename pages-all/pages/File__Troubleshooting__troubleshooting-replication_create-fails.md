# Creating a Replication Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/troubleshooting-replication_create-fails.htm
- Fetched: 2026-09-05 02:06 CDT

# Creating a Replication Fails

When creating a replication resource, the File Storage service returns an error message.

## Error Code 400: Source and target file systems not compatible: snapshot mismatch

This error might occur when a file system is reused as a target file system.

For example, you can't re-establish a replication relationship between a source and target file system after deleting a prior replication if the snapshot configurations have changed on either side in the meantime.

Target a brand new file system when you[create the replication](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/fsreplication-creating-a-replication.htm).

## Error Code 409: File system not targetable: is or was exported

A replication resource can't be created if the file system selected to be the target is currently exported or was exported in the past. Once a target file system has been exported and used, there is no way to re-establish a replication relationship to it from a source file system.

Option 1 : Create a replication with a new target file system.

[Create a new replication resource](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/fsreplication-creating-a-replication.htm)using a new target file system. This requires a full base copy.

Option 2 : Create a replication with a clone of the target file system.

If the target file system still contains replication snapshots, you can re-establish a replication relationship using a clone that is created from any snapshot on the target file system. The replication will be created without the need for a full base copy.
Note  
  
The original file system can no longer be deleted because it is the root of the clone that was created.

## Error Code 409: File system not targetable: attached to a filesystem snapshot policy

A replication resource can't be created if the file system selected to be the target is currently attached to a[snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/snapshot-policies-and-schedules.htm).

If the file system had an active snapshot policy and schedules that created policy-based snapshots, the file system can't be reused as a replication target.

Option 1 : Create a replication with a new target file system.

[Create a new replication resource](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/fsreplication-creating-a-replication.htm)using a new target file system. This requires a full base copy.

Option 2 : Create a replication with a clone of the target file system.

If the target file system still contains replication snapshots, you can re-establish a replication relationship using a clone that is created from any snapshot on the target file system. The replication will be created without the need for a full base copy.
Note  
  
The original file system can no longer be deleted because it is the root of the clone that was created.

## Error Code 404: Exceeded file system replications limit (3)

The maximum number of replications for a file system has been exceeded.

[Remove an existing replication](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-replication.htm)if you need to create another. This limit can't be changed.
Note  
  
If you created a new file system as part of your failed attempt, you may delete it if needed. For more information, see[Managing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingfilesystems.htm)
