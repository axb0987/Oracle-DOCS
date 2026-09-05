# Setting a File System's Reported Size
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm
- Fetched: 2026-09-05 02:02 CDT

# Setting a File System's Reported Size

Learn how and why to change the reported size of a File Storage file system.

The File Storage service reports file system capacity as 8589934592 gibibytes (GiB) and 8589934592 gibiinodes (GiI) by default. Sometimes, application installers perform a space requirement check before running an installation process but can't correctly interpret the reported size or reported inodes of the file system. When this occurs, you can define the file system size reported to the OS by setting the Reported Size or Reported Inodes value in the file system's mount target. Typically, setting the size to 1024 GiB and the inodes to 1024 GiI permits successful installation.
Important  
  
Changing the Reported Size or Reported Inodes for a mount target affects all file systems exported by the mount target. Changing these values doesn't limit the amount of data you can store.

Because users can change these two values at any time in a file system's lifecycle, it's important to keep Reported Size set to a value large enough to meet the needs of the OS and its applications. If the value is too small, the OS could report insufficient space, such as when running the`df`command on a Linux OS.
Note  
  
There can be a delay of up to 1 hour when reporting file system usage, either in the Console or by using the`df`command. For more information, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Exports .
- Select the mount target.
- On the mount target's details page, from the Actions menu, select Edit reported size or Edit reported Inodes .
- Enter the maximum free space in gibibytes or the maximum inodes in gibinodes you want the File Storage service to report.
- Select Update .
- 

Use the[`fs export-set update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export-set/update.html)command and required parameters to change the reported size of the file systems exported by the export set:

```

```

Important  
  
The maximum free space setting affects each export in the export set. Setting the maximum free space does not limit the amount of data you can store.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateExportSet](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSet/UpdateExportSet)operation to change the reported size of a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
