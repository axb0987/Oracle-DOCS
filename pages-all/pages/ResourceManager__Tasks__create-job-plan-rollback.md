# Creating a Plan Rollback Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Plan Rollback Job

Create a plan rollback job in Resource Manager.

Creating (running) a plan rollback job parses the Terraform configuration in the target job and converts it into an execution plan for the associated stack. The execution plan lists the sequence of specific actions planned to rollback your Oracle Cloud Infrastructure resources, including actions that are expected after running an apply rollback job.

We recommend running a plan rollback job (generating an execution plan) before running an[apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm), using the following flow.
- 

Identify the successful apply job that you want to roll back to.

The job you want to roll back to is also known as the "target job."
- 

Create a plan rollback job for the target job.

Instructions are on this page.
- 

Confirm that the plan rollback job succeeded.
- 

Confirm that the generated execution plan meets expectations.
- 

[Create an apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm)using the generated execution plan (`executionPlanRollbackStrategy`).

The execution plan is handed off to the apply rollback job, which then executes the instructions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- In the Jobs list, find the apply job that you want to roll back to.
- From the Actions menu (three dots) for the job, select Rollback .
The Rollback panel opens, showing the OCID and name of the selected[apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-apply.htm)( OCID of target rollback job and Name of target rollback job ).
- For Rollback job type , select Plan to create a plan rollback job.
- (Optional) Edit the default name for the rollback job. Avoid entering confidential information.
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
- Select Ok .

The plan rollback job is created. The new job is listed under Jobs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-rollback-job.html)oci resource-manager job create-plan-rollback-job`command and required parameters to run a plan rollback job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob)operation to create a plan rollback job.

For examples of details for a plan rollback job, see[PlanRollbackJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/PlanRollbackJobOperationDetails).

## What's Next

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm)
