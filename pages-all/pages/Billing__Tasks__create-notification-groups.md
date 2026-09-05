# Creating a Notification Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-notification-groups.htm
- Fetched: 2026-09-05 01:43 CDT

# Creating a Notification Group

Create a notification group to include all the email recipients who receive notifications when a cost anomaly's alert threshold is exceeded.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-notification-groups.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-notification-groups.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/create-notification-groups.htm#)
- 

On the Notification Groups list page, select Create notification group . If you need help finding the list page, see[Listing Notification Groups](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm).

Enter the following information to create a notification group:
- Name : Enter a name for the notification group. The name can include only alphanumeric characters, dashes, and underscores, and it can't start with a number. Don't include confidential information.
- Description : Enter a suitable description for the notification groups. Avoid entering confidential information.
- Email recipients : View the list of one or more valid email addresses in the notification group. Separate multiple email addresses using a comma, space, or adding each address in its own line.
- 

Use the[oci costad cost-alert-subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-alert-subscription/create.html)command and required parameters to create a notification group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCostAlertSubscription](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAlertSubscription/CreateCostAlertSubscription)
