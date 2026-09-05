# Listing Job Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Job Resources

List job resources in Resource Manager for a completed apply or apply rollback job. Job resources are infrastructure objects such as virtual networks and compute instances that were provisioned by the job.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm#)
- 

These steps show how to list resources for a job in a compartment. You can also list resources for a job[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- On the Jobs list page, select the job that you want to work with. If you need help finding the list page or the stack, see[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-jobs.htm).
- On the job's details page, select Job resources .
Don't see Job resources ? Check that the job has finished running, and that it's either an[apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)or an[apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm). No job resources are available for[canceled](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm)jobs.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/associated-resource-summary/list-job-associated-resources.html)oci resource-manager associated-resource-summary list-job-associated-resources`command and required parameters to list job resources.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ListJobAssociatedResources](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/AssociatedResourceSummary/ListJobAssociatedResources)
