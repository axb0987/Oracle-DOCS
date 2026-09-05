# Moving a File System Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-file-system.htm
- Fetched: 2026-09-05 02:04 CDT

# Moving a File System Between Compartments

Move File Storage file systems from one compartment to another.

When you move a file system to a new compartment, its associated snapshots move with it. After you move the file system to the new compartment, inherent policies apply immediately and affect access to the file system and snapshots through the Console. Moving these resources doesn't affect access to file systems and snapshots from mounted instances. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

The file system is moved immediately. Moving a file system doesn't affect mounted instances.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-file-system.htm#)
- 

- On the File Systems list page, find the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- From the the Actions menu (three dots) for the file system, select Move resource .
- Select the Destination compartment from the list.
- Select Move resource .
- 

Use the[`fs file-system change-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/change-compartment.html)command and required parameters to move a file system to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeFileSystemCompartment](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/ChangeFileSystemCompartment)operation to move a file system to another compartment.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
