# Creating a Stack from a Folder
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local-folder.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Stack from a Folder

Create a stack in Resource Manager from a local Terraform configuration stored in a folder.

Ensure that the Terraform configuration is valid. See[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm)and[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/authoring-configurations.htm).

This task can be performed using the Console only.

- On the Stacks list page, select Create stack . If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
- On the Create stack page, under Choose the origin of the Terraform configuration , select My configuration .
- Under Stack configuration , select Folder .
- Select Folder and add the revised[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm).
You can either drag the file onto the dialog's control or select Browse and navigate to the location of the file or folder.
The page is populated with information contained in the Terraform configuration.
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
