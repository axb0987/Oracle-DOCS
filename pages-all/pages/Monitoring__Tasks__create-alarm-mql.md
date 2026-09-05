# Editing the MQL Expression When Creating an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm
- Fetched: 2026-09-05 02:38 CDT

# Editing the MQL Expression When Creating an Alarm

Directly edit an alarm's MQL expression when you create the alarm in Monitoring.

For an example MQL expression, see[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example). For information about all query elements, including compartment and metric namespace, see[Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm#)
- 

On the Create Alarm page in the Console, the MQL expression is available in Advanced mode only.

- On the Alarm Definitions list page, select Create Alarm . If you need help finding the list page, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- (Optional) To prepopulate the MQL expression with required fields, in the Metric description section on the Create Alarm page, select a metric namespace and metric name.
- At the top of the page, select Switch to Advanced Mode .
The Metric description area is relabeled to Metric description, dimensions, and trigger rule .
- In that area, edit the text in the Query code editor box.
For reference, see[Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm).
- Provide values for the remaining fields.
For reference, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create an alarm. Use the`--query-text`parameter to specify the MQL expression.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an alarm. Use the`query`
