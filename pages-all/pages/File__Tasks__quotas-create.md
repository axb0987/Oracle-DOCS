# Creating an Individual Quota for a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-create.htm
- Fetched: 2026-09-05 02:04 CDT

# Creating an Individual Quota for a File System

Administrators can create individual quotas for users and groups. Individual quotas override user and group defaults, but not the file system limit. Individual quotas are tied to a specific UNIX principal and designated by UID or GID.

A quota can be a soft quota or a hard quota. For more information, see[Quota Types](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/file-system-quotas.htm#top__types).
Note  
  
Creating quotas doesn't automatically enable those quotas. You still need to[enable quotas for the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-enable.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/quotas-create.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select User and group quota rules amd then select Add quota rule .
- To add a default quota, select Add default user hard quota rule or Add default user soft quota rule .
- In the panel, provide the following information:

- Quota name : Name of the quota.
- Select whether the quota is a Hard quota or a Soft quota.
- Select whether this is an Individual group quota rule or an Individual group quota rule .
- Principal ID : The UID or GID to which the quota applies.
- Quota limit in GB : The size of the quota, in gigabytes.
- Select Add .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/create-quota-rule.html)oci fs file-system create-quota-rule`command and required parameters to create a quota:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateQuotaRule](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateQuotaRule)operation to create a quota.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
