# Editing a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-file-system.htm
- Fetched: 2026-09-05 02:03 CDT

# Editing a File System

Change an existing File Storage file system.

You can change the display name of the file system or[manage its tags](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-file-system.htm). You can also[encrypt a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm),[set the file system's reported size](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm), and[tag a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-file-system.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the file system's details page, select Rename .
- Enter the new file system name. Avoid entering confidential information. Then select Update .
- 

Use the[`fs file-system update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html)command and required parameters to update a file system:

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem)operation to edit a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
