# Listing Error Messages for a Work Request
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-errors.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Error Messages for a Work Request

List error messages for a Resource Manager work request.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-errors.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-errors.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-errors.htm#)
- 

In the Console, you can list error messages for a work request related to a private endpoint. Error messages provide a concise failure summary; for execution-level diagnostic information, see[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm).

## Listing Error Messages for a Work Request Related to a Private Endpoint

- On the Private endpoints list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- On the private endpoint's details page, select Work requests .
- Select the work request that you want.
The work request's details page opens.
- Select Error messages .
- 

Use the[oci resource-manager work-request list-work-request-errors](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/list-work-request-errors.html)command and required parameters to list error messages for a work request:

```

```

Error messages do not replace work request log entries or raw log content. For supported operations, you can review the work request's execution details in the available logs. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)and[Getting Log Content for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequestErrors](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/ListWorkRequestErrors)operation to list error messages for a work request.

For log entries and raw log content, see[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)
