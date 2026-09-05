# Snapshots Stuck in DELETING State
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/snapshots_in_deleting_state.htm
- Fetched: 2026-09-05 02:06 CDT

# Snapshots Stuck in DELETING State

A File Storage snapshot remains in DELETING state instead of progressing to DELETED.

Cause: One or more clones, created from the snapshot that is being deleted, have hydration in progress.

Solution: Wait for the hydration process to complete, which will then allow the snapshot to be deleted. The hydration status can be seen on the[File System details](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/get-file-system-details.htm)page in the OCI Console. For more information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm)
