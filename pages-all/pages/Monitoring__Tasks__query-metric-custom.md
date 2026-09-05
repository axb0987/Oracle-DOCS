# Creating a Query for a Custom Metric
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm
- Fetched: 2026-09-05 02:39 CDT

# Creating a Query for a Custom Metric

Define a query for a custom metric in Monitoring.

For information about custom metrics, see[Publishing Custom Metrics Using the API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm). For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm#)
- 

These steps show how to create a query in Basic mode on the Metrics Explorer page. To create a query in Advanced mode (MQL), see[Editing the MQL Expression for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- In the query under the chart, select the compartment that contains the custom metric that you want.
- Select the metric namespace that contains the custom metric that you want.
Example:`mymetricsnamespace`
- (Optional) Select the resource group that you want.
Example:`divisionX`
- Select the name of the custom metric.
Example:`productOrder`
- (Optional) Update the interval or statistic.
Example: Select 1 minute for Interval , and select Sum for Statistic .
- To view and update the MQL expression, select Advanced mode .

The MQL expression is in the Query code editor box. Example:`productOrder[1m].sum()`
- Select Update Chart .
The chart shows data points for the custom metric, in a graph view. Example:
- (Optional) To switch to a table view, select Show Data Table .
The chart shows data points for the custom metric, in a table view.
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data.

```

```

The following example uses the`--from-json`parameter to retrieve custom metric information from a JSON file.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).

[Example JSON file for request](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm#)

Compare this file to the example of posted metric data at[Publishing Custom Metrics Using the API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).
```

```

[Example response](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm#)

This example response includes data points for the resource group division`X`only (`ball`product,`NL`country). Aggregation uses a one-minute interval, resulting in three timestamps.

Compare this response to the example of posted metric data at[Publishing Custom Metrics Using the API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).
```

```

- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)
