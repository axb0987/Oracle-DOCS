# Listing File Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-file-systems.htm
- Fetched: 2026-09-05 02:04 CDT

# Listing File Systems

List File Storage file systems.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-file-systems.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-file-systems.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-file-systems.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- 

To view the file systems in a different compartment,change the Compartment to find the resource that you want.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- 

Use the[`fs file-system list`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/list.html)command to list all the file systems in a specified availability domain and compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListFileSystems](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystemSummary/ListFileSystems)operation to list file systems.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
