# Creating a Destroy Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Destroy Job

Create a destroy job in Resource Manager to release (tear down) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.

The stack's job history and state remain after running a destroy job. You can monitor the status and review the results of a destroy job by inspecting the stack's log files.

The destroy job is available when resources exist that were created by the stack.
Note  
  

We recommend running a destroy job before[deleting a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm)to release associated resources first. When you delete a stack, its associated state file is also deleted; therefore, you lose track of the state of its associated resources. Cleaning up resources associated with a deleted stack can be difficult without the state file, especially when those resources are spread across multiple compartments. To avoid difficult cleanup later, we recommend that you release associated resources first by running a destroy job. If the stack has no associated resources, then a destroy job isn't available. You can safely[delete](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm)such a stack without concern about missing state files.

Data cannot be recovered from destroyed resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Destroy .
- (Optional) In the Destroy panel, edit the default name for the job. Avoid entering confidential information.
- To retrieve the latest versions available from the configured source of Terraform providers, select Show advanced options and select Upgrade provider versions .
The stack must be Terraform 0.14 or later, and if the stack is older, it must be upgraded to[use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-stack-tf-reg.htm). This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack.[Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock)are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration.
- To generate detailed log content for debugging, select Show advanced options and select the log level that you want from Detailed log level .
For more information, see[Debugging Terraform](https://developer.hashicorp.com/terraform/internals/debugging).
- To adjust the maximum number of concurrent operations as[Terraform walks the graph](https://developer.hashicorp.com/terraform/internals/graph#walking-the-graph), select Show advanced options and edit the value for Maximum number of parallel operations . (Default:`10`.) Use this option to speed up the job.

Note  
  
A high value might cause throttling of resources. For example, consider a Terraform configuration that defines hundreds of compute instances. An[Apply job attempts to create as many instances as possible at the same time. In this example, a value of`100`might cause throttling by the Compute service.
- To fetch the latest state before running the job, select Show advanced options and select Refresh resource states before checking for differences .

Use this option to refresh the state first. For example, consider using this option with an[Apply job that you intend to run on manually updated (existing) infrastructure.
Note  
  
Refreshing the state can affect performance. If the configuration includes several resources, consider not using this option.
- (Optional) Add one or more tags to the job: Select Show advanced options to show tagging options.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Destroy .

The destroy job is created. The new job is listed under Jobs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-destroy-job.html)oci resource-manager job create-destroy-job`command and required parameters to run a destroy job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob)operation to create a destroy job.

For an example of the`operation`part of the request, see[CreateDestroyJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateDestroyJobOperationDetails).

## What's Next

After running a destroy job, get the job's details to check its status. You can optionally view the Terraform state file, view the logs, and confirm deletion of the resources. You can also re-create destroyed resources.

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm).

To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the Job details page, then select View state under Resources . Optionally select Show changes in this version .

To view the logs for the job, select the job to open its details page, then select Logs under Resources .

To confirm deletion of the resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm).

To re-create a stack's resources after the resources are destroyed,[run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm). The new resources differ from previously destroyed resources by their unique[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)
