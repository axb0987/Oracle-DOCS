# Selecting Dimensions to Filter Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-dimensions.htm
- Fetched: 2026-09-05 02:40 CDT

# Selecting Dimensions to Filter Metrics

Use dimensions to filter the data plotted that's plotted on default metric charts on the Service Metrics page in the Console. For example, filter results to a particular resource or fault domain. Available dimensions vary by metric.

Dimensions can't be selected for default metric charts on resource details pages. To add dimensions to a query from a resource details page,[open](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-explore.htm)the related query in the Metrics Explorer page and then[select dimensions](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm).

- [Open](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-namespace.htm)the Service Metrics page.
- Next to Dimensions , select Add .
- Provide the following information.

Additional or other dimension fields appear for some metric namespaces. For example, a deployment type field appears for the`oci_autonomous_database`metric namespace. See the service-specific documentation for details.
- Dimension name : A qualifier specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.

To select a specific resource within the selected compartment, filter results by a resource-specific dimension, such as resourceDisplayName .
Note  
  

Long lists of dimensions are trimmed.
- To view dimensions by name, type one or more characters in the box. A refreshed (trimmed) list shows matching dimension names.
- To retrieve all dimensions for a metric, see[Listing Metric Definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
- Dimension value : The value that you want to use for the specified dimension, for example, the resource identifier for an instance.
- Additional dimension : Adds another name-value pair for a dimension.
- Select Done .

The charts now show data filtered to the selected dimensions.

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Selecting Dimensions for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm)
