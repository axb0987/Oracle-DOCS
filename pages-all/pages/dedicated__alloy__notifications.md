# Oracle Alloy Announcements & Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#dcoc-content-body)

# Oracle Alloy Announcements &amp; Notifications

Notification management helps Alloy partners communicate service events and operational updates in a controlled way. The workflow supports draft authoring, recipient targeting, approval, publication, console-banner distribution, and follow-up updates through notification history. These controls help customer communications remain timely and traceable.

End customers use the Customer Console to access announcements, review announcement content and history, manage read state and banner visibility, and subscribe to announcement streams that are relevant to their environment.

## Access and Roles

Use Notification Management from My Tools on the Operator Console home page or from Governance &amp; Administration in the navigation menu. Grant access through the operator identity domain groups that support notification operations. Notification managers can create and review notifications. Operator administrators provide the final approval that enables publication.

## Create and Manage Notifications

Draft notifications capture the operational context needed for customer communication. This context includes notification type, related ticket references, summary, description, optional timing in UTC, platform type, impacted services, and optional additional information.

Target recipients by uploading a CSV file or by selecting regions in the current realm. When required, schedule a console banner for the customer console in the same workflow.

Before publication, edit draft content, update the recipient list, or clone a draft to reuse the structure for a related communication. Review the email preview before approval so that the final customer message and recipient scope are validated in the same workflow.

## Approve, Publish, and Update Notifications

Notifications use a role-based approval workflow so that customer communications are reviewed before release. Oracle-authored notifications can also be reviewed, edited when needed, approved, and published through the same path. Final publication becomes available after operator-administrator approval. Approved notifications can then be released to the selected recipients.

For multi-step incidents or ongoing outages, link related messages through notification history. This workflow chains related notifications together, preserves visibility into prior updates, and can aggregate earlier recipients so that follow-up communications stay aligned with the affected audience.

When an active notification includes a console banner, deactivate the banner early when it must no longer appear in the customer console.

After a notification is published, the published content and recipient list are no longer editable. Issue additional customer communication as a related follow-up notification through the existing approval and publication workflow.

## Access the Customer Console

From the Operator Console home page, open View Customer Console in a separate authenticated window to review the customer-facing announcements experience. After the initial sign-in flow, bookmark the Customer Console URL for direct access when you need to validate announcement behavior or support customer questions.

## View Announcements

The Announcements bell icon in the Customer Console displays a green dot when unread announcements are present. From the bell icon, End customers can open the announcements overview and move to the full announcements list for the selected compartment, including the root compartment when they have the required permissions.

The overview highlights recent announcement activity across common timeframes so that End customers can identify current items that might require attention.

## Filter and Sort Announcements

End customers can narrow the announcements list by category, event dates, impacted service, status, or platform. These filters help End customers focus on items that matter to a specific operational context.

The list can also be sorted by summary, type, event time, or publish time. Sorting helps End customers review the most recent updates or the announcements with the highest operational relevance.

## Review Announcement Details and History

Each announcement opens to a details page that includes the summary, lifecycle state, description, announcement Oracle Cloud ID (OCID), reference ticket number, type, affected services, impacted regions, event start and end times, required-action deadline when applicable, created and updated timestamps, additional information, and impacted resources.

End customers can download the impacted resources list and use announcement history to review related follow-up updates for the same event.

## Manage Read State and Banner Visibility

End customers can mark an announcement as read from the announcements list when they no longer need the item to remain unread in the console.

When an announcement is published as a console banner, closing the banner dismisses the banner only until the next sign-in session. To stop seeing the banner before its expiration date, the customer must mark the underlying announcement as read.

## Create Announcement Subscriptions

End customers can create announcement subscriptions so that relevant announcements are also delivered through an OCI Notifications topic. A subscription can be configured for all announcements or for selected announcements only.

Selected-announcement subscriptions support filter groups based on announcement type, compartment, platform, region, resource OCID, or service. They also support display preferences such as time zone and, for Oracle Fusion Applications announcements, language.

The subscription workflow supports an existing Notifications topic or a newly created topic in the selected compartment. New topics can use email, Functions, HTTPS custom URL, PagerDuty, Slack, or SMS endpoints. This model lets End customers route notifications to the channels that best fit their operating workflow while keeping the subscription scope aligned to the services, regions, and resources that they monitor.

For more information about Oracle Cloud Infrastructure (OCI) Announcements and Notifications, see[Announcements](https://docs.oracle.com/iaas/Content/General/Concepts/announcements_topic-Viewing_Announcements.htm)&amp;[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

- [Oracle Alloy Announcements &amp; Notifications](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#oracle-alloy-notifications)
- [Access and Roles](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#access-and-roles)
- [Create and Manage Notifications](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#create-and-manage-notifications)
- [Approve, Publish, and Update Notifications](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#approve-publish-and-update-notifications)
- [Access the Customer Console](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#access-the-customer-console)
- [View Announcements](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#view-announcements)
- [Filter and Sort Announcements](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#filter-and-sort-announcements)
- [Review Announcement Details and History](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#review-announcement-details-and-history)
- [Manage Read State and Banner Visibility](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#manage-read-state-and-banner-visibility)
- [Create Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/notifications.htm#create-announcement-subscriptions)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
