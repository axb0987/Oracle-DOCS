# Listing Metric Stream Status in an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm
- Fetched: 2026-09-05 02:39 CDT

# Listing Metric Stream Status in an Alarm

List the status of each metric stream in an alarm in Monitoring. A metric stream corresponds to a set of dimension key-value pairs.

Note  
  

Ensure that the alarm is configured for split notifications ( Split notifications per metric stream ). Viewing states of metric streams is available only for alarms with this configuration.

Monitoring stops tracking metric streams associated with`RESET`messages. For more information about message types, see[Message Types](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#MessageTypes).

Messages are sent at the time the alarm transitions, either collectively for all metric streams or individually per metric stream. For more information about messages sent, see[Message Types](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#MessageTypes). For a scenario using individual messages per metric stream, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Next to Metric streams , select View status .

Metric streams is shown on details pages only for those alarms that are configured for split notifications ( Split notifications per metric stream ). Viewing states of metric streams is only available for alarms with this configuration.

The Metric streams status dialog box is displayed, listing the current state ( Firing or OK ) for each metric stream that transitioned to another alarm state. The list includes alarm summaries and trigger rules.

The name of each trigger rule indicates its severity, query, and rule number. The query indicator depends on which mode was used to save the alarm query. If the query was saved in Basic mode, then the query indicator includes the metric namespace, operator, and value (example:`oci_computeagent-greater-than-90`). If the query was saved in Advanced mode, then the name includes the phrase`advanced`.

Example names of trigger rules:
- Basic mode:`Critical-oci_computeagent-greater-than-90-Rule2`
- Advanced mode:`Critical-advanced-Rule2`
- 

Use the[oci monitoring alarm-dimension-states-collection retrieve-dimension-states](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm-dimension-states-collection/retrieve-dimension-states.html)command and required parameters to list status of each metric stream in an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[RetrieveDimensionStates](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmDimensionStatesCollection/RetrieveDimensionStates)
