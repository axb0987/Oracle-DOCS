# Listing Private Templates
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Private Templates

List private templates in Resource Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#)
- 

- Open the navigation menu and select Developer Services . Under Resource Manager , select Private Templates .
The Private templates list page opens. All private templates in the selected compartment are displayed in a table.
- To view the private templates in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the private templates in the list.
- To filter the list by tag, select add next to Tag filters .

## Actions

In the list table, select the name of a private template to open its details page, where you can view its status and perform other tasks.

To perform an action on a private template directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that private template:
- View private template details :[Open the details page for the private template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template.htm).
- Create stack from private template :[Create a stack from the private template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm).
- Delete private template :[Delete the private template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-template.htm).

To create a private template, select Create private template .
- 

Use the[oci resource-manager template list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/list.html)command and required parameters to list templates, setting`--template-category-id`to`3`:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[ListTemplates](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/ListTemplates)operation to list templates. To filter the list to private templates, set`templateCategoryId`to`3`
