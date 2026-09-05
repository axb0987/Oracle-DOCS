# Creating an Absence Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm
- Fetched: 2026-09-05 02:38 CDT

# Creating an Absence Alarm

Create an absence alarm in Monitoring to send notifications when a metric doesn't emit data for a specified interval.

The`absent()`statistic in an absence alarm returns`1`(true) when the metric is absent for the entire[interval](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval). After continuous`1`values for the duration of the absence detection period , the statistic stops returning values. When the metric is present during the interval, the statistic returns`0`(false).

The default absence detection period is two hours. For more information about the absence detection period, see[Absence Alarm Example](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#reset__absent). Example The following metric query has an absence alarm for a compute instance that's set on an interval of 1 minute (with the default absence detection period):
```

```
The following metric query sets the absence detection period to 20 hours:
```

```

Note  
  

We recommend including[`groupBy`](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-groupby.htm)in the query of the absence alarm. Using`groupBy`prevents irrelevant alarm triggers when OCI introduces new dimensions. A new dimension creates an initially empty metric stream.

With`groupBy`, the alarm monitors grouped metric streams only. The previous example query triggers the alarm when no metric streams exist for the instance. If OCI Compute adds a dimension to`CpuUtilization`, and other metric streams (from other dimensions) aren't absent, then the alarm isn't triggered.

Without`groupBy`, the alarm monitors all metric streams. For example, consider the query`CpuUtilization[1m].absent()`. If OCI Compute adds a dimension to`CpuUtilization`, then the alarm is triggered, regardless of the presence of other metric streams. In the metric chart on the Create Alarm page, a dashed red line indicates the absence threshold. The following example shows a`1`value for a metric stream, which indicates that the compute instance corresponding to this metric stream didn't emit`CpuUtilization`metric data until 1:30.

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm#)
- 

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- In the Trigger rule section in the Create Alarm , configure the absence trigger:

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

- (Optional) To prevent irrelevant alarm triggers when OCI introduces new dimensions (recommended):
- Go to the Metric dimensions area and provide the following values:

- Dimension name : Select a qualifier that's specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.
- Dimension value : Select the value to use for the specified dimension. For example, if you selected`resourceId`as the dimension, select the resource identifier for the instance that you're monitoring.
- At the top of the page, select Switch to Advanced Mode .
The query appears in Monitoring Query Language (MQL), in the Query code editor box. Example:
```

```

- In the Query code editor box, before`.absent()`, insert`.groupBy( <dimension_name> )`.
Example:
```

```

- Provide values for the remaining fields.
For reference, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create a threshold alarm. For the required parameter`--query-text`, use an MQL expression that specifies an absence trigger rule:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an absence alarm.

When defining details for[CreateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/CreateAlarmDetails), set`query`
