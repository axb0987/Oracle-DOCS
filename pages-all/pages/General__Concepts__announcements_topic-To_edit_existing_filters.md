# Editing an Existing Filter Group
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm
- Fetched: 2026-09-05 02:10 CDT

# Editing an Existing Filter Group

You can add a filter to an existing filter group, change the values selected for a particular filter in the filter group, or delete a filter from the filter group.
Note  
  
You can't change filter groups when a language display preference is part of a subscription. If you need changes to filter groups, you must create a new subscription.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_edit_existing_filters.htm#)
- 

- On the Subscriptions list page, find the subscription you want to update, and then select the subscription name. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- On the details page, perform one of the following action, depending on what's available:
- Select Filter groups , and then find the filter you want to edit.
- Under Filter groups , find the filter you want to edit.
- Select the Actions menu (three dots) , and then select Edit .
- Perform one or more of the following actions, depending on what's available:
- To add a filter, either select Add filter or + Another filter , and then continue to the next step.
- To change the value of an existing filter, either select Value or select the Actions menu (three dots) , and then select Edit . Then, enter a new value or select the arrows to select a new value from a menu, as appropriate. For help with entering a new value, refer to the table in the next step.
- To delete a filter, either select the Actions menu (three dots) , and then select Delete , or select the X on the filter row.
- If, in the previous step, you deleted a filter and don't want to specify a new filter, continue to the next step. Otherwise, select Type , and then use the following table to configure a Value for what announcements you want to receive:

Note  
  

You can't have more than one of any particular filter type within a filter group.

When filtering announcements, the Announcements service evaluates announcements against all configured filters in a subscription. To be considered a match, an announcement must meet the criteria specified by all filters. When several possible values are configured for a particular filter, alignment with any one of the values is considered a match with that filter.

Option Description
Announcement type Specify an announcement type to include in the filter. Every announcement is assigned to a category that helps you understand the relative severity of the information in the announcement. For more information, see[Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements.htm#Types).
Compartment Specify a compartment to include in the filter. Not all announcements impact a specific compartment, but this filter lets you include announcements that do. The service performs an exact match and doesn't include announcements about child compartments of the specified compartment.

Note: If you specify the root compartment, then subscribers receive announcements about the root compartment. These announcements might pertain to resources in the root compartment. They can also describe events for which specific impacted resources haven't been identified. Announcements for the root compartment might also address impacts to the tenancy as a whole. However, if you want all announcements about the tenancy, then we recommend you create a subscription for all announcements instead of creating a subscription for selected announcements only.
Platform Specify whether you want to see announcements that impact the Oracle Cloud Infrastructure ( IaaS ) platform or announcements that impact Software as a Service ( SaaS ) applications.
Region Specify a region to include in the filter.
Resource OCID Specify up to 10 resources that you want to include in the filter by doing the following:
- Select Browse , select the checkbox next to the resource that you want to include, and then select Add to filter . (If needed, to list resources in a different compartment, select Compartment and select a compartment.)

Note: You can't combine this filter with any other type of filter in a particular filter group.
Service

Select the name of the service that you want to include. To narrow the list, you can type or otherwise enter the service name. Not all announcements impact a particular service, but this filter lets you include announcements that do.

If a filter specifies more than one service, then the Announcements service notifies subscribers of announcements impacting any of the specified services.

Note: When you create a subscription based on a service, you get all the announcements for that service. You don't need to separately create a subscription for each region where you use the service.
- When you're finished, select Submit .
- 

Use the[oci announce announcement-subscription update-filter-group](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/update-filter-group.html)command and required parameters to update an existing filter group in an announcement subscription:

```

```

For example, to add a filter:
```

```

Or, to update the values selected for a given filter:
```

```

Or, to delete a filter from the filter group:
```

```

For more information about filter group options, see[FilterGroupDetails](https://docs.oracle.com/iaas/api/#/en/announcements/latest/datatypes/FilterGroupDetails).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateFilterGroup](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/UpdateFilterGroup)
