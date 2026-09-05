# Creating a Query for Block Volume Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-query.htm
- Fetched: 2026-09-05 01:45 CDT

# Creating a Query for Block Volume Resources

Define a query for Block Volume resource metric data (`oci_blockstore`).

For an example query, see[Example Query and Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example).

For more information about these metrics, see[Block Volume Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-reference.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-query.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-query.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics-query.htm#)
- 

To create a user-defined query for Block Volume resource metric data in the Console, use the Metrics Explorer page.

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
Metric namespace Select oci_blockstore .
Metric name Select the metric that you want. For example, select VolumeReadThroughput
- (Optional) To filter returned data by dimension, select a Dimension name and Dimension value .
For example, to filter by resource identifier, select resourceId from Dimension name and then select the value that you want from Dimension value .
- Select Update Chart .
The chart shows the results of your query for the selected compartment and region.

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For other querying tasks, see[Querying Metric Data](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm).
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. To query Block Volume metrics, set`--namespace`to`oci_blockstore`.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. To query Block Volume metrics, set`namespace`to`oci_blockstore`
