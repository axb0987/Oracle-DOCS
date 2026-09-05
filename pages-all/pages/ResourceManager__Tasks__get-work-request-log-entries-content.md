# Getting Log Content for a Work Request
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm
- Fetched: 2026-09-05 02:56 CDT

# Getting Log Content for a Work Request

Download console logs (raw .txt job logs content) for a work request in Resource Manager.
Note  
  

Raw log content is available for supported operations, including drift detection and creating a stack from an existing compartment. The response includes a maximum of 100,000 log entries.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Work requests .
- Select the work request that you want.
- Select Logs .
- Select the Actions menu (three dots) and then select Download logs .
- 

Use the`oci resource-manager work-request get-work-request-log-entries-content`command and required parameters to get raw log content for a work request.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetWorkRequestLogEntriesContent](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/GetWorkRequestLogEntriesContent)
