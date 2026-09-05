# Listing Jobs
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Jobs

List jobs in Resource Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#)
- 

These steps show how to list jobs in a compartment. You can also list jobs[in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm).

- Open the navigation menu and select Developer Services . Under Resource Manager , select Jobs .
The Jobs list page opens. All jobs in the selected compartment are displayed in a table.
- To view the jobs in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the jobs in the list.
- To filter the list by tag, select add next to Tag filters .

## Actions

In the list table, select the name of a job to open its details page, where you can view its status and perform other tasks.

To perform an action on a job directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that job:
- View job details :[Open the details page for the job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm).
- Open support request : Open the Support Request panel, in which you can access support options. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Cancel job :[Cancel the job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm).
- Download Terraform configuration :[Get the Terraform configuration for the job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-config.htm).
- Copy OCID : Copy the OCID of the job to the clipboard.
- Add tags : Add one or more tags to the job. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- View tags : View the job's existing tags. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/list.html)oci resource-manager job list`command and required parameters to list jobs.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ListJobs](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/JobSummary/ListJobs)
