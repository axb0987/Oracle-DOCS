# Deleting a Filter Group
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm
- Fetched: 2026-09-05 02:10 CDT

# Deleting a Filter Group

You can delete a filter group from an existing subscription.
Note  
  
You can't change filter groups when a language display preference is part of a subscription. If you need changes to filter groups, you must create a new subscription.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_delete_filters.htm#)
- 

- On the Subscriptions list page, find the subscription with a filter group you want to delete, and then select the subscription name. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- On the details page, perform one of the following actions, depending on what's available:
- Select Filter groups , and then find the filter group you want to delete.
- Under Filter groups , find the filter group you want to delete.
- Select the Actions menu (three dots) , and then select Delete .
- To confirm, select Delete .
- 

Use the[oci announce announcement-subscription delete-filter-group](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/delete-filter-group.html)command and required parameters to delete a filter group from an announcement subscription:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteFilterGroup](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/DeleteFilterGroup)
