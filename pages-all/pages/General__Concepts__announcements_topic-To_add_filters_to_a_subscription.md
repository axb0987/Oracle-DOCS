# Adding a Filter Group to an Existing Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm
- Fetched: 2026-09-05 02:10 CDT

# Adding a Filter Group to an Existing Subscription

You can add a filter group to an existing subscription.
Note  
  
You can't create a subscription with multiple filter groups when any filter group specifies Oracle Fusion Applications as the service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_add_filters_to_a_subscription.htm#)
- 

- On the Subscriptions list page, find the subscription you want to update, and then select the subscription name. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- On the details page, perform one of the following actions, depending on what's available:
- Select Filter groups , and then select Add filter group .
- Under Filter groups , select Add filter group .
- Select Name , and then enter a name for the filter. Avoid entering confidential information.

Note  
  
Include only alphanumeric, hyphen, underscore, or whitespace characters in the filter group name.
- Select Add filter .
- Perform one of the following actions, depending on what's available:
- Select Type , and then use the following table to configure a Value for what announcements you want to receive.
- Under Filters , select Type , and then use the following table to configure a Value for what announcements you want to receive.

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
- (Optional) To add another filter to the filter group, select Add filter , and then repeat the previous step. (You can't do this if the filter you created in the previous step specified resource OCIDs. You can't combine that type of filter with any other filter in a particular filter group.)
- When you're finished, perform one of the following actions, depending on what's available:
- Select Save changes , and then select Save changes again.
- Select Submit .
- 

Use the[oci announce announcement-subscription create-filter-group](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/create-filter-group.html)command and required parameters to add a filter group to an existing announcement subscription:

```

```

For example:
```

```

For more information about filter group options, see[FilterGroupDetails](https://docs.oracle.com/iaas/api/#/en/announcements/latest/datatypes/FilterGroupDetails).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateFilterGroup](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/CreateFilterGroup)
