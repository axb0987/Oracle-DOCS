# Viewing Metrics for the DNS Service
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/view-dns-metrics.htm
- Fetched: 2026-09-05 01:58 CDT

# Viewing Metrics for the DNS Service

View metrics for the DNS service.
See[DNS Metrics](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/dnsmetrics.htm)for more information and a feature overview.

## Using the Console

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- Select the`oci_dns`metric namespace.
- Select a metric to view from the Metric name field.
- Select a qualifier specified in the Dimension Name field. For example, the dimension`resourceId`is specified in the metric definition for`DNSQueryCount`.
- Select the value you want to use for the specified dimension in the Dimension Value field.
- Select Update Chart .
The chart is updated with the metrics that have been requested.
For more information about monitoring metrics and using alarms, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm). For information about notifications for alarms, see[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)
