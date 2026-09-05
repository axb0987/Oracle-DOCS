# Selecting a Nondefault Time Range for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-time-range.htm
- Fetched: 2026-09-05 02:40 CDT

# Selecting a Nondefault Time Range for a Query

Set the bounds, or timestamps, of the metric data that you want returned from a query of metric data in Monitoring.

## Considerations

Available options for time range depend on[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm)and[resolution](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resolution.htm).

[Maximum time range returned for a query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-time-range.htm#)

The maximum time range returned for a metric query depends on the resolution. By default, for metric queries, the resolution is the same as the query interval.

The maximum time range is calculated using the current time, regardless of any specified end time. Following are the maximum time ranges returned for each interval selection available in the Console (Basic mode).

Interval Default resolution (metric queries) Maximum time range returned

1 minute

Auto ( Service Metrics page)*, when the selected period of time is 6 hours or less 1 minute 7 days

5 minutes

Auto ( Service Metrics page)*, when the selected period of time is more than 6 hours and less than 36 hours 5 minutes 30 days

1 hour

Auto ( Service Metrics page)*, when the selected period of time is more than 36 hours 1 hour 90 days

1 day 1 day 90 days

* The maximum time range returned when you select Auto for Interval ( Service Metrics page only) is determined by the automatic interval selection. The automatic interval selection is based on the selected period of time.

To specify a nondefault resolution that differs from the interval, see[Selecting a Nondefault Resolution for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-resolution.htm). Example 1 for Returned Data One-minute interval and resolution up to the current time, sent at 10:00 on January 8. No resolution or end time is specified, so the resolution defaults to the interval value of`1m`, and the end time defaults to the current time (`2023-01-08T10:00:00.789Z`). This request returns a maximum of 7 days of metric data points. The earliest data point possible within this seven-day period would be 10:00 on January 1 (`2023-01-01T10:00:00.789Z`). Example 2 for Returned Data Five-minute interval with one-minute resolution up to two days ago, sent at 10:00 on January 8. Because the resolution drives the maximum time range, a maximum of 7 days of metric data points is returned. While the end time specified was 10:00 on January 6 (`2023-01-06T10:00:00.789Z`), the earliest data point possible within this seven-day period would be 10:00 on January 1 (`2023-01-01T10:00:00.789Z`). Therefore, only 5 days of metric data points can be returned in this example.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-time-range.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-time-range.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-time-range.htm#)
- 

By default, charts show the last hour of metric data. For information about time range on default charts, see[Changing the Time Range for Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-time-range.htm). (Time range isn't available for the metric chart displayed while creating or editing an alarm.)

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- Select a period of time from Quick selects .

Example of chart for Last hour :  
  

Example of chart for Last 6 hours :  
  

- To specify the start or end of a period time, enter a value in Start time or End time and then type a value.

You can also select the date and time from the provided calendar tool.
[
- 

Note  
  
The default time range for CLI and API is the last three hours.

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--start-time`and`--end-time`parameters to select a nondefault time range for the query.

```

```

Example value for start or end time:`2023-09-29T13:58:00.000Z`

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Note  
  
The default time range for CLI and API is the last three hours.

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`startTime`and`endTime`attributes to select a nondefault time range for the query. For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
