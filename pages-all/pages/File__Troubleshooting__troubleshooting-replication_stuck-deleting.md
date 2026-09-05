# Unable to Delete Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/troubleshooting-replication_stuck-deleting.htm
- Fetched: 2026-09-05 02:06 CDT

# Unable to Delete Replication

The replication is not getting deleted, and the replication reports a DELETING state for a long time.

A replication can go into the DELETING state as soon as a delete command is issued, but deletion is an asynchronous process. The total time taken to delete the replication will vary depending on the delete mode chosen when deleting the replication resource. For more information, see[Deleting a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-replication.htm).

After the replication process finishes its actions, the File Storage service deletes the replication.
Tip  
  
If the target file system will no longer be needed after the replication is deleted, you can[delete the target file system](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-file-system.htm)
