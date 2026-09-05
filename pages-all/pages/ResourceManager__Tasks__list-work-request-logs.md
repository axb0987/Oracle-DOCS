# Getting Logs for a Work Request
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm
- Fetched: 2026-09-05 02:56 CDT

# Getting Logs for a Work Request

List logs for a Resource Manager work request.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm#)
- 

In the Console, you can list logs for a work request related to a stack or a private endpoint.

## Getting Logs for a Work Request Related to a Stack

Note  
  

Detailed execution log entries are available for supported operations, including drift detection and creating a stack from an existing compartment.

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Work requests .
- Select the work request that you want.
- Select Logs .

You can search the displayed log entries, hide timestamps, and download the log.

## Listing Logs for a Work Request Related to a Private Endpoint

- On the Private endpoints list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- On the private endpoint's details page, select Work requests .
- Select the work request that you want.
The work request's details page opens.
- Select Log messages .
- 

- 

Use the[oci resource-manager work-request list-work-request-logs](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/list-work-request-logs.html)command and required parameters to list logs for a work request:

```

```

- 

Use the`oci resource-manager work-request get-work-request-log-entries`command and required parameters to get structured log entries for a work request.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

- 

Run the[ListWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/ListWorkRequestLogs)operation to list logs for a work request.
- 

Use the[GetWorkRequestLogEntries](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/GetWorkRequestLogEntries)
