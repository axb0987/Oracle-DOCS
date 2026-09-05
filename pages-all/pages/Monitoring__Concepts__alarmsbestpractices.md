# Best Practices for Your Alarms
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/alarmsbestpractices.htm
- Fetched: 2026-09-05 02:38 CDT

# Best Practices for Your Alarms

Read about best practices for alarms.

## Create a Set of Alarms for Each Metric

For each metric emitted by resources,[create alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/managingalarms.htm)that define the following resource behaviors:
- At risk. The resource is at risk of becoming inoperable, as indicated by metric values.
- Nonoptimal. The resource is performing at nonoptimal levels, as indicated by metric values.
- Resource is up or down. The resource is either not reachable or not operating.

The following examples use the`CpuUtilization`metric emitted by[the oci_computeagent metric namespace](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm). This metric monitors the utilization of the compute instance and the activity level of any services and applications running on the instance.`CpuUtilization`is a key performance metric for a cloud service because it indicates CPU usage for the compute instance and it can be used to investigate performance issues. To learn more about CPU usage, see the following URL:[https://en.wikipedia.org/wiki/CPU_time](https://en.wikipedia.org/wiki/CPU_time).

### At-Risk Example

A typical at-risk threshold for the`CpuUtilization`metric is any value greater than 80 percent. A compute instance breaching this threshold is at risk of becoming inoperable. Often the cause of this behavior is one or more applications consuming a high percentage of the CPU.

In this example, you decide to notify the operations team immediately, setting the severity of the alarm as "Critical" because repair is required to bring the instances back to optimal operational levels. You configure alarm notifications to the responsible team by both PagerDuty and email, requesting an investigation and appropriate fixes before the instances go into an inoperable state. You set repeat notifications every minute. When someone responds to the alarm notifications, you temporarily stop notifications using the best practice of suppressing the alarm . When metrics return to optimal values, you remove the suppression.

### NonOptimal Example

A typical nonoptimal threshold for the`CpuUtilization`metric is from 60 to 80 percent. When the metric values for a compute instance are within this range, the instance exceeds the optimal operational range.

In this example, you decide to notify the appropriate individual or team that an application or process is consuming more CPU than usual. You configure a[threshold alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-threshold.htm)to notify the appropriate contacts, setting the severity of the alarm as "Warning," as no immediate actions are required to investigate and reduce the CPU. You set notification to email only, directed to the appropriate developer or team, with repeat notifications every 24 hours to reduce email notification noise.

### Resource is Up or Down Example

A typical indicator of resource availability is a five-minute absence of the`CpuUtilization`metric. A compute instance breaching this threshold is either not reachable or not operating. The resource might have stopped responding, or it might have become unavailable because of connectivity issues.

In this example, you decide to notify the operations team immediately, setting the severity of your[absence alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-absence.htm)as "Critical" because repair is required to bring the instances online. You configure alarm notifications to the responsible team by both PagerDuty and email, requesting an investigation and a move of the workloads to another available resource. You set repeat notifications every minute. When someone responds to the alarm notifications, you temporarily stop notifications using the best practice of[suppressing the alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-suppression.htm). When the`CpuUtilization`metric is again detected from the resource, you remove the suppression.

Sometimes you want to get notified whenever an event occurs, such as a shutdown of a database instance. In this scenario, set repeat notifications to zero minutes to create an event-based alarm. For instructions, see[Getting Event-Based Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/update-alarm-event.htm).

## Select the Correct Alarm Interval for Your Metric

Select an alarm interval based on the frequency at which the metric is emitted. For example, a metric emitted every five minutes requires a 5-minute alarm interval or greater. Most metrics are emitted every minute, which means most metrics support any alarm interval. To determine valid alarm intervals for a specific metric, check the[relevant service's metric reference](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices).

## Suppress Alarms During Investigations

When a team member responds to an alarm, suppress notifications during the effort to investigate or mitigate the issue. Temporarily stopping notifications helps to avoid distractions during the investigation and mitigation. Remove the suppression when the issue has been resolved. For instructions, see[Suppressing a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-suppression.htm)and[Suppressing Multiple Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-suppression-multiple.htm).

## Routinely Tune Your Alarms

On a regular basis, such as weekly, review your alarms to ensure optimal configuration. Calibrate each alarm's threshold, severity, and notification details, including method, frequency, and targeted audience.
[

Optimal alarm configuration addresses the following factors:
- Criticality of the resource.
- Appropriate resource behavior. Assess behavior singly and within the context of the service ecosystem. Review metric value fluctuations for a specific period of time and then adjust thresholds as needed.
- Acceptable notification noise. Assess the notification method (for example, email or PagerDuty), the appropriate recipients, and the frequency of repeated notifications.

The following table shows an example alarm calibration.

Threshold CPU % Severity Notification Method Frequency Targeted Audience
&gt;80% Critical PagerDuty + Email 1 minute Compute, Ops, and Customer Communications
&gt;60% &amp; &lt;80% Warning Email Once per day Compute + Ops

For instructions, see[Updating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/update-alarm.htm)
