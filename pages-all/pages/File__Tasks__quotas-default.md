# Setting Default Quotas for a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm
- Fetched: 2026-09-05 02:04 CDT

# Setting Default Quotas for a File System

Default quotas limit storage consumption for all users and all groups for any file system, without the need to set individual quotas for users or groups. Individual quotas override user and group defaults, but not the file system limit.

File system quotas and default quotas can be soft quotas or a hard quotas. For more information, see[Quota Types](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm#top__types).
Note  
  
Setting default quotas doesn't automatically enable those quotas. You still need to[enable quotas for the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Actions and then select File system quota rule .
- Select Add file system hard quota rule or Add file system soft quota rule .
- In the panel, enter the Quota limit in GB and select Add or Update .

To edit default quotas for a file system, select Actions , and then select Edit file system hard quota rule or Edit file system soft quota rule .

To delete default quotas for a file system, select Actions , and then select Delete file system hard quota rule or Delete file system soft quota rule .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/create-quota-rule.html)oci fs file-system create-quota-rule`command and required parameters to set default quotas. The`--principal-id`option isn't used for default quotas. For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateQuotaRule](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateQuotaRule)operation without`principalId`to create a default quota.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
