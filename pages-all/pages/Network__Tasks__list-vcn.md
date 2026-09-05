# Listing VCNs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing VCNs

List the VCNs available in a particular compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm#)
- 

- Open the navigation menu , select Networking , and then select Virtual cloud networks .

The Virtual cloud networks list page opens. All VCNs in the selected compartment are displayed in a table.
- To view the VCNs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the VCNs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a VCN to open its details page, where you can view its status and perform other tasks.

To create another VCN, select Create VCN .

Use the Actions button above the table to perform the following actions:
- Start VCN wizard : See[Virtual Networking Wizards](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartnetworking.htm)
- View or manage logs : See[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)

To perform other actions on a VCN directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that VCN:
- View details : Open the details page for the VCN.
- Copy OCID : Copy the OCID of the VCN to the clipboard.
- Move resource :[Move the VCN to another compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm).
- Manage tags : Add one or more tags to the VCN. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Manage security attributes : Add one or more security attributes to the VCN. See[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
- Delete :[Delete the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm)
- 

Use the[network vcn list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/list.html)command and required parameters to list the VCNs in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVcns](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns)
