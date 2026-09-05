# Getting a Cost Monitor's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/get-cost-monitor-details.htm
- Fetched: 2026-09-05 01:43 CDT

# Getting a Cost Monitor's Details

Get the details of a cost monitor in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/get-cost-monitor-details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/get-cost-monitor-details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/get-cost-monitor-details.htm#)
- 

On the Cost monitors list page, select the cost monitor that you want to work with. If you need help finding the list page or the cost monitor, see[Listing Cost Monitors](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm).

The details page opens and displays information about the cost monitor. Some items in the page are read-only, and other items enable you to[edit and update the cost monitor's configuration](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm#top). Access the various resources associated with the cost monitor by selecting the Details , Alert subscription , or Tags tabs.

## Alert Subscription

Alert subscriptions proactively email recipients within the notification group when an anomaly is detected that exceeds the alert subscription's alert threshold.
Note  
  
Cost anomaly alert subscriptions aren't configured by default.[Create an alert subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#top)for each cost monitor that you want to receive alerts for.
An alert subscriptions defines the criteria and recipients for the cost anomaly alerts. Each subscription includes:
- Associated Cost Monitor : The resource that tracks and evaluates cost anomalies.
- Alert threshold (absolute) : The minimum difference in daily cost (in currency) required to trigger an alert. For example, if the threshold is $10, an alert is triggered when the difference between the daily cost forecast and the actual cost is at least ±$10.
- Alert threshold (relative percentage) : The minimum percentage difference in daily cost required to trigger an alert. For example, a value of 10 triggers an alert if the difference between the daily cost forecast and the actual cost is at least ±10%.
- Operator : Specifies how many thresholds are evaluated. You can use the AND operator to require both absolute and percentage conditions to be met for an alert to trigger, or the OR operator to trigger an alert if either condition is met.
- Notification Group : The list of recipients who receive alert notifications.
Using the Actions menu, you can perform one of the following actions for alert subscriptions:
- Edit Alert Thresholds : Edit the alert threshold criteria values.
- Edit Notification Group : Edit the associated notification group by selecting an existing notification group or creating a new one.
- Edit : Edit the cost monitor. For more information, see[Editing a Cost Monitor](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm)
- Delete : Delete the cost monitor. For more information, see[Deleting a Cost Monitor](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-cost-monitor.htm).
- Deactivate : Temporarily deactivate the cost monitor until reactivated.
- 

Use the[oci costad cost-anomaly-monitor get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-anomaly-monitor/get.html)command and required parameters to get the details of a cost monitor by an identifier:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetCostAnomalyMonitor](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAnomalyMonitor/GetCostAnomalyMonitor)
