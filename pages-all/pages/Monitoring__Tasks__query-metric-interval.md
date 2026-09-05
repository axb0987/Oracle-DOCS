# Selecting the Interval for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting the Interval for a Query

Select the interval, or time window, for querying metric data in Monitoring.
Example: One-Minute Interval
```

```

Supported values for interval depend on the specified time range in the metric query (not applicable to alarm queries). More interval values are supported for smaller time ranges. For example, if you select one hour for the time range, then all interval values are supported. If you select 90 days for the time range, then only interval values between 1 hour and 1 day are supported. For valid interval options in MQL expressions, see[Interval (Monitoring Query Language (MQL) Reference)](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval).

[Illustration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm#)

The timestamp of the aggregated data point corresponds to the end of the time window during which raw data points are assessed. For example, for a five-minute interval, the timestamp "2:05" corresponds to the five-minute time window from 2:00: n to 2:05:00.

[

For alarm instructions, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm#)
- 

This section describes how to select the interval on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- To select the interval using Basic mode (default), select from Interval .

- 1 minute
- 5 minutes
- 15 minutes
- 30 minutes
- 1 hour
- 2 hours
- 6 hours
- 12 hours
- 1 day
- Custom - specify a Custom value and select a Unit ( Minutes or Hours )
- To select the interval by updating the MQL expression, follow these steps:
- Select Advanced mode .
- Edit the text in the Query code editor box.
For valid interval options in MQL expressions, see[Interval (Monitoring Query Language (MQL) Reference)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#Interval).
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to select the interval (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to select the interval (part of the MQL expression). For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
