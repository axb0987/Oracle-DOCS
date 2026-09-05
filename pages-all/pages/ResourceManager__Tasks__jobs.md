# Managing Jobs
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm
- Fetched: 2026-09-05 02:56 CDT

# Managing Jobs

Manage jobs in Resource Manager.
Note  
  
For descriptions of job types, lifecycle states, and the default retry policy, see[job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resourcemanager.htm#concepts__jobdefinition)in the overview page.

## Required IAM Policy

Use policies to grant access to jobs in Resource Manager.

To manage jobs, you must be given the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).

Administrators: For common policies that give groups access to jobs in Resource Manager, see[Manage Stacks and Jobs (Securing Resource Manager)](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__stacks-jobs).

## Tasks

You can perform the following job management tasks:
- [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm)
- [Creating a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job.htm)
- [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-plan.htm)
- [Creating a Plan Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-plan-rollback.htm)
- [Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-apply.htm)
- [Creating an Apply Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-apply-rollback.htm)
- [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-import.htm)
- [Creating a Destroy Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-destroy.htm)
- [Enabling Premium Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/premium-jobs.htm#top)
- [Implementing Automatic Rollback](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/auto-rollback.htm)
- [Bulk Destroying Resources and Deleting Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/bulk-destroy-delete2.htm)
- [Retrieving the Latest Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-lock-file.htm)
- [Debugging a Job by Generating Detailed Log Content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-debug.htm)
- [Getting a Job's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm)
- [Listing Job Resources](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-job-resources.htm)
- [Listing Job Outputs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-job-outputs.htm)
- [Getting Detailed Log Content for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-detailed-log-content.htm)
- [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs.htm)
- [Getting Logs Content for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm)
- [Getting a Job's Terraform Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-tf-config.htm)
- [Getting the Terraform Output for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-tf-plan.htm)
- [Getting a Job's State File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-tf-state.htm)
- [Updating a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-job.htm)
- [Canceling a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/cancel-job.htm)

## Lifecycle States

Review possible lifecycle states for jobs.
- Accepted (`ACCEPTED`): The job was accepted for processing.
- In progress (`IN_PROGRESS`): The job is running (executing).
- Failed (`FAILED`): The job did not complete execution.
- Succeeded (`SUCCEEDED`): The job has completed successfully.
- Canceling (`CANCELING`): The job is being canceled; a notification has been sent, but the job has not yet stopped running.
- Canceled (`CANCELED`): The job was canceled and has stopped running.

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
