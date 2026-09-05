# Creating a Plan Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Plan Job

Create a plan job in Resource Manager.

Creating (running) a plan job parses your Terraform configuration and converts it into an execution plan for the associated stack. The execution plan lists the sequence of specific actions planned to provision your Oracle Cloud Infrastructure resources, including actions that are expected after running an apply job. We recommend running a plan job (generating an execution plan) before[running an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm). The execution plan is handed off to the apply job, which then executes the instructions.

For configurations stored in a source code control system, such as GitHub or GitLab, the job uses the most recent commit.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Plan .
- (Optional) In the Plan panel, edit the default name for the job. Avoid entering confidential information.
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
- Select Plan .

The plan job is created. The new job is listed under Jobs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-job.html)oci resource-manager job create-plan-job`command and required parameters to run a plan job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob)operation to create a plan job.

For an example of the`operation`part of the request, see[CreatePlanJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreatePlanJobOperationDetails).

## What's Next

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm)
