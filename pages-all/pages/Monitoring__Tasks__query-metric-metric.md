# Selecting the Metric Name for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-metric.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting the Metric Name for a Query

Select the name of the metric for querying metric data in Monitoring.
Example: CPU Utilization
```

```

Valid metric names include predefined service metrics as well as[custom metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm). For names of predefined service metrics, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#SupportedServices)and[Listing Metric Definitions](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm). For alarm instructions, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-metric.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-metric.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-metric.htm#)
- 

This section describes how to select the metric name on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select the Compartment that contains the metric name that you want.
- Select the Metric namespace that contains the metric name that you want.
- Select the Metric name that you want.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to select the metric name (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to select the metric name (part of the MQL expression). For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
