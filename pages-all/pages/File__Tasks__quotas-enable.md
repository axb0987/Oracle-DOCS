# Enabling or Disabling Quotas for a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm
- Fetched: 2026-09-05 02:04 CDT

# Enabling or Disabling Quotas for a File System

Enabling or disabling quotas for a file system affects all individual and default file system, user, and group quotas.

To set default quotas, see[Setting Default Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm). To create individual quotas, see[Creating an Individual Quota for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-create.htm).
Note  
  
It might take up to one hour after quotas are initially enabled for a file system for enforcement to take place.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, from the Actions menu, select Enable quota limit . If the file system has existing quotas, select Disable quota limit to disable the quotas.
- Confirm when prompted.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/toggle-quota-rules.html)oci fs file-system toggle-quota-rules`command and required parameters to enable or disable quotas:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ToggleQuotaRules](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/ToggleQuotaRules)operation to enable or disable quotas.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
