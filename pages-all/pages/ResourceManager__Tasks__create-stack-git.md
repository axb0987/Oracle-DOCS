# Creating a Stack from Git
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Stack from Git

Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.

Ensure that the Terraform configuration is valid. See[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm)and[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/authoring-configurations.htm).

For information about configuration source providers, see[Managing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/managingconfigurationsourceproviders.htm).

## Modules from Private Git Repositories

No credentials are required in a private Git source URL within the Terraform configuration.

Following are prerequisites for a job to install a module from a private Git repository without these credentials:
- The module's private Git repository must be stored on a public Git server.
- The configuration source provider must have access to this private repository.

For examples of Git source URLs, see[Generic Git Repository](https://developer.hashicorp.com/terraform/language/modules/sources#generic-git-repository).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#)
- 

- On the Stacks list page, select Create stack . If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
- On the Create stack page, under Choose the origin of the Terraform configuration , select Source code control system .
- Under Stack configuration , for Source code management type , select GitHub or GitLab .
- Select the Git configuration source provider that you want.
If you need to create a configuration source provider, select Create configuration source provider and enter values. For information about the fields, see[Creating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm)or[Creating a GitLab Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm).
- Select the Git repository and branch. The list of branches is limited to 100.
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
- (Optional) To automatically provision resources on creation of the stack, select Run apply .
- Select Create .

The stack is created and its details page opens.

If you selected Run apply , then Resource Manager runs the apply action on the new stack.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-git-provider.html)oci resource-manager stack create-from-git-provider`command and required parameters to create a stack from Git.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#)

```

```

- 

Use the[CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack)operation to create a stack from Git.

For an example of the`configSource`part of the request, see[CreateGitConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateGitConfigSourceDetails).

[Example request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#)

```

```
