# Managing Budget Alert Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/managingalertrules.htm
- Fetched: 2026-09-05 01:43 CDT

# Managing Budget Alert Rules

View and manage budget alert rules in Billing and Cost Management.

You can set email alerts on your budgets. You can set alerts that are based on a percentage of your budget or an absolute amount, and on your actual spending or your forecast spending.

You can perform the following budget alert rules tasks:
- 

[Listing Budget Alert Rules](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-alert-rule.htm)
- 

[Creating a Budget Alert Rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-alert-rule.htm)
- 

[Getting a Budget Alert Rule's Details](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/get-alert-rule.htm)
- 

[Editing a Budget Alert Rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-alert-rule.htm)
- 

[Deleting a Budget Alert Rule](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-alert-rule.htm)

## About Budget Alert Emails

Budget alert emails are sent during the billing period when an alert threshold for the following criteria has been exceeded:
- Budget Threshold Amount
- Alert Type
- Alert Threshold Amount
- Alert Threshold Type
Note  
  
If you change any of your threshold criteria after a budget alert email has already been sent, you will receive a subsequent email when the new criteria is exceeded, even during the same billing period.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm)
