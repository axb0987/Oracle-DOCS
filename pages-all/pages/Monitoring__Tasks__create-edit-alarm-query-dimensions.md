# Selecting Dimensions for an Alarm Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-dimensions.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting Dimensions for an Alarm Query

Limit the metric data that's returned by selecting dimensions for an alarm in Monitoring. A dimension is a qualifier provided in a metric definition. In MQL, the dimension selection component specifies name-value pairs for dimensions, surrounded by curly brackets.

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

## Considerations

Any text is accepted as a dimension name. If the dimension doesn't exist, then data isn't filtered.

To ensure that the dimension exists,[list dimensions for the metric name](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm)or see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#SupportedServices).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-dimensions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-dimensions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-dimensions.htm#)
- 

For information about selecting dimensions from the Metrics Explorer page, see[Selecting Dimensions for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm).

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Metric description area, verify that the metric namespace and the metric name that you want to specify dimensions for are selected.
- To select dimensions by using Basic mode (default), go to the Metric dimensions area and provide the following values:

- Dimension name : Select a qualifier that's specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.
- Dimension value : Select the value to use for the specified dimension. For example, if you selected`resourceId`as the dimension, select the resource identifier for the instance that you're monitoring.
- Additional dimension : Add another name-value pair for a dimension, as needed.
- To select dimensions by updating the MQL expression, follow these steps:
- At the top of the Edit alarm page, select Switch to Advanced Mode .
- In the Metric description, dimensions, and trigger rule area, edit the text in the Query code editor box.
For reference, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm).
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--query-text`parameter to select dimensions (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`query`
