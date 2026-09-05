# Listing Notification Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Notification Groups

View the list of notification groups in a compartment Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-notification-groups.htm#)
- 

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Anomaly Detection .
- Select Notification Groups .

The Notification Groups list page opens listing all notification groups in a table.

## Filtering List Results

Use filters to limit the notification groups in the list. Perform one of the following actions depending on the options that you see:
- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list.
- Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a notification group to open its details page, where you can view its status and perform other tasks.

To perform an action on a notification group directly from the list table, select an available option from the Actions menu in the row for that notification group:
- View details : Open the details page for the notification group.
- Edit :[Edit the notification group](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/edit-notification-groups.htm#top).
- Delete :[Delete the notification group](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/delete-notification-groups.htm#top).

To perform an action on more than one notification group at a time, select the checkboxes next to the notification group name and then select an action from the Actions menu preceding the table.

To create a notification group select Create notification group .
- 

Use the[oci costad cost-alert-subscription-collection list-subs](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-alert-subscription-collection/list-subs.html)command and required parameters to get a list of notification groups in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListCostAlertSubscriptions](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAlertSubscriptionCollection/ListCostAlertSubscriptions)
