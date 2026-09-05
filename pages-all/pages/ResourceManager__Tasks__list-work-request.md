# Listing Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Work Requests

List Resource Manager work requests.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request.htm#)
- 

In the Console, you can list work requests for a stack or a private endpoint.

## Listing Work Requests for a Stack

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Work requests .
The Work requests page lists the stack's work requests. Select a work request to view its details and log information.

## Listing Work Requests for a Private Endpoint

- On the Private endpoints list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- On the private endpoint's details page, select Work requests .
The Work requests page lists the private endpoint's work requests. Select a work request to view its details, error messages, and log information.
- 

Use the[oci resource-manager work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/work-request/list.html)command and required parameters to list work requests:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/ListWorkRequests)
