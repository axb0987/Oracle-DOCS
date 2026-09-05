# Detaching a Snapshot Policy from a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-detach-file-system.htm
- Fetched: 2026-09-05 02:05 CDT

# Detaching a Snapshot Policy from a File System

Stop automatic snapshots of a file system or attach a different snapshot policy by detaching the snapshot policy from the file system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-detach-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-detach-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-detach-file-system.htm#)
- 

You can detach a snapshot policy from a file system in two ways: through the snapshot policy's details page or through the file system's details page.

## To detach the policy through the snapshot policy's details page

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, select Associated File Systems .
- Use the checkboxes to select one or more file systems that you want to detach from the snapshot policy.
- Select Detach .
- In the Detach file systems panel , select Detach .

## To detach the policy through the file system's details page

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the page, select Snapshot Policy .
- Find the snapshot policy that you want to detach, then, from the the Actions menu (three dots) , select Detach .
- When prompted, confirm the detachment.
- 

Use the[`oci fs file-system update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html)command with an empty`--filesystem-snapshot-policy-id`parameter to detach a snapshot policy from a file system:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem)and with an empty`filesystemSnapshotPolicyId`to detach a snapshot policy from a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
