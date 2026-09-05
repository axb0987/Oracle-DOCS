# Creating an Import Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating an Import Job

Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack.

For example, use an import job to migrate a local Terraform environment to Resource Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#)
- 

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- Go to More actions and select Import state .
- (Optional) In the Import panel, edit the default name for the job. Avoid entering confidential information.
- For Select a Terraform state file to upload , add the Terraform state file that you want to import into the stack.
You can drag the file onto the control or select Browse and navigate to the file location.
- To retrieve the latest versions available from the configured source of Terraform providers, select Show advanced options and select Upgrade provider versions .
The stack must be Terraform 0.14 or later, and if the stack is older, it must be upgraded to[use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-stack-tf-reg.htm). This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack.[Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock)are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration.
- (Optional) Add one or more tags to the job: Select Show advanced options to show tagging options.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Import .

The import job is created. The new job is listed under Jobs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-import-tf-state-job.html)oci resource-manager job create-import-tf-state-job`command and required parameters to run an import job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob)operation to create an import job.

For an example of the`operation`part of the request, see[CreateImportTfStateJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateImportTfStateJobOperationDetails).

## What's Next

After running an import job, get the job's details to check its status. You can optionally view the Terraform state file and view the logs.

Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm).

To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the Job details page, then select View state under Resources . Optionally select Show changes in this version .
