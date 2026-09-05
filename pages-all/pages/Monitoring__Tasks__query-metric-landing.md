# Querying Metric Data
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm
- Fetched: 2026-09-05 02:39 CDT

# Querying Metric Data

Define a query to retrieve metric data in Monitoring. Actively monitor cloud resources with metric queries that you generate spontaneously, on demand. In the Console, update a chart to show data from multiple queries. Passively monitor resources by creating alarms from queries that you define.

The following pages describe tasks you can perform with queries of metric data.
- [Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric.htm)
- [Creating a Query for a Custom Metric](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-custom.htm)
- [Editing the MQL Expression for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-mql.htm)
- [Selecting the Metric Namespace for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-namespace.htm)
- [Selecting the Metric Name for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-metric.htm)
- [Selecting a Resource Group in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-resource-group.htm)
- [Selecting the Interval for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-interval.htm)
- [Selecting the Statistic for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-statistic.htm)
- [Selecting a Nondefault Time Range for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-time-range.htm)
- [Selecting Dimensions for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-dimension.htm)
- [Selecting a Resource for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-resource.htm)
- [Using filter(x) in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-filter.htm)
- [Using groupBy(x) in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-groupby.htm)
- [Aggregating Metric Streams in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-grouping.htm)
- [Specifying a Predicate in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-predicate.htm)
- [Selecting a Nondefault Resolution for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-resolution.htm)
- [Nesting Queries in an MQL Expression](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-nested.htm)
- [Creating an Alarm from a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-create-alarm.htm)

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Before You Begin

IAM policies: To query metrics, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For an example policy, see[Query Metrics](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups-query).

## Example Query and Metric Chart

The query in this example uses the following MQL expression:
```

```

This query returns aggregated`mean()`(statistic) values of emitted metric data for the metric named`CpuUtilization`every minute (from the`1m`interval).

For more information about the`CpuUtilization`metric, see[Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm).

Following are example metric charts in both graph and table data view.

### Graph View Example of Metric Chart

The following image shows several metric streams in the graph view of a metric chart. Each metric stream corresponds to a compute instance.

The 85% value at 1:30 indicates that a compute instance used 85% of its CPU (averaged over the specified interval). Absent values are indicated for a metric stream toward the bottom of the graph, indicating that a compute instance didn't emit metric data until 1:30.
[

Very small or large values are indicated by International System of Units (SI units), such as M for mega (10 to the sixth power). Units correspond to the selected metric and don't change by statistic .

### Data Table Example of Metric Chart

The following abbreviated example lists the values of the`myinstance`metric stream at the 1:30 timestamp and immediately before and after.

Timestamp Percent
Oct 1, 2022, 01:29:00 UTC 81.158842305151567
Oct 1, 2022, 01:30:00 UTC 85.689932345683178
Oct 1, 2022, 01:31:00 UTC 79.925088231917334

For instructions on switching a custom metric chart to a data table or graph view, see[Switching Table and Graph Views for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-toggle-view.htm).

For more information about metric charts (graphs and tables) in the Console, see[Viewing Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/viewingcharts.htm)and[Viewing a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-view-chart.htm). For more information about queries, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)
