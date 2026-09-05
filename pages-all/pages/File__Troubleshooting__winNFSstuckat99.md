# File Copy or Delete is Stuck at 99%
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSstuckat99.htm
- Fetched: 2026-09-05 02:07 CDT

# File Copy or Delete is Stuck at 99%

Learn how to troubleshoot an issue where a Windows mounted file system can't complete a copy or delete operation.

Symptom: When you try to copy or delete a file in a file system mounted on a Windows instance, the process gets stuck at 99%.

Cause: By default, a Windows instance tries to access a mounted file system using Server Message Block (SMB) ports 139 and 445. Because File Storage file systems use an NFS mount, the process fails.
Solution: Reorder the network provider list to place`Nfsnp`first. Follow the steps in[To change the network provider order on Windows 2012+](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/winNFSerror53.htm#Access_to_File_System_using_UNC_Path_is_Slow_or_Fails__change-provider-order).
Important
