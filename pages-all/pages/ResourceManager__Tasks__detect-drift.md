# Detecting Drift in a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm
- Fetched: 2026-09-05 02:55 CDT

# Detecting Drift in a Stack

Detect drift in a stack in Resource Manager. Drift is the difference between the actual, real-world state of your infrastructure and the stack's last executed configuration.

Common reasons for drift include a team member adding a production tag to your resources or deleting a resource.

You can detect drift for new stacks created from compartments or for stacks where the last job run was Apply or Import state . When detecting drift, you can specify all resources or selected resources.
Tip  
  
After detecting drift, list the drift status for resources. See[Listing Drift Status for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- Go to the Actions menu at the top of the page and select Run drift detection .
- In the Run drift detection panel, select the option you want.
- 

All resources : Detects drift for all resources in the stack.
- 

Selected resources : Detects drift for the specified resources in the stack.

You can select an address from the list or enter the address. Each resource is identified by a resource address, which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index. For example, the resource address for the fourth Compute instance with the name "test_instance" is`oci_core_instance.test_instance[3]`. The resource type is`oci_core_instance`, a period acts as delimiter, the resource name is`test_instance`, and the index is`3`in bracket. For more details and examples of resource addresses, see the Terraform documentation at[Examples](https://developer.hashicorp.com/terraform/cli/state/resource-addressing#examples).
- To retrieve the latest versions available from the configured source of Terraform providers, select Show advanced options and select Upgrade provider versions .
The stack must be Terraform 0.14 or later, and if the stack is older, it must be upgraded to[use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-stack-tf-reg.htm). This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack.[Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock)are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration.
- Select Run drift detection .

A work request is started. When the work request is complete, the drift status appears on the stack's details page, in the Stack information section.

To monitor the operation or investigate a failure, open the work request and view its logs. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)and[Getting Log Content for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-work-request-log-entries-content.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/detect-drift.html)oci resource-manager stack detect-drift`command and required parameters to detect drift in a stack.

```

```

Tip  
  
Store the work request OCID returned for this asynchronous operation. Use it to retrieve work request details, error messages, log entries, or raw log content. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm).

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[DetectStackDrift](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/DetectStackDrift)operation to detect drift.
Tip  
  
Use the work request OCID returned by the operation to retrieve log entries or raw log content. See[Getting Logs for a Work Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-work-request-logs.htm)
