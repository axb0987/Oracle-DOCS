# Required IAM policies
- Source: https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/implementing-iam-policies.htm
- Fetched: 2026-09-05 01:48 CDT

# Required IAM policies

This page describes the Identity and Access Management requirements and security policies that Cloud Advisor uses to ensure that your resources are protected.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

To get started with Cloud Advisor, an administrator must grant each user access to Cloud Advisor and to the resources that Cloud Advisor recommendations impact through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

The resource name for Cloud Advisor is`optimizer-api-family`. The following is an example policy to grant users access to Cloud Advisor to the resources that Cloud Advisor recommendations impact:

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For more information about Cloud Advisor policies, see[Creating Cloud Advisor policies](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/../Reference/cloudadvisorpolicyreference.htm).

Additional Cloud Advisor required permissions

Although the permissions described above let you view the recommendations and some information about them, Cloud Advisor features granular permissions to support compartment and resource based security policies. These permissions are granted at the compartment level rather than the tenancy level as was previously done. If you do not have the correct permissions, you might not be able to view all the recommendation details, or the resource details for the recommendation you are viewing. To view all the recommendation and resource metadata, contact your account administrator to get the permissions for your compartment. For more information, see[Viewing Categories and Recommendations](https://docs.oracle.com/iaas/Content/CloudAdvisor/Concepts/view-recommendations.htm#recommendations)
