# Listing CPEs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm
- Fetched: 2026-09-05 02:43 CDT

# Listing CPEs

List the CPEs available in a particular compartment.

The actual device in the on-premises network (whether hardware or software) at the on-premises end of Site-to-Site VPN is commonly called the customer-premises equipment (CPE) in some industries for this type of on-premises equipment. When setting up the VPN, you must create a virtual representation of the device. Oracle calls the virtual representation a CPE, but this documentation typically uses the term CPE object to help distinguish the virtual representation from the actual CPE device. The CPE object contains basic information that Oracle needs about the device and how it must be configured to work with Site-to-Site VPN.

A single CPE object public IP can have up to 8 IPSec connections.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-list.htm#)
- 

- Open the navigation menu and select Networking . Under Customer connectivity , select Customer-premises equipment .

The Customer-premises equipment list page opens. All CPEs in the selected compartment are displayed in a table.
- To view the CPEs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the CPEs in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a CPE to open its details page, where you can view its status and perform other tasks.

To create another CPE, select Create CPE .

To perform other actions on a CPE directly from the list table, you can also select any of the following options from the Actions menu (three dots) in the row for that CPE:
- View details : Open the details page for the CPE.
- Copy OCID : Copy the OCID of the CPE to the clipboard.
- Move resource : See[Moving a CPE to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm).
- Manage tags : Add one or more tags to the CPE. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : See[Deleting a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-delete.htm)
- 

Use the[network cpe list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/cpe/list.html)command and required parameters to list the available CPEs:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListCpes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/ListCpes)
