# Creating a Threshold Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-threshold.htm
- Fetched: 2026-09-05 02:38 CDT

# Creating a Threshold Alarm

Create a threshold alarm in Monitoring to send notifications when a metric meets a specified threshold value.
Example: The following metric query has a threshold alarm set to greater than 80%:
```

```
In the metric chart on the Create Alarm page, a dashed red line indicates the threshold. The following example shows the threshold at 80% and a single value that exceeds the threshold: 85% value at 1:30. That value triggers the alarm. See also[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-threshold.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-threshold.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-threshold.htm#)
- 

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- In the Trigger rule section in the Create Alarm page, configure the absence trigger:

- Operator : The operator used in the condition threshold. For example: between .
- Value : The value to use for the condition threshold. For example: 60 and 80 (the number of values depends on the operator).
- Trigger delay minutes : The number of minutes that the condition must be maintained before the alarm is in the firing state.
- Provide values for the remaining fields.
For reference, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create a threshold alarm. For the required parameter`--query-text`, use an MQL expression that specifies a threshold trigger rule:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an absence alarm.

When defining details for[CreateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/CreateAlarmDetails), set`query`
