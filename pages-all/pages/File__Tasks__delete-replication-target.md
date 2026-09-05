# Deleting a Replication Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting a Replication Target

Delete a File Storage replication target.

Important  
  
Delete a target file system's associated replication target to make the file system exportable. Deleting the replication target doesn't delete the associated replication resource, but places it in a`FAILED`state. You should only delete the replication target if the source file system is no longer available (such as during an outage). If the source file system is still available,[delete the replication resource](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- 

In the Replication section, select the Replication Target .
Note  
  
If no Replication Target name link appears in the file system's details page, it means that the file system is not a target file system.
- On the replication target's details page, select Delete .
- When prompted, confirm the deletion.
- 

Use the[`fs replication-target delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication-target/delete.html)command and required parameters to delete a replication target:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteReplicationTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ReplicationTarget/DeleteReplicationTarget)operation to delete a replication target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
