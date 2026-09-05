# Monitoring Memory Usage and Availability for Provisioned Concurrency
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsmonitoringcapacityusage_topic-Monitoring-provisioned-concurrency.htm
- Fetched: 2026-09-05 02:09 CDT

# Monitoring Memory Usage and Availability for Provisioned Concurrency

Find out how to monitor the usage and availability of memory for provisioned concurrency by OCI Functions.

OCI Functions has a limit for the total amount of memory available for provisioned concurrency for all functions in a region. The limit is named provisioned-concurrency-mb, and specifies the maximum amount of memory that can be allocated for provisioned concurrency.

The provisioned-concurrency-mb memory limit has a default value, as shown in[Function Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Functions_Limits). The default value might have already been increased in your tenancy, perhaps in response to Support requests that were logged on previous occasions when memory capacity was exceeded.

You can use the Console to see the current value of the provisioned-concurrency-mb memory limit in a region (see[Viewing the Current Memory Limit for Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsmonitoringcapacityusage_topic-Monitoring-provisioned-concurrency.htm#functionsmonitoringcapacityusage_topic-Viewing-provisioned-concurrency-memory-limits)).

If OCI Functions needs more memory for provisioned concurrency to avoid initial latency when invoking functions, you can submit a request to increase the provisioned-concurrency-mb memory limit (see[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)).

Instead of waiting for the provisioned-concurrency-mb memory limit to be reached, and then addressing the requirement, you can use Oracle Cloud Infrastructure Monitoring and the`AllocatedProvisionedConcurrency`metric to monitor how much of the memory available for provisioned concurrency has been allocated. Note that the value of the`AllocatedProvisionedConcurrency`metric is the amount of allocated memory. The amount of memory that is actually used for provisioned concurrency is always less than, or equal to, the value of the`AllocatedProvisionedConcurrency`metric. For more information, see[Viewing the Amount of Memory Recently Allocated for Concurrent Function Execution](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsmonitoringcapacityusage_topic-Monitoring-concurrent-function-execution.htm#functionsmonitoringcapacityusage_topic-Viewing-concurrent-memory-usage).

You can also use the`AllocatedProvisionedConcurrency`metric to create an alarm to notify you if provisioned concurrency memory allocation passes a threshold that you define. For more information, see[Creating a provisioned concurrency memory allocation threshold alarm](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsmonitoringcapacityusage_topic-Monitoring-provisioned-concurrency.htm#functionsmonitoringcapacityusage_topic-Creating-provisioned-memory-usage-threshold-alarm).

## Viewing the Current Memory Limit for Provisioned Concurrency

To view the current memory limit for provisioned concurrency:
- 

Open the navigation menu and select Governance &amp; Administration . Under Tenancy Management , select Limits, Quotas and Usage .
- Select Functions from the Service list.
- 

Select the region from the Scope list.
- 

Select the root compartment from the Compartment list.

The provisioned-concurrency-mb limit shows the current memory limit for provisioned concurrency.
- (Optional) To request additional memory for provisioned concurrency, select the the Actions menu (three dots) beside the provisioned-concurrency-mb limit, select Open Support Request , and follow the instructions.

## Viewing the Amount of Memory Recently Allocated for Provisioned Concurrency

To view the amount of memory recently allocated for provisioned concurrency:
- 

Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Metrics Explorer .
- Use the Start time and End time fields to specify a representative time period to analyze.
- In the Query 1 panel, create a query as follows:
- For Compartment , select the root compartment.
- For Metric namespace , select oci_faas .
- Select the Advanced mode option and enter one of the following queries in the Query code editor :
- To show the total amount of memory allocated for provisioned concurrency for all the functions in the tenancy at 5 minute intervals, during the time period you specified, enter the following query:
```

```

- To show the total amount of memory allocated for provisioned concurrency for a specific function at 5 minute intervals, during the time period you specified, enter the following query:
```

```

where &lt;function-OCID&gt; is the OCID of a function. For example:
```

```

- 

Select Update Chart .

The chart updates, and shows the amount of memory that was allocated for provisioned concurrency, during the time period you selected.

## Creating a provisioned concurrency memory allocation threshold alarm

To create an alarm that fires when provisioned concurrency memory allocation exceeds a threshold that you define:
- 

Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
- Select Create Alarm .
- For Alarm name , enter a meaningful name for the alarm. Avoid entering confidential information.
- Select the Switch to Advanced Mode option.
- In the Metric details area, specify the metric to evaluate for the alarm, as follows:
- For Compartment , select the root compartment.
- For Metric namespace , select oci_faas .
- In the Trigger rule area, specify the condition that must be satisfied for the alarm to fire:
- Trigger delay minutes: Enter the number of minutes that the condition must be maintained for the alarm to fire.
- Alarm severity: Select the importance to be given to a notification that the alarm has fired.
- 

Query code editor: Enter a query to define a condition that, when satisfied, causes the alarm to fire, as follows:
- If you want the alarm to fire when memory allocation for provisioned concurrency exceeds a certain amount, enter the following query:
```

```

where &lt;memory-threshold&gt; is an amount of memory (in MiB) to use as the threshold, above which you want the alarm to fire.

For example, you might want an alarm to fire when the amount of memory allocated for provisioned concurrency exceeds 70% of the total memory available for provisioned concurrency. If the total memory for provisioned concurrency is 40 GB (that is, 40,960 MiB), enter the following query:
```

```

- If you want the alarm to fire when memory allocation for provisioned concurrency for a specific function exceeds a certain amount, enter the following query:
```

```

where:
- &lt;function-OCID&gt; is the OCID of the function
- &lt;memory-threshold&gt; is an amount of memory (in MiB) to use as the threshold, above which you want the alarm to fire.

For example, you might want an alarm to fire when the amount of memory allocated for provisioned concurrency for a single function exceeds 10% of the total memory available for provisioned concurrency. If the total memory available for provisioned concurrency is 40 GB (that is, 40,960 MiB), enter the following query:
```

```

- Select the Switch to Basic Mode option.
- In the Define alarm notifications area:
- For Destination , specify where notifications are sent when the alarm fires:
- Destination service: Select Notifications.
- Compartment: Select the compartment that contains the resources that emit the metrics evaluated by the alarm. The selected compartment is also the storage location of the alarm.
- Topic : The[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition)to use for notifications. Each topic supports one or more[subscription](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptiondefinition)protocols, such as PagerDuty. If a suitable topic does not already exist, select Create a topic and define a new topic. For reference, see[Creating a Basic Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).
- For Message grouping , select one of the following options:
- Group notifications across metric streams : Collectively track metric status across all metric streams. Send a message when metric status across all metric streams changes.
- Split notifications per metric stream : Individually track metric status by metric stream. Send a message when metric status for each metric stream changes. For an example, see[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/split-messages.htm).
- For Message Format , select one of the following options:
- Send formatted messages : Simplified, user-friendly layout. To view supported subscription protocols and message types for formatted messages (options other than Raw ), see[Friendly formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).
- Send Pretty JSON messages (raw text with line breaks) : JSON with new lines and indents.
- Send raw messages : Raw JSON blob.
- To suppress evaluations and notifications for a specified length of time, select Suppress notifications . This option is useful for avoiding alarm notifications during system maintenance periods. Specify a start time, end time, and an optional description. See[Best Practices for Your Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/alarmsbestpractices.htm)and[Suppressing a Single Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-suppression.htm).
- To save the alarm without starting to evaluate metric data, clear the Enable this alarm? check box.
-
