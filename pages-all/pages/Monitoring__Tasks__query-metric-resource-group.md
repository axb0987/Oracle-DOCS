# Selecting a Resource Group in a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource-group.htm
- Fetched: 2026-09-05 02:40 CDT

# Selecting a Resource Group in a Query

Limit returned metric data by matching a resource group when querying custom metric data in Monitoring.

Resource groups are available with[custom metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm). Blank (null) for[resource group](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#concepts__resourcegroupdefinition)returns metric data that doesn't have a resource group.

For troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource-group.htm#)
- 

This section describes how to select the resource group for a new query on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- Select the Compartment that contains the custom metric that you want.
- Select the Metric namespace that contains the custom metric that you want.
- Select the Resource group that you want.
- Provide minimum required fields: Select a Metric name .
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--resource-group`parameter to select a resource group for the query.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`resourceGroup`
