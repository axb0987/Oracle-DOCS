# Selecting a Resource for an Alarm Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-resource.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting a Resource for an Alarm Query

Limit returned metric data to a resource by selecting a resource-specific dimension when querying metric data for an alarm in Monitoring.

Available dimensions vary by metric.

This page describes how to query metrics from a resource through resource-specific dimensions. You can also access resource-specific metric charts by going to the resource's details page in the Console and creating an alarm from a predefined service query. See[Viewing Default Metric Charts for a Single Resource](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-resource.htm)and[Creating an Alarm from a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-create-alarm.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-resource.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-resource.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-resource.htm#)
- 

For information about selecting a resource from the Metrics Explorer page, see[Selecting a Resource for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource.htm).

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Metric description area, verify that the metric namespace and the metric name that you want to specify dimensions for are selected.
- To select dimensions by using Basic mode (default), go to the Metric dimensions area and provide the following values:

Additional or other dimension fields appear for some metric namespaces. For example, a deployment type field appears for the`oci_autonomous_database`metric namespace. See the service-specific documentation for details.
- 

Dimension name : Select a qualifier that's specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.

To select a specific resource within the selected compartment, filter results by a resource-specific dimension, such as resourceDisplayName .
Note  
  

Long lists of dimensions are trimmed.
- To view dimensions by name, type one or more characters in the box. A refreshed (trimmed) list shows matching dimension names.
- To retrieve all dimensions for a metric, see[Listing Metric Definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
- Dimension value : Select the value to use for the specified dimension. For example, if you selected`resourceId`as the dimension, select the resource identifier for the instance that you're monitoring.
- Additional dimension : Add another name-value pair for a dimension, as needed.
- To select a resource by updating the MQL expression, follow these steps:
- At the top of the Edit alarm page, select Switch to Advanced Mode .
- In the Metric description, dimensions, and trigger rule area, edit the text in the Query code editor box.
For reference, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm).
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--query-text`parameter to select resource-specific dimensions (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`query`
