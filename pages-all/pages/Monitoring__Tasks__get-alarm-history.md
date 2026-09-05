# Getting the History of an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm
- Fetched: 2026-09-05 02:39 CDT

# Getting the History of an Alarm

Get the history of an alarm in Monitoring. Alarm history is retained for 90 days.

For history of alarm suppressions, see[Getting Suppression History for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm). For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

## Before You Begin

IAM policies: To get alarm history, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For an example policy, see[Get Alarm Details and History](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#get-alarm-history).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm-history.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
The alarm's details page opens. History is available under Alarm data .
- (Optional) Select a period of time from Quick selects .

Under Alarm data , the chart shows data for the indicated time range.

Following the chart is a list of timestamped transitions, such as Firing to OK . The list includes trigger rules.
- To view resources evaluated by the alarm, select the down-arrow for Query .
- To view timestamps for alarm transitions, such as the time that a trigger rule last transitioned to Firing , select the Alarm transition history tab.

The name of each trigger rule indicates its severity, query, and rule number. The query indicator depends on which mode was used to save the alarm query. If the query was saved in Basic mode, then the query indicator includes the metric namespace, operator, and value (example:`oci_computeagent-greater-than-90`). If the query was saved in Advanced mode, then the name includes the phrase`advanced`.

Example names of trigger rules:
- Basic mode:`Critical-oci_computeagent-greater-than-90-Rule2`
- Advanced mode:`Critical-advanced-Rule2`
- 

Use the[oci monitoring alarm-history-collection get-alarm-history](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm-history-collection/get-alarm-history.html)command and required parameters to get history for an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[GetAlarmHistory](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmHistoryCollection/GetAlarmHistory)
