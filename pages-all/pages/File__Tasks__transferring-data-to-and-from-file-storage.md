# Transferring Data To and From File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/transferring-data-to-and-from-file-storage.htm
- Fetched: 2026-09-05 02:05 CDT

# Transferring Data To and From File Storage

Many common use cases for Oracle Cloud Infrastructure (OCI) File Storage include the transfer of a large amount of data. Based on the origination, destination, and the direction of the data transfer, the best method to accomplish that transfer can vary.

The following table provides recommendations for common File Storage data transfer scenarios, including the migration of on-premises data, copying File Storage data from one region to another, copying File Storage data within a region, and copying File Storage data to Object Storage.

For general information about private connections between OCI and on-premises data, see[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm)and[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm).

File Storage Data Transfer Scenarios
Transfer Data From... To... Recommended Method Prerequisites and Considerations
On-premises storage File Storage on OCI

Linux users can use instance-to-instance streaming and the`fpsync`tool.

Windows users can mount the Windows on-premises file share as a Common Internet File System (CIFS) share on an OCI Oracle Linux instance and use a copy tool such as[`fss-parallel-tools`](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm)or`fpsync`to transfer data.

For more information, see[Transferring On-Premises Data to File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/transferring-data-to-and-from-file-storage.htm#on-prem-to-oci-sync).

Ensure that network connectivity is established between source and destination instances.
OCI File Storage File Storage in another region

Use one of the following methods, depending on the specifics of the use case:
- Use[File System Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm). See[Using Replication for Data Transfer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-copy-data.htm)for more information.
- 

Use instance-to-instance streaming and the`fpsync`tool. For more information, see[Using Instance-to-Instance Streaming to Transfer File Storage Data](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/transferring-data-to-and-from-file-storage.htm#oci-instance-to-instance).

If using replication, see replication's[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm#limitations-and-considerations).

If using instance-to-instance streaming, ensure that network connectivity is established between source and destination instances.
OCI File Storage File Storage within the same availability domain

Use one of the following methods, depending on the specifics of the use case:
- Use[File System Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm). See[Using Replication for Data Transfer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-copy-data.htm)for more information.
- 

Use the`parcp`command in our suite of[parallel tools](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm)to transfer data.

See the`parcp`usage examples in[Using File Storage Parallel Tools](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm), particularly[how to use`parcp`as an effective alternative for`rsync`](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm#using-the-tools-advanced__parcp-as-rsync-alternative).

If using replication, see replication's[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm#limitations-and-considerations).

If using`parcp`, ensure that both source and destination file systems are mounted in the instance.
OCI File Storage OCI Object Storage

Use`rclone`. See[Backing Up Snapshots to Object Storage Using rclone](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/backing-up-snapshots-to-object-storage.htm)for more information.

Instance should be able to connect to the Object Storage bucket.
OCI File Storage On-premises storage or other cloud providers Linux users can use instance-to-instance streaming and the`fpsync`tool to transfer data from OCI. For some examples, see[Transferring On-Premises Data to File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/transferring-data-to-and-from-file-storage.htm#on-prem-to-oci-sync). The same technique can be used in reverse. Ensure that network connectivity is established between source instance and destination.

## Transferring On-Premises Data to File Storage

The following scenarios have been proven effective for Linux and Windows users when transferring large amounts of data from on-premises storage to OCI File Storage. They might not be applicable to all environments or meet all requirements. You can use similar scenarios and tools to transfer data from File Storage to on-premises storage or other providers.

### For Linux Users

Use the`fpsync`tool to perform an initial copy of on-premises data to OCI File Storage. Then, incremental data changes can be synchronized using`rsync`because`fpsync`can't delete files and folders in the destination that don't exist in the source.

The`fpsync`tool is a parallel wrapper of`rsync`. Linux users can download`fpsync`from a yum repository. The commands differ depending on the version of Linux.
- 

Download from the repository.

Linux 8 users can download the tool using the following command:

```

```

Linux 9 users can download the tool using the following command:

```

```

- Install the tool:

```

```

Before beginning the data transfer, complete the following prerequisites:
- Ensure that network connectivity is established between the on-premises data source and OCI. Use[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm)or[Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)connection to enable fast instance-to-instance streaming over SSH.
- Create an Oracle Linux[instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/instances.htm)in OCI.
- Attach or mount the on-premises storage share on a Linux server. A dedicated instance is recommended.

In this scenario, we suggest that the initial copy uses`fpsync`. Later, incremental syncs use`rsync`because`fpsync`doesn't have the`--delete`option.

- [Mount the file system in the Oracle Linux instance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingunixstyleos.htm).
- Run the following command from the on-premises Linux server where the source share is attached or mounted to perform the initial copy:

```

```

- (Optional) If you need to run an incremental sync until a specific date, you can schedule the following`rsync`command as a[cron job](https://linux.die.net/man/8/cron):

```

```

For more`fpsync`options, see the[`fpsync`man page](http://manpages.ubuntu.com/manpages/xenial/man1/fpsync.1.html).

### For Windows Users

Don't use Windows copy utilities for large data copies to File Storage. Instead, use an OCI Linux instance to perform large copies using the parallel tools that come with an OCI Linux instance. Mount the Windows share as a Common Internet File System (CIFS) share and use a copy tool such as`parcp`or`fpsync`to transfer data.

Because the SMB protocol and the NFS protocol used by File Storage aren't compatible, an instance that can mount both the NFS file system and the SMB share is used to create a bridge between them.
- Identify or create a Linux instance in Oracle Cloud Infrastructure that has network access to both the File Storage file system and the Windows SMB share.
- Open a terminal on the instance.
- 

Type the following to install the Common Internet File System (CIFS) utility and verify its installation:
```

```

- 

Mount the Windows SMB share as a CIFS share.
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

- Copy the files from the CIFS share to the mounted file system using the`parcp`utility from the File Storage Parallel Tools suite or`fpsync`. For installation information about`parcp`, see[Using File Storage Parallel Tools](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/using_file_storage_parallel_tools.htm). For information about`fpsync`, visit the[`fpsync`man page](http://manpages.ubuntu.com/manpages/xenial/man1/fpsync.1.html).

For example:
```

```

```

```

## Using Instance-to-Instance Streaming to Transfer File Storage Data

The`fpsync`tool is a parallel wrapper of`rsync`. You can use`fpsync`and instance-to-instance streaming to transfer data between mounted File Storage file systems.

To install`fpsync`, enable the Oracle Linux developer repository, which includes the`fpsync`utility, on the OCI instance using a command such as the following. The command differs based on the version of Oracle Linux in use:

```

```

```

```

After installing the tool, use an instance-to-instance streaming command such as this to stream data:

```

```

For more information and options, see the[`fpsync`man page](http://manpages.ubuntu.com/manpages/xenial/man1/fpsync.1.html).

An example showing the performance difference between the two approaches follows:
```

```
