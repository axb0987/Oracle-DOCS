# Setting a File System's Reported Size
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size-mt.htm
- Fetched: 2026-09-05 02:02 CDT

# Setting a File System's Reported Size

Learn how to set a File Storage file system's reported size through a mount target.

The File Storage service reports file system capacity as 8589934592 gibibytes (GiB) and 8589934592 gibiinodes (GiI) by default. Sometimes, application installers perform a space requirement check before running an installation process but can't correctly interpret the reported size or reported inodes of the file system. When this occurs, you can define the file system size reported to the OS by setting the Reported Size or Reported Inodes value in the file system's mount target. Typically, setting the size to 1024 GiB and the inodes to 1024 GiI permits successful installation.
Important  
  
Changing the Reported Size or Reported Inodes for a mount target affects all file systems exported by the mount target. Changing these values doesn't limit the amount of data you can store.
Important  
  
There can be a delay of up to 1 hour when reporting file system usage, either in the Console or by using the`df`command. For more information, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size-mt.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size-mt.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size-mt.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select the Reported Size (GiB) or the Reported Inodes (Gil) edit icon.
- Enter the maximum size in gibibytes or the maximum inodes in gibiinodes you want the File Storage service to report.
- Select the Save icon.
- 

Use the[`fs export-set update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export-set/update.html)command and required parameters to set the reported size of the file system made available through the mount target's exports:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateExportSet](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSet/UpdateExportSet)operation to change the reported size of a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
