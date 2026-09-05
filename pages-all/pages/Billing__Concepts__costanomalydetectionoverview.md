# Cost Anomaly Detection
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanomalydetectionoverview.htm
- Fetched: 2026-09-05 01:43 CDT

# Cost Anomaly Detection

Cost anomaly detection continuously monitors the daily cloud cost and informs you of abnormal usage trends. It minimizes the detection time and negative cost impacts. Cost anomaly alerts proactively notify you about anomaly events. For each detected event, cost anomaly insights help reduce the investigation and remediation efforts by providing thorough root cause analysis.

## How Cost Anomaly Detection Works

### Cost Monitors

Cost monitors define the resources to analyze. Following are the different types of cost monitors:
- Default Cost Monitors : OCI automatically creates a default service monitor for the combination of a tenancy, service, and region (for example: tenancy 1, Compute, and Ashburn region).
- Custom Cost Monitors : You can create custom cost monitors by applying filters to analyze specific resources or workloads.
Note  
  
A cost monitor requires 60 days of historical data before it becomes active.
Cost Monitor Scenarios Examples

Cost Monitor Scenario How to Configure Cost Monitoring Scenarios
Monitor costs for resources in a child tenancy (business entity).

Create a custom cost monitor with a filter, where Tenancy = Business Entity and other criteria as needed.
Monitor resources with a specific tags (for example, Cost Center and Application). Create a custom cost monitor with filters, where Tag Namespace = Tag Namespace name , Tag key = CostCenter and value = ' CostCenter1'

AND

Tag Namespace = Tag Namespace name , Tag key = Application and Value = Application Name 1 .
Monitor specific compartment's cost (for example, Development compartment). Create a Custom Cost Monitor with a filter, where Compartment =`Development`.
Service level cost for a specific region (for example, Compute in Ashburn). Default monitors automatically monitor region specific service-level cost within a tenancy.

### Cost Anomaly Algorithms

Cost anomaly detection's algorithm uses machine learning considering yearly, weekly, and daily seasonality plus holiday effects to forecast daily cost data and automatically detect anomaly events. It learns from user provided feedback improving its accuracy.
Each anomaly includes cost anomaly insights, which suggest possible causes for the anomaly. Cost anomaly insights identify changes to the resources within the cost monitor by comparing the resources from the previous day with those on the event day. Insights highlight the cost impact of:
- New resources created : Resources present on the event day but not on the previous day.
- Resources deleted : Resources not present on the event day but available on the previous day.
- Resource usage changes : Resources present on both days with changes in cost.

### Cost Anomaly Alerts

Cost anomaly alerts are available for each cost monitor. If an anomaly is detected, and its cost variance exceeds the alert threshold, then an email alert is sent to the notification group. An email is sent once per day for each anomaly event.

A cost anomaly alert subscription, associated with a cost monitor, defines the alert threshold and email addresses to notify. Alert thresholds, set as an absolute value and as a percentage variance between the forecasted and actual costs, define the minimum cost variation required to trigger an alert. For example, if the anomaly's cost impact is $100 and the alert threshold is $500, OCI doesn't trigger an alert. If the expected cost is $100 and the actual cost is $120, an alert threshold of 10% triggers an alert.
Note  
  
You can use email aliases and distribution lists to send out anomaly alerts. We recommend adding at least one actual email address to ensure that recipients receive alerts if another address becomes inactive.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).
To use Cost Anomaly Detection, you must belong to a group with permission to use Cost Anomaly Detection resources in the tenancy (the root compartment) or permission to use all resources in the tenancy. All cost anomalies and cost monitors are created in the root compartment, regardless of the compartment they target. IAM policies that grant permissions outside of the root compartment don't grant access to Cost Anomaly Detection resources.

Use Case IAM Policy
Administrator of Cost Anomaly Detection Features

`Allow group <groupname> to manage costad-family in tenancy`

`Allow group <group-name> to read usage-report in tenancy`

`Allow group <group-name> to read organizations-family in tenancy`
View only access of Cost Anomaly Detection Features

`Allow group <groupname> to read costad-family in tenancy`

`Allow group <group-name> to read usage-report in tenancy`

`Allow group <group-name> to read organizations-family in tenancy`
