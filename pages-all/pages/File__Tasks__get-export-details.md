# Getting an Export's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-details.htm
- Fetched: 2026-09-05 02:03 CDT

# Getting an Export's Details

Get details about a File Storage export.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-details.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- Select the compartment that contains the mount target and export you want to work with.
- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select Exports .
- In the list of exports, select the name or Export path of the export that you're interested in.

The export's details page is displayed.
- 

Use the[`fs export get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/get.html)command and required parameters to get details about an export:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/GetExport)operation to get details about an export.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
