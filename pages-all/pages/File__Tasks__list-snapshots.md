# Listing Snapshots
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-snapshots.htm
- Fetched: 2026-09-05 02:04 CDT

# Listing Snapshots

List File Storage snapshots of file systems.

Snapshots are accessible on the file system at`./snapshot/ <snapshot_name>`.
Note  
  
When you use an NFSv3 client to perform operations such as`ls`,`du`, or`find`on the snapshot directory, the service automatically exports the directory. The client uses`nfs_d_automount()`to detect and mount the directory. After the directory is detected and mounted the first time, the client mounts the directory automatically.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-snapshots.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-snapshots.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-snapshots.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
You see a list of snapshots along with details.
- 

Use the[`fs snapshot list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/list.html)command and required parameters to list snapshots for a file system:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSnapshots](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/SnapshotSummary/ListSnapshots)operation to list snapshots.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
