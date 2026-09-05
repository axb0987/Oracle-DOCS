# Moving a Snapshot Policy to Another Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-move.htm
- Fetched: 2026-09-05 02:05 CDT

# Moving a Snapshot Policy to Another Compartment

Move a snapshot policy to another compartment.

If you move a snapshot policy to another compartment, the snapshots created by the policy are still created in the compartment that contains the attached file system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-move.htm#)
- 

- On the Snapshot Policies list page, find the snapshot policy that you want to work with. If you need help finding the list page or the snapshot policy, see[Listing Snapshot Policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/snapshot-policy-list.htm).
- From the Actions menu (three dots) for the snapshot policy, select Move resource .
- Select the Destination compartment from the list.
- Select Move resource .
- 

Use the[`oci fs filesystem-snapshot-policy change-compartment`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/change-compartment.html)command with the required parameters to move a snapshot policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[ChangeFilesystemSnapshotPolicyCompartment](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicy/ChangeFilesystemSnapshotPolicyCompartment)to move a snapshot policy to another compartment within the same tenancy.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
