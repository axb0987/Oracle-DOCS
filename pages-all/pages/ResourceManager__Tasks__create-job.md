# Creating a Job
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Job

Create a job in Resource Manager, such as plan, apply, or destroy.
Note  
  
A job might fail because of a downstream service issue. For example, an apply job for creating a compute instance might fail because of a temporary connectivity issue in the Compute service. When a job fails because of downstream service issue, the job retries according to the Go SDK default retry policy. See[Go SDK for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/tools/go/latest/).

You can perform the following job creation tasks:
- [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-plan.htm)
- [Creating a Plan Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-plan-rollback.htm)
- [Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-apply.htm)
- [Creating an Apply Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-apply-rollback.htm)
- [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-import.htm)
- [Creating a Destroy Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-job-destroy.htm)
- [Enabling Premium Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/premium-jobs.htm#top)
- [Implementing Automatic Rollback](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/auto-rollback.htm)
- [Bulk Destroying Resources and Deleting Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/bulk-destroy-delete2.htm)
