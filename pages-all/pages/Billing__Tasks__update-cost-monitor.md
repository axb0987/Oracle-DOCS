# Editing a Cost Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm
- Fetched: 2026-09-05 01:44 CDT

# Editing a Cost Monitor

Edit a cost monitor in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/update-cost-monitor.htm#)
- 

- On the Cost monitor list page, find the cost monitor that you want to work with. If you need help finding the list or the cost monitor, see[Listing Cost Monitors](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm).
- On cost monitor Details page, from the the Actions menu (three dots) select Edit .
- 

In the Edit cost monitor panel, update the settings as needed. Avoid entering confidential information.

The fields that are editable depend on the type of cost monitor:
- For default cost monitors, you can change the alert subscription.
- For custom cost monitors, you can change the budget name, description, alert subscription, and tags.
- Select Update .
Note  
  
You can also add an[alert subscription](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-cost-monitor.htm#set-alert-subscription-cost-monitor-create)while updating a cost monitor. Select the cost monitor you want to work with and select Add alert subscription .
- 

Use the[oci costad cost-anomaly-monitor update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-anomaly-monitor/update.html)command and required parameters to edit a cost monitor:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCostAnomalyMonitor](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAnomalyMonitor/UpdateCostAnomalyMonitor)
