# Creating a Query for Health Checks
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/query-metric.htm
- Fetched: 2026-09-05 02:14 CDT

# Creating a Query for Health Checks

Define a query for health check metric data (`oci_healthchecks`).

For an example query, see[Example Query and Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example).

For more information about these metrics, see[Health Checks Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/../Reference/metricsalarms-reference.htm#top).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/query-metric.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/query-metric.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/query-metric.htm#)
- 

To create a user-defined query for health check metric data in the Console, use the Metrics Explorer page.

These steps show how to create a query in Basic mode. To create a query in Advanced mode (MQL), see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Metrics Explorer .
The Metrics Explorer page displays an empty chart with fields to build a query.
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- (Optional) To change the time range for the query, select the range you want from Quick Selects .
Alternatively, you can define a custom range by specifying the Start time and End time .
- Select the metric:

- Compartment : The compartment containing the resources that you want to monitor. By default, the first accessible compartment is selected.
- Metric namespace : Select oci_healthchecks .
- Metric name : Select the metric that you want. For example, select PING.isHealthy
- (Optional) To filter returned data by dimension, select a Dimension name and Dimension value .
For example, to filter by endpoint, select target from Dimension name and then select the value that you want from Dimension value .
- Select Update Chart .
The chart shows the results of the query for the selected compartment and region.

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Editing the MQL Expression for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm). For other querying tasks, see[Querying Metric Data](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm).
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. To query Health Checks metrics, set`--namespace`to`oci_healthchecks`.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. To query Health Checks metrics, set`namespace`to`oci_healthchecks`
