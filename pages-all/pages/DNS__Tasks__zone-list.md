# Listing DNS Zones
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm
- Fetched: 2026-09-05 01:59 CDT

# Listing DNS Zones

View a list of domain name service (DNS) zones in a compartment.
For more information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#)
- 

- Zones can be either public or private.
- To list Public zones: Open the navigation menu and select Networking . Under DNS management , select Public Zones .
- To list Private zones: Open the navigation menu and select Networking . Under DNS management , select Private Zones .
- To view the Zones in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the Zones in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a Zone to open its details page, where you can view its status and perform other tasks.

To create another Zone, select Create Zone .

To perform actions on a Zone directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that VCN:
- View details : Open the details page for the Zone.
- Copy OCID : Copy the OCID of the Zone to the clipboard.
- Move resource :[Moving a DNS Zone Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm#top).
- Manage tags : Add one or more tags to the Zone. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete :[Deleting a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm#top).
- 

Use the[zone list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/list.html)command and required parameters to view a list of zones in a compartment.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListZones](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/ListZones)
