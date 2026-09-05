# Listing VMware Solution License Allocations
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm
- Fetched: 2026-09-05 03:08 CDT

# Listing VMware Solution License Allocations

List the Oracle Cloud VMware Solution license allocations in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm#)
- 

## Navigate to Allocations

- Open the navigation menu and select Hybrid &amp; Multicloud . Under VMware Solution , select Allocations .

The Allocations list page opens. All license allocations in the selected compartment are displayed in a table.
- 

To view the license allocations in a different compartment, use the Compartment filter to switch compartments.
Tip  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the license allocations in the list.

From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a license allocation to open its details page, where you can view its status and perform other tasks.

To perform an action on a license allocation directly from the list table, select an available option from the Actions menu in the row for that license allocation:
- View details : Open the details page for the license allocation.
- Copy OCID : Copy the OCID of the license allocation to the clipboard.
- Move resource : Move the license allocation.
- Manage Tags : Add one or more tags to the license allocation. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : Delete the license allocation.

To create a license allocation, select Create . See[Creating VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-create.htm)
- 

Use the[byol-allocation list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/byol-allocation/list.html)command and required parameters to list all license allocations in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListByolAllocations](https://docs.oracle.com/iaas/api/#/en/vmware/latest/ByolAllocationSummary/ListByolAllocations)
