# Unsubscribing a Subscription from a Topic
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/unsubscribe-subscription.htm
- Fetched: 2026-09-05 02:50 CDT

# Unsubscribing a Subscription from a Topic

Unsubscribe a subscription from a topic in Notifications.

You can alternatively[delete the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/unsubscribe-subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/unsubscribe-subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/unsubscribe-subscription.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci ons subscription unsubscribe](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/unsubscribe.html)command and required parameters to unsubscribe a subscription from a topic:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[GetUnsubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/GetUnsubscription)operation to unsubscribe a subscription from a topic.

## Using Email

These steps are for unsubscribing an[email subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-email.htm). Every message sent out as email contains a link to unsubscribe from the related topic.

- In the email message, select the link to unsubscribe.
- In the textbox on the resulting webpage, enter the associated email address.
Ensure that the email address you enter is the one that was subscribed with. If distribution list is subscribed, add the distribution list's email address.
- Select Click here to unsubscribe .

## Using SMS

These steps are for unsubscribing an[SMS subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm).
Note  
  
This method of unsubscribing is available from recipient phone numbers that use the +1 country code only. For a recipient phone number in another country code,[delete the subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/delete-subscription.htm)instead. To find the subscription in the Console,[search the Console](https://docs.oracle.com/iaas/Content/Search/Tasks/queryingresources.htm#queryingresources_topic_Finding_Resources_by_OCID)for the subscription OCID. This OCID is included in the[confirmation URL](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)that was sent when the subscription was created.

Reply to the received SMS message with the following text.

```

```
