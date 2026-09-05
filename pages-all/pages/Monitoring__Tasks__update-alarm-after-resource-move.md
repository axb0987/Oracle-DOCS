# Updating an Alarm After Moving a Resource
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm
- Fetched: 2026-09-05 02:40 CDT

# Updating an Alarm After Moving a Resource

Update an alarm in Monitoring after you move a monitored resource.

After you move a resource that's emitting metrics monitored by the alarm, update the metric compartment of related alarms. For example, if you move a block volume to another compartment, then the associated alarm must be updated if you want to continue monitoring metrics from the moved block volume.

Inherent policies in the destination compartment apply immediately and affect access to the moved resource through the Console. For more information about moving resources, see[Moving a Resource Between Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/To_move_a_resource_to_a_different_compartment.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- Update the metric compartment: On the Edit alarm page, under Metric description (or Metric description, dimensions, and trigger rule for Advanced Mode ), change the Compartment to the compartment where the resource has been moved.

The chart under the Define alarm section dynamically updates according to the selected compartment, displaying the last six hours of emitted metrics. Very small or large values are indicated by International System of Units (SI units), such as M for mega (10 to the sixth power).

If the chart isn't showing the expected data, then the old compartment might be specified in the query (MQL), as in the following example:

```

```

- If the old compartment is specified in the query, then update the query to reference the new compartment.
- Select Switch to Advanced Mode to view the alarm query as a Monitoring Query Language (MQL) expression.
- In the Query code editor box, update the query to reference the new compartment.

[View example](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm#)

Original query:

```

```

Updated query:

```

```

For information about MQL queries, see[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm).

The chart under the Define alarm section dynamically updates according to the updated query, displaying the last six hours of emitted metrics. Very small or large values are indicated by International System of Units (SI units), such as M for mega (10 to the sixth power).

If the chart isn't showing the expected data, then confirm that every compartment reference ( Compartment , the Query code editor box) points to the new compartment.
- Select Save alarm .
The alarm now monitors metrics from the new compartment.
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm to query metrics in the resource's new compartment. Ensure that the query doesn't specify the resource's old compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm to query metrics in the resource's new compartment.

When defining details for[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails), set`metricCompartmentId`to the resource's new compartment, and ensure that the old compartment isn't specified in`query`
