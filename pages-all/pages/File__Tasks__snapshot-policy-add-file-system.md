# Attaching a File System to a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-file-system.htm
- Fetched: 2026-09-05 02:04 CDT

# Attaching a File System to a Snapshot Policy

Attach file systems to a snapshot policy.

[Create at least one snapshot policy](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-create.htm)before you attach[file systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm)to that policy.

A snapshot policy can apply to one or more file systems, up to a maximum of 100 file systems, so you might want to create the policy and its schedules first, and then associate that policy with many file systems. You can also[attach a single snapshot policy to a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-to-file-system.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-add-file-system.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, select Associated File Systems .
- Select Attach .
- In the Attach file systems panel, perform the following actions:
- Select the compartment that contains the file system that you want to attach to this snapshot policy.
- Use the check boxes to select one or more file systems that you want to attach to the snapshot policy.
- Select Attach File Systems .
- 

Use the[`oci fs file-system update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html)command and the`--filesystem-snapshot-policy-id`parameter to associate a snapshot policy and a file system:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem)and`filesystemSnapshotPolicyId`to associate a snapshot policy and a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
