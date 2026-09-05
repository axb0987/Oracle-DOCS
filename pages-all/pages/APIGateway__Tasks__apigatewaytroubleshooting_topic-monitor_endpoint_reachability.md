# How to monitor whether an API Gateway endpoint is actually reachable
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-monitor_endpoint_reachability.htm
- Fetched: 2026-09-05 01:39 CDT

# How to monitor whether an API Gateway endpoint is actually reachable

Find out how to troubleshoot problems monitoring the health and reachability of API gateways created with the API Gateway service.

Use this guidance when you need to monitor whether an API Gateway endpoint is reachable. API Gateway metrics show traffic, latency, and response patterns, but they do not provide a single built-in gateway-alive status metric. For endpoint liveness, use Health Checks with a deployed API path, and use API Gateway metrics to investigate traffic and failures.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

No direct reachability signal is available for an API Gateway endpoint.
- 

API Gateway metrics do not show a dedicated health status metric.
- 

Traffic volume, latency, and response-code trends do not confirm endpoint liveness.
- 

No OCI-native health check is configured for the API Gateway deployment endpoint.

## Possible Causes

Endpoint reachability and gateway metrics measure different parts of the request path:
- 

Health Checks indicate whether a deployed API path is reachable from the health check probe location.
- 

API Gateway metrics indicate how the gateway behaves after traffic reaches the gateway.
- 

A reachable gateway can still return increasing`4xx`or`5xx`responses.
- 

A gateway with little or no traffic can have few recent metric data points, which makes metrics alone a weak liveness signal.

## Configure a Health Check for Endpoint Liveness

Use Health Checks when you need a binary or near-binary signal that a deployed endpoint is reachable.

Select an API route that meets the following requirements:
- 

The route returns a predictable success response, such as`200`or`204`.
- 

The route does not trigger sign-in redirects.
- 

The route does not require per-user credentials or short-lived query parameters.
- 

The route does not perform a write operation or create a business-side effect.
- 

The route represents the API Gateway path that you want to monitor.

Before you create the health check, verify the route manually:
```

```

Create an OCI Health Check that targets the exact deployed endpoint that you verified. Use the health check for the following monitoring goals:
- 

Endpoint reachability.
- 

External availability checks.
- 

Alerts when the endpoint stops responding with the expected status code.

## Review API Gateway Metrics

Use API Gateway metrics to understand traffic and failure patterns after the endpoint is reachable. In Metrics Explorer, review the public API Gateway metrics in the`oci_apigateway`namespace.

Start with the following metrics and dimensions:
- 

`HttpResponses`,`httpStatusCode`, and`httpStatusCategory`.
- 

`BackendHttpResponses`,`backendHttpStatusCode`, and`backendHttpStatusCategory`.
- 

`Latency`,`IntegrationLatency`, and`InternalLatency`.
- 

`resourceId`,`deploymentId`, and`route`.

Use`HttpResponses`to review status codes returned by API Gateway. Use`BackendHttpResponses`to review status codes returned by back-end services.

## Interpret Monitoring Results

Use health check status and API Gateway metrics together to identify where the problem occurs:
- 

If the health check fails, the endpoint might be unreachable or unhealthy from the probe path.
- 

If the health check succeeds but`4xx`or`5xx`responses increase, the endpoint is reachable but requests are failing.
- 

If traffic is low and metrics show no recent data, the missing data does not prove that the gateway is unavailable.
- 

If reachability succeeds but latency increases, the gateway is reachable but request processing might be degraded.

## Fix Monitoring Gaps

Use the monitoring signal that matches the question that you need to answer:
- 

To monitor endpoint liveness, configure Health Checks for a deployed API route.
- 

To investigate response behavior, review API Gateway metrics.
- 

To monitor both availability and behavior, combine Health Checks with API Gateway metrics and alarms.
- 

To avoid false conclusions, do not rely on one API Gateway metric as a direct gateway-alive indicator.

## Verify Endpoint Monitoring

After you configure endpoint monitoring, verify the setup:
- 

Confirm that the selected API path returns the expected status code when you test it with`curl`.
- 

Confirm that the OCI Health Check can probe the endpoint successfully.
- 

Confirm that Metrics Explorer shows request and response trends for the gateway.
- 

Confirm that alarms distinguish endpoint reachability problems from response-code or latency problems.

## For More Information

For more information, see:
- 

[Health Checks](https://docs.oracle.com/iaas/Content/HealthChecks/home.htm)
- 

[Creating an HTTP Monitor](https://docs.oracle.com/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm)
- 

[API Gateway Metrics](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Reference/apigatewaymetrics.htm)
