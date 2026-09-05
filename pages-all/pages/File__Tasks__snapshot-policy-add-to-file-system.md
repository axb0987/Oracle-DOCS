# Attaching a Snapshot Policy to a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-to-file-system.htm
- Fetched: 2026-09-05 02:05 CDT

# Attaching a Snapshot Policy to a File System

Attach a snapshot policy to a file system.

A file system can only have a single snapshot policy associated with it. Use this information to attach a snapshot policy to a file system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-to-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-to-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-to-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- From the Actions menu, select Attach snapshot policy .
- Select Attach Snapshot Policy .

Note  
  
If Attach Snapshot Policy is unavailable, the file system is already associated with a snapshot policy.
- In the Attach Snapshot Policy panel:
- Select the Snapshot policy compartment that contains the snapshot policy
- Select the Snapshot policy you want to associate with this file system.

Note  
  
A snapshot policy can apply to many file systems, but a file system can only have one snapshot policy.
- Select Attach .
- 

Use the[`oci fs file-system update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html)command and the`--filesystem-snapshot-policy-id`parameter to associate a snapshot policy and a file system:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem)and`filesystemSnapshotPolicyId`to add a snapshot policy to a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
