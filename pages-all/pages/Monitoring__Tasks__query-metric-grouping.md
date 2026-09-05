# Aggregating Metric Streams in a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-grouping.htm
- Fetched: 2026-09-05 02:39 CDT

# Aggregating Metric Streams in a Query

Aggregating metric streams returns the combined value of all metric streams for the selected statistic. For example, aggregate all metric streams for CPU Utilization to return the combined value across all resources.

The Aggregate metric streams option is equivalent to`grouping()`in the MQL expression.
Note  
  
If you aggregate metric streams, then only one stream is tracked. Don't aggregate metric streams with[split notifications](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/split-messages.htm).

By default, a chart represents each metric stream with a line, which results in multiple lines per chart. When you aggregate metric streams, a chart represents all metric streams with a single line, which results in just one line per chart.

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Examples

Example 1: Aggregate Metric Streams for count()
```

```

In example 1, the query returns the count (`count()`) of errors at a one-minute interval, with all results aggregated. Example 2: Aggregate Metric Streams for max()
```

```

In example 2, the query returns the maximum (`max()`)`IopsRead`metric data at a one-minute interval, filtered to a compartment, with all results aggregated.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-grouping.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-grouping.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-grouping.htm#)
- 

This section describes how to aggregate metric streams on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- To aggregate metric streams by using Basic mode (default), select Aggregate metric streams .
- To aggregate metric streams by updating the MQL expression, follow these steps:
- Select Advanced mode .
- Edit the text in the Query code editor box.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to employ the`grouping()`element (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to employ the`grouping()`
