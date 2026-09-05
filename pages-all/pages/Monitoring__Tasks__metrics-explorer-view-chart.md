# Viewing a Custom Metric Chart
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-view-chart.htm
- Fetched: 2026-09-05 02:39 CDT

# Viewing a Custom Metric Chart

Define a query for a custom metric chart on the Metrics Explorer page in the Console.

The following pages describe tasks you can perform with the metric chart on the Metrics Explorer page.
- [Creating a Basic Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-basic-query.htm)
- [Changing the Time Range for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-time-range.htm)
- [Switching Table and Graph Views for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-toggle-view.htm)
- [Customizing Y-Axis Labels in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-customize-y-axis.htm)
- [Viewing Queries for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-view-queries.htm)
- [Adding and Deleting Queries in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-add-delete-query.htm)
- [Editing a Query in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-edit-query.htm)
- [Hiding and Showing Queries in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-hide-show-query.htm)
- [Creating an Alarm from a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-create-alarm.htm)

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Example Metric Chart

The following image shows several metric streams in the graph view of a metric chart. Each metric stream corresponds to a compute instance.

The 85% value at 1:30 indicates that a compute instance used 85% of its CPU (averaged over the specified interval). Absent values are indicated for a metric stream toward the bottom of the graph, indicating that a compute instance didn't emit metric data until 1:30.
[

Very small or large values are indicated by International System of Units (SI units), such as M for mega (10 to the sixth power). Units correspond to the selected metric and don't change by statistic .

For more information about this example, see[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)
