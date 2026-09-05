# Creating a Stack from an Existing Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Stack from an Existing Compartment

Using resource discovery, create a stack in Resource Manager based on an existing compartment to generate a Terraform configuration that describes the compartment's resources.

For more information about resource discovery, see[Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#)
- 

- On the Stacks list page, select Create stack . If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
- On the Create stack page, under Choose the origin of the Terraform configuration , select Existing compartment .
- Select the compartment and region that contain the resources that you want to[capture](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm).
- (Optional) To filter for specific[services supported for resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Reference/services-reference.htm#supported-services), select Selected and then select the services you want.

Note  
  
This setting can't be changed when editing the stack later.
- (Optional) To use[custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm), select Use custom providers and then select the bucket that contains the custom provider.
- (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
- Select the compartment that you want to store the stack in.
- (Optional) Under Tags , add one or more tags to the stack.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next twice.
No variables are listed for the Existing compartment stack origin because no Terraform configuration exists yet.
- In the Review panel, verify the stack configuration.
- Select Create .
A work request runs on the stack. When the work request finishes, a job runs to generate a[Terraform configuration file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm)for the stack. When the job finishes, the resources in the selected compartment are captured in the generated configuration. You can[recreate these resources in another compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/recreate-infra.htm).

To monitor the operation or investigate a failure, open the work request and view its logs. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)and[Getting Log Content for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-compartment.html)oci resource-manager stack create-from-compartment`command and required parameters to create a stack from a compartment.

```

```

[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#)

For example (discovers[supported resources](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm#supported-resources)from the`core`and`database`services; the source compartment is not a root compartment):

```

```

[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#)

```

```

```

```

Tip  
  
Save the`opc-work-request-id`returned by this asynchronous operation. Use it to retrieve work request details, error messages, log entries, or raw log content. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm).

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack)operation to create a stack from a compartment.

For an example of the`configSource`part of the request, see[CreateCompartmentConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateCompartmentConfigSourceDetails).
Tip  
  
Use the work request OCID returned by the operation to retrieve log entries or raw log content. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm).

[Example request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#)

```

```

## What to Do Next

You can[download](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm)the generated Terraform configuration file. You can also[re-create](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/recreate-infra.htm)infrastructure in another compartment.
Note  
  
Alternatively, you can view the generated Terraform configuration file in Code Editor. For more information, see[Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/code-editor.htm)
