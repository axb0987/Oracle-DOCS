# Getting a Stack's State File
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-state.htm
- Fetched: 2026-09-05 02:55 CDT

# Getting a Stack's State File

Download the Terraform state file used by a stack in Resource Manager. The Terraform state file for a stack is the one associated with the most recent successful job.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-state.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-state.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-state.htm#)
- 

The Terraform state file listed on the stack details page is the same as the Terraform state file listed on the job details page for the most recent successful job.

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select View state .
- To download the stack's state file, go to More actions and select Download Terraform state .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/get-stack-tf-state.html)oci resource-manager stack get-stack-tf-state`command and required parameters to get the Terraform state file for a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[GetStackTfState](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/GetStackTfState)
