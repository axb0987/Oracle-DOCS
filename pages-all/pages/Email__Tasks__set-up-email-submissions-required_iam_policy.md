# Required IAM Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/set-up-email-submissions-required_iam_policy.htm
- Fetched: 2026-09-05 02:01 CDT

# Required IAM Policy

Learm about the required policies to manage DKIM.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Email Delivery, see[Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm).

To enable all operations on all email resources for a specific user group, use the following policy:
```

```

To set up email submissions, use the following policy:
```

```
