# Viewing a List of All Announcements
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm
- Fetched: 2026-09-05 02:10 CDT

# Viewing a List of All Announcements

View a list of all announcements when you want to know what announcements you have for a particular compartment, including the root compartment.
Note  
  
Announcements have a retention period of 90 days. You can't view announcements sent more than 90 days in the past.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm#)
- 

- In the top navigation bar, select the Announcements icon ( ), and then select Announcements .
- The Announcements page displays all announcements for the selected compartment. From this page, you can do the following:
- Filter . You can filter announcements by event start date, event end date, service, status, or platform. For more information, see[Filtering Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_filter_a_list_of_announcements.htm).
- Sort . You can sort announcements by summary, status, service, event start time, or publish time (which indicates when the announcement was last updated). For more information, see[Sorting Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_sort_a_list_of_announcements.htm).
- Mark as read . You can mark announcements as read if you want stop seeing them as banners in the Console in later sessions. For more information, see[Marking an Announcement as Read](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_mark_an_announcement_as_read.htm).
- Subscribe to announcements like this . You can create a subscription to receive email delivery of only announcements that meet the criteria that you specify. For more information, see[Subscribing to Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm).
- View announcement details . You can view the details of an announcement. For more information, see[Viewing the Details of an Announcement](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm).
- To view the announcements in a different compartment, perform one of the following actions, depending on what's available:
- Use the Compartment filter to switch compartments.
- Under List scope , select Compartment , and then select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
- 

Use the[oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html)command and required parameters to list all announcements:

```

```
For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements)
