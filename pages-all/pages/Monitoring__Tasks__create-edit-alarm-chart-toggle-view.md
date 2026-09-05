# Switching Table and Graph Views for an Alarm Metric Chart
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-chart-toggle-view.htm
- Fetched: 2026-09-05 02:38 CDT

# Switching Table and Graph Views for an Alarm Metric Chart

View the metric chart for a new or existing alarm in the Console as a table, or switch back to the graph (chart) view.

See also:
- [Switching Table and Chart Views for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-toggle-view.htm)
- [Switching Table and Graph Views for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-toggle-view.htm)

- To view a metric chart for a new alarm, follow these steps:
- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- In the Metric description section on the Create Alarm page, select a metric namespace and metric name.

Note  
  
The Metric namespace list shows metric namespaces for the selected compartment. For example, if the current compartment contains load balancers, then the list includes oci_lbaas .
The chart shows metric data for the alarm query.
- To view a metric chart for an existing alarm: On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
The chart shows metric data for the alarm query.
- Select Show Data Table .
The metric data is now presented as a table. Example excerpt:

Timestamp Percent
Oct 1, 2022, 01:29:00 UTC 81.158842305151567
Oct 1, 2022, 01:30:00 UTC 85.689932345683178
Oct 1, 2022, 01:31:00 UTC 79.925088231917334
- To switch back to a chart view, select Show Graph .
