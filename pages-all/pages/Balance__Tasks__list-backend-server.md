# Listing a Load Balancer's Backend Servers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-backend-server.htm
- Fetched: 2026-09-05 01:41 CDT

# Listing a Load Balancer's Backend Servers

View a list of the backend servers contained within a backend set for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-backend-server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-backend-server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-backend-server.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
The Backend sets tab opens. All backend sets in the selected load balancer are displayed in a table.
- Select the backend set that contains the backend server you want.
The backend set's details page opens.
- Select Backends .
The Backends tab opens. All backend servers in the selected backend set are displayed in a table.
- To view the backend servers in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the backend servers in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a backend server to open its details page, where you can view its status and perform other tasks.

To perform an action on a backend server directly from the list table, select an available option from the Actions menu in the row for that backend server:
- Edit backend :[Edit the backend server's settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_backend_server.htm).
- Delete :[Delete the backend server](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_backend_server.htm).

To add a backend server to the backend set, select Add backends .

To perform an action on more than one backend server at a time, select the checkboxes next to the backend server names and then select an action from the Actions menu above the table.
- 

Use the[oci lb backend list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/list.html)command and required parameters to list the backend servers in a load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListBackends](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/ListBackends)
