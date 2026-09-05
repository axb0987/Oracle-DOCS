# Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Email_Delivery.htm
- Fetched: 2026-09-05 02:10 CDT

# Email Delivery

As part of an organization's service agreement, Oracle Cloud Infrastructure also contacts the tenancy administrator with service status announcements through email.

These emails help alert you to upcoming changes that impact the tenancy, such as those involving data centers or instances you use, or about required action on the part of an administrator. Whenever possible, we try to provide advance notice of impactful events. For events that have more than one update, a tenancy administrator might see emails as part of one related chain of messages or as separate messages upon each update.

By default, Oracle sends service status announcements to the default tenancy administrator email address on record. To change the default tenancy administrator email address on record, contact[Oracle Support](http://support.oracle.com/). For more information, see[Contacting Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

If you want announcements sent through other delivery mechanisms or to multiple recipients, create an announcement subscription. For more information, see[Subscribing to Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-Subscribing.htm).

Lastly, although you can receive announcements through email, because of its inherently unreliable nature as a communication mechanism, we strongly recommend that you prioritize the information available in the Console or through the API and CLI instead.
Note  
  
Recipients can prepare to receive announcements from a range of different email addresses. The region of the sender email address doesn't necessarily correspond with the affected region. If you have mailbox rules for receiving email announcements, an example sender email address is noreply@mail.announcements.us-ashburn-1.oci.oraclecloud.com. For a list of region identifiers, see[About Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/regions.htm#About).

You can perform the following management tasks related to email delivery:
- [Managing Email Preferences for Tenancy Administrators](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_manage_email_preferences_for_announcements.htm)
- [Viewing All Preferences for Email Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_all_preferences_for_email_announcements_CLI.htm)
- [Viewing the Details of Email Announcement Preferences](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_the_details_of_email_announcement_preferences_CLI.htm)
