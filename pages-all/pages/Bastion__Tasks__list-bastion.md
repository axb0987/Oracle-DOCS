# Listing Bastions
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm
- Fetched: 2026-09-05 01:42 CDT

# Listing Bastions

List the bastions in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Bastion .
The Bastions list page opens. All bastions in the selected compartment are displayed in a table.
- To view the bastions in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the bastions in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a bastion to open its details page, where you can view its status and perform other tasks.

To perform an action on a bastion directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that bastion:
- View details : Open the details page for the bastion.
- Copy OCID : Copy the OCID of the bastion to the clipboard.
- Move resource :[Move the bastion to another compartment](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/change-compartment-bastion.htm).
- Delete :[Delete a bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/delete-bastion.htm).

To create a bastion, select Create bastion .
- 

Use the[oci bastion bastion list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/bastion/list.html)command and required parameters to list all bastions in a compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListBastions](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Bastion/ListBastions)
