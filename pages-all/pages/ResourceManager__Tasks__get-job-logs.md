# Getting Logs for a Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm
- Fetched: 2026-09-05 02:55 CDT

# Getting Logs for a Job

View console logs for a job in Resource Manager.
Note  
  

For plan jobs, the log file is the same as the execution plan. Review the execution plan to ensure that it lists the resources you intend to provision. View the log file and note the "message" fields in the sequence of log entries. These values represent the sequence of operations specified in the configuration.

If you see problems or errors and want to make changes, then update the appropriate[Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm)(`.tf`file),[update the stack to use the revised configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm),[run a plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm), and then[review the new execution plan (output of the plan job)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#)
- 

These steps show how to get logs for a job in a compartment. You can also get logs for a job[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- On the Jobs list page, select the job that you want to work with. If you need help finding the list page or the stack, see[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm).
- On the job's details page, select Logs .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs.html)oci resource-manager job get-job-logs`command and required parameters to get logs for a job as a paged list of entries.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Response for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#)

The command returns JSON objects that describe log entries. Each object has a message member with a property that displays one line of the execution plan. In this example, the plan job creates a single virtual cloud network (VCN); the remaining members show details about the VCN.
```

```

- 

Use the[GetJobLogs](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobLogs)
