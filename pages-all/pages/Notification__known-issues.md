# Known Issues for Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/known-issues.htm
- Fetched: 2026-09-05 02:50 CDT

# Known Issues for Notifications

Known issues have been identified in Notifications.

See also[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

## Long SMS messages sent to KR are split
Details When you send a long SMS message to South Korea (`KR`), the message is split, resulting in delivery of multiple messages to the recipient's device. Any URLs in the long SMS message could be broken up across the split messages, and the split messages might be delivered out of order. A long SMS message is one that exceeds 140 bytes, which is equivalent to 140 English characters, 70 Unicode characters, or 40 Korean characters. Cause: Long SMS messages are no longer supported by carriers in South Korea (`KR`). This lack of support is a`KR`telecom industry limitation in place to comply with anti-spam and fraud regulations. Workaround Consider sending notifications to other subscription types instead, such as Slack or email. For more information about available subscription types, and steps to create them, see[Creating a Subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription.htm)
