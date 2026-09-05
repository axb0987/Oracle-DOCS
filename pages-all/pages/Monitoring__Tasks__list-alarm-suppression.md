# Listing Alarm Suppressions
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-suppression.htm
- Fetched: 2026-09-05 02:39 CDT

# Listing Alarm Suppressions

List suppressions for an alarm in Monitoring.
See also[Getting Suppression History for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-suppression.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-suppression.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-suppression.htm#)
- 

Some alarm suppression details aren't shown in the Console. To view all details about alarm suppressions, use the SDK, CLI, or API.

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
The Suppressed column lists existing suppressions for each alarm. When an alarm contains one or more dimension-specific alarm suppressions, then an option is displayed for viewing details. If you need help with the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm.htm).
- To see information about dimension-specific suppressions for an alarm, under Suppressed , select View details .
This option is available when an alarm contains one or more dimension-specific alarm suppressions.
The Edit alarm suppression panel for the specified alarm opens, listing all suppressions for the alarm. Expand a suppression to list its start time, end time, and other details.
- 

Use the[oci monitoring alarm-suppression-collection list-alarm-suppressions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm-suppression-collection/list-alarm-suppressions.html)command and required parameters to list alarm suppressions:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[ListAlarmSuppressions](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmSuppressionCollection/ListAlarmSuppressions)
