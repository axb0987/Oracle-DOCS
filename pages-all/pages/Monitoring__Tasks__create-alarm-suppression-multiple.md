# Suppressing Multiple Alarms
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression-multiple.htm
- Fetched: 2026-09-05 02:38 CDT

# Suppressing Multiple Alarms

Temporarily stop notifications from alarms by applying a suppression to selected alarms in the Console. For example, use a suppression to suspend notifications from selected alarms.

This feature is available in the Console only.

Tagging alarm suppressions isn't available in the Console. To tag a new alarm suppression, use the SDK, CLI, or API. See[Suppressing a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm).
Note  
  
A dimension-specific suppression can't be added to multiple alarms at the same time.

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
The page lists alarms in the indicated compartment. Suppression status is indicated for each alarm.
- Select the checkbox for each alarm that you want to suppress.
- Select Actions and then select Add suppressions .
- In the Suppress Alarms dialog box, provide the following values:

- Start time : The date and time to start the suppression. The default is the current time. The value must be within 90 days of the current time. If you're editing an existing suppression, the field shows the start time of that suppression.
- End time : The date and time to end the suppression. The default is one hour from the current time. The value must be within 90 days of the current time. If you're editing an existing suppression, the field shows the end time of that suppression.
- Suppression description : Optional description of the suppression.
- Select Apply suppressions .
The new suppressions are listed in the dialog box.
-
