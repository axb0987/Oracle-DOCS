# Managing Email Preferences for Tenancy Administrators
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm
- Fetched: 2026-09-05 02:10 CDT

# Managing Email Preferences for Tenancy Administrators

Administrator email preferences specify whether the tenancy administrator wants to opt in or opt out of receiving emailed copies of service status announcements. Administrator email preferences have no impact on any announcement subscriptions you might have.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- Open the Subscriptions list page. If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- Select Manage administrator email preferences .
- Do one of the following:
- If you want Oracle to send email announcements, select Opt in to receive email announcements .
- If you want Oracle to withhold email copies of announcements, select Opt out to stop receiving all email announcements . You must also select the checkbox to acknowledge that you understand opting out can result in important missed email that could impact the tenancy.
Note  
  
Regardless what you configure here, the tenancy administrator can still receive email announcements if you create a subscription that includes the administrator's email address as a delivery endpoint. For more information about subscriptions, see[Subscribing to Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm).
- Then, do one of the following:
- To receive only announcements that impact tenancy resources, select Send email only for announcements pertaining to this tenancy, including outage information .
- To receive all announcements, including informational announcements that require no action or that more generally address customers, also select Send email for all announcements, including informational announcements that might not be specific to this tenancy . By default, Oracle emails only announcements that impact tenancy resources and about outages.
- In the previous steps, if you chose to opt in, also specify the time zone you prefer for announcement time stamps by selecting Time zone and choosing a time zone. Otherwise, continue to the next step.
- When you're finished, select Save changes .
- 

Note  
  
By default, the tenancy administrator receives email announcements. When explicitly specifying email preferences, you can either create or update them. You get the same result. However, you do need the preference ID if you want to update preferences.

Use the[oci announce announcements-preferences create](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/create.html)or[oci announce announcements-preferences update](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcements-preferences/update.html)command and required parameters to specify email preferences for the tenancy administrator.
To use the`oci announce announcements-preferences create`command to create email preferences:

```

```

For example:
```

```

To use the`oci announce announcements-preferences update`command to update email preferences:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Note  
  
By default, the tenancy administrator receives email announcements. When explicitly specifying email preferences, you can either create or update them. You get the same result. However, you do need the preference ID if you want to update preferences.

Run the[CreateAnnouncementsPreference](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsPreferencesSummary/CreateAnnouncementsPreference)operation to create email preferences for the tenancy administrator. Or, run the[UpdateAnnouncementsPreference](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementsPreferencesSummary/UpdateAnnouncementsPreference)
