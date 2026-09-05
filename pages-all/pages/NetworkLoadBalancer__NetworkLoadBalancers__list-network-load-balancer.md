# Listing Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm
- Fetched: 2026-09-05 02:48 CDT

# Listing Network Load Balancers

View a list of the network load balancers in a Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm#)
- 

- Open the navigation menu and select Networking .
The Load balancers overview page opens.
- Under Load balancers , select Network load balancer .
The Network load balancers list page opens. All network load balancer in the selected compartment are displayed in a table.
- To view the network load balancers in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the network load balancers in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a network load balancer to open its details page, where you can view its status and perform other tasks.

To perform an action on a network load balancer directly from the list table, select an available option from the Actions menu (three dots) in the row for that network load balancer:
- View details : Open the details page for the network load balancer.
- Copy OCID : Copy the OCID of the network load balancer to the clipboard.
- Move resource :[Move the network load balancer to another compartment](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/change-compartment-network-load-balancer.htm).
- Manage security attributes :[Add and view security attributes to the network load balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/security-attributes-network-load-balancer.htm).
- Manage tags : Add one or more tags to the network load balancer. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Delete the network load balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/delete-network-load-balancer.htm).
- Open support request : Open the Support Request panel, in which you can access support options. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

To create a network load balancer, select Create network load balancer .
- 

Use the[oci nlb network-load-balancer list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/list.html)command and required parameters to list the network load balancers in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListNetworkLoadBalancers](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/ListNetworkLoadBalancers)
