# Listing VMware Solution Licenses
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-list.htm
- Fetched: 2026-09-05 03:08 CDT

# Listing VMware Solution Licenses

List the Oracle Cloud VMware Solution licenses in a compartment using the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-list.htm#)
- 

## Navigate to Licenses

- Open the navigation menu and select Hybrid &amp; Multicloud . Under VMware Solution , select License Management .

The License Management list page opens. All licenses in the selected compartment are displayed in a table.
- 

To view the licenses in a different compartment, use the Compartment filter to switch compartments.
Tip  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the licenses in the list.

From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a license to open its details page, where you can view its status and perform other tasks.
Important  
  
After opening the details page, if no allocations have been made for this license, the Create Allocation button is displayed. Select the button to create a license allocation.

To perform an action on a license directly from the list table, select an available option from the Actions menu in the row for that license:
- View details : Open the details page for the license.
- Copy OCID : Copy the OCID of the license to the clipboard.
- Move resource : Move the license to another compartment.
- Manage Tags : Add one or more tags to the license. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : Delete the license.

To create a license, select Register BYOL License .
- 

Use the[byol list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/byol/list.html)command and required parameters to list all licenses in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListByols](https://docs.oracle.com/iaas/api/#/en/vmware/latest/ByolSummary/ListByols)
