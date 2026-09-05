# Updating Variables for a Stack (Manual)
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating Variables for a Stack (Manual)

Update the variable values used by a stack in Resource Manager through manual entry.

When you update a stack, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm#)
- 

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Edit .
- On the Edit stack panel, select Configure variables .
- Change the variable values that you want.
- Select Next .
- In the Review panel, verify the stack configuration.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)oci resource-manager stack update`command and required parameters to update the variable values used by a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack)operation to update the variable values used by a stack.

When defining details for[UpdateStackDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateStackDetails), provide the updated variable values using the`variables`
