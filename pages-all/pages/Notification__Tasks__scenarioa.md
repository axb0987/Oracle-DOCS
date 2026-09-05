# Scenario A: Automatically Resizing VMs
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm
- Fetched: 2026-09-05 02:49 CDT

# Scenario A: Automatically Resizing VMs

Set up automatic resizing for virtual machines (VMs) that exceed memory by using Notifications, Functions, and Monitoring services.

This scenario involves writing a[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm)to resize VMs and creating an alarm that sends a message to that function. When the alarm fires, the Notifications service sends the[alarm message](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)to the destination topic, which then fans out to the topic's subscriptions. In this scenario, the topic's subscriptions include the function as well as your email address and an SMS phone number. The function is invoked on receipt of the alarm message.
Note  
  

The Notifications service has no information about a function after it's invoked. For details, see the troubleshooting information in[Function Not Invoked or Run](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/troubleshootingnotifications.htm#fxno).

[

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're a member of the Administrators group, you already have the required access to execute this scenario. Otherwise, you need access to[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Authenti),[Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#Authenti), and[Functions](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm#requiredpolicy). You must have`FN_INVOCATION`permission against the function to be able to add the function as a subscription to a topic. To resize VMs, the function must be authorized to update compute instances. To authorize your function for access to other Oracle Cloud Infrastructure resources, such as compute instances, include the function in a dynamic group and create a policy to grant the dynamic group access to those resources. For more information, see[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm).

## Task 1: Create and Authorize Your Function

Once you[create your function](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm)to resize VMs using your preferred SDK and authorize your function to access VMs (include the function in a dynamic group and grant that dynamic group access), all other scenario steps can be completed in the Console. Alternatively, you can use the Oracle Cloud Infrastructure CLI or API, which lets you execute the individual operations yourself.

For more information about authorizing functions to access other Oracle Cloud Infrastructure resources, see[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm).

[Function code sample](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)

Note  
  
For this code sample, we recommend handling idempotency via a database.

The following code sample is for a function to resize VMs. For instructions on creating and deploying functions, see[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm).

```

```

[Include your function in a dynamic group](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)

Find and note your function OCID (format is`ocid1.fnfunc.oc1.iad.exampleuniqueID`), then specify the following rule in the relevant dynamic group :

```

```

[Create a policy to grant the dynamic group access to VMs (compute instances)](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)

Add the following policy :

```

```

## Task 2: Create the Topic

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- 

Note  
  
Another Console workflow for this scenario involves creating a new topic and the first subscription when you[create the alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm), then[creating additional subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/create-subscription.htm)in that topic.

- Open the Create Topic panel: On the Topics list page, select Create topic . If you need help finding the list page, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- For Name , type the following: Alarm Topic
- Select Create .
- 

Use the[oci ons topic create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/topic/create.html)command and required parameters to create a topic:

```

```

Example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateTopic](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/CreateTopic)operation to create a topic.

Example:
```

```

## Task 3: Create the Subscriptions

Your function must be deployed before creating the function subscription.

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- 

- Select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#create-topic)(example name was Alarm Topic ): On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- Create the function subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select Function .
- Fill in the remaining fields.

Field Description
Function Compartment Select the compartment containing the function.
Function Application Select the application containing the function.
Function Select the function.
- Select Create .
No confirmation is needed for new function subscriptions.
- Create the SMS subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select SMS .
- Fill in the remaining fields.

Field Description
Country Select the country for the phone number. See[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm#prerequisites).
Phone Number Enter the phone number, using[E.164 format](https://www.itu.int/rec/T-REC-E.164/en).
- Select Create .
- Confirm the new SMS subscription: Follow the instructions[received on the phone](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm#sms).
- Create the email subscription.
- Open the Create Subscription panel: In the detail page for the topic, select Create Subscription .
The Create Subscription panel opens.
- For Protocol , select Email .
- Fill in the remaining fields.

Field Description
Email Type an email address.
- Select Create .
- [Confirm the new email subscription:](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)Open the email and navigate to the confirmation URL.
- 

Note  
  
After creating the SMS and email subscriptions,[confirm them](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create each subscription:

```

```

Function subscription example:

```

```

SMS subscription example:

```

```

Email subscription example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Note  
  
After creating the SMS and email subscriptions,[confirm them](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm).

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create each subscription.

Function subscription example:
```

```

SMS subscription example:
```

```

Email subscription example:
```

```

## Task 4: Create the Alarm

For help with troubleshooting, see[Troubleshooting Notifications](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#)
- 

- Open the Create Alarm page.
- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
- 

Select Create Alarm .
- For Alarm name , type the following: VM Memory Alarm
- 

Under Metric description , select the metric, interval, and statistic.

Field Example value for this scenario
Compartment Select the compartment that contains the VM that you want to automatically resize.
Metric namespace oci_computeagent
Metric name MemoryUtilization
Interval 1m
Statistic Max
- 

Under Trigger rule , set up the alarm threshold.

Field Example value for this scenario
Operator greater than
Value 90
Trigger delay minutes 1
- Under Notifications , Destinations , select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#create-topic).

Field Example value for this scenario
Destination Service[Notifications Service
Compartment Select the compartment that contains[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#create-topic).
Topic Select[the topic that you created earlier](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/scenarioa.htm#create-topic).
- 

Select Save alarm .
- 

Use the[oci monitoring alarm create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/create.html)command and required parameters to create an alarm:

```

```

Example:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[CreateAlarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm/CreateAlarm)operation to create an alarm.

Example:
```

```
