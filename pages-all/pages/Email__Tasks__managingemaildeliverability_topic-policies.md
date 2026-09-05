# Required IAM Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingemaildeliverability_topic-policies.htm
- Fetched: 2026-09-05 02:01 CDT

# Required IAM Policy

Learn about the policies required to access metrics in Email Deliverabilty and Reputation Governance dashboard.

The Email Deliverability and Reputation Governance dashboard displays two types of data: metrics from the Monitoring service and logs from the Logging service. You must configure policies to allow access to both types of data. If you see authorization or related errors when viewing the dashboard, check for missing or incomplete policies.

The following are example policies that show how to allow access for each type of data displayed on the dashboard:

```

```

```

```

Replace`<group-name>`and`<compartment-name>`with the values specific to your environment. If you don’t need permissions for each compartment, use`in tenancy`instead of specifying a compartment.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Email Delivery, see[Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm)
