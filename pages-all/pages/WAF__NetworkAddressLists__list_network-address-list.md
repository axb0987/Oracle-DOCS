# Listing Web Application Firewall Network Address Lists
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm
- Fetched: 2026-09-05 03:10 CDT

# Listing Web Application Firewall Network Address Lists

View a list of the web application firewall policy network address lists in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Network Address Lists .
The network address list's details page opens. The list indicates name, address type (Public or Private), status, and created date/time (UTC date timestamp) for each network address list.
- To view the WAF network address lists in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the WAF network address lists in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a network address list to open its details page, where you can view its status and perform other tasks.

To perform an action on a network address list directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that network address list:
- View details : Open the details page for the network address list.
- Create support request : Open the Support Request panel, in which you can access support options. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Delete :[Delete the network address list](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/delete_network-address-list.htm#top).
- Move resource :[Move the network address list to another compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/change-compartment_network-address-list.htm#top).
- Manage tags : Add one or more tags to the WAF network address list. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Copy OCID : Copy the OCID of the network address list to the clipboard.

To create a network address list, select Create network address list .

To delete more than one network address list at a time, select the checkboxes next to the network address list names and then select Delete .
- 

Use the[oci waf network-address-list list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/network-address-list/list.html)command and required parameters to list the web application firewall policy network address lists in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[
