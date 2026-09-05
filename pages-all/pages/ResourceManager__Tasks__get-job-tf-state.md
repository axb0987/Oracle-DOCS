# Getting a Job's State File
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm
- Fetched: 2026-09-05 02:55 CDT

# Getting a Job's State File

Download the Terraform state file (`.json`) from a completed apply, apply rollback, or import job in Resource Manager.
Note  
  
To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a`409`error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#)
- 

These steps show how to get the state for a job in a compartment. You can also get the state for a job[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- On the Jobs list page, find the job that you want to work with. If you need help finding the list page or the stack, see[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm).
- For the job that you want, select View state

The job's details page opens with View state selected.

Don't see View state ? Check that the job has finished running, and that it's an[apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm),[apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm), or[import job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm). No state files are available for[canceled](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm)jobs.
- (Optional) Select Show changes in this version .
- (Optional) Select Download Terraform state .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-state.html)oci resource-manager job get-job-tf-state`command and required parameters to get a job's state.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[GetJobTfState](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobTfState)operation to get a job's state.

[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#)

```

```

## Example State File

The following example state file is from a successful apply job for the Document[template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Reference/templates.htm).

[Expand to see example](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#)

```

```
