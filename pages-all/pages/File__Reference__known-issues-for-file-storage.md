# Known Issues for File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Reference/known-issues-for-file-storage.htm
- Fetched: 2026-09-05 02:02 CDT

# Known Issues for File Storage

These known issues have been identified in File Storage.

## File Storage does not currently support Access Control Lists (ACLs)
Details

File Storage does not support file level Access Control Lists (ACLs). Only`user`,`group`, and`world`permissions are supported. File Storage uses the NFSv3 protocol, which doesn't include support for ACLs.`setfacl`fails on mounted file systems.`getfacl`returns only standard permissions. Workaround We're working on a resolution.

## Semaphore timeout error when creating a snapshot with the Windows command line
Details

When using the`mkdir`command in Windows CMD to create a snapshot of a mounted file system, an error appears. For example:

`C:\>mkdir X:\.snapshot\snapshot1`

`The semaphore timeout period has expired.`

Although the error appears, the snapshot is successfully created. Workaround

Use the Console, API or CLI to create snapshots. For more information, see[Creating a Snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/create-snapshot.htm).

## Unable to move file storage resources to a different compartment
Details

When moving a file system or mount target from one compartment to another, the operation fails. Users are required to be members of the Administrators group. Workaround

We're working on a resolution. To work around this problem, be sure the user is a member of the Administrators group. For more information, see[Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm).

## 409 error occurs when creating or moving a file system or mount target
Details

When creating or moving a file system or mount target from one compartment to another, you might encounter one of the following 409 API errors:

Create file system:

```

```

Move file system:

```

```

Create mount target:

```

```

Move mount target:

```

```

The[Compartment Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm)feature introduces constraints that limit the number of concurrent operations that a tenancy can perform on file system and mount target resources in a region:
- Each tenancy in a region can have one`CreateFileSystem`or`ChangeFilesystemCompartment`operation in progress at a time.
- Each tenancy in a region can have one`CreateMountTarget`or`ChangeMountTargetCompartment`operation in progress at a time.

If a tenancy attempts to do more than one simultaneous operation, one operation succeeds and the others receive the 409 error response code. The default retry strategy for the OCI SDK is to not retry 409 conflicts. See[SDK Behaviors - Retries](https://docs.oracle.com/iaas/tools/python/latest/sdk_behaviors/retries.html). Workaround

We're working on a resolution. To work around this problem, create a custom retry strategy that retries on 409. Several examples of building a custom retry strategy are provided at[https://github.com/oracle/oci-python-sdk/blob/master/examples/retries.py.](https://github.com/oracle/oci-python-sdk/blob/master/examples/retries.py)

## File Storage in-transit TLS encryption does not currently support DNS hostnames

File systems that use in-transit TLS encryption can't be mounted using a DNS hostname. Only IP addresses can be used to mount file systems with in-transit TLS encryption. Details

The`oci-fss-utils`in-transit encryption tool does not currently support the use of DNS hostnames for mounting file systems. Workaround
We're working on a resolution. Until this issue is resolved, use the IP address of the mount target in the`oci-fss-utils`mount command. For example:

```

```
Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`yourmountpoint`with the path to the local mount point. The export path is the path to the file system (relative to the mount target IP address). See[Using In-transit TLS Encryption](https://docs.oracle.com/en-us/iaas/Content/File/Reference/../Tasks/intransitencryption.htm)
