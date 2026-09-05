# Creating an Alarm That Splits Messages by Metric Stream
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-split.htm
- Fetched: 2026-09-05 02:38 CDT

# Creating an Alarm That Splits Messages by Metric Stream

Create an alarm in Monitoring that sends a separate alarm message for each metric stream.

For a scenario with examples, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-split.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-split.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-split.htm#)
- 

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- In the Metric description section of the Create Alarm page, select a metric namespace and metric name.
- In the Message grouping section, select Split notifications per metric stream .
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create an alarm that sends a message for each metric stream. Set`--is-notifications-per-metric-dimension-enabled`to`true`.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an alarm that sends a message for each metric stream.

When defining details for[CreateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/CreateAlarmDetails), set`isNotificationsPerMetricDimensionEnabled`to`true`
