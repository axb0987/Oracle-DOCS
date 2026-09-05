# Sorting Announcements
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm
- Fetched: 2026-09-05 02:10 CDT

# Sorting Announcements

Sort announcements when you want to view announcements in a particular order, whether by the event start time, the announcement summary, the announcement type, or the time the announcement was last published.
Note  
  
Announcements have a retention period of 90 days. You can't view announcements sent more than 90 days in the past.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm#)
- 

- Open the Announcements list page. If you need help finding the list page, see[Viewing a List of All Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm). By default, the list displays announcements according to the event start time, from most recent to least.
- To sort the list another way, perform one of the following actions, depending on what's available:
- Select Announcement . The list sorts alphabetically, according to the summary of the announcement.
- Read status . The list sorts to show read messages first, instead of unread messages.
- Reference ticket number . The list sorts to show announcements in ascending order by reference ticket number.
- Service . The list sorts alphabetically, according to the service name.
- Action type . The list sorts alphabetically, according to the announcement type.
- Platform type . The list sorts alphabetically, according to the platform type.
- Event time . The list sorts to show announcements from oldest to most recent start time of the event described in the announcement.
- Publish time . The list sorts according to the time that an announcement was last updated. You might find it helpful to sort by this column to track an ongoing issue or if an announcement requires action from an administrator.
- (Optional) To sort the list again, repeat the previous step.
- 

Use the[oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html)command and required parameters to sort a list of announcements:

```

```

You can sort a list of announcements in order of time created, either oldest to newest or newest to oldest. You can also sort a list of announcements according to one of the following criteria: announcement type (`announcementType`), reference ticket number (`referenceTicketNumber`), summary (`summary`), time created (`timeCreated`), start time (`timeOneValue`), or end time (`timeTwoValue`).
To sort a list of announcements in ascending order of time created, from oldest to newest:

```

```

For example:
```

```

To sort a list of announcements by other criteria:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements)
