# API Gateway Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm
- Fetched: 2026-09-05 01:37 CDT

# API Gateway Metrics

Find out about the metrics emitted by API Gateway.

You can monitor the health, capacity, and performance of API gateways and API deployments managed by the API Gateway service using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

This topic describes the metrics emitted by the API Gateway service in the`oci_apigateway`metric namespace.

Resources: gateways

## Overview of the API Gateway Service Metrics

The API Gateway service metrics help you measure the connections to API gateways, and the quantity of data received and sent by API gateways. You can use metrics data to diagnose and troubleshoot API gateway and API deployment issues.

While frequency varies by metric, default service metrics typically have a frequency of 60 seconds (that is, at least one data point posted per minute).

To view a default set of metrics charts in the Console, navigate to the API gateway you're interested in, and then select Metrics . You also can use the Monitoring service to create custom queries. See[Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).

## Prerequisites

IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

## Available Metrics: oci_apigateway

The metrics listed in the following tables are automatically available for any API gateways you create. You do not need to enable monitoring on the resource to get these metrics.

API Gateway metrics include the following dimensions: RESOURCEID The OCID of the resource to which the metrics apply. RESOURCENAME The name of the resource to which the metrics apply. DEPLOYMENTID The OCID of the API deployment. DEPLOYMENTNAME The name of the API deployment. ROUTE The route path for API calls to the back-end service. HTTPMETHODTYPE The HTTP methods of incoming connections accepted by the back-end service (such as GET, HEAD, POST, PUT, DELETE). HTTPSTATUSCODE The HTTP response status code received from the API gateway (such as 200, 201, 502, 504). HTTPSTATUSCATEGORY The category of the HTTP response status code received from the API gateway (such as 2xx, 3xx, 4xx, 5xx). BACKENDNAME The name of the back end (derived from the name of the back end rule) to which an API gateway routes requests. BACKENDTYPE The type of back end to which an API gateway routes requests to a back-end service (such as HTTP_BACKEND, ORACLE_FUNCTIONS_BACKEND, STOCK_RESPONSE_BACKEND). BACKENDHTTPSTATUSCODE The HTTP response status code received from the back end (such as 200, 201, 502, 504). BACKENDHTTPSTATUSCATEGORY The category of the HTTP response status code received from the back end (such as 2xx, 3xx, 4xx, 5xx). RESPONSECACHERESULT The action taken by the response cache (one of HIT, MISS, BYPASS). ENTITLEMENTNAME The name of the entitlement. SUBSCRIBERID The OCID of the subscriber. SUBSCRIBERNAME The name of the subscriber. CLIENTNAME The name of a subscriber's client. ACTION The action taken if the maximum number of requests in the entitlement's quota's time period was exceeded. USAGEPLANID The OCID of the usage plan. USAGEPLANNAME The name of the usage plan.

Metric Metric Display Name Unit Description Dimensions
`BytesReceived`Bytes Received Bytes Number of bytes received by the API gateway from API clients.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`

`backendType`
`BytesSent`Bytes Sent Bytes Number of bytes sent by the API gateway to API clients.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`

`backendType`
`HttpRequests`API Requests count Number of incoming API client requests to the API gateway.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`backendType`

`backendName`
`HttpResponses`API Responses Count Number of http responses that the API gateway has sent back.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`

`backendType`

`backendName`
`BackendHttpResponses`Backend Responses Count Count of the HTTP responses returned by the back-end services.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`

`backendType`

`backendName`

`backendHttpStatusCode`

`backendHttpStatusCategory`
`Latency`Gateway Latency Seconds Time taken for a request to be processed and its response to be sent. This is calculated from the time the API gateway receives the first byte of an HTTP request to the time when the response send operation is completed.

Latency is the sum of Integration Latency and Internal Latency .

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`

`backendType`
`IntegrationLatency`Integration Latency Seconds

Time spent by the API gateway calling external integrations (such as HTTP backends, OCI Functions, DNS, and authentication servers).

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`

`backendType`
`InternalLatency`Internal Latency Seconds Time spent internally in the API gateway to process the request.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`httpMethodType`

`httpStatusCode`

`httpStatusCategory`
`ResponseCacheAction`Response Cache Actions Count The action taken by the response cache.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`

`responseCacheResult`
`ResponseCacheAvailability`Response Cache Availability Count Availability of the response cache as seen by the API gateway.

`resourceId`

`resourceName`
`ResponseCacheLatency`Response Cache Latency Milliseconds Total time taken for connect, read, and store operations on the response cache.

`resourceId`

`resourceName`

`deploymentId`

`deploymentName`

`route`
`UsagePlanRequests`Usage Plan Requests Sum Number of requests to a given entitlement. Emitted per request.

`resourceId`

`resourceName`

`entitlementName`

`subscriberId`

`subscriberName`

`clientName`

`action`
`SubscriberRequests`Subscriber Requests Sum Number of requests made by a subscriber. Emitted per request.

`resourceId`

`resourceName`

`clientName`

`usagePlanId`

`usagePlanName`

`entitlementName`

`action`
`SubscriberQuotaProportionUsed`Subscriber Quota Proportion Used Mean Proportion of an entitlement's quota that has been consumed by a subscriber. Emitted per request.

Calculated as:`<current number of requests this period> / <quota for entitlement this period>`

`resourceId`

`resourceName`

`clientName`

`usagePlanId`

`usagePlanName`

`entitlementName`
`SubscriberRateLimitProportionUsed`Subscriber Rate Limit Proportion Used Mean Proportion of an entitlement's rate limit that has been consumed by a subscriber. Emitted per request.

Calculated as:`<current number of requests this period> / <rate limit for entitlement this period>`

`resourceId`

`resourceName`

`clientName`

`usagePlanId`

`usagePlanName`

`entitlementName`

## Using the Console

[To view default metric charts for a single API gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm#)

- On the Gateways list page, select the API gateway for which you want to view metrics. If you need help finding the list page or the API gateway, see[Listing API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/../Tasks/apigatewaylisting.htm).
- 

Select the Monitoring tab.

The Metrics section displays a chart for each metric that is emitted by the metric namespace for API Gateway. For more information about the emitted metrics, see[Available Metrics: oci_apigateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm#Availabl).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

[Not seeing the API gateway metrics data you expect?](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm#)

If you don't see the metrics data for an API gateway that you expect, see the following possible causes and resolutions.

Problem Possible Cause How to check Resolution
I called an API deployed on an API gateway but the HTTP Requests chart doesn't show the API call. You might have called the API outside the time period covered by the HTTP Requests chart. Confirm the Start Time and End Time cover the period when you called the API. Adjust the Start Time and End Time as necessary.
I called an API deployed on an API gateway but the HTTP Requests chart doesn't show the API call, even though I called the API between the Start Time and End Time . Although you called the API between the Start Time and End Time , the x-axis (window of data display) might be excluding the API call. Confirm the x-axis (window of data display) covers the period when the API was called. Adjust the x-axis (window of data display) as necessary.
I want to see data in the charts as a continuous line over time, but the line has gaps in it. This is expected behavior. If there is no metrics data to show in the selected interval, the data line is discontinuous. Increase the Interval (for example, from 1 minute to 5 minutes, or from 1 minute to 1 hour). Adjust the Interval as necessary.

[To view default metric charts for all the API gateways in a compartment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .
- Select the region you are using with API Gateway
- 

Select the compartment containing the API gateways for which you want to view metrics.
- 

For Metric namespace , select oci_apigateway .

The Service metrics page dynamically updates the page to show charts for each metric that is emitted by the selected metric namespace. For more information about the emitted metrics, see[Available Metrics: oci_apigateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm#Availabl).

For more information about monitoring metrics and using alarms, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see[Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
- [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms
- [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)
