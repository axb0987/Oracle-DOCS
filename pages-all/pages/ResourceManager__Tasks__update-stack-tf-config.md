# Updating a Stack's Terraform Configuration (Zip File or Folder)
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating a Stack's Terraform Configuration (Zip File or Folder)

Update the zip file or folder Terraform configuration used by a stack in Resource Manager. The updated configuration is used when you run jobs on the stack. A folder-based update is available using the Console only.

When you update a stack, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Before You Begin

Review prerequisites for updating the Terraform configuration used by a stack in Resource Manager.
Important  
  
If you're uploading a different Terraform configuration, ensure that the configuration file is valid. See[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/authoring-configurations.htm)and[Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm).

Ensure that you have your revised[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm)(`.zip`file or folder) ready for upload. No configuration file is available for download until a job is successfully run on the stack. To edit a Terraform configuration that was generated from a[template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Reference/templates.htm)or existing compartment using[resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm), first[download the configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm). Then use the edited configuration`.zip`file for the update.

If the stack's configuration is stored in Git or a bucket, then upload the configuration there.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm#)
- 

Tip  
  
As an alternative to these steps, edit the generated Terraform configuration file in Code Editor. For more information, see[Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/code-editor.htm).

After completing all the prerequisites, follow these steps in the Console to update a stack's Terraform configuration from a zip file or folder.

- On the Stacks list page, find the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- From the Actions menu (three dots) for the stack, select Edit .
- On the Edit stack page, select Folder or .Zip file and add the revised[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm).
You can either drag the file onto the dialog's control or select Browse and navigate to the location of the file or folder.
- (Optional) Update other values as needed.
For example, update the stack name or description. For information about the fields, see[Creating a Stack from a Zip File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm).
- Select Next .
- In the Configure variables panel, update variable values as needed.
- Select Next .
- In the Review panel, verify the stack configuration.
- To automatically provision resources on creation of the stack, select Run apply .
- Select Save changes .

The Stack details page opens.

If Run apply was selected, then Resource Manager runs the apply action on the updated stack.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)oci resource-manager stack update`command and required parameters to update the Terraform configuration zip file used by a stack.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack)operation to update the Terraform configuration zip file used by a stack.

For an example of the`configSource`part of the request, see[UpdateZipUploadConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateZipUploadConfigSourceDetails)
