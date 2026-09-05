# Viewing the History of an Announcement
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm
- Fetched: 2026-09-05 02:10 CDT

# Viewing the History of an Announcement

View the history of an announcement for which you have related updates.
Note  
  
Only announcements published with a chain ID show related messages that share the same chain ID in their announcement history.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_history_of_an_announcement.htm#)
- 

- Do one of the following:
- If you're viewing a banner, select the link embedded in the text of the banner.
- If you're viewing a list of announcements, under the Announcement column, select the announcement summary. If you need help finding the list page, see[Viewing a List of All Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm).
- On the announcement details page, perform one of the following actions, depending on what's available:
- Select Announcement history .
- Under Resources , select Announcement history .
- (Optional) To view the contents of any related announcements, in the Announcement history list, under Announcement , select the announcement summary.
- 

Use the[oci announce announcements list](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/list.html)command and required parameters to view the history of an announcement that has a chain of related messages:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListAnnouncements](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsCollection/ListAnnouncements)
