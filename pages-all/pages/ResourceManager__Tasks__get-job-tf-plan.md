# Getting the Terraform Output for a Plan Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm
- Fetched: 2026-09-05 02:55 CDT

# Getting the Terraform Output for a Plan Job

Download the output of a plan job in Resource Manager.
Note  
  
To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a`409`error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm#)
- 

These steps show how to get plan output for a job in a compartment. You can also get plan output for a job[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- On the Jobs list page, select the job that you want to work with. If you need help finding the list page or the stack, see[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm).
- Select Download Terraform plan and then select the file format option you want (binary or JSON file).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-plan.html)oci resource-manager job get-job-tf-plan`command and required parameters to get the output of a plan job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).

[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm#)

Example to get the output of a plan job in JSON format:

```

```

- 

Use the[GetJobTfPlan](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobTfPlan)
