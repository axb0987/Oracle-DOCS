# Using groupBy(x) in a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-groupby.htm
- Fetched: 2026-09-05 02:39 CDT

# Using groupBy(x) in a Query

Use the optional`groupBy(x)`element when querying metric data in Monitoring.

Aggregate query results by group to plot a value for each group. This option returns the combined value of all metric streams in each specified group for the selected statistic. Each group's combined value is plotted as a single line on the metric chart. This option is helpful when you want to identify trends by group rather than individual resource.

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Examples

Example 1: Group by Fault Domain
```

```
Example 2: Group by[Resource Group](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#concepts__resourcegroupdefinition)
```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-groupby.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-groupby.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-groupby.htm#)
- 

This section describes how to use`groupBy(x)`on the Metrics Explorer page.`groupBy(x)`is available in Advanced mode (MQL) only. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select Advanced mode .
- Edit the text in the Query code editor box.

The following example MQL expression groups by fault domain:
```

```

The graph from[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)now shows three metric streams. Each metric stream corresponds to a fault domain, aggregating all compute instances in that fault domain.

- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to employ the`groupBy(x)`element (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to employ the`groupBy(x)`
