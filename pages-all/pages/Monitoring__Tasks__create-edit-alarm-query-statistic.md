# Selecting the Statistic for an Alarm Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-statistic.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting the Statistic for an Alarm Query

Select the statistic for an alarm query. The statistic is the aggregation function applied to the set of raw data points at the specified interval .

For valid statistic options in MQL expressions, see[Statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic). For alarm instructions, see[Creating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-statistic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-statistic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-statistic.htm#)
- 

For information about selecting the statistic from the Metrics Explorer page, see[Selecting the Statistic for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-statistic.htm).

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- Select the Compartment that contains the metric that you want.
- Select the Metric namespace that contains the metric that you want.
- To select the statistic using Basic mode (default), use Statistic :

- Mean - The value of Sum divided by Count during the specified time period.
- Rate - The per-interval average rate of change.
- Sum - All values added together.
- Max - The highest value observed during the specified time period.
- Min - The lowest value observed during the specified time period.
- Count - The number of observations received in the specified time period.
- P50 - The value of the 50th percentile.
- P90 - The value of the 90th percentile.
- P95 - The value of the 95th percentile.
- P99 - The value of the 99th percentile.
- To select the statistic by updating the MQL expression, follow these steps:
- At the top of the Edit alarm page, select Switch to Advanced Mode .
- In the Metric description, dimensions, and trigger rule area, edit the text in the Query code editor box.
For reference, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Statistic (Monitoring Query Language (MQL) Reference)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic).
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--query-text`parameter to select the statistic (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`query`
