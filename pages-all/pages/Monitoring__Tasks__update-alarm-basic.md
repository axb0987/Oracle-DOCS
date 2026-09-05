# Making Basic Updates to an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-basic.htm
- Fetched: 2026-09-05 02:40 CDT

# Making Basic Updates to an Alarm

Update an alarm in Monitoring.

When you update an alarm, you can also update its tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm). See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-basic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-basic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-alarm-basic.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- On the Edit alarm page, update the values as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
The updated alarm settings are listed on the alarm details page.
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)
