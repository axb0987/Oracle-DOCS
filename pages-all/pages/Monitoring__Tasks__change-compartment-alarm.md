# Moving an Alarm to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm
- Fetched: 2026-09-05 02:38 CDT

# Moving an Alarm to a Different Compartment

Move an alarm in Monitoring to another compartment.

Important  
  
To move resources between compartments, resource users must have sufficient access permissions for the compartment that the resource is being moved to and the current compartment. For more information about permissions for Monitoring resources, see[Details for Monitoring](https://docs.oracle.com/iaas/Content/Identity/policyreference/monitoringpolicyreference.htm).

When you move an alarm to a new compartment, its associated metrics remain where they are. After you move the alarm to the new compartment, inherent policies apply immediately and affect access to the alarm through the Console. For more information about moving resources, see[Moving a Resource Between Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/To_move_a_resource_to_a_different_compartment.htm).

For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-alarm.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- On the alarm's details page, select Move resource .
- In the Move resource dialog box, select the compartment that you want to move the alarm to.
- Select Move resource .
- 

Use the[oci monitoring alarm change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/change-compartment.html)command and required parameters to move an alarm:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[ChangeAlarmCompartment](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/ChangeAlarmCompartment)
