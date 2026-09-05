# Unable to Export a Target File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/troubleshooting-replication_unable-to-export-target.htm
- Fetched: 2026-09-05 02:06 CDT

# Unable to Export a Target File System

The File Storage service returns the error message "This file system is part of an ongoing Replication" and status code 409.

A target file system cannot be exported.

A target file system can only be exported after[deleting the replication resource](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/delete-replication.htm).

If you need immediate access to the replication target's data, clone the latest replication snapshot on the target side and then create an export on the clone. For more information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm)
