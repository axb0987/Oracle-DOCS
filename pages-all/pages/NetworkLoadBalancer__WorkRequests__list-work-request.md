# Listing Network Load Balancer Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request.htm
- Fetched: 2026-09-05 02:49 CDT

# Listing Network Load Balancer Work Requests

View a list of the work requests for a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Work requests .
The Work requests list opens. All work requests in the selected network load balancer are displayed in a table.
- To view the work requests in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the work requests in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a work request to open its details page, where you can view its status and perform other tasks.

To perform an action on a work request directly from the list table, select an available option from the Actions menu (three dots) in the row for that work request:
- Copy OCID : Copy the OCID of the work request to the clipboard.
- 

Use the[oci nlb work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/work-request/list.html)command and required parameters to list the work requests of a network load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/WorkRequest/ListWorkRequests)
