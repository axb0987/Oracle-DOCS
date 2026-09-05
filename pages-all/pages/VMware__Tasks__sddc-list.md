# Listing VMware Solution SDDCs
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-list.htm
- Fetched: 2026-09-05 03:09 CDT

# Listing VMware Solution SDDCs

List the Oracle Cloud VMware Solution SDDCs in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-list.htm#)
- 

- Open the navigation menu and select Hybrid . Under VMware Solution , select Software-Defined Data Centers .

The Software-Defined Data Centers list page opens. All SDDCs in the selected compartment are displayed in a table.
- To view the SDDCs in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the SDDCs in the list.

From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a SDDC to open its details page, where you can view its status and perform other tasks.

To perform an action on a SDDC directly from the list table, select an available option from the Actions menu in the row for that SDDC:
- View details : Open the details page for the SDDC.
- Copy OCID : Copy the OCID of the SDDC to the clipboard.
- Move resource :[Move the SDDC to another compartment](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-move.htm).
- Manage Tags : Add one or more tags to the SDDC. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Terminate :[Delete the SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-delete.htm).

To create a SDDC, select Create SDDC .
- 

Use the[sddc list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/list.html)command and required parameters to list all SDDCs in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListSddcs](https://docs.oracle.com/iaas/api/#/en/vmware/latest/SddcSummary/ListSddcs)
