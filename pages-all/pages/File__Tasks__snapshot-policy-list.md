# Listing Snapshot Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-list.htm
- Fetched: 2026-09-05 02:05 CDT

# Listing Snapshot Policies

List File Storage snapshot policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policy-list.htm#)
- 

- Open the navigation menu and select Storage . Select File Storage . Under Additional resources , select Snapshot Policies .
- To view the snapshot policies in a different compartment, switch the Compartment

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

Use the[`oci fs filesystem-snapshot-policy list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/filesystem-snapshot-policy/list.html)command with the required parameters to list snapshot policies:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[ListFilesystemSnapshotPolicies](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FilesystemSnapshotPolicySummary/ListFilesystemSnapshotPolicies)to list snapshot policies.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
