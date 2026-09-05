# Creating a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm
- Fetched: 2026-09-05 02:40 CDT

# Creating a Query

Define a query to retrieve data from Monitoring.

For an example query, see[Example Query and Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm#)
- 

These steps show how to create a query in the Metrics Explorer page, in Basic mode. To create a query in Advanced mode (MQL), see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Metrics Explorer .
The Metrics Explorer page displays an empty chart with fields to build a query.
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- In the query under the chart, select the compartment that contains the metric that you want.
- Select the metric namespace that contains the metric that you want.

Note  
  
The Metric namespace list shows metric namespaces for the selected compartment. For example, if the current compartment contains load balancers, then the list includes oci_lbaas .
- Select the name of the metric.
- Update the interval or statistic as needed.
- (Optional) To select dimensions, provide values for the following fields:

- Dimension name : A qualifier specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.
- Dimension value : The value that you want to use for the specified dimension, for example, the resource identifier for an instance.
- Additional dimension : Adds another name-value pair for a dimension.
- (Optional) To aggregate metric streams, select Aggregate metric streams .
- Select Update Chart .
The chart shows data points for the custom metric, in a graph view. Example:  
  

- (Optional) To switch to a table view, select Show Data Table .
The chart shows data points for the custom metric, in a table view.

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data:

```

```

When specifying a dimension value within the query (`--query-text`), surround it with double quotes, and escape each double quote with a backslash character (`\`). Example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)
