# Getting a Stack's Terraform Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm
- Fetched: 2026-09-05 02:55 CDT

# Getting a Stack's Terraform Configuration

Download the Terraform configuration used by a stack in Resource Manager. The Terraform configuration file for a stack is the one associated with the most recent successful job.
Note  
  
For stacks created from[Terraform configurations in Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm), configuration files aren't available for download until a[job is successfully run](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm)on the stack.

Alternatively, you can view the generated Terraform configuration file in Code Editor. For more information, see[Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/code-editor.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- Next to Terraform configuration , select Download .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/get-stack-tf-config.html)oci resource-manager stack get-stack-tf-config`command and required parameters to get a stack's Terraform configuration file.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[GetStackTfConfig](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/GetStackTfConfig)
