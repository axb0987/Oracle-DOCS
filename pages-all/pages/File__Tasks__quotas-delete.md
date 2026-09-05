# Deleting an Individual Quota from a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-delete.htm
- Fetched: 2026-09-05 02:04 CDT

# Deleting an Individual Quota from a File System

Individual quotas can be deleted if they're no longer needed.

If you delete an individual quota, that user or group still might be subject to other quotas, including[default quotas](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-default.htm)and the file system overall quota.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-delete.htm#)
- 

- On the File Systems list page, select the file system that contains the quota rules that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select User and group quota rules .
- From the Actions menu (three dots) for the quota, select Delete .
- When prompted, confirm the deletion.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/delete-quota-rule.html)oci fs file-system delete-quota-rule`command and required parameters to delete a quota:

```

```

Use[oci fs file-system list-quota-rules](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/list-quota-rules.html)to get the`--quota-rule-id`value. For more information, see[Listing Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteQuotaRule](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/DeleteQuotaRule)operation to delete a quota.

Use[ListQuotaRules](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/ListQuotaRules)to get the required`quotaRuleId`value. For more information, see[Listing Quotas for a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-list.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
