# Billing Tools Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingtoolsoverview.htm
- Fetched: 2026-09-05 01:42 CDT

# Billing Tools Overview

The Oracle Cloud Infrastructure Console Billing pages let you view and manage financial transactions related to your Oracle Cloud account.

You can view subscription details and usage, view and download invoices and usage statements, view payment history, make payments using the Oracle payment service with a credit card or PayPal, and manage account upgrades and payment method.
- [Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/subscriptions.htm)
- [Invoices](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm)
- [Usage Statements](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagestatements.htm)
- [Payment History](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm)
- [Managing Account Upgrades and Payment Method](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/changingpaymentmethod.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

To use the Subscriptions , Invoices , and Payment History pages, the following policy statements are required:
```

```

For Invoices usage, the following policy statement is required:
```

```

For Subscriptions , the following policy statement is required:
```

```

For Invoices , the following policy statement is required:
```

```

For Payment History , the following policy statement is required:
```

```

To use the Usage Statements page, the policy statements from both[Cost Analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#policy)and[Cost and Usage Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#policy)
