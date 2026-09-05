# Listing Quotas for a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm
- Fetched: 2026-09-05 02:04 CDT

# Listing Quotas for a File System

List quotas for individual users and groups to see limits, usage, and violators.

Note  
  
If quotas are disabled, the usage reported when listing quota rules is zero (0). In this case, a value of 0 doesn't mean that the user, group, or file system has no usage, it means that the usage is undefined. Reported quota usage is only correct when enforcement is enabled. For more information, see[Enabling or Disabling Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm). When you use the CLI or API to list quotas, the response includes an ID that you can use when[updating](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-edit.htm)or[deleting](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-delete.htm)individual quotas.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, to view whether quotas are enabled or disabled, file system quotas, and default user and group quotas, see the Quota , File system quota rule and Default user and group quota rules sections.
- To view a list of quotas rules, select User and group quota rules .
By default, only individual group quota rules are displayed. To view all quotas, select the Search and Filter fields and then select List quota scope . Here, you can select the type of quota rule that you want to list. To identify users and groups exceeding their quota, you can specify whether to display only the violators for a particular rule.
- Individual group quota rule
- Individual group quota rule violators only
- Individual user quota rule
- Individual user quota rule violators only
- File System quota rule
- File System quota rule violators only
- Default group quota rule
- Default group quota rule violators only
- Default user quota rule
- Default user quota rule violators only
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/list-quota-rules.html)oci fs file-system list-quota-rules`command and required parameters to list quotas:

```

```

Tip  
  

Use the optional`--are-violators-only`parameter to display only the users or groups that violate the quota rules of the file system.

Use the optional`--principal-id`parameter to display only the quotas associated with a specific user or group.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListQuotaRules](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/ListQuotaRules)operation to list quotas.
Tip  
  

Use the optional`areViolatorsOnly`parameter to display only the users or groups that violate the quota rules of the file system.

Use the optional`principalId`parameter to display only the quotas associated with a specific user or group.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
