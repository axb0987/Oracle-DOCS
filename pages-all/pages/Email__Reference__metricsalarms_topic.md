# Retrieving Email Delivery Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic.htm
- Fetched: 2026-09-05 02:01 CDT

# Retrieving Email Delivery Metrics

Learn how to retrieve Email Delivery metrics.

Email Delivery service metrics are currently available using the console through following options:
- [Accessing Email Deliverability and Reputation Governance Dashboard](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/accessing_dashboard.htm).
- Accessing the Metrics sidebar menu under the detail pages for approved senders or email domains.
- Customizing[OCI Dashboard](https://docs.oracle.com/iaas/Content/Dashboards/Tasks/dashboards.htm)using[Monitoring widgets](https://docs.oracle.com/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#monitoringchart).
- Using the Service Metrics feature under the Monitoring service. For more information, see[Viewing Default Metric Charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm).
- Using the[Metrics Explorer](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-view-chart.htm)under the Monitoring service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic.htm#)
- 

- Open the navigation menu and click Observability &amp; Management . Under Monitoring , click Metrics Explorer . For Metric namespace , select oci_emaildelivery .
- Select a metric to view from the Metric name field.
- Select a qualifier specified in the Dimension Name field. For example, the dimension`resourceId`is specified in the metric definition for`EmailsAccepted`.
- Select the value you want to use for the specified dimension in the Dimension Value field. For example, the resource identifier for your instance of interest.
- Click Update Chart . The chart will be updated with the metrics that have been requested.

For more information about monitoring metrics and using alarms, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm). For information about notifications for alarms, see[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
- 

Use the[oci iam domain get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/get.html)command and required parameters to &lt;task-being-performed&gt;:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the following APIs for metrics, alarms, and notifications:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
