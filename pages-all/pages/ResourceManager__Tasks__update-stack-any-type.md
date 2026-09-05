# Updating a Stack (Any Type)
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating a Stack (Any Type)

Update a stack in Resource Manager. This page provides the basic steps for updating a stack.

When you update a stack, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm#)
- 

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Edit .
- On the Edit stack page, update the values you want.
For example, upload a different[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm), or update the stack name or description. For information about the fields, see[Creating a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm).
- Select Next .
- In the Configure variables panel, update variable values as needed.
- Select Next .
- In the Review panel, verify the stack configuration.
- To automatically provision resources on creation of the stack, select Run apply .
- Select Save changes .

The Stack details page opens.

If Run apply was selected, then Resource Manager runs the apply action on the updated stack.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)oci resource-manager stack update`command and required parameters to update a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack)
