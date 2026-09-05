# Email Log Searching
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/log-guide.htm
- Fetched: 2026-09-05 02:01 CDT

# Email Log Searching

OCI Email Delivery integrates with the OCI Logging service to provide detailed activity logs. Logs are associated with each email sending domain (Email Domain) and requires to be enabled. We highly recommend enabling email delivery logs to track submissions, relaying activities, and post-delivery events such as spam complaints, unsubscribes, opens, and clicks.
To enable and access email delivery logs:
- [Set up logging policies](https://docs.oracle.com/iaas/Content/Identity/Reference/loggingpolicyreference.htm#loggingpolicyreference)so your tenancy can manage, write, and access logs.
- To enable logging for all or selected domains, use the[Deliverability Dashboard . To enable for a single domain, open its details page,[select the Logs sidebar menu](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/dashboard-topic-enabling-logging.htm), and enable one or both options: Outbound Accepted and Outbound Relayed logging.
- After you enable logging for a domain, you can browse and search activity logs by using the[Log Search page in the OCI web console.

## Email Delivery Log Types

The OCI Logging service tracks all activities across interfaces such as the web console, API, and CLI. In addition to default audit logs, Email Delivery provides[two log types for sending activity](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm):
- OutboundAccepted: Records inbound email submission activity (successful or failed).
- Successful submissions (accepted by the Email Delivery service)
- Accepted but suppressed, due to the recipient being on the suppression list
- Invalid recipient or sender (including senders not on the Approved Senders list)
- OutboundRelayed: Tracks outbound delivery and user engagement.
- Successful deliveries
- Bounces, spam complaints, and unsubscribes
- Opens and clicks

You can enable one or both log types for each email domain as needed.

## Common Email Domain Log Events and Filters

The following table summarizes typical log events and filters. For detailed records, see the[Logging Details for Email Delivery](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm).

Event Log Type Log Filter(s) (assume AND for multiple) Notes
Email accepted for delivery by OCI Email OutboundAccepted`data.action = 'accept'`
Email rejected or blocked (recipient on suppression list) OutboundAccepted`data.action = 'accept'`and`data.errorType = 'Recipient suppressed'``data.smtpStatus`field contains the formal reason
Email successfully relayed to recipient provider OutboundRelayed`data.action = 'relay'`
Emails relayed for a specific custom header value OutboundRelayed`data.action = 'relay'`and`data.headers."x-campaignid" = '999'`Use double quotes for custom header names with non-alphanumeric characters
Email bounced (delivery issue: recipient unknown, spam, etc.) OutboundRelayed`data.action = 'bounce'`Further filter with`data.errorType`(`hard`or`soft`). See additional fields:`data.bounceCategory`,`data.bounceCode`,`data.smtpStatus`,`data.message`
Recipient registered a spam complaint OutboundRelayed`data.action = 'complaint'`
Recipient opened an email OutboundRelayed`data.action = 'open'`

Extra field may have information about recipient's email client and operating system:`data.userAgent`
Opens for a specific custom header value OutboundRelayed`data.action = 'open'`and`data.headers.region = 'Northeast'`
Recipient clicked a link in an email OutboundRelayed`data.action = 'click'`

## Searching Email Delivery Logs

You can search detailed Email Delivery activity logs by using the[Logging Query Language](https://docs.oracle.com/iaas/Content/Logging/Reference/query_language_specification.htm), similar to how you work with OCI metrics. Instead of just accessing pre-aggregated activity counts, log queries help you define the scope and filter the search results.

For example, the following query searches all Email Delivery logs for every domain in a specified compartment (using the compartment OCID), and returns all email submissions, outbound deliveries, and related activities. Results are sorted by date, with the newest entries listed first:
```

```

You can narrow your search by using additional filters. Here are some examples:

Data Needed Search Filter
Count of emails accepted for a given custom header value

```

```

Failed Submissions for sender domain mycompany.com (no matter the reason)

```

```

The`errorType`field appears only for failed submissions and is not present for successful ones. All failed submissions are recorded in the OutboundAccepted log. To search across multiple domains, use only the compartment OCID and apply the same filtering clause.
Suppressed submissions across all sender domains

```

```

This query helps you identify which email submissions are blocked or suppressed because the recipient is on the suppression list. Remove these recipients from your mailing lists or update their information as needed.
Successful relayed email (that is, accepted by recipient email provider for delivery), optionally by sending domain

```

```

This query displays all successfully relayed emails for every sending domain in the specified compartment. To show results for only the sending domain`mycompany.com`, add the`source`field to your filter:
```

```

You can filter by the source field to search for a specific sending domain without specifying the log group and log name in the search clause. However, when you have multiple sending domains, searching a specific log, as shown here, is usually faster and more efficient.
Email bounces for a particular recipient email provider, sorted by type of bounce (hard, soft)

```

```

All hard bounces across all sending domains

```

```

Count of opens for a given custom header value
```

```

## Searching Email Delivery Logs Using the API

OCI provides SDKs in several major programming languages, including SDK methods for each service. To search logs programmatically, use the[OCI Logging API's](https://docs.oracle.com/iaas/Content/Logging/Concepts/using_the_api_searchlogs.htm)`SearchLogs`method. This method accepts a date and time range and a query object that uses the same syntax as the web console. You can also specify a few optional fields.
Note  
  
List APIs such as`SearchLogs`return a default maximum number of records per request. If the response contains the maximum number of records, it includes an`opc-next-page`field. To retrieve more records, send the same request with the`opc-next-page`value in the`page`parameter. You can also increase the number of records per page by setting the`limit`parameter. For details, see[OCI API List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

For more examples, see the[Using the OCI Logging API](https://docs.oracle.com/iaas/Content/Logging/Concepts/using_the_api_searchlogs.htm)page. Here are some real-world Email Delivery log searches in Python:

Data Needed Code Example (Python)
Bounces during a three-day period, sent from mycompany.com senders
```

```

Emails successfully relayed for all sending domains in a compartment over a one-hour period
```

```

All Gmail and Comcast recipients successfully relayed to during a 24-hour period
```

```

Count of emails delivered by recipient domain for a given custom header value
```

```
