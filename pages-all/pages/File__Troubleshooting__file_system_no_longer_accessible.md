# Mounted File System No Longer Accessible
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/file_system_no_longer_accessible.htm
- Fetched: 2026-09-05 02:05 CDT

# Mounted File System No Longer Accessible

A file system that was previously mounted and available is no longer accessible. Every command fails with a permission denied error, even for the owner or the root.

Cause 1: The file system's mount target or export was deleted.

File systems are made available to the network using an associated mount target. An export controls how NFS clients access the file systems when they connect to the mount target. A file system needs at least one export in an associated mount target to be available for mounting. Deleting a mount target or an export of a file system makes the file system unavailable.

Even if the file system is exported through multiple mount targets, any instance that uses the deleted mount target or export information to mount the file system loses access. See[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingmounttargets.htm).

Solution 1: Re-create the mount target and a new export for the file system.
- Re-create the mount target and export. For more information, see[Creating a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/create-mount-target.htm)and[Creating an Export](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/create-export.htm).
- If the mount target still exists, choose Select an Existing Mount Target . If the mount target has been deleted, choose Create a New Mount Target .
- If you're re-creating the mount target, you can re-use the same name, IP address, and hostname information as the old mount target. Click on Advanced Options to set the IP address and hostname.

Cause 2: You are using a customer-managed Vault key to encrypt the data in this file system and the key has expired. The file system relies on a valid key for every operation.

Solution 2: Renew and validate the key to resume normal operation. See[Encrypting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/encrypt-file-system.htm)
