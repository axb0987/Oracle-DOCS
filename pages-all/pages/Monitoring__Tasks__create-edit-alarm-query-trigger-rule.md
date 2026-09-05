# Adding Trigger Rules to an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm
- Fetched: 2026-09-05 02:39 CDT

# Adding Trigger Rules to an Alarm

Define one or more trigger rules, or predicates, for an alarm. A trigger rule is a condition (defined by the query) that must be satisfied for the alarm to be in the firing state, and also includes severity, trigger delay (`pendingDuration`), and the alarm body to include in notifications. A condition in a trigger rule can specify a threshold, such as 90% for CPU utilization, or an absence.

Add up to two trigger rules, or predicates, to an alarm. For example, add a critical trigger rule for 95 percent and a warning trigger rule for 90 percent.
Note  
  
To understand how notifications are sent when an alarm has multiple trigger rules, see[Grouping Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-group-messages.htm)and[Splitting Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-split-messages.htm). Example trigger rules in an alarm
```

```

For valid predicate operators in MQL expressions, see[Predicate Operators](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#predicate).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- In the Metric description area, verify that the metric namespace and the metric name that you want are selected.
- To define a trigger rule (predicate) by using Basic mode (default), go to the Trigger rule area and provide the following values:

- For Operator , select the operator to use in the condition threshold. See[Predicate Operators](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#predicate).
- For Value , enter the value to use for the condition threshold. For the between and outside operators, enter both values for the range.
- For Trigger delay minutes , enter the number of minutes that the condition must be maintained before the alarm is in the firing state.
- For Alarm severity , select the perceived type of response required when the alarm is in the firing state for this condition (trigger rule).
- For Alarm body , enter the human-readable content of the notification for this condition (trigger rule).

We recommend providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Example: "High CPU usage alert. Follow runbook instructions for resolution." Optionally insert[dynamic variables](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm)to render the value of associated[alarm message parameters](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-format.htm)in alarm messages. For example, insert`{{query}}`to render the value of`query`.
- To add another trigger rule (condition), select Additional trigger rule .
- To define a trigger rule (predicate) by updating the MQL expression, perform the following steps:
- At the top of the Edit alarm page, select Switch to Advanced Mode .
- Provide the following values:

- For Trigger delay minutes , enter the number of minutes that the condition must be maintained before the alarm is in the firing state.
- For Alarm severity , select the perceived type of response required when the alarm is in the firing state for this condition (trigger rule).
- For Query code editor , edit the MQL query to specify the trigger rule that you want.

The trigger rule is the operator and value fragment in the MQL query. For example, the fragment`> 90`represents the greater-than operator and a 90 value. Example MQL query:
```

```

For reference, see[Querying Metric Data](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-landing.htm)and[Monitoring Query Language (MQL) Reference](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm).
- For Alarm body , enter the human-readable content of the notification for this condition (trigger rule).
- To add another trigger rule (condition), select Additional trigger rule .
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update trigger rules in an alarm. A trigger rule is part of the MQL expression, or query.

For an alarm with one rule, use the`--query-text`parameter. Example updating trigger rule to greater than 90 percent (`>90`):

```

```

For an alarm with multiple rules, use the`--overrides`parameter. Example:

```

```

[Example JSON file for request (alarm with multiple trigger rules)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-trigger-rule.htm#)

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. A trigger rule is part of the MQL expression in a`query`attribute.

Provide the trigger rules using[UpdateAlarmDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/UpdateAlarmDetails). For an alarm with one rule (no`overrides`value), use the`query`attribute. For an alarm with multiple rules, use the`overrides`
