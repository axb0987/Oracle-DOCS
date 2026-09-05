# Deleting a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-file-system.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting a File System

Learn how to permanently delete a File Storage file system.
Before you can delete the root file system of a clone tree, all of its descendants must first be deleted or detached. If a file system has only a single clone, you can delete the file system and detach the clone with the same operation. See[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm)for more information.

Caution  
  
You can't undo this operation. Any data in a file system is permanently deleted with the file system. Snapshots of the file system are permanently deleted with the file system. You can't recover a deleted file system or its snapshots.

To delete related resources, see the following topics:
- [Deleting a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm)
- [Deleting an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-export.htm)
- [Deleting a Replication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm)
- [Deleting a Replication Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm)

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Exports .
- Select the checkbox for each export listed, and then select Delete . When prompted, confirm the deletion..
- When all the exports are deleted, from the Actions menu, select Delete to delete the file system.
- Select Delete to confirm the deletion.
Note  
  
If the file system has only a single clone, you can choose to detach that clone from the parent file system before deleting the parent. In the Delete file system window, select Detach clone .
- When prompted, confirm the deletion.
- 

You can use the CLI to delete a file system if no non-deleted export resources reference it.

Use the[`fs file-system delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/delete.html)command and required parameters to delete a file system:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/DeleteFileSystem)operation to delete a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
