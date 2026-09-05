# Guide to Metrics and Logs for Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/guide-to-metrics-logs.htm
- Fetched: 2026-09-05 02:00 CDT

# Guide to Metrics and Logs for Email Delivery

Oracle Cloud Infrastructure (OCI) Email Delivery provides two types of reporting data to help you gain insight into your email sending activity. OCI integrates this data through the Metrics and Logging services.

## Reporting Data Through Metrics

OCI provides the reporting data through the Metrics service using the pre-aggregated time-series count data provided by the OCI Monitoring service. Metrics use the`oci_emaildelivery`namespace and are filtered by approved sender or email sender domain.

You can view metrics in any of the following locations:
- [Email Deliverability Dashboard](https://www.oracle.com/cloud/sign-in.html?redirect_uri=https%3A%2F%2Fcloud.oracle.com%2Fmessaging%2Femail%2Fdashboard)(top set of boxes)
- Metrics sidebar menu on the detail pages for approved senders or email domains
- [Service Metrics page in the Monitoring service
- [Metrics Explorer page in the Monitoring service
- [Customizable OCI Dashboards by using Monitoring widgets

For API access, use the[ListMetrics](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Metric/ListMetrics)operation to list available metric names. Use the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to retrieve metric data from the`oci_emaildelivery`namespace.
Note  
  
Metrics data is available for 90 days. Some limitations apply to filtering data, depending on the specified time range.

Setup needed:

Apply metrics monitoring policies for Email Delivery (inspect and read permissions).

Available data:

For full metric details, see[Available Metrics: oci_emaildelivery](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic-Available_Metrics_oci_emaildelivery.htm). Metric types include:
- Emails Accepted
- Emails Relayed
- Emails Hard Bounced
- Emails Soft Bounced
- Emails Suppressed (blocked)
- Email Complaints
- Emails ListUnsubscribed
- Total Emails Opened
- Total Emails Clicked

Metrics data can be grouped by the following dimensions:
- `resourceId`(approved sender)
- `resourceDomain`(email sender domain)
Note  
  
Custom headers aren't available for filtering metric data.

## Reporting Data Through Logs

OCI provides the reporting data using the detailed event log data from the OCI Logging service. Logs are available by email sender domain and you can query logs for up to 14 days at a time.

Setup needed:

EMAIL_DOMAIN_UPDATE and[standard logging policies](https://docs.oracle.com/iaas/Content/Identity/Reference/loggingpolicyreference.htm#loggingpolicyreference)are required.[Enable logs](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/dashboard-topic-enabling-logging.htm)on each domain to collect and view log data.

Available data:

For information about log record structure, available fields, and sample log records, see[Email log details](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm)
