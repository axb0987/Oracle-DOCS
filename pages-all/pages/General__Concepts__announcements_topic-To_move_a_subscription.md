# Moving an Announcement Subscription to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm
- Fetched: 2026-09-05 02:10 CDT

# Moving an Announcement Subscription to a Different Compartment

You can move an announcement subscription from one compartment to another.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_move_a_subscription.htm#)
- 

- On the Subscriptions list page, find the subscription you want to move, and then select the subscription name. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- On the details page, perform one of the following actions, depending on what's available:
- Select Actions , and then select Move resource .
- Select Move resource .
- Select Destination compartment , and then select a new compartment from the list.
- When you're ready, select Move resource .
- 

Use the[oci announce announcement-subscription change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/change-compartment.html)command and required parameters to move an announcement subscription to a different compartment:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeAnnouncementSubscriptionCompartment](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/ChangeAnnouncementSubscriptionCompartment)
