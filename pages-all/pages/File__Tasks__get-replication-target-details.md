# Getting a Replication Target's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm
- Fetched: 2026-09-05 02:03 CDT

# Getting a Replication Target's Details

Get details about a File Storage replication target.

For more information, see[Managing Replications](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-managing-replications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-target-details.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, under Replication , select the Replication Target .

If no replication target is listed, it means that the file system is not a target file system.
- 

Use the[`fs replication-target get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication-target/get.html)command and required parameters to get details about a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetReplicationTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ReplicationTarget/GetReplicationTarget)operation to get details about a replication target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
