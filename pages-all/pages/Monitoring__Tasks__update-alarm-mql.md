# Editing the MQL Expression When Updating an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-mql.htm
- Fetched: 2026-09-05 02:40 CDT

# Editing the MQL Expression When Updating an Alarm

Directly edit an alarm's MQL expression when you update the alarm.

For an example MQL expression, see[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example). For information about components of MQL expressions, see the tasks listed under[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm). For information about all query elements, including compartment and metric namespace, see[Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-mql.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-mql.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-mql.htm#)
- 

On the Edit alarm page in the Console, the MQL expression is available in Advanced mode only.

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- On the Edit alarm page, select Switch to Advanced Mode .
- Edit the text in the Query code editor box.
For reference, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm).
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--query-text`parameter to specify the MQL expression.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`query`
