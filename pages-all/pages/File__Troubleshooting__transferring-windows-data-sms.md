# Copying data to File Storage using Robocopy, Terracopy, or Xcopy is slow in Windows
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/transferring-windows-data-sms.htm
- Fetched: 2026-09-05 02:06 CDT

# Copying data to File Storage using Robocopy, Terracopy, or Xcopy is slow in Windows

Windows copy utilities scan a directory for every batch of writes during a copy. Directory scans increase as the copy utility writes files, resulting in a decrease in write throughput and a slow copy rate.

Solution: Don't use Windows copy utilities for large data copies to File Storage. Instead, use an OCI Linux instance to perform large copies using the parallel tools that come with an OCI Linux instance. Mount the Windows Server Message Block (SMB) share as a Common Internet File System (CIFS) share and use a copy tool such as PARCP or FPSYNC to transfer data.

This topic describes how to transfer data from a Windows Server Message Block (SMB) share to a File Storage file system. Because the SMB protocol and the NFS protocol used by File Storage aren't compatible, an instance that can mount both the NFS file system and the SMB share is used to create a bridge between them.
- Identify or create a Linux instance in Oracle Cloud Infrastructure that has network access to both the File Storage file system and the Windows SMB share.
- Open a terminal on the instance.
- 

Type the following to install the Common Internet File System (CIFS) utility and verify its installation:
```

```

- 

Mount the Windows SMB share as a CIFS share:
- 

Create a mount point directory. For example:
```

```

- 

Mount the CIFS share:
```

```

For example:
```

```

- Copy the files from the CIFS share to the mounted file system using the`parcp`utility from the File Storage Parallel Tools suite or`fpsync`. For installation information about`parcp`, see[Using File Storage Parallel Tools](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/using_file_storage_parallel_tools.htm). For information about`fpsync`, visit[`fpsync`Manual Page](http://manpages.ubuntu.com/manpages/xenial/man1/fpsync.1.html).

For example:
```

```

```

```
