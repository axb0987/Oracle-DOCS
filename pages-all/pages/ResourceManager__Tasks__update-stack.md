# Updating a Stack
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack.htm
- Fetched: 2026-09-05 02:57 CDT

# Updating a Stack

Update a stack in Resource Manager.

[Updating a Stack (Any Type)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm)provides the basic steps. The following pages describe specific ways to update stacks:
- [Updating a Stack's Terraform Configuration (Zip File or Folder)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm)
- [Updating the Bitbucket Cloud Configuration Source Provider for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp-bitbucket-cloud.htm)
- [Updating the Bitbucket Server Configuration Source Provider for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp-bitbucket-server.htm)
- [Updating the Bucket for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-bucket.htm)
- [Updating the DevOps Location for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-devops.htm)
- [Updating the Git Configuration Source Provider for a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-csp.htm)
- [Updating Variables for a Stack (Manual)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm)
- [Using Custom Providers with a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm)
- [Using Terraform Registry with an Older Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm)
Tip  
  
After updating a stack, run a plan job and then get the job logs. Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/jobs.htm#lifecycle)) by[getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job.htm). Succeeded (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can[get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-job-logs-content.htm)
