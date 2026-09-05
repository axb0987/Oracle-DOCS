# Editing a Notification Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/edit-notification-groups.htm
- Fetched: 2026-09-05 01:43 CDT

# Editing a Notification Group

Edit a notification group related to a cost monitor in Billing and Cost Management

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/edit-notification-groups.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/edit-notification-groups.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/edit-notification-groups.htm#)
- 

- On the Notification groups list page, select the notification group that you want to work with. If you need help finding the list page or the notification group, see[Listing Notification Groups](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm).
- On notification group Details page, select Edit . Or, from the the Actions menu (three dots) for the notification group select Edit .
- In the Edit notification group panel, update the Description or the Email recipients . Avoid entering confidential information.
Note  
  
You can't edit the notification group name.
- Select Update .
- 

Use the[oci costad cost-alert-subscription update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-alert-subscription/update.html)command and required parameters to edit a notification group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCostAlertSubscription](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAlertSubscription/UpdateCostAlertSubscription)
