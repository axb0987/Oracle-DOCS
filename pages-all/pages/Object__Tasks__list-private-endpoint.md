# Listing Object Storage Private Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm
- Fetched: 2026-09-05 02:50 CDT

# Listing Object Storage Private Endpoints

View a list of the Object Storage private endpoints in a Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm#)
- 

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Private Endpoints .
The Private endpoints list page opens. All existing Object Storage private endpoint resources in the selected compartment are displayed in a list table.
- To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the Object Storage replication policy in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a private endpoint to open its details page, where you can view its status and perform other tasks.

To perform an action on a bucket directly from the list table, select any of the following options from the Actions menu in the row for that private endpoint:
- View details :[Open details on the private endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-private-endpoint.htm).
- Copy v2 fqdn :[Copy the fully qualified domain name prefix for the Object Storage API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-fqdn.htm).
- Copy swift fqdn :[Copy the fully qualified domain name prefix for the AWS S3 Compatibility API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-fqdn.htm).
- Copy s3 fqdn :[Copy the fully qualified domain name prefix for the Swift API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-fqdn.htm).
- Edit endpoint :[Update the private endpoint's settings](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm).
- Delete endpoint :[Delete the private endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm).

To create a private endpoint, select Create private endpoint .
- 

Use the[oci os private-endpoint list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/list.html)command and required parameters to list the private endpoints in a compartment in Object Storage:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the following API operation:
```

```
