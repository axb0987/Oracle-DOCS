# Implementing Automatic Rollback
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/auto-rollback.htm
- Fetched: 2026-09-05 02:54 CDT

# Implementing Automatic Rollback

Use scripts to implement automatic rollback when an apply job fails in Resource Manager. Automatic rollback scripts involve monitoring for job failures and defining a rollback procedure that includes validation, custom triggers, and actions.

In production environments, establishing a robust and flexible deployment strategy is essential. A common best practice is to integrate OCI Resource Manager with a Continuous Integration/Continuous Delivery (CI/CD) system to manage the full deployment lifecycle—including automatic rollback.

Oracle Cloud Infrastructure (OCI) offers a native, fully-featured CI/CD platform:[OCI DevOps](https://docs.oracle.com/iaas/Content/devops/using/devops_overview.htm). This service provides the necessary tools and pipelines to seamlessly orchestrate deployment, testing, monitoring, and rollback operations.

## Automatic Rollback Script

To help you get started, we've provided the following sample Bash script, which can be used in an OCI DevOps deployment pipeline. This script demonstrates a mechanism for automatically rolling back an OCI Resource Manager stack in the event of a deployment failure.

The script serves as a starting point that you can customize to suit your specific requirements, ensuring it aligns with the unique needs of your deployment workflows.

[Script](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/auto-rollback.htm#)

```

```

The automatic rollback logic implemented in the script includes the following steps:
- Initiate Deployment :[Create an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)to deploy the updated Terraform configuration.
- Monitor Deployment Status : Continuously monitor the status of the apply job: See[Getting a Job's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm).
- Evaluate Failure : If the apply job fails, evaluate predefined criteria to determine whether to trigger an automatic rollback.
- Identify Stable State : Retrieve the successful apply jobs for the stack and determine the target job that you want to roll back to: See[Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm).
- Trigger Rollback :[Create an apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm)
