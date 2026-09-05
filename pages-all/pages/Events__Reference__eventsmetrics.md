# Events Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventsmetrics.htm
- Fetched: 2026-09-05 02:02 CDT

# Events Metrics

Understand the metrics emitted by the metric namespace oci_cloudevents (the Events service).

You can monitor performance of your rules by using[metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics),[alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). This topic describes the metrics emitted by the metric namespace`oci_cloudevents`(the Events service).

Resources: rules. Also measures data for events, which are not resources.

## Prerequisites

IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

## Overview of the Events Service Metrics

You create rules that specify which events should be delivered to other services for processing. This delivery creates the automation in your tenancy. A rule identifies an event pattern to match and specifies other services to deliver matching events to. Metrics help you measure the success of the rules you create (in terms of pattern matching and delivery) and the quality and scope of the emitted events in your tenancy. For more information, see[Overview of Events](https://docs.oracle.com/en-us/iaas/Content/Events/Reference/../Concepts/eventsoverview.htm).

## Available Metrics: oci_cloudevents

The metrics listed in the following table are automatically available for rules you create. You do not need to enable monitoring to get these metrics.

Each metric includes one or more of the following dimensions: RESOURCEID The OCID of the rule or compartment to which the metric applies. EVENTTYPE The type of event emitted by a resource. RESOURCEDISPLAYNAME The name of the rule. ACTIONTYPE One or more of the following types of resources that receives an event from the Events service.

- [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)
- [Streaming](https://docs.oracle.com/iaas/Content/Streaming/home.htm)
- [Functions](https://docs.oracle.com/iaas/Content/Functions/home.htm)

Metric Metric Display Name Unit Description Dimensions
`PublishedEvents`Events Emitted`count`Total number of events emitted by resources in a compartment.

`eventType`

`resourceId`
`MatchedEvents`Events Matched`count`If you view the default chart from a rule, this metric provides the total number of events matched for the rule. If you view the chart from the Service Metrics page, this metric gives a total number of matched events for all the rules in a compartment.

`resourceDisplayName`

`resourceId`
`DeliverySucceedEvents`Events Delivered`count`If you view the default chart from a rule, this metric provides the total number of successful deliveries to actions for the rule. If you view the chart from the Service Metrics page, this metric gives a total number of successful deliveries to actions for all the rules in a compartment.

`actionType`

`resourceDisplayName`

`resourceId`
`DeliveryFailedEvents`Delivery Failure`count`If you view the default chart from a rule, this metric provides the total number of unsuccessful deliveries to actions for the rule. If you view the chart from the Service Metrics page, this metric gives a total number of unsuccessful deliveries to actions for all the rules in a compartment.

## Using the Console

[To view default metric charts for a rule](https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventsmetrics.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- Select the Compartment that contains the rule you want to view, and then select the rule's name.
- Select the Metrics tab. The Metrics page displays a default set of charts for the current rule.

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[To view default metric charts for a region](https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventsmetrics.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- The Metrics page displays a default set of charts for your tenancy and region.

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Using the API

Use the following APIs for monitoring:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
