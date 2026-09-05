# Customizing the Slack Period for an Alarm Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-slack-period.htm
- Fetched: 2026-09-05 02:39 CDT

# Customizing the Slack Period for an Alarm Query

Specify a custom value for the slack period to use when querying metric data in an alarm in Monitoring.

The default slack period is three minutes. For more information about the slack period, see[About the Internal Reset Period](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#reset).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-slack-period.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-slack-period.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-slack-period.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--evaluation-slack-duration`parameter to specify the custom slack period.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`evaluationSlackDuration`
