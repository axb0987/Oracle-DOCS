# Creating a Cost Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm
- Fetched: 2026-09-05 01:43 CDT

# Creating a Cost Monitor

Create a custom cost monitor to analyze cloud spending based on your selected filters, such as compartment, region, or service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#)
- 

On the Cost monitors list page, select Create cost monitor . If you need help finding the list page, see[Listing Cost Monitors](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm).

Creating a cost monitor consists of the following pages:
- 

[1. Basic information](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#basic-info-cost-monitor-create)
- 

[2. Resources to monitor](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#define-resources-to-monitor-create)
- 

[3. (Optional) Alert subscriptions](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#set-alert-subscription-cost-monitor-create)
- 

[4. Review and create](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#review-fleet)

## 1. Basic information

The Basic information page is where you provide the basic information for a cost monitor in Cost Anomaly Detection .

Enter the following information:
- Name : Enter a name for the cost monitor. The name can include only alphanumeric characters, dashes, and underscores, and it can't start with a number. Don't include confidential information.
- Description : Enter a suitable description for the cost monitor. Avoid entering confidential information.
- (Optional) Tags : Add tags to the cost monitor resource. Select existing tag namespace, tag key, and value.

### Tags

Add tags to the cost monitor and subscription. For more information, see[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)
- Select one or more tag namespaces, keys, and values.

## 2. Resources to monitor

The Resources to monitor page is where you define the resources to be monitored.

Enter the following information:
- Tenancy : Select the tenancy where the resources are active. You can select a child tenancy only if you're signed in to a parent tenancy in an[organization](https://docs.oracle.com/iaas/Content/General/organization/home.htm).
- Create a resource filter :
Note  
  

- Only values with cost data appear in the filter parameter value list. For example, if you aren't using the Logging service, it doesn't appear as an option when you filter by Service.
- 

When you filter by several parameters, such as Compartment and Region, the filter uses the AND operator. For example: Compartment =`Development`AND Region =`US East (Ashburn)`AND Service =`Compute`.

When you select several values for the same parameter, the filter uses the OR operator. For example: Service =`Compute`OR`Database`.
- Compartment : Select all, or filter for one or more compartment names. To monitor cost for the entire tenancy select root compartment name.
- Region (Optional) : Select all, or filter for one or more region names.
Add Additional Parameters : You can create filters using any of the following parameters.
- Tag: Select a tag namespace, a tag key, and one or more values.
- Service: Select one or more values.
- Product Description
- SKU (Part Number)
- Unit
- Subscription ID
- Availability Domain
- Platform
- Resource Type

To combine filters with AND logic, select Add Parameter (for example,`Tag = application:Application1 AND Tag = environment:production)`.

## 3. (Optional) Alert subscriptions

Note  
  

- You can still view cost anomalies in the Console, API, or CLI without an alert subscription.
- Anomalies are visible when anomaly cost impact doesn't trigger an alert.
- 

Select Yes to set the thresholds and define the recipients to be alerted when the thresholds are met.
Set the following thresholds:
- Alert threshold - absolute (currency) : Define an absolute value for daily cost anomaly variance used to trigger an alert. (for example, $10 triggers an alert if the difference between the daily cost forecast and the actual cost is +/- $10. If the difference is less than $10 an alert isn't triggered.
- Operator : Add an additional criteria to your alert threshold by selecting an AND or OR operators. Use the AND operator to trigger an alert based on a percentage variance but only if the absolute cost impact is greater than a certain amount. (for example, if threshold = 10% AND $100 if the variance is 1,000% but the absolute cost impact is $5 then an alert isn't be triggered.
- Alert threshold - relative (%): Define the percentage value for daily cost anomaly variance used to trigger an alert. (for example, a value of 10 triggers an alert if the difference between the daily cost forecast and the actual cost is +/- 10%. If the difference is less than 10% an alert isn't triggered.
- Select No to create the alert subscriptions later. For more information n, see[Editing a Cost Monitor](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm).

### Recipients

Define the alert's email recipients by selecting one of the following options:
- Link to an existing notification group : Select the notification group name.
- Create a new notification group :
- Name : Enter a name for the notification group.
- Description : Enter a description for the notification group.
- Email recipients : Enter one or more email addresses. If you enter more than one email address, then separate them using a comma, space, or adding each address on its own line.

## 4. Review and create

Review the information you provided in each section and select Create .
- 

Use the[oci costad cost-anomaly-monitor create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-anomaly-monitor/create.html)command and required parameters to create a new cost monitor:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCostAnomalyMonitor](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAnomalyMonitor/CreateCostAnomalyMonitor)
