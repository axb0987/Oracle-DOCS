# Using OCI FinOps Hub
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/FinOps.htm
- Fetched: 2026-09-05 01:42 CDT

# Using OCI FinOps Hub

Use the Console's Cost Management FinOps Hub to get an overall view of the most common cost management features, and as the central location for cost management resources in Oracle Cloud Infrastructure.

Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Overview .

The FinOps Hub page is organized in terms of the following sections:
- Inform
- Subscriptions
- Costs
- Budgets and Forecasts
- Optimize
- Operate

## Subscriptions

Under Subscriptions , you can visualize a summary of the IaaS/PaaS[Oracle Universal Credits](https://www.oracle.com/cloud/universal-credits/)subscription's annual commitment (or funded allocation) usage period. The[Pay As You Go](https://www.oracle.com/cloud/universal-credits/)pricing model only shows a costs summary.
Note  
  
Cloud[Applications Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm)aren't supported.

To view the subscription summary, select an active[Oracle Universal Credits](https://www.oracle.com/cloud/universal-credits/)subscription from the Subscription field (both the subscription ID and name are indicated).

The vertical stacked bar chart shows the subscription's usage over time (by month) for the past year, inclusive of any overages. You can hover over a data point to view more details, such as the amount of usage or overage for the particular month.

During a commitment (or funded allocation) usage period for the subscription, either a gauge icon is shown, or a horizontal bar chart for one or more simultaneous usage periods indicating the amount of credits that have been used, along with the commitment expiration date. You can hover your mouse over the bar chart to view the usage and the remaining credits balance.

For more information, see[Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/subscriptions.htm).

## Costs

Depending on your[organization](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm)(single tenancy, or parent tenancy with one or more child tenancies), under Costs you can visualize costs by region (single tenancy or multi-tenant organization), compartment, and product description. A donut chart is available for each, and you can hover your mouse over a data point to view more region, compartment, or product description cost details in the local currency.
From Time Frame , select from the following date ranges:
- Last Month (the default)
- Last 2 Months
- Last 3 Months
- Last 6 Months

For example, if the current date was June 3, 2024, Last Month shows costs from May 4, 2024 to June 3, 2024. Total cost at the top of the chart indicates the sum of costs for the selected time frame, across the three cost categories.

Click Analyze costs to go directly to[Cost Analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm), where you can view more charts, and download reports of aggregated cost data on your Oracle Cloud Infrastructure consumption.

## Budgets and Forecasts

Under Budgets &amp; forecasts , you can view any active[budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm), and create budgets to monitor spending against budgets and manage forecast spending. Budget details are shown in a similar manner as the Budgets page, in terms of the budget name, type, amount, spent amount, percent spent in period, and the forecast.

Click Create budget to go to the Budgets page, where you can create a new budget. For more information, see[Listing Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/list-budget.htm),[Creating a Budget](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/create-budget.htm), and[Getting a Budget's Details](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/get-budget.htm).

## Optimize

Under Optimize (powered by[Cloud Advisor](https://docs.oracle.com/iaas/Content/CloudAdvisor/home.htm)) personalized and actionable cost saving opportunities are recommended for the top three OCI services with potential cost savings and potential cost saving actions. The vertical bar chart shows the potential cost savings per month, in terms of the service on the X axis, and the cost savings in the local currency on the Y axis. You can also hover your mouse over one of the data points corresponding to the top three services, to view the amount of cost savings.

Under Recommendations , the list of cost saving opportunities are available, where you can view the recommendation type and the potential monthly savings amount in the local currency. Under Recommendation type , click the name to go to Cloud Advisor's detail page for the particular recommendation.

Click All recommendations to go directly to Cloud Advisor's[Recommendations](https://docs.oracle.com/iaas/Content/CloudAdvisor/Concepts/view-recommendations.htm)page.
For more information, see[Cloud Advisor](https://docs.oracle.com/iaas/Content/CloudAdvisor/home.htm)and[Implementing Cloud Advisor Recommendations](https://docs.oracle.com/iaas/Content/CloudAdvisor/Tasks/implementing_cloud_advisor_recommendations.htm).
Note  
  
It can take up to 32 hours for any recommendations to appear in the Optimize interface.

## Operate
Under Operate , access related functions in the Oracle Cloud Infrastructure Console:
- FinOps FOCUS compliant data export : Download FOCUS CSV cost reports from the Cost and Usage Reports page. The reports conform to the industry-standard[FinOps Open Cost &amp; Usage Specification (FOCUS)](https://focus.finops.org/#specification). Click Exports to go the Cost and Usage Reports page. For more information, see[Cost Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm).
- Control User Access : Create IAM policies to enable access for cost management. If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). Also see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingoverview.htm#Required)for more information on setting up all Billing and Cost Management policies.
- Manage resource metadata : Define resource metadata using[tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm), and automate tagging using tag default values. Click Tag Namespaces to go this part of the Console. For more information, see[Tags and Tag Namespace Concepts](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm).
- Find savings opportunities : Click Resource Utilization Monitoring to use the Monitoring service's Metrics Explorer page to analyze resource usage and identify potential resource waste. See[Viewing a Custom Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-view-chart.htm)
