# Notifications Metrics Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/notificationmetrics-reference.htm
- Fetched: 2026-09-05 02:49 CDT

# Notifications Metrics Reference

Review information about metrics emitted by the metric namespace`oci_notification`(the Notifications service).

Resources: Not applicable. Measures data for messages, which aren't resources.

## Before You Begin

IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

The metrics in the`oci_notification`metric namespace are automatically available for messages you publish to topics. You don't need to enable monitoring on any resources to get these metrics.

## Available Metrics: oci_notification

Availability of service metrics (including dimensions) is governed by[Monitoring storage limits](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Storage). For a successful query of a metric or dimension to occur, that metric or dimension must be stored in Monitoring.

### Dimensions

Each metric includes a subset of the following dimensions : availabilityDomain The availability domain in which the associated topic resides. endpointType The[subscription protocol](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#concepts__subscriptiondefinition)of the endpoint used for the delivery attempt. region The region in which the associated topic resides. resourceId The OCID of the resource to which the metric applies. resultCode

The code of the result for a failed message, if the result code exists. The only value is`4702`, which indicates that the message was dropped because the email recipient was suppressed. To remove a recipient from the suppression list, open a[support request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
Note  
  
This dimension exists only when a message failed and a valid value is emitted. resultMessage

The explanation of the result for a failed message, if the result explanation exists. The only value is`Email subscription is suppressed`, which indicates that the message was dropped because the email recipient was suppressed. To remove a recipient from the suppression list, open a[support request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
Note  
  
This dimension exists only when a message failed and a valid value is emitted. subscriptionId

The OCID of the subscription.
Note  
  
This dimension exists only when a message failed and a valid value is emitted. topicDisplayName The friendly name of the associated topic .

### Descriptions

Following are descriptions of the Notifications service metrics:

Metric Metric Display Name Unit Description Dimensions
`DeliveredMessagesCount`Delivered Messages Count count Count of messages that Notifications successfully transmitted to endpoints (subscriptions in topics). See[Flow of Message Publication and Delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#Flow).

`availabilityDomain`

`endpointType`

`region`

`resourceId`

`topicDisplayName`
`DeliveredMessagesSize`Delivered Messages Size (Bytes) bytes Size of messages that Notifications successfully transmitted to endpoints (subscriptions in topics). See[Flow of Message Publication and Delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#Flow).

`availabilityDomain`

`endpointType`

`region`

`resourceId`

`topicDisplayName`
`FailedMessagesCount`Failed Messages Count count

Count of messages that Notifications could not transmit to endpoints (subscriptions in topics). See[Flow of Message Publication and Delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#Flow).

Note: This metric exists only when a message failed.

`availabilityDomain`

`endpointType`

`region`

`resourceId`

`resultCode`

`resultMessage`

`subscriptionId`

`topicDisplayName`
`FailedMessagesSize`Failed Messages Sizes (Bytes) bytes

Size of messages that Notifications could not transmit to endpoints (subscriptions in topics). See[Flow of Message Publication and Delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#Flow).

Note: This metric exists only when a message failed.

`availabilityDomain`

`endpointType`

`region`

`resourceId`

`resultCode`

`resultMessage`

`subscriptionId`

`topicDisplayName`
`PublishedMessagesCount`Published Messages Count count Count of messages in requests that Notifications received from the service or customer. See[Flow of Message Publication and Delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#Flow).

`availabilityDomain`

`region`

`resourceId`

`topicDisplayName`
`PublishedMessagesSize`Published Messages Size (Bytes)

bytes Size of messages in requests that Notifications received from the service or customer. See[Flow of Message Publication and Delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Reference/../Concepts/notificationoverview.htm#Flow).

`availabilityDomain`

`region`

`resourceId`

`topicDisplayName`
