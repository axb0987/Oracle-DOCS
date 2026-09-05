# Listing Subscriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm
- Fetched: 2026-09-05 02:49 CDT

# Listing Subscriptions

List subscriptions in Notifications.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription.htm#)
- 

These steps show how to list subscriptions in a compartment. You can also list subscriptions[in a topic](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription-topic.htm).

- Open the navigation menu and select Developer Services . Under Application Integration , select Notifications .
- Under Notifications , select Subscriptions .
The Subscriptions list page opens. All subscriptions in the selected compartment are displayed in a table.
- To view the subscriptions in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the subscriptions in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a subscription to open its details page, where you can view its status and perform other tasks.

To perform an action on a subscription directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that subscription:
- Copy OCID : Copy the OCID of the subscription to the clipboard.
- Resend confirmation :[Resend the confirmation URL for the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/resend-confirmation-subscription.htm).
- Manage tags : Add one or more tags to the topic. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Add tags : Add one or more tags to the topic. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- View tags : View the topic's existing tags. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Move resource :[Move the subscription to another compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/change-compartment-subscription.htm).
- Update delivery policy :[Update the subscription's delivery policy](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/update-subscription.htm).
- Delete :[Delete the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/delete-subscription.htm).

To create a subscription, select Create subscription .
- 

Use the[oci ons subscription list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/list.html)command and required parameters to list subscriptions:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[ListSubscriptions](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/ListSubscriptions)
