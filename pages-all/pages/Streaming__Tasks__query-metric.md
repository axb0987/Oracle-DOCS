# Creating a Query for Streams
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/query-metric.htm
- Fetched: 2026-09-05 03:06 CDT

# Creating a Query for Streams

Define a query for stream metric data (`oci_streaming`).

For more information about these metrics, see[Streaming Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Reference/metric-ref.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/query-metric.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/query-metric.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/query-metric.htm#)
- 

To create a user-defined query for connector metric data in the Console, use the Metrics Explorer page.

These steps show how to create a query in Basic mode. To create a query in Advanced mode (MQL), see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Metrics Explorer .
The Metrics Explorer page displays an empty chart with fields to build a query.
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- (Optional) To change the time range for the query, select the range you want from Quick Selects .
Alternatively, you can define a custom range by specifying the Start time and End time .
- Select the metric:

Field Description
Compartment The compartment containing the resources that you want to monitor. By default, the first accessible compartment is selected.
Metric namespace Select oci_streaming .
Metric name Select the metric that you want. For example, select PutMessagesLatency.Time
- (Optional) To filter returned data by dimension, select a Dimension value and Dimension value .
For example, to filter by stream, select resourceId from Dimension value and then select the stream OCID that you want from Dimension value .
- Select Update Chart .
The chart shows the results of your query for the selected compartment and region.

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For other querying tasks, see[Querying Metric Data](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm).
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. To query Streaming metrics, set`--namespace`to`oci_streaming`.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. To query Streaming metrics, set`namespace`to`oci_streaming`
