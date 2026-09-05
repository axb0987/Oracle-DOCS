# Accessing Email Deliverability and Reputation Governance Dashboard
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/accessing_dashboard.htm
- Fetched: 2026-09-05 02:00 CDT

# Accessing Email Deliverability and Reputation Governance Dashboard

Use the Email Deliverability and Reputation Governance dashboard to view high-level aggregated metrics and detailed logs for email sending activity..

## Using the Console

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Deliverability Dashboard .
- Select a compartment to display data. If you select the tenancy, you see data only for the root compartment.

You can filter the data under the Deliverability Logs section by text. Text filters apply only to the displayed columns.

If you have more advanced filtering or display needs, we highly recommend using Logging Search. For more information, see the[Email Log Searching](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/log-guide.htm)guide.

The following key terms appear on the dashboard:

- Unsubscribes: Shows List-Unsubscribe requests. This is different from users unsubscribing through a link in your email content. Industry best practice is to include List-Unsubscribe and List-Unsubscribe-Post headers in all bulk emails. Major email providers, such as Gmail and Yahoo, now require these headers. OCI Email Delivery will add the headers automatically if they are missing to help maintain your sender reputation. For details, see[our List-Unsubscribe support documentation](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-unsubscribe.htm).
- Accepted: Accepted consists of the unique emails accepted and sent by the Email Delivery service. Emails are defined by the number of unique emails and the number of unique recipients per message that are attempted to be delivered, resulting in successful delivery, and blocked email. For example, sending an email with 10 recipients is equal to 10 emails accepted.
- Suppressed: Suppressed consists of the percentage of emails suppressed during the selected time window. The percentage is calculated based on emails accepted.
- Relayed: Emails relayed consists of the percentage of emails that the Email Delivery service has successfully transferred to a recipient domain. The recipient domain has accepted responsibility and typically delivers these emails, but can still choose to discard, quarantine, or bounce. A single email can have many logs for different events such as relay, bounce, and complaint.
- Soft Bounces: Soft bounces are messages from a mailbox provider that provide a signal that the email address you have tried to send to is valid, however, it's temporarily not accepting messages. For example, a message soft bounces when the inbox is full, the server is down, or the email size is too large. You can try to email this address again in the future. The emails soft bounced metric consists of the percentage of emails soft bounced (persistent transient failure) by the recipient domain's email service or because of an inability to reach that service. The percentage is calculated based on the number of emails accepted. Causes of some soft bounces are within your control, it's important to follow all[Best Practices](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm)and ensure you have the correct email authentication mechanisms set up to help avoid soft bounces.
- Hard Bounces: Hard bounces occur when a mailbox provider provides a signal that the email address you have tried to send to isn't valid. Most often, this happens because the email address doesn't exist. Avoid to email this address again in the future. The emails hard bounced metric consists of the percentage of emails hard bounced (permanent failure) for a sender by the recipient domain's email service. The percentage is calculated based on the number of emails accepted. important to follow all[Best Practices](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm)to avoid hard bounces.
- Complaints: Complaints consist of the percentage of email complaints for a sender by the Email Delivery service. The percentage is calculated based on the number of emails accepted. A complaint is when a recipient marks an email as spam. Complaints are a feedback mechanism from some mailbox providers to help senders understand what recipients think of their content. For ways to keep the recipients engaged with your content and to minimize complaints, see[Best Practices](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm).
Because complaint events are logged at the time when the recipient marks the email as spam and not when the email was sent, there can be cases where the sender did not send any emails for the time range, but there were complaints logged.
Note  
  
If zero emails were accepted for your search range, and there was email activity (for example, a spam complaint), the metric percentage displayed is 0%.
- Blocklists: Blocklists consist of the percentage of emails that could not be delivered because of errors related to blocklists. Email senders or sending IP addresses can be placed on blocklists in response to bad sending practices such as sending spam, not using DKIM, sending too many emails to a single recipient, sending to invalid recipients, failure to include an unsubscribe mechanism or other failures to follow[Best Practices](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm)
