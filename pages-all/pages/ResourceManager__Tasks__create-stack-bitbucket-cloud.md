# Creating a Stack from Bitbucket Cloud
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Stack from Bitbucket Cloud

Create a stack in Resource Manager from a Terraform configuration stored in Bitbucket Cloud . Select a configuration source provider that specifies the Bitbucket Cloud information needed to access the configurations.

Ensure that the Terraform configuration is valid. See[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm)and[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/authoring-configurations.htm).

For information about configuration source providers, see[Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/managingconfigurationsourceproviders.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bitbucket-cloud.htm#)
- 

- On the Stacks list page, select Create stack . If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
- On the Create stack page, under Choose the origin of the Terraform configuration , select Source code control system .
- Under Stack configuration , for Source code management type , select Bitbucket Cloud .
- Select the Bitbucket Cloud configuration source provider that you want.
If you need to create a configuration source provider, select Create configuration source provider and enter values. For information about the fields, see[Creating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm).
- Select the Bitbucket Cloud workspace, repository, and branch. The list of branches is limited to 100.
For information about Bitbucket Cloud workspaces, see[https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/](https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/).
- (Optional) To use a directory other than the root directory for running Terraform, specify the working directory. This field is visible when the selected branch has directories. Examples:

- One level: Directory
- Two levels: Directory/Subdirectory
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
- (Optional) Run apply
- Select Create .

The stack is created and its details page opens.

If you selected Run apply , then Resource Manager runs the apply action on the new stack.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-bitbucket-cloud.html)oci resource-manager stack create-from-bitbucket-cloud`command and required parameters to create a stack from Bitbucket Cloud .

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack)operation to create a stack from Bitbucket Cloud .

For an example of the`configSource`part of the request, see[CreateBitbucketCloudConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateBitbucketCloudConfigSourceDetails)
