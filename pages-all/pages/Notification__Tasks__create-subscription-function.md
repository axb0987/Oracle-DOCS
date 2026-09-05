# Creating a Function Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-function.htm
- Fetched: 2026-09-05 02:49 CDT

# Creating a Function Subscription

Create a function subscription in Notifications.

Use a function subscription to invoke and run a[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)when a triggering condition occurs.

When the configured triggering condition occurs,[an alarm, announcement subscription, event rule, connector, or contextual notification (alarm or event rule)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Flow)sends (publishes) a message to the configured topic, and Notifications delivers that message to active subscriptions in the topic. On receipt of the message, the function is invoked and run. For an example scenario, see[Scenario A: Automatically Resizing VMs](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm).

The Notifications service has no information about a function after it's invoked. For details, see the troubleshooting information in[Function Not Invoked or Run](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/troubleshootingnotifications.htm#fxno).

## Before You Begin

You must have`FN_INVOCATION`permission against the function to be able to add the function as a subscription to a topic. See Add a Function Subscription in[Securing Notifications](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-function.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-function.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-function.htm#)
- 

These steps show how to open the Create subscription panel from the details page for the topic that you want to add the subscription to. You can also open this panel from the[Subscriptions list page , specifying the topic in the panel: Select Create subscription , and then select a Subscription topic .

- On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- On the topic's details page, select Subscriptions .
- Select Create subscription .
- In the Create subscription panel, for Protocol , select Function .
- Select the compartment and application that contain the function that you want, and then select the function.
- Select Create .

Notifications creates the function subscription. Confirmation isn't required for function subscriptions.
- 

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create a function subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create a function subscription.

Example:
```

```

## What's Next

Although a new subscription must be in the same compartment as its parent topic, you can move it to another compartment after creation. See[Moving a Subscription to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm)
