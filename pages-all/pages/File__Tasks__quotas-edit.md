# Updating an Individual Quota on a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-edit.htm
- Fetched: 2026-09-05 02:04 CDT

# Updating an Individual Quota on a File System

Update an existing individual user or group quota to change its limit or rename the rule.

To update default quotas that apply to all users and groups, see[Setting Default Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm).
Note  
  
Only one quota rule can be updated at a time. Bulk edits of individual user or group quotas aren't supported.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-edit.htm#)
- 

- On the File Systems list page, select the file system that contains the quota rules that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page select User and group quota rules .
- From the Actions menu (three dots) for the quota, select Edit .
- In the Edit quota rule panel, provide a new Quota limit in GB and select Update .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update-quota-rule.html)oci fs file-system update-quota-rule`command and required parameters to update a quota:

```

```

Use[oci fs file-system list-quota-rules](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/list-quota-rules.html)to get the`--quota-rule-id`value. For more information, see[Listing Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateQuotaRule](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateQuotaRule)operation to update a quota.

Use[ListQuotaRules](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/ListQuotaRules)to get the required`quotaRuleId`value. For more information, see[Listing Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
