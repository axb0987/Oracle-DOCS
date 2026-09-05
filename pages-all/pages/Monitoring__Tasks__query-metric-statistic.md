# Selecting the Statistic for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-statistic.htm
- Fetched: 2026-09-05 02:40 CDT

# Selecting the Statistic for a Query

Select the statistic for querying metric data in Monitoring. The statistic is the aggregation function applied to the set of raw data points at the specified interval .
Example: Mean Statistic
```

```

For valid statistic options in MQL expressions, see[Statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic). For alarm instructions, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-statistic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-statistic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-statistic.htm#)
- 

This section describes how to select the statistic on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- To select the statistic using Basic mode (default), select from Statistic .

- Count : Returns the number of observations received in the specified interval.
- Max : Returns the highest value observed during the specified interval.
- Mean : Returns the value of Sum divided by Count during the specified interval.
- Min : Returns the lowest value observed during the specified interval.
- P50 : Returns the estimated value of the 50th percentile during the specified interval.
- P90 : Returns the estimated value of the 90th percentile during the specified interval.
- P95 : Returns the estimated value of the 95th percentile during the specified interval.
- P99 : Returns the estimated value of the 99th percentile during the specified interval.
- Rate : Returns the per-interval average rate of change. The unit is per-second.
- Sum : Returns all values added together, per interval.
- To select the statistic by updating the MQL expression, follow these steps:
- Select Advanced mode .
- Edit the text in the Query code editor box.
For valid statistic options in MQL expressions, see[Statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic).
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to select the statistic (part of the MQL expression).

```

```

For valid statistic options in MQL expressions, see[Statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic).

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to select the statistic (part of the MQL expression). For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails).

For valid statistic options in MQL expressions, see[Statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic)
