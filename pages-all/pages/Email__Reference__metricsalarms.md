# Email Delivery Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms.htm
- Fetched: 2026-09-05 02:01 CDT

# Email Delivery Metrics

Monitor the health, capacity, and performance of the Email Delivery service by using metrics, alarms, and notifications.

This topic describes the metrics emitted by the metric namespace`oci_emaildelivery`(the Email Delivery service).

Oracle Cloud Infrastructure Email Delivery (Email Delivery) is an email sending service that provides a fast and reliable managed solution for sending high-volume emails that need to reach your recipients' inbox. Email Delivery service metrics help you measure counts for emails accepted, emails relayed, email complaints, emails hard bounced, and emails soft bounced.
- Emails Accepted : Emails accepted consists of the unique emails accepted and sent by the Email Delivery service. Emails are defined by the number of unique emails and the number of unique recipients per message attempted to be delivered, resulting in successful delivery and blocked email. For example, sending an email with 10 recipients means 10 emails accepted.
- Emails Relayed: Emails relayed consists of the number of emails that the Email Delivery service has successfully transferred to a recipient domain. The recipient domain has accepted responsibility and will typically deliver these emails, but can still choose to discard, quarantine, or bounce. A single email may be both relayed and bounced.
- Emails Hard Bounced : Hard bounces occur when a mailbox provider provides a signal that the email address you have tried to send to is not valid. Most often, this happens because the email address does not exist. You should not try to send an email to hard bounced address again in the future. The emails hard bounced metric consists of the number of emails hard bounced (permanent failure) for a sender by the recipient domain's email service.
- Emails Soft Bounced : Soft bounces are messages from a mailbox provider that provide a signal that the email address you have tried to send to is not valid for the time being. Usually, a message soft bounces when the inbox is full or cannot be reached. You can try to send an email to soft bounced address again in the future. The emails soft bounced metric consists of the number of emails soft bounced (persistent transient failure) by the recipient domain's email service or because of an inability to reach that service.
- Email Complaints : Email complaints consists of the number of email complaints for a sender by the Email Delivery service.
- Emails Suppressed : Emails suppressed consists of the number of emails suppressed by the Email Delivery service.
- Emails ListUnsubscribed : Emails ListUnsubscribed consists of the number of emails unsubscribed by email recipients for a sender or domain.
Note
