# Deleting a Notification Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-notification-groups.htm
- Fetched: 2026-09-05 01:43 CDT

# Deleting a Notification Group

Delete a notification group related to a cost monitor in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-notification-groups.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-notification-groups.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-notification-groups.htm#)
- 

- On the Notification groups page, find the notification group that you want to delete. If you need help finding the list page or the cost monitor, see[Listing Notification Groups](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm).
- 
Select a notification group and select Delete . Or, from the Actions menu (three dots) for the notification group, select Delete .
Note  
  
Deleting a notification group deletes all alert subscriptions where the notification group is associated.
- 

Use the[oci costad cost-alert-subscription delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-alert-subscription/delete.html)command and required parameters to delete a notification group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteCostAlertSubscription](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAlertSubscription/DeleteCostAlertSubscription)
