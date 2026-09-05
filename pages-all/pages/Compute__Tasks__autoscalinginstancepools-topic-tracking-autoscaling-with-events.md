# Tracking Autoscaling Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools-topic-tracking-autoscaling-with-events.htm
- Fetched: 2026-09-05 01:50 CDT

# Tracking Autoscaling Events

You can use the Events service to monitor autoscaling actions.

For example, an event is emitted when a scaling action occurs. For details about autoscaling event types and an example event, see[Autoscaling Event Types](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#computeevents__autoscaling).

For steps to create event notifications, see[Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm).

As an example, to create an event notification for a scaling action, when you[create the event rule](https://docs.oracle.com/iaas/Content/Events/Task/create-events-rule.htm), do the following:
- For Condition , select Event Type .
- For Service Name , select Compute .
- For Event Type , select Autoscaling Configuration - Scaling Action .

To filter notifications to scaling action errors:
- Click + Another Condition to create an additional condition.
- For Condition , select Attribute .
- For Attribute Name , select actionType .
- For Attribute Values , enter ERROR .

The possible attribute values for actionType are:
- SCALE_OUT
- SCALE_IN
- NO_ACTION
- ERROR
- LIMIT_EXCEEDED
- POWER_ACTION

You can also use the[audit logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm)to track autoscaling actions. If errors occur during autoscaling events, you can find error details in the these logs, and you can use the audit logs to[explore the details of autoscaling events](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm#audit_logs__export-audit)
