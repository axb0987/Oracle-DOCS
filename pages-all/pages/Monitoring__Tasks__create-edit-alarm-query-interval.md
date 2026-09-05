# Selecting the Interval for an Alarm Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting the Interval for an Alarm Query

Select the interval, or time window, for querying metric data in an alarm in Monitoring.

For valid interval options in MQL expressions, see[Interval (Monitoring Query Language (MQL) Reference)](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval).

[Illustration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm#)

The timestamp of the aggregated data point corresponds to the end of the time window during which raw data points are assessed. For example, for a five-minute interval, the timestamp "2:05" corresponds to the five-minute time window from 2:00: n to 2:05:00.

[

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-interval.htm#)
- 

For information about selecting the interval from the Metrics Explorer page, see[Selecting the Interval for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-interval.htm).

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- Select the Compartment that contains the metric that you want.
- Select the Metric namespace that contains the metric that you want.
- To select the interval using Basic mode (default), use Interval :

- 1 minute
- 5 minutes
- 15 minutes
- 30 minutes
- 1 hour
- 2 hours
- 6 hours
- 12 hours
- 1 day
- Custom - specify a Custom value and select a Unit ( Minutes or Hours )
- To select the interval by updating the MQL expression, follow these steps:
- At the top of the Edit alarm page, select Switch to Advanced Mode .
- In the Metric description, dimensions, and trigger rule area, edit the text in the Query code editor box.
For reference, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Interval (Monitoring Query Language (MQL) Reference)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#Interval).
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--query-text`parameter to select the interval (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`query`
