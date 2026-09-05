# Suppressing a Single Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm
- Fetched: 2026-09-05 02:38 CDT

# Suppressing a Single Alarm

Temporarily stop notifications from an alarm by applying a suppression. For example, use a suppression to suspend alarm notifications during system maintenance.

Note  
  
Dimension-specific suppressions are available for alarms that are configured for split messages only. See[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/split-messages.htm). A dimension-specific suppression can't be added to multiple alarms at the same time.

When you create an alarm suppression using the SDK, CLI, or API, you can also add tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). you can also update its tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

See also[Suppressing Multiple Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression-multiple.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm#)
- 

Tagging alarm suppressions isn't available in the Console. To tag a new alarm suppression, use the SDK, CLI, or API.

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- On the alarm's details page, select Edit alarm suppression .
- In the Edit alarm suppression panel, provide the following values:

- Start time : The date and time to start the suppression. The default is the current time. The value must be within 90 days of the current time. If you're editing an existing suppression, the field shows the start time of that suppression.
- End time : The date and time to end the suppression. The default is one hour from the current time. The value must be within 90 days of the current time. If you're editing an existing suppression, the field shows the end time of that suppression.
- Suppression description : Optional description of the suppression.
- To specify dimensions for the suppression (alarm must be configured for[split messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-split.htm)), select Suppress per Dimension , and then provide the following values:

- Display name (dimension-specific suppression only): User-friendly name for the suppression. Avoid entering confidential information.
- Suppress per Dimension : Select this option for a dimension-specific suppression of the alarm.
- Dimension name : Select the name of the dimension that you want to suppress notifications for. For example, select`resourceId`.
- Dimension value : Select the value that you want to suppress notifications for. For example, the OCID for a compute instance. (Only one value can be specified.)
- To add another dimension-specific suppression, select Additional dimension .
- Select Add suppressions .
- 

Use the[oci monitoring alarm-suppression create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm-suppression/create.html)command and required parameters to create an alarm suppression:

```

```

Note  
  
You can alternatively use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command. Dimensions can't be specified with this command.

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarmSuppression](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/AlarmSuppression/CreateAlarmSuppression)operation to create a dimension-specific alarm suppression.
Note  
  
You can alternatively use the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)
