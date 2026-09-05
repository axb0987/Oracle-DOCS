# Viewing the Details of an Announcement
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm
- Fetched: 2026-09-05 02:10 CDT

# Viewing the Details of an Announcement

View detailed information when you want to know more about a particular announcement.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_an_announcement.htm#)
- 

- Do one of the following:
- If you're viewing a banner, select the link embedded in the text of the banner.
- If you're viewing a list of announcements, under the Announcement column, select the announcement summary. If you need help finding the list page, see[Viewing a List of All Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_announcements.htm).
- On the announcement details page, you can view the following information:

- Description. A description of the issue or event that provides more detail than the summary title of the announcement.
- OCID. The announcement's unique, Oracle-assigned identifier.
- Reference ticket number. The number to use to identify the issue when talking to Support.
- Type. One of several predefined categories that helps to set expectations about the nature and severity of the issue described. For more information, see[Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements.htm#Types).
- Affected service. The Oracle Cloud Infrastructure services affected by the issue or event.
- Region. What Oracle Cloud Infrastructure regions are impacted.
- Start time. When the issue or event was first detected, if applicable.
- End time. When the issue or event was resolved, if applicable.
- Action required by. The date by which you must address any required actions described in the announcement, if applicable.
- Created. When the announcement was created.
- Updated. When the announcement was updated.
- User status. Whether the announcement has been read or not.
- Impacted resources. Resources that were affected in some way by the event that prompted the announcement.
- Announcement history. Messages related to the announcement.
- 

Use the[oci announce announcements get](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements/get.html)command and required parameters to view detailed information about an announcement:

```

```

For example:
```

```

Viewing the details of an announcement provides you with the following information:

- Description. A description of the issue or event that provides more detail than the summary title of the announcement.
- OCID. The announcement's unique, Oracle-assigned identifier.
- Reference ticket number. The number to use to identify the issue when talking to Support.
- Type. One of several predefined categories that helps to set expectations about the nature and severity of the issue described. For more information, see[Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements.htm#Types).
- Affected service. The Oracle Cloud Infrastructure services affected by the issue or event.
- Region. What Oracle Cloud Infrastructure regions are impacted.
- Start time. When the issue or event was first detected, if applicable.
- End time. When the issue or event was resolved, if applicable.
- Action required by. The date by which you must address any required actions described in the announcement, if applicable.
- Created. When the announcement was created.
- Updated. When the announcement was updated.
- User status. Whether the announcement has been read or not.
- Impacted resources. Resources that were affected in some way by the event that prompted the announcement.
- Announcement history. Messages related to the announcement.

- Environment Name. The name of the environment impacted by the issue or event.
- Platform Type. The type of platforms affected by the issue or event, whether IaaS or SaaS.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetAnnouncement](https://docs.oracle.com/iaas/api/#/en/announcements/latest/Announcement/GetAnnouncement)
