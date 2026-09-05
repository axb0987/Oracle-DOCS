# Creating an Apply Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating an Apply Job

Create an apply job in Resource Manager.

When you create (run) an apply job for a stack, Terraform provisions the resources and executes the actions defined in your Terraform configuration, applying the execution plan to the associated stack to create (or modify) your Oracle Cloud Infrastructure resources. We recommend[running a plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm)(generating an execution plan) before running an apply job.

For a walk-through using CLI for cloud provisioning in a CI/CD pipeline, see[IaC in the Cloud: Integrating Terraform and Resource Manager into your CI/CD Pipeline - Building With the OCI CLI](https://blogs.oracle.com/developers/iac-in-the-cloud%3a-integrating-terraform-and-resource-manager-into-your-cicd-pipeline-building-with-the-oci-cli).

For configurations stored in a source code control system, such as GitHub or GitLab, the job uses the most recent commit. The time required to complete an apply job depends on the number and type of cloud resources to be created.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Apply .
- (Optional) In the Apply panel, edit the default name for the job. Avoid entering confidential information.
- (Optional) For Apply job plan resolution , select the name of the latest generated plan job. Only the latest generated plan job is available. If no plan job has been generated for this stack, then only the default value is available ( Automatically approve ). For more information about Automatically approve , see[Auto-Approve Option for Terraform Apply Command](https://developer.hashicorp.com/terraform/cli/commands/apply#auto-approve).
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
- Select Apply .

The apply job is created. The new job is listed under Jobs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-apply-job.html)oci resource-manager job create-apply-job`command and required parameters to run an apply job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Examples](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#)

Example 1: Reference a plan job.

```

```

Example 2: Automatically approve (don't reference a plan job).

```

```

- 

Use the[CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob)operation to create an apply job.

For an example of the`operation`part of the request, see[CreateApplyJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateApplyJobOperationDetails).

## What's Next

Depending on the number and type of resources specified, a given apply job can take some time.

After running an apply job, get the job's details to check its status. You can optionally view the Terraform state file, view the logs, and confirm existence of provisioned resources.

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm).

To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the Job details page, then select View state under Resources . Optionally select Show changes in this version .

To view the logs for the job, select the job to open its details page, then select Logs under Resources .

To confirm existence of newly provisioned resources,[inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm)
