# Creating an Apply Rollback Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating an Apply Rollback Job

Create an apply rollback job in Resource Manager.

When you create (run) an apply rollback job for a stack, Terraform provisions the resources and executes the action defined in the target job's Terraform configuration, applying the execution plan to the associated stack. This job rolls back your Oracle Cloud Infrastructure resources to a previous state.

We recommend[creating (running) a plan rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)(generating an execution plan) before running an apply rollback job, using the following flow.
- 

Identify the successful apply job that you want to roll back to.

The job you want to roll back to is also known as the "target job."
- 

[Create a plan rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)for the target job.
- 

Confirm that the plan rollback job succeeded.
- 

Confirm that the generated execution plan meets expectations.
- 

Create an apply rollback job using the generated execution plan (`executionPlanRollbackStrategy`).

Instructions are on this page.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- In the Jobs list, find the job that you want to use for creating an apply rollback job.
You can select a[plan rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)(recommended) or an[apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm).
- From the Actions menu (three dots) for the job, select Rollback .
The Rollback panel opens, showing the OCID and name of the selected job. Execution plan rollback strategy is automatically selected based on the selected job you're using for the apply rollback job: Use execution plan from plan rollback job for a[plan rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)and Automatically approve for an[apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm). For more information about Automatically approve , see[Auto-Approve Option for Terraform Apply Command](https://developer.hashicorp.com/terraform/cli/commands/apply#auto-approve)
- For Rollback job type , select Apply to create an apply rollback job.
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

The apply rollback job is created. The new job is listed under Jobs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-apply-rollback-job.html)oci resource-manager job create-apply-rollback-job`command and required parameters to run an apply rollback job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob)operation to create an apply rollback job.

For examples of details for an apply rollback job, see[ApplyRollbackJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/ApplyRollbackJobOperationDetails).

## What's Next

Depending on the number and type of resources specified, a given apply rollback job can take some time.

After running an apply rollback job, get the job's details to check its status. You can optionally view the Terraform state file, view the logs, and confirm existence of provisioned resources.

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm).

To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the Job details page, then select View state under Resources . Optionally select Show changes in this version .

To view the logs for the job, select the job to open its details page, then select Logs under Resources .

To confirm existence of newly provisioned resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm)
