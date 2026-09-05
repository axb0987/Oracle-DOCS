# Managing Email Deliverability and Reputation Governance Dashboard
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/dashboard.htm
- Fetched: 2026-09-05 02:00 CDT

# Managing Email Deliverability and Reputation Governance Dashboard

Use the Email Deliverability and Reputation Governance dashboard to view key statistics for email delivery. Sender reputation and email deliverability depend on these statistics. Regularly monitor the dashboard and address any issues you find.
The dashboard shows data from two sources:
- Metrics from the OCI Monitoring service
- Logs from the OCI Logging service

Metrics from the OCI Monitoring service
- The top section of the dashboard uses Metrics data.
- The displayed metrics are pre-aggregated and do not include detailed data.
- By default, the dashboard displays metrics data since the beginning of the current day, in five-minute intervals
- For more advanced filtering or visualization, use the Monitoring service's[Metrics Explorer](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metrics-guide.htm).
- For detailed logs or to use special filtering or grouping requirements that Metrics Explorer cannot provide, use[Logging](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/dashboard.htm#top__log).

Logs from the OCI Logging service
- Detailed logs provide information on email acceptance and outbound delivery activities.
- Logging is not enabled by default.[Enable logs](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/dashboard-topic-enabling-logging.htm)for each Email Domain as needed.
- Logs show detailed records, but you can also aggregate on many different fields with the Logging Query Language.
- The Data Insights and Deliverability Logs sections of the dashboard use logging data. For more advanced filtering or data analysis, use the[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/log-guide.htm)feature.
Note
