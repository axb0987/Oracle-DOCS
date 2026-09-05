# Getting a Work Request's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm
- Fetched: 2026-09-05 02:56 CDT

# Getting a Work Request's Details

Get details for a Resource Manager work request.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request.htm#)
- 

In the Console, you can get details of a work request for a stack or for a private endpoint. Work request details include operation status, progress, and timestamps.

## Getting Details for a Stack's Work Request

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Work requests .
- Select the work request that you want.
The details page opens and displays information about the work request. To investigate a failed operation, view its logs. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)and[Getting Log Content for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm).

## Getting Details for a Private Endpoint's Work Request

- On the Private endpoints list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- On the private endpoint's details page, select Work requests .
- Select the work request that you want.
The details page opens and displays information about the work request. To investigate a failed operation, view its error messages and logs. See[Listing Error Messages for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-errors.htm)and[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm).
- 

Use the[oci resource-manager work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/get.html)command and required parameters to get details for a work request:

```

```

This command returns work request metadata, not log content. To retrieve logs, see[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/GetWorkRequest)
