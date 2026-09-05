# Getting an Export Set's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-set-details-mt.htm
- Fetched: 2026-09-05 02:03 CDT

# Getting an Export Set's Details

Get details about an export set.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-set-details-mt.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-set-details-mt.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-export-set-details-mt.htm#)
- 

- On the Mount Targets list page, select the mount target that contains the export that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- On the details page, select NFS .

The Exportset OCID is displayed, along with configuration options related to the export set, such as Reported size (GiB) and Reported Inodes (GiI) .
- 

Use the[`fs export-set get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export-set/get.html)command and required parameters to get details about an export:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetExportSet](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSet/GetExportSet)operation to get details about an export set.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
