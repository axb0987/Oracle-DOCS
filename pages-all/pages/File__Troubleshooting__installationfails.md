# Application Installation Fails Due to Too Much or Too Little Available Capacity
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/installationfails.htm
- Fetched: 2026-09-05 02:06 CDT

# Application Installation Fails Due to Too Much or Too Little Available Capacity

Some application installers perform a capacity check before running an installation process. Sometimes an installation fails due to too much or too little available capacity on the File Storage file system. 32-bit applications, such as Oracle Universal Installer, might not correctly interpret file system size.

The File Storage service reports file system capacity as 8589934592 gibibytes (GiB) and 8589934592 gibiinodes (GiI) by default. Sometimes, application installers perform a space requirement check prior to running an installation process but can't correctly interpret the reported size or reported inodes of the file system. When this occurs, you can define the file system size reported to the OS by setting the Reported Size or Reported Inodes value in the export set of the file system's mount target.
Important  
  
Changing the Reported Size or Reported Inodes for a mount target affects all file systems exported by the mount target. Changing these values does not limit the amount of data you can store.

If your application installation is failing because of too little available space, you can expand the reported available free space. If your application installation is failing because of too much reported available free space, you can reduce it. Typically, setting the size to 1024 GiB and the inodes to 1024 GiI permits successful installation.
Important  
  
There can be a delay of up to 1 hour when reporting file system usage, either in the Console or by using the`df`command.

For more information, see[Setting a File System's Reported Size](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/change-file-system-size.htm).

[To set the reported free space in the API](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/installationfails.htm#)

You can use the[UpdateExportSet](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSet/UpdateExportSet)operation to update the`MaxFsStatBytes`.

See[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)
