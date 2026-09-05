# Using filter(x) in a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-filter.htm
- Fetched: 2026-09-05 02:39 CDT

# Using filter(x) in a Query

Use`filter(x)`to remove values from the metric streams in the returned data, where the metric streams are defined by the previous query components.
Example: Remove Values Less than 20
```

```

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-filter.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-filter.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-filter.htm#)
- 

This section describes how to use`filter(x)`on the Metrics Explorer page.`filter(x)`is available in Advanced mode (MQL) only. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select Advanced mode .
- Edit the text in the Query code editor box.

The following example MQL expression includes only values greater than 20.
```

```

The graph from[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)now shows only those values higher than 20. In addition to the 85% value at 1:30, a constant 21% value is shown in another metric stream over the time displayed in the graph.

- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to employ the`filter(x)`element (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to employ the`filter(x)`
