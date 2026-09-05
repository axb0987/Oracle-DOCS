# Creating a Private Template
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-template.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Private Template

Create a private template in Resource Manager.

You can share private templates with anyone in your tenancy who has[sufficient permissions](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm#policies).

For instructions to create a stack from your private template, see[Creating a Stack from a Template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-template.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-template.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-template.htm#)
- 

- On the Private templates list page, select Create private template . If you need help finding the list page or the private template, see[Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-template.htm).
- In the Create private template panel, select the option corresponding to the location of the Terraform configuration ( Folder or .Zip file ) and then perform one of the following actions to upload the configuration:
- Drag the folder or zip file onto the panel.
- Select Browse and navigate to the location of the folder or zip file.
- Enter a name and optional description for the private template. Avoid entering confidential information.
- (Optional) Enter a detailed description of the private template.
The detailed description is displayed in the Browse templates panel when the template is expanded.
- Select Show advanced options .
- Select the compartment that you want to store the private template in.
- (Optional) Upload an icon to use with the template by performing one of the following actions:
- Drag the icon file onto the panel.
- Select Browse and navigate to the location of the icon file.
The icon is displayed in the Browse templates panel when the template is expanded. A template icon file has the following requirements: PNG format, 50 KB maximum, 110 x 110 pixels.
- (Optional) Add one or more tags to the private template: Select Show advanced options to show tagging options.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
- 

Use the[oci resource-manager template create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/create.html)command and required parameters to create a private template:

```

```

Example request:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[CreateTemplate](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/CreateTemplate)
