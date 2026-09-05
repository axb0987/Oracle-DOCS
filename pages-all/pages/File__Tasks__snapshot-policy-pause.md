# Pausing and Unpausing a Snapshot Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-pause.htm
- Fetched: 2026-09-05 02:05 CDT

# Pausing and Unpausing a Snapshot Policy

You can pause a snapshot policy to stop automatic scheduled snapshots, and unpause a snapshot policy to resume automatic scheduled snapshots. A paused snapshot policy's lifecycle state is INACTIVE. Unpausing a snapshot policy sets the lifecycle state to ACTIVE.

You can edit a snapshot policy while it's paused. Changes to the policy's name, prefix, tags, and other related metadata show up immediately. Any schedule-related change in the policy takes effect only after the policy is unpaused.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-pause.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-pause.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-pause.htm#)
- 

- On the Snapshot Policies list page, select the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- On the details page, from the Actions menu, perform one of the following actions:

- To pause an active policy, select Pause . Confirm when prompted.
- To resume a paused policy, select Unpause . Confirm when prompted.
- 

To pause a snapshot policy, use the[`oci fs filesystem-snapshot-policy pause`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/pause.html)command and required parameters:

```

```

To unpause a snapshot policy, use the[`oci fs filesystem-snapshot-policy unpause`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/unpause.html)command and required parameters:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[PauseFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/PauseFilesystemSnapshotPolicy)and[UnpauseFilesystemSnapshotPolicy](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/UnpauseFilesystemSnapshotPolicy)to pause and unpause snapshot policies.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
