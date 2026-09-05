# Logging Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/metrics.htm
- Fetched: 2026-09-05 02:38 CDT

# Logging Metrics

Review available Monitoring metrics for the Logging service.

You can monitor the health, capacity, and performance of your logs and log groups by using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

This topic describes the metrics emitted by the Logging service in the`<oci_logging>`metric namespace.

Resources: Service and custom logs.

## Overview of the Logging Service Metrics

The Logging service metrics help you measure the number and type of connections between services in Oracle Cloud Infrastructure. You can use metrics data to diagnose and troubleshoot logging issues.

To view a default set of metrics charts in the Console, navigate to the log or log group you're interested in, and then click Metrics . You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

## Prerequisites

IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

## Available Metrics: oci_logging

The metrics listed in the following table are automatically available for any logs you create. You do not need to enable monitoring on the resource to get these metrics.

Logging service metrics include the following dimensions : logGroupId The OCID of the log group that the metrics apply to. logGroupName The name of the log group that the metrics apply to. logObjectId The OCID of the log object that the metrics apply to. logObjectName The name of the log object that the metrics apply to. logSourceService The log source service that the metrics apply to (for example, "custom" or "flowlogs"). namespace The namespace that the metrics apply to. resourceId The OCID of the resource that the metrics apply to.

Metric Metric Display Name Unit Description Dimensions
`BytesIngested`Bytes Ingested Bytes

Number of bytes read from the source.

`resourceId`

`logObjectId`

`logObjectName`

`logGroupId`

`logGroupName`

`logSourceService`
`SearchSuccess`Search Success Count Number of successful search queries issued by the user.

`resourceId`

`logObjectId`

`logObjectName`

`logGroupId`

`logGroupName`

`logSourceService`
`CustomLogAcceptanceRate`Custom Log Acceptance Rate Count The throttling rate for[custom logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/custom_logs.htm). See[Viewing the Custom Logs Acceptance Rate](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/viewing_custom_logs_acceptance_rate.htm)for more information.`resourceId`

## Using the Console

[To view metric charts for a single log](https://docs.oracle.com/en-us/iaas/Content/Logging/metrics.htm#)

- On the Logs list page, select the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm).

The log's details page opens.
- 

Select Metrics .

The Metrics page displays a default set of charts for the log.

[To view metric charts for a single log group](https://docs.oracle.com/en-us/iaas/Content/Logging/metrics.htm#)

- On the Logs list page, select the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm).

The log's details page opens.
- Select the Monitoring tab.

You can see a default set of charts for the log group.

[To view default metric charts for multiple logs](https://docs.oracle.com/en-us/iaas/Content/Logging/metrics.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- 

For Metric namespace , select oci_logging .

The Service Metrics page displays a default set of charts for the selected metric namespace. For more information about the emitted metrics, see[Available Metrics: oci_logging](https://docs.oracle.com/en-us/iaas/Content/Logging/metrics.htm#metrics_table). You can also use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Using the API

Use the following APIs for monitoring:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
