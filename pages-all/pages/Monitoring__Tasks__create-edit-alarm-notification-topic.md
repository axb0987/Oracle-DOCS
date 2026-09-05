# Selecting a Topic as the Notification Destination for an Alarm
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm
- Fetched: 2026-09-05 02:38 CDT

# Selecting a Topic as the Notification Destination for an Alarm

Select the topic to send alarm notifications to.

Note  
  
If you expect more than 60 messages per minute,[select a stream as notification destination](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm)(instead of a topic). For more information, see[Alarm Message Limits](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits-alarm-messages).

See also[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm#)
- 

- On the Alarm Definitions list page, select the alarm that you want to work with. If you need help finding the list page or the alarm, see[Listing Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-alarm.htm).
- Go to Actions and then select Edit alarm .
- To select an existing topic, provide the following values in the Destination area under Define alarm notifications . Then, skip to step 7.

- Destination service : Select Notifications .
- Compartment : Select the compartment that contains the topic that you want. This compartment can be a different compartment than the one specified for the alarm and metric. By default, the first accessible compartment is selected.
- Topic : Select an existing topic that you want to send the notifications to.
- To create a topic and subscription, provide the following values in the Destination area under Define alarm notifications :

- Destination service : Select Notifications .
- Compartment : Select the compartment that you want to store the new topic in. This compartment can be a different compartment than the one specified for the alarm and metric. By default, the first accessible compartment is selected.
- Create a topic : Select this link to display fields under Create a new topic and subscription for a new topic and subscription.
- Topic name : Enter a user-friendly name for the topic. For example, enter: "Operations Team" for a topic used to notify operations staff of firing alarms.
- Topic description : Enter a description of the new topic.
- Subscription protocol : See the next step.
- For Subscription protocol , select the type of subscription that you want to create, then enter values in the associated fields. For details about each subscription type, select the links.

- [Email : Enter an email address.
- [Function : Select the compartment and application that contain the function that you want, and then select the function.
- [HTTPS (Custom URL) : Enter the URL that you want to use as the endpoint.
- [PagerDuty : Enter the integration key portion of the URL for the PagerDuty subscription. (The other portions of the URL are hard-coded.)
- [Slack : Enter the Slack endpoint, including the webhook token.
- [SMS : Select the country for the phone number, and then enter the phone number, using[E.164 format](https://www.itu.int/rec/T-REC-E.164/en). Example: +14255550100
- Update any other values for the alarm, as needed.
For more information about the fields, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- Select Save alarm .
- 

Use the[oci monitoring alarm update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/update.html)command and required parameters to update an alarm. Use the`--destinations`parameter to select a topic as the alarm's notifications destination.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[UpdateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/UpdateAlarm)operation to update an alarm. Use the`destinations`
