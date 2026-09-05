# Selecting the Metric Namespace for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-namespace.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting the Metric Namespace for a Query

Select the metric namespace for querying metric data in Monitoring.

## Before You Begin

IAM policies: To query metrics, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For example policies, see[Query Metrics for a Metric Namespace](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups-query-namespace)(restricted to a metric namespace) and[Query Metrics](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups-query)(unrestricted).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-namespace.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-namespace.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-namespace.htm#)
- 

This section describes how to select the metric namespace on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select the Compartment that contains the metric namespace that you want.
The page lists metric namespaces for the selected compartment. For example, if the current compartment contains load balancers, then the page includes oci_lbaas in its list of metric namespaces.
- Select the Metric namespace that you want.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--namespace`parameter to select the metric namespace for the query.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`namespace`attribute to select the metric namespace for the query. For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
