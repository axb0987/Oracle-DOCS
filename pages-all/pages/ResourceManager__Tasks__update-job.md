# Updating a Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating a Job

Update a job's name or tags in Resource Manager.

When you update a job, you can also update its tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm#)
- 

These steps show how to update a job in a compartment. You can also update a job[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- On the Jobs list page, select the job that you want to work with. If you need help finding the list page or the stack, see[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm).
- To update the job name, follow these steps:
- Select Edit job .
- In the Edit job panel, update the job name.
- Select Save changes .
- Add one or more tags to the job: Select Tags .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/update.html)oci resource-manager job update`command and required parameters to update a job.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[UpdateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/UpdateJob)
