# Folder Becomes Unresponsive When Opened
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/windows-server-2022-directory-slow.htm
- Fetched: 2026-09-05 02:07 CDT

# Folder Becomes Unresponsive When Opened

When opening a folder or running a`dir`command on a File Storage file system mounted to a Windows Server 2022 system, the action doesn't complete.

Cause : This is a known issue with how Windows Server 2022 handles NFS requests. The issue doesn't occur in earlier Windows releases, such as Windows Server 2019, for the same file system using same mount target.

The NFS client uses`READDIR`to request a directory's contents. It uses the cookie value in responses to retrieve results in batches until the NFS client gets a reply with an`EOF=1`response, indicating that no more files are in the directory.

When this problem occurs, instead of using the correct cookie value from the most recent batch, the NFS client selects an incorrect cookie value of 0. This causes the`READDIR`process to continually repeat.

Solution : Work with support to test possible resolutions.

Some users have disabled`READDIR`as described in[Slow Data Copy in Windows Compared to Copy of Same Data in Linux](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/windows-directory-scan-slow.htm), but many applications require`READDIR`to function.

For other users, Microsoft has suggested increasing the directory buffer size by adding a new registry setting called`MaxDirCacheSize`. Because these details aren't found in official Microsoft documentation, create a Microsoft service request or[ask Oracle support](https://support.oracle.com)to do so on your behalf. In the request, ask about the difference in performance when Windows 2022 is working with same remote NFS storage as other Windows versions. Ask for the appropriate value for`MaxDirCacheSize`
