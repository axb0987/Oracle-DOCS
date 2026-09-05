# Updating the DevOps Location for a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating the DevOps Location for a Stack

Update the DevOps repository or other location details used by a stack in Resource Manager. The updated location is used when you run jobs on the stack.
Note  
  
For information about configuration source providers, see[Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm).

When you update a stack, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm#)
- 

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Edit .
- On the Edit stack page, select a different[DevOps](https://docs.oracle.com/iaas/Content/devops/using/home.htm)repository or branch.
- Change other values as needed.
For information about the fields, see[Creating a Stack from DevOps](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm).
- Select Next twice.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update-stack-update-dev-ops-config-source-details.html)oci resource-manager stack update-stack-update-dev-ops-config-source-details`command and required parameters to update the DevOps location used by a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack)operation to update the DevOps location used by a stack.

For an example of the`configSource`part of the request, see[UpdateDevOpsConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateDevOpsConfigSourceDetails)
