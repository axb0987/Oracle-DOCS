# Listing Stacks
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Stacks

List stacks in Resource Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#)
- 

- Open the navigation menu and select Developer Services . Under Resource Manager , select Stacks .
The Stacks list page opens. All stacks in the selected compartment are displayed in a table.
- To view the stacks in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the stacks in the list.
- To filter the list by tag, select add next to Tag filters .

## Actions

In the list table, select the name of a stack to open its details page, where you can view its status and perform other tasks.

To perform an action on a stack directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that stack:
- View stack details :[Open the details page for the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).
- Edit :[Update the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack.htm).
- Open support request : Open the Support Request panel, in which you can access support options. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Delete :[Delete the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm).

To create a stack, select Create stack .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list.html)oci resource-manager stack list`command and required parameters to list stacks.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ListStacks](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/StackSummary/ListStacks)
