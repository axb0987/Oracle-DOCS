# Function Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm
- Fetched: 2026-09-05 02:07 CDT

# Function Metrics

Find out about the metrics emitted by OCI Functions in the oci_faas metric namespace.

You can monitor the health, capacity, and performance of functions you've deployed to OCI Functions by using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

This topic describes the metrics emitted by the metric namespace`oci_faas`(the OCI Functions service).

Resources: functions

## Overview of the OCI Functions Service Metrics

OCI Functions monitors function execution, and collects and reports metrics such as:
- The number of times a function is invoked.
- The length of time a function runs for.
- The number of requests to invoke a function that failed with an error response (including the error code and error message).
- The number of requests to invoke a function that returned a '429 Too Many Requests' error in the response (known as 'throttled function invocations').
- The amount of memory that is allocated for concurrent function execution and for provisioned concurrency (see[Monitoring Memory Usage and Availability for OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/../Tasks/functionsmonitoringcapacityusage.htm)).

While frequency varies by metric, default service metrics typically have a frequency of 60 seconds (that is, at least one data point posted per minute).

## Prerequisites

IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

For more information about the policy statement required to access metrics emitted by OCI Functions, see[Policy Statements to Give OCI Functions Users Access to Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/../Tasks/functionscreatingpolicies.htm#userfunctionpolicy).

## Available Metrics: oci_faas

The metrics listed in the following tables are automatically available for any functions you create. You do not need to enable monitoring on the resource to get these metrics.

OCI Functions metrics include the following dimensions: APPLICATIONID The OCID of the application containing functions. APPLIATIONSHAPE The architecture of the application. COMPARTMENTID The OCID of the compartment containing the application. DESTINATIONID The identifier of the destination for invocation records. Detached invocations only. DESTINATIONTYPE The type of destination for invocation records (one of Success or Failure). Detached invocations only. ERRORMESSAGE The error details if an invocation record is not delivered successfully. Detached invocations only. INVOKETYPE The way in which the function was invoked (one of Sync or Detached). This dimension is only available in some commercial realms. RESOURCEDISPLAYNAME The name of the application containing the function, and the name of the function. RESOURCEID The OCID of the function. RESOURCENAME The name of the resource to which the metric applies (application, or application and function). RESPONSETYPE The response when a function is invoked (one of Success, Error, or Throttled). STATUS The HTTP status code of the delivery of an invocation record, received from the destination (for example, 200). Detached invocations only. USERTENANCYID The OCID of the tenancy that invoked the function.

Metric Metric Display Name Unit Description Dimensions
`AllocatedProvisionedConcurrency`Functions Allocated Provisioned Concurrency megabytes Memory consumed by provisioned concurrency slots.`applicationId`

`compartmentId`

`resourceId`

`resourceName`
`AllocatedTotalConcurrency`Functions Allocated Concurrency megabytes Total concurrent memory allocated.`applicationShape`

`compartmentId`

`resourceId`

`resourceName`
`FunctionDetachedDeliveries`Function Detached Invoke deliveries count Total number of function detached invoke deliveries

`resourceId`

`resourceName`

`responseType`

`applicationId`

`destinationType`

`destinationId`

`status`

`errorMessage`
`FunctionExecutionDuration`Function Duration ms Total function execution duration. Expressed in milliseconds.`applicationId`

`invokeType`

`resourceDisplayName`

`resourceId`

`userTenancyId`
`FunctionInvocationCount`Function Invocations count Total number of function invocations.`applicationId`

`invokeType`

`resourceDisplayName`

`resourceId`

`userTenancyId`
`FunctionResponseCount`

This metric is used in the following default metric charts:

Errors (with`responseType = "Error"`)

Throttles (with`responseType = "Throttled"`) count Total number of function responses.`applicationId`

`invokeType`

`resourceDisplayName`

`resourceId`

`userTenancyId`

`responseType`Additionally, when`responseType = "Error"`, the following dimensions are available for individual functions:

`ErrorCode`

`ErrorMessage`

## Using the Console

[To view default metric charts for a single function](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#)

- On the Applications list page, select the application containing the function for which you want to view metrics. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/../Tasks/list-applications.htm).
- Select the Functions tab and select the name of the function for which you want to view metrics.
- 

Select the Monitoring tab.

The Metrics section displays a chart for each metric that is emitted by the metric namespace for OCI Functions. For more information about the emitted metrics, see[Available Metrics: oci_faas](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#Availabl).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[Not seeing the function metrics data you expect?](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#)

If you don't see the metrics data for a function that you expect, see the following possible causes and resolutions.

Problem Possible Cause Resolution
Missing functions: A function I invoked is missing from the Invocations chart. The chart range (time period or x-axis window) does not cover the time of invocation. Adjust the chart range or time period as necessary.
Gaps in metrics data: The chart line is discontinuous. I want to see data in the charts as a continuous line over time, but the line has gaps in it. No metrics data exist in the times indicated by the gaps. Smooth out the display by increasing the chart interval to see if gaps are removed.
Empty charts: The Errors and Throttles charts never show data. No metrics data exists for these charts in the specified chart range. No errors have occurred, and no requests have been throttled. Empty Errors and Throttles charts are expected. Not applicable.
Throttles data: The Throttles chart shows data. What should I do? Data in the Throttles chart indicates at least one request to invoke a function returned a '429 Too Many Requests' error in the response. Resubmit the throttled invocation requests. Submit future invocation requests less frequently.

[To view default metric charts for all functions in an application](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#)

- On the Applications list page, select the application for which you want to view function metrics. If you need help finding the list page or the application, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/../Tasks/list-applications.htm).
- 

Select the Monitoring tab.

The Metrics section displays a chart for each metric that is emitted by the metric namespace for OCI Functions. For more information about the emitted metrics, see[Available Metrics: oci_faas](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#Availabl).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[To view default metric charts for all the functions in all the applications in a compartment](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- Select the region you're using with OCI Functions.

We recommend that you use the same region as the Docker registry that's specified in the Fn Project CLI context. See[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/../Tasks/functionscreatefncontext.htm).
- 

Select the compartment containing the applications for which you want to view function metrics.
- 

For Metric namespace , select oci_faas .

The Service Metrics page dynamically updates the page to show charts for each metric that is emitted by the selected metric namespace. For more information about the emitted metrics, see[Available Metrics: oci_faas](https://docs.oracle.com/en-us/iaas/Content/Functions/Reference/functionsmetrics.htm#Availabl).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
