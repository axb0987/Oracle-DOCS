# Editing a Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-replication.htm
- Fetched: 2026-09-05 02:03 CDT

# Editing a Replication

Update a File Storage replication.

You can change a replication's display name or replication interval.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-replication.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-replication.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-replication.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the source file system's details page, select Replications .
- Select the replication.
- To rename the replication, select Rename , and enter a new name for the replication.
- To change the replication interval, select the edit icon next to Replication interval in minutes and enter a new value.
- 

Use the[`fs replication update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/update.html)command and required parameters to update a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateReplication](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Replication/UpdateReplication)operation to update a replication.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
