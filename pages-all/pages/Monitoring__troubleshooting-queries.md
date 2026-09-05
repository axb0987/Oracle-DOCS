# Troubleshooting Queries
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/troubleshooting-queries.htm
- Fetched: 2026-09-05 02:40 CDT

# Troubleshooting Queries

Use troubleshooting information to identify and address common issues that can occur while working with queries in Monitoring.

## Error: Exceeded Maximum Metric Streams

Troubleshoot too many metric streams when querying metric data.

An error indicates that the metric query exceeded the maximum number of metric streams .

This issue occurs when the query evaluates too many metric streams.
Limits information for returned data includes the 100,000 data point maximum and[time range maximums (determined by resolution, which relates to interval)](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval). See[MetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData).

To remedy this issue, update the query to evaluate a number of metric streams that's within the limit.

For example, select dimensions to reduce the number of metric streams. See[Selecting Dimensions for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm).

To evaluate all metric streams that were in the original query, spread the metric streams across multiple queries.

## Missing Resources or Metrics

Troubleshoot missing resources or metrics when querying metric data.

When[querying metric data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm), you don't see all expected resources or metrics. In the Console, you might notice this issue when viewing a[default chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/viewingcharts.htm),[custom chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-view-chart.htm), or[chart for an alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-chart.htm).

### Cause: Incorrect time range

The metric data returned from the query doesn't include times when the resources emit data points.

### Remedy: Change the time range

See the relevant instructions:
- Service Metrics or resource page in the Console:[Changing the Time Range for Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-time-range.htm).
- Metrics Explorer page in the Console:[Changing the Time Range for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-time-range.htm).
- Query (CLI, API, or Console):[Selecting a Nondefault Time Range for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-time-range.htm)

### Cause: Incorrect compartment

Metric namespaces are shown only when associated resources exist in the selected compartment. For example, the`oci_autonomous_database`namespace is shown only when Autonomous AI Databases exist in the selected compartment.

### Remedy: Change the compartment

Select the compartment that contains the resource that you want.

See the relevant instructions:
- Service Metrics page in the Console:[Viewing Default Metric Charts for a Metric Namespace (Multiple Resources)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-namespace.htm).
- Query (CLI, API, or the Metrics Explorer page in the Console):[Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm).
- Alarm query (CLI, API, or the Create Alarm page in the Console):[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

### Cause: Compute instance isn't enabled for monitoring

The compute instance doesn't emit metric data because the instance isn't enabled for monitoring.

### Remedy: Enable the compute instance for monitoring
See[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
