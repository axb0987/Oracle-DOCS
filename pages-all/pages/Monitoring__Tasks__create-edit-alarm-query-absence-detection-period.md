# Customizing the Absence Detection Period for an Alarm Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm
- Fetched: 2026-09-05 02:38 CDT

# Customizing the Absence Detection Period for an Alarm Query

Specify a custom value for the absence detection period to use when querying metric data in an alarm in Monitoring.

Note  
  
To understand the impact of customizing the absence detection period, see[Absence Alarm Example](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#reset__absent).

The default absence detection period is two hours. An alarm query containing`absent()`uses the default.

Valid values range from one minute (`1m`) to three days (`3d`or`72h`). Specify the amount of time in the absence detection period using a number and unit (`m`,`h`, or`d`for minute, hour, or day).

Example alarm query for a custom absence detection period of 20 hours:
```

```

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Trigger rule section in the Create Alarm page, configure the absence trigger:

- Operator : Select absent .
- Trigger delay minutes : Enter the number of minutes that the condition must be maintained before the alarm is in the firing state.

Alternatively, select Switch to Advanced Mode to use[MQL](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm).
- To customize the absence detection period:
The default absence detection period is two hours. For more information about the absence detection period, see[Absence Alarm Example](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#reset__absent).
- At the top of the page, select Switch to Advanced Mode .
The query appears in Monitoring Query Language (MQL), in the Query code editor box. Example:
```

```

- Replace`absent()`with`absent( <number-and-unit )`.
Valid values range from one minute (`1m`) to three days (`3d`or`72h`). Specify the amount of time in the absence detection period using a number and unit (`m`,`h`, or`d`for minute, hour, or day).
Example (20-hour absence detection period):
```

```

- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--query-text`parameter to specify the custom absence detection period (part of the MQL expression, such as`absent(20h)`).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`query`attribute to specify the custom absence detection period (part of the MQL expression, such as`absent(20h)`
