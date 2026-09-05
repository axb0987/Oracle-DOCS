# Getting a Snapshot's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-snapshot-details.htm
- Fetched: 2026-09-05 02:03 CDT

# Getting a Snapshot's Details

Get details about a File Storage snapshot.

For more information, see[Details About Your Snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm#Details_About_Your_Snapshot).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-snapshot-details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-snapshot-details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-snapshot-details.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- Select the snapshot.

The details page for the snapshot opens and displays information about the snapshot.
- 

Use the[`fs snapshot get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/get.html)command and required parameters to get details about a snapshot:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/GetSnapshot)operation to get details about a snapshot.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
