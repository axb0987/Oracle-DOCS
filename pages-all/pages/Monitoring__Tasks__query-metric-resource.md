# Selecting a Resource for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource.htm
- Fetched: 2026-09-05 02:40 CDT

# Selecting a Resource for a Query

Limit returned metric data to a resource by selecting a resource-specific dimension when querying metric data in Monitoring.

Available dimensions vary by metric.

This page describes how to query metrics from a resource through resource-specific dimensions. You can also access resource-specific metric charts by going to the resource's details page in the Console. See[Viewing Default Metric Charts for a Single Resource](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-resource.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Examples

Example 1: Selecting a Resource by Name
```

```
Example 2: Selecting a Resource by OCID
```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource.htm#)
- 

This section describes how to select a resource on the Metrics Explorer page by selecting a resource-specific dimension. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- To select a resource by using Basic mode (default), provide the following information.

Additional or other dimension fields appear for some metric namespaces. For example, a deployment type field appears for the`oci_autonomous_database`metric namespace. See the service-specific documentation for details.
- Dimension name : A qualifier specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.

To select a specific resource within the selected compartment, filter results by a resource-specific dimension, such as resourceDisplayName .
Note  
  

Long lists of dimensions are trimmed.
- To view dimensions by name, type one or more characters in the box. A refreshed (trimmed) list shows matching dimension names.
- To retrieve all dimensions for a metric, see[Listing Metric Definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
- Dimension value : The value that you want to use for the specified dimension, for example, the resource identifier for an instance.
- Additional dimension : Adds another name-value pair for a dimension.
- To select a resource by updating the MQL expression, follow these steps:
- Select Advanced mode .
- Edit the text in the Query code editor box.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to select resource-specific dimensions (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to select resource-specific dimensions (part of the MQL expression). For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
