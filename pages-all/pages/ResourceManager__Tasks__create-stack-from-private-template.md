# Creating a Stack from a Private Template
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Stack from a Private Template

Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.

For more information about templates, see[Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Reference/templates.htm)and[Managing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm#)
- 

- On the Private templates list page, find the private template that you want to work with. If you need help finding the list page or the private template, see[Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-template.htm).
- From the Actions menu (three dots) for the private template, select Create stack from private template .
The Create stack page opens with the private template already selected.
- (Optional) To use[custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm), select Use custom providers and then select the bucket that contains the custom provider.
- (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
- Select the compartment that you want to store the stack in.
- For Terraform version , select the version used by the Terraform configuration.
- (Optional) Under Tags , add one or more tags to the stack.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .
- In the Configure variables panel, review the variables listed from the Terraform configuration and change as needed.

Important  
  
Don't add your private key or other confidential information to configuration variables.
- Select Next .
- In the Review panel, verify the stack configuration.
- (Optional) To automatically provision resources on creation of the stack, select Run apply .
Run apply is selected by default for stacks created from[the Deploy to Oracle Cloud button](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/deploybutton.htm#tocreatestack)or from[Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/launch_a_stack.htm).
- Select Create .

The stack is created and its details page opens.

If you selected Run apply , then Resource Manager runs the apply action on the new stack.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-template.html)oci resource-manager stack create-from-template`command and required parameters to create a stack from a template.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack)operation to create a stack from a template.

For an example of the`configSource`part of the request, see[CreateStackTemplateConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateStackTemplateConfigSourceDetails)
