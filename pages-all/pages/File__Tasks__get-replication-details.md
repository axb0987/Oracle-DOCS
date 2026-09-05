# Getting a Replication's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm
- Fetched: 2026-09-05 02:03 CDT

# Getting a Replication's Details

Get details about a File Storage replication.

For more information, see[Managing Replications](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-managing-replications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-replication-details.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the source file system's details page, select Replications .
Note  
  
If no Replications option exists in Resources , it means that the file system is the target of an active replication.
- Select the replication. If no replications are listed, it means that the file system is not a source file system.

The details page for the replication opens and displays information about the replication.
- 

Use the[`fs replication get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/get.html)command and required parameters to get details about a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetReplication](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Replication/GetReplication)operation to get details about a replication.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
