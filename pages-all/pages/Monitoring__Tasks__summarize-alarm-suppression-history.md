# Getting Suppression History for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm
- Fetched: 2026-09-05 02:40 CDT

# Getting Suppression History for an Alarm

Get history of suppressions for an alarm in Monitoring.
See also[Listing Alarm Suppressions](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-alarm-suppression.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Under Alarm data , select the time range that you want the history for.

You can use Quick Selects or specify a start and end time using the calendar tool.

[Example selections from calender tool](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/summarize-alarm-suppression-history.htm#)
  
  

- Select the Alarm suppression history tab.
- (Optional) To view the dimension name and value associated with an alarm suppression, select the name of the alarm suppression you want.
- 

Use the[oci monitoring alarm-suppression summarize-alarm-suppression-history](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm-suppression/summarize-alarm-suppression-history.html)command and required parameters to get suppression history for an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeAlarmSuppressionHistory](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmSuppression/SummarizeAlarmSuppressionHistory)
