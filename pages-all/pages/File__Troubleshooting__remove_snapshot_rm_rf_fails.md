# Removing Snapshots With RM -RF Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/remove_snapshot_rm_rf_fails.htm
- Fetched: 2026-09-05 02:06 CDT

# Removing Snapshots With RM -RF Fails

Learn how to troubleshoot the inability to use the`rm`operation to delete a snapshot from a mounted file system.

Symptom: Using the`rm -rf .snapshot/<snapshot_folder>`operation to delete a snaphot from a mounted file system fails.

Cause: Snapshots are read-only and can't be deleted by running`rm -rf .snapshot/<snapshot_folder>`from a client instance.

Solution:[Delete the snapshot using the Console, CLI, or API](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-snapshot.htm)
