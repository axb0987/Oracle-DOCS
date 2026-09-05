# Viewing the Details of an Announcement Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm
- Fetched: 2026-09-05 02:10 CDT

# Viewing the Details of an Announcement Subscription

View detailed information about an announcement subscription when you want to learn more about a particular subscription.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_a_subscription.htm#)
- 

- On the Subscriptions list page, under the Name column, select the name of the subscription that you want to view in detail. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- On the subscription details page, you can view the following information:

- Name . The name of the announcement subscription.
- Lifecycle state . The current lifecycle state of the announcement subscription resource itself.
- OCID . The announcement subscription's unique, Oracle-assigned identifier.
- Compartment . The compartment where the announcement subscription exists.
- Description . A description of the announcement subscription.
- Notifications topic . The Notifications topic used by the announcement subscription to publish announcements to subscribers.
- Time zone .
- Language . The language used to display announcements to subscribers.
- Filter groups . Information about the filter groups configured for the announcement subscription.
- Tags . Any defined or freeform tags added to the announcement subscription resource.
- 

Use the[oci announce announcement-subscription get](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/get.html)command and required parameters to view the details of an announcement subscription:

```

```

For example:
```

```

Viewing the details of an announcement subscription provides you with the following information:

- Name . The name of the announcement subscription.
- Lifecycle state . The current lifecycle state of the announcement subscription resource itself.
- OCID . The announcement subscription's unique, Oracle-assigned identifier.
- Compartment . The compartment where the announcement subscription exists.
- Description . A description of the announcement subscription.
- Notifications topic . The Notifications topic used by the announcement subscription to publish announcements to subscribers.
- Time zone .
- Language . The language used to display announcements to subscribers.
- Filter groups . Information about the filter groups configured for the announcement subscription.
- Tags . Any defined or freeform tags added to the announcement subscription resource.

- Time created . When the announcement subscription was created.
- Time updated . When the announcement subscription was last updated.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/GetAnnouncementSubscription)
