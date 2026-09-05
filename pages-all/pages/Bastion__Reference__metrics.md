# Bastion Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/metrics.htm
- Fetched: 2026-09-05 01:42 CDT

# Bastion Metrics

You monitor the health, capacity, and performance of Oracle Cloud Infrastructure Bastion by using metrics, alarms, and notifications.

This topic describes the metrics emitted by the metric namespace`oci_bastion`.

## Overview

Metrics help you monitor bastions and sessions. Namespace A namespace is a container for metrics. The namespace identifies the service sending the metrics. The namespace for Bastion is`oci_bastion`. Metrics Metrics are the fundamental concept in telemetry and monitoring. Metrics define a time-series set of datapoints. Each metric has a namespace, metric name, compartment identifier, one or more dimensions, and a unit of measure. Each datapoint has a timestamp, value, and count associated with it. Dimensions A dimension is a key-value pair that defines the characteristics associated with the metric. For example,`resourceId`is the OCID of the resource that was scanned. Statistics Statistics are metric data aggregations over specified periods of time. Aggregations are done using the namespace, metric name, dimensions, and the data point unit of measure within the time period specified. Alarms Alarms are used to automate operations monitoring and performance. An alarm tracks changes that occur over a specific time period and performs one or more defined actions, based on the rules defined for the metric.

## Required IAM Policy

To monitor resources in Oracle Cloud Infrastructure, you must be given the required type of access in a policy (IAM) written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool.

The policy must give you access to the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you were granted and which compartment you are supposed to work in.

For more information on user authorizations for monitoring, see the Authentication and Authorization section for the related service:[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Authenti)or[Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#Authenti).

## Available Metrics

Bastion metrics include the following dimensions.
- `resourceId`: The OCID of the bastion resource.
- `osUserName`: The operating system user name associated with a session on the bastion.
- `sessionType`: The type of session: Managed SSH or SSH Port Forwarding. See[Session Types](https://docs.oracle.com/en-us/iaas/Content/Bastion/Reference/../Concepts/bastionoverview.htm#session_types).

Metric Metric Display Name Unit Description
`activeSessions`Active Sessions count

Current number of active sessions on a bastion.

This metric is updated every 5 minutes.

## Using the Console

View the metric charts for Bastion.

- In the Console, open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- For Compartment , select the compartment that contains the bastion that you're interested in.
- For Metric namespace , select oci_bastion .

If you don't see an expected resource or metric, see[To investigate missing resources or metrics.](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm)
- Select a Metric name , Interval , and Statistic .

For example, select the metric named`activeSessions`and set Interval to 5 minutes.
- (Optional) To view the raw data points for the selected metric, select Show Data Table .

The Service Metrics page dynamically updates to show charts for each metric that's emitted by the selected metric namespace.

## Using the API

Use the following APIs for monitoring.
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)for notifications (used with alarms)

For information about using the API and signing requests, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm#Security_Credentials). For information about SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface)
