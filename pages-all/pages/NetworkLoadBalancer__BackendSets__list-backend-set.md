# Listing Network Load Balancer Backend Sets
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/list-backend-set.htm
- Fetched: 2026-09-05 02:48 CDT

# Listing Network Load Balancer Backend Sets

View a list of the backend sets for a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/list-backend-set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/list-backend-set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/list-backend-set.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
The Backend sets list opens. All backend sets in the selected network load balancer are displayed in a table.
- To view the backend sets in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the backend sets in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a backend set to open its details page, where you can view its status and perform other tasks.

To perform an action on a backend set directly from the list table, select an available option from the Actions menu (three dots) in the row for that backend set:
- View details : Open the details page for the backend set.
- Edit :[Edit a backend set's settings](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/update-backend-set.htm).
- Update health check :[Edit a backend set's health check policies](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/../HealthCheckPolicies/update-health-check-policy.htm).
- Delete :[Delete a backend set](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/delete-backend-set.htm).

To create a backend set, select Create backend set .
- 

Use the[oci nlb backend-set list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/list.html)command and required parameters to list a network load balancer's backend sets:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListBackendSets](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendSetSummary/ListBackendSets)
