# Required IAM Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders_topic-policies.htm
- Fetched: 2026-09-05 02:01 CDT

# Required IAM Policy

Learn about the policies required to manange aproved senders.

Permissions are required for managing approved senders. For example, to manage approved senders, use the following policy:

```

```

Using the`email-family`policy ensures that the user has the necessary access to all Email Delivery resources and not just approved senders. In addition, the user whose credentials will be used to send email from the approved sender must have the right policies. For more information, see[Create SMTP Credentials](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/gettingstarted_topic-create-smtp-credentials.htm#console).

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Email Delivery, see[Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm)
