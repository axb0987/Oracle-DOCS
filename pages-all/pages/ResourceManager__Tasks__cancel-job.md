# Canceling a Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm
- Fetched: 2026-09-05 02:54 CDT

# Canceling a Job

Cancel a running job in Resource Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#)
- 

These steps show how to cancel a job in a compartment. You can also cancel a job[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- On the Jobs list page, find the job that you want to work with. If you need help finding the list page or the stack, see[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm).
- From the Actions menu (three dots) for the job, select Cancel .
The Cancel job dialog box opens.
- If the job is for[Import state ,[Apply , or[Destroy , then select the option that you want:

- Cancel job : Resource Manager attempts to cancel the job gracefully. Internally, the running Terraform process signals the child processes to end. The job might run partially, depending on the responses of the child processes, even though the ultimate job status is Canceled .
- Force the job to cancel now : Forces the job to cancel.
Note  
  
Forcing a job to cancel might cause a mismatch between the state file and the actual resource states.
- Select Yes, cancel job .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/cancel.html)oci resource-manager job cancel`command and required parameters to cancel a job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[CancelJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CancelJob)
