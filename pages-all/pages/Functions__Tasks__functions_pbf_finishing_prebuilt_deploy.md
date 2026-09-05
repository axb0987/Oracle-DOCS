# Finishing Pre-Built Function Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_finishing_prebuilt_deploy.htm
- Fetched: 2026-09-05 02:07 CDT

# Finishing Pre-Built Function Deployment

Find out how to complete pre-built function deployment in OCI Functions, and find out about the different deployment states shown in the deployment dialog.

## Initial Waiting State

After you select Create , the dialog displays the state of each deployment task. Initially, each task has a "Waiting" state.
- The following resources are being created :`Waiting`
- Function: &lt;your-function-name&gt; :`Waiting`
- Dynamic Group: &lt;your-dynamic-group-name&gt; :`Waiting`
- IAM Policy: &lt;your-iam-policy-name&gt; :`Waiting`

## Deployment States Updated

As each deployment task completes, its state changes to "Done."
- The following resources are being created :`Waiting`
- Function: &lt;your-function-name&gt; :`Done`
- Dynamic Group: &lt;your-dynamic-group-name&gt; :`Done`
- IAM Policy: &lt;your-iam-policy-name&gt; :`Waiting`

## Deployment Completes

When deployment completes, all deployment tasks change to a "Done" state.
- The following resources are being created :`Done`
- Function: &lt;your-function-name&gt; :`Done`
- Dynamic Group: &lt;your-dynamic-group-name&gt; :`Done`
- IAM Policy: &lt;your-iam-policy-name&gt; :`Done`

Select Close to display the function's details page.
