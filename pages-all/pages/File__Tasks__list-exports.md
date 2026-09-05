# Listing Exports
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-exports.htm
- Fetched: 2026-09-05 02:04 CDT

# Listing Exports

List a File Storage file system's exports, or exports in a specific compartment.

You can also list the exports associated with a mount target. For more information, see[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-exports.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-exports.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-exports.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- On the File Systems list page, select the file system that contains the export that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Exports .
- 

Use the[`fs export list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/list.html)command and required parameters to list exports in the specified compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListExports](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSummary/ListExports)operation to list exports.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
