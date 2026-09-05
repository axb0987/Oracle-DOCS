# Deleting a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm
- Fetched: 2026-09-05 02:55 CDT

# Deleting a Stack

Delete a stack in Resource Manager. You can't undo the deletion of a stack.
Important  
  
When you delete a stack, its associated resources persist but its associated state file is deleted. Cleaning up the resources associated with a deleted stack can be difficult without the state file, especially when those resources are spread across multiple compartments. To avoid difficult cleanup, we recommend that you release associated resources first by[running a destroy job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm). If the stack has no associated resources, then you can safely delete it without concern about missing state files.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm#)
- 

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Delete .
- When prompted, confirm the deletion.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/delete.html)oci resource-manager stack delete`command and required parameters to delete a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[DeleteStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/DeleteStack)
