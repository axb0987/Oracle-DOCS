# Deleting a Snapshot
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-snapshot.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting a Snapshot

Delete a File Storage snapshot.

Note  
  
If a snapshot is deleted while a clone of it is being hydrated, the source snapshot remains in the DELETING state until hydration is complete. For more information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-snapshot.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-snapshot.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-snapshot.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot or snapshots that you want to delete.
- Select Delete .
- When prompted, confirm the deletion.
- 

Use the[`fs snapshot delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/delete.html)command and required parameters to delete a snapshot:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/GetSnapshot)operation to delete a snapshot.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
