# Viewing Categories and Recommendations
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/view-recommendations.htm
- Fetched: 2026-09-05 01:47 CDT

# Viewing Categories and Recommendations

This section explains how to view Cloud Advisor categories and recommendations. Recommendations help you reduce costs by finding and adjusting resources that are underutilized. For example, they find underutilized compute instances, overprovisioned Autonomous AI Lakehouse and Autonomous AI Transaction Processing instances, and unattached block volumes and boot volumes.

This section contains the following main topics:

[Viewing Categories](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/viewing-categories.htm)

[Viewing Recommendations](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Tasks/list-and-get-recommendations.htm)

## Required IAM Policies

This page describes the Identity and Access Management requirements and security policies that Cloud Advisor uses to ensure that your resources are protected.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

To get started with Cloud Advisor, an administrator must grant each user access to Cloud Advisor and to the resources that Cloud Advisor recommendations impact through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

The resource name for Cloud Advisor is`optimizer-api-family`. The following is an example policy to grant users access to Cloud Advisor to the resources that Cloud Advisor recommendations impact:

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For more information about Cloud Advisor policies, see[Creating Cloud Advisor policies](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/../Reference/cloudadvisorpolicyreference.htm).

Additional Cloud Advisor required permissions

Although the permissions described above let you view the recommendations and some information about them, Cloud Advisor features granular permissions to support compartment and resource based security policies. These permissions are granted at the compartment level rather than the tenancy level as was previously done. If you do not have the correct permissions, you might not be able to view all the recommendation details, or the resource details for the recommendation you are viewing. To view all the recommendation and resource metadata, contact your account administrator to get the permissions for your compartment. For more information, see[Additional Required Permissions](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/additional_required_permissions.htm).
