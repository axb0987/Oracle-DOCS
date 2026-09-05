# Securing DevOps
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/devops_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing DevOps

Oracle Cloud Infrastructure DevOps provides an end-to-end, continuous integration and continuous delivery (CI/CD) platform for developers.

## Security Recommendations
- Assign least privilege access for IAM users and groups to resource types in devops-family.
- To minimize inadvertent deletes by an authorized user or malicious deletes, Oracle recommends to giving DEVOPS_&lt;Resource name&gt;_DELETE permission to a minimum possible set of IAM users and groups. Give DEVOPS_&lt;Resource name&gt;_DELETE permissions only to tenancy and compartment admins.
- To protect your DevOps resources from any security vulnerability, provide credentials to read-only accounts only.
DevOps includes the following resources:
- devops-project
- devops-deploy-artifact
- devops-deploy-environment
- devops-deploy-pipeline
- devops-deploy-stage
- devops-deployment
- devops-work-requests
- devops-repository
- devops-build-pipeline
- devops-build-pipeline-stage
- devops-build-run
- devops-connection
- devops-trigger For more information, see[Resource Types and Permissions](https://docs.oracle.com/iaas/Content/devops/using/devops_iampolicies.htm#resource-types).

## Security Policy Examples

Create this policy to allow group`DevopsUsers`to perform all actions on the resources, except deleting them.

```

```

For more information on DevOps policies and examples, see[DevOps IAM Policies](https://docs.oracle.com/iaas/Content/devops/using/devops_iampolicies.htm)
