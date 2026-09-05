# Listing Replications
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replications.htm
- Fetched: 2026-09-05 02:04 CDT

# Listing Replications

Get a list of File Storage replications.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replications.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replications.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-replications.htm#)
- 

If a file system is a source file system, you can view its associated replication resources.

- 

On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the source file system's details page, select Replications .
Note  
  
If no Replications option exists under Resources , it means that the file system is the target of an active replication.

If no replications are listed, it means that the file system is not a source file system.
- 

Use the[`fs replication list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/list.html)command and required parameters to list replications:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListReplications](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ReplicationSummary/ListReplications)operation to list replications.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
