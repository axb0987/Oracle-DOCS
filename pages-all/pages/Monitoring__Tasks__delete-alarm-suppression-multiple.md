# Removing Suppressions from Multiple Alarms
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression-multiple.htm
- Fetched: 2026-09-05 02:39 CDT

# Removing Suppressions from Multiple Alarms

Remove suppressions from selected alarms in the Console. For example, if two alarms have existing (expired) alarm-wide suppressions and you want to add a new alarm-wide suppression to them, then remove the existing ones first. An alarm can have only one alarm-wide suppression at a time.

This feature is available in the Console only.
Note  
  
A dimension-specific suppression can't be removed from multiple alarms at the same time.

See also[Removing a Suppression from a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-alarm-suppression.htm). For alarm troubleshooting, see[Troubleshooting Alarms](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-alarms.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
The page lists alarms in the indicated compartment. Suppression status is indicated for each alarm.
- Select the checkbox for each alarm that you want.
- Select Actions and then select Remove suppressions .
The Remove suppressions dialog box opens, listing the selected alarms along with their suppressions.
- Review the listed suppressions and then select Remove suppressions .
The list is updated.
-
