# Billing and Cost Management Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingoverview.htm
- Fetched: 2026-09-05 01:42 CDT

# Billing and Cost Management Overview

Oracle Cloud Infrastructure provides various billing and cost management tools that make it easy to manage your service costs. You can estimate costs, create budgets to set spending thresholds, view cost reports, and visualize your spending with charts and reports. View your subscription details, invoices, usage statements, payment history, manage your payment method, and earn rewards.

Tip  
  
Watch a[video introduction](https://www.youtube.com/watch?v=amF1q1BdtSM)to the service.

## FinOps Hub

Use the OCI FinOps Hub to get an overall view of the most common cost management features. View subscription usage, costs by region, compartment, and product description. Create budgets to set limits on your spending and manage forecast spending, and optimize costs using Cloud Advisor functionality. For more information, see[Using OCI FinOps Hub](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/FinOps.htm).

## Billing and Usage on the Console Home Page

You can get a snapshot of billing and usage, and check your balance, on the Console home page. For more information, see[Viewing Billing Details](https://docs.oracle.com/iaas/Content/GSG/Concepts/console_topic-AccountCenter-Billing.htm).

## Console Dashboards Integration

You can use Console Dashboards to get a quick view of billing and cost management information in your tenancy. For more information, see[Console Dashboards Integration](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/dashboards-billing-widgets.htm).

## Cost Estimator

The Cloud Cost Estimator helps you figure out your estimated monthly usage and costs for Oracle's Infrastructure and Platform Cloud services, before you commit to an amount. See[Estimating Monthly Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/signingup_topic-Estimating_Costs.htm)for more information.

## Budgets

Use Budgets to set thresholds for your Oracle Cloud Infrastructure spending. You can set alerts on your budget to let you know when you might exceed your budget, and you can view all of your budgets and spending from one single place in the Oracle Cloud Infrastructure Console. See[Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm)for more information.

## Cost Analysis

Cost Analysis is a visualization tool that helps you track and optimize your Oracle Cloud Infrastructure spending, allows you to generate charts, and download accurate, reliable tabular reports of aggregated cost data on your Oracle Cloud Infrastructure consumption. Use the tool for spot checks of spending trends and for generating reports. For more information, see[Cost Analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm).

## Scheduled Reports

Use the Scheduled reports page to generate scheduled reports based on[saved reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports)from Cost Analysis. For more information, see[Scheduled Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/scheduledreportoverview.htm).

## Cost Reports

On the Cost and Usage Reports page, you can download[cost reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports)that indicate the cost of resource consumption. Industry-standard FOCUS CSV cost reports, which conform to the[FinOps Open Cost &amp; Usage Specification (FOCUS)](https://focus.finops.org/#specification), are also generated and available for download.

For more information, see[Cost Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm).

## Subscriptions

Use the Subscriptions page to view subscriptions detail, usage information, billing schedule, and rate card information. For more information, see[Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/subscriptions.htm).

## Invoices

You can pay invoices, and view and download invoices for your Oracle Cloud Infrastructure usage on the Invoices page. For more information, see[Invoices](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm).

## Usage Statements

Download and view usage statements that show your monthly subscription usage. For more information, see[Usage Statements](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagestatements.htm).

## Payment History

Use the Payment History page to track and monitor your Oracle Cloud Infrastructure paid invoice history. Only paid invoices are shown on this page. For more information, see[Payment History](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm).

## Account Upgrades and Payment Method

Use the Upgrade and Manage Payment section of the Console to manage how you pay for your Oracle Cloud Infrastructure usage. For more information, see[Managing Account Upgrades and Payment Method](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/changingpaymentmethod.htm).

## Oracle Support Rewards

Oracle Support Rewards lets you earn rewards when using OCI services. Rewards can be applied to pay for support contracts that you have for other eligible on-premises Oracle products. See[Oracle Support Rewards Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/supportrewardsoverview.htm)for more information.

## Organizations and Billing Integration

You can use the Oracle billing and cost reporting features to centrally manage the cost and usage information across all tenancies in your[organization](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm).

See[Cost Reporting Integration](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm#organization_management_cost_reporting)and[Viewing Subscription Details and Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#viewing_subscription_details)for more information.

## Required IAM Policy

To enable users to use Billing and Cost Management tools and monitor the costs associated with your account, you must grant them access by writing a policy . If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

See the corresponding required IAM policy topics for each Billing and Cost Management feature:
- [Upgrade and Manage Payment](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/changingpaymentmethod.htm#Required_IAM_Policy).
- [Subscriptions, Invoices, Payment History, and Usage Statements](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingtoolsoverview.htm#subs_inv_paymenthist_required_IAM_policy)
- [Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm#policy)
- [Cost and Usage Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#policy)
- [Cost Analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#policy)
- [Oracle Support Rewards](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/supportrewardsoverview.htm#supportrewards_required_IAM_policy)
- [Scheduled Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/scheduledreportoverview.htm#scheduledreports_required_IAM_policy)
