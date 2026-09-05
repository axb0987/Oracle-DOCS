# Filtering Announcements
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm
- Fetched: 2026-09-05 02:10 CDT

# Filtering Announcements

Filter announcements to view only announcements that fit specific criteria. You can filter on criteria such as the announcement type, start or end date, impacted service, resolution status, and impacted platform.
Note  
  
Announcements have a retention period of 90 days. You can't view announcements sent more than 90 days in the past.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm#)
- 

- Open the Announcements list page. If you need help finding the list page, see[Viewing a List of All Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm). By default, the list displays a list of all announcements for the selected compartment.
- To view announcements filtered by announcement type, perform one of the following actions, depending on what's available. For more information about announcement types, see[Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm#Types).
- In the search box, select the Action type filter, select one or more of the announcement types you want to list, and then select Apply filter .
- Select one or more of the following tabs:
- Required actions
- Recommended actions
- Planned maintenance
- Other . This tab shows all announcements of a different type from the three preceding announcement types.
- (Optional) To filter the list of announcements further, either in the search box or under Filters , do one or more of the following, depending on what's available:
- Select Announcement , and then enter a full or partial announcement title.
- Select Read status , and then select one or more statuses.
- Select Reference ticket number , and then enter a reference ticket number.
- Select Service , and then select one or more services.
- Select Action type , and then select one or more announcement types.
- Select Platform type , and then select one or more platform types.
- Select Event time , and then enter a start date, start time, end date, and end time. Or, you can select one of the preset time ranges, up to the last year.
- Select Publish time , and then enter a start date, start time, end date, and end time. Or, you can select one of the preset time ranges, up to the last year.
- Select Apply filter .
- (Optional) To clear filters, perform one of the following actions, depending on what's available:
- To clear an individual filter, select the X next to the filter name.
- To clear all filters on the list of announcements, select Reset .
- 

Use the[oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html)command and required parameters to filter a list of announcements. When using the command line, you can filter a list of announcements by announcement type, environment name, lifecycle state, platform type, service, and time (earliest start time and latest start time).
To filter a list of announcements by announcement type:

```

```

For example:
```

```

To filter a list of announcements by environment name:

```

```

For example:
```

```

To filter a list of announcements by lifecycle state:

```

```

For example:
```

```

To filter a list of announcements by platform type:

```

```

For example:
```

```

To filter a list of announcements by service:

```

```

For example:
```

```

Note  
  
If you include more than one service, then the filter effectively screens for announcements that impact all specified services.
To filter a list of announcements by time:

```

```
For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements)
