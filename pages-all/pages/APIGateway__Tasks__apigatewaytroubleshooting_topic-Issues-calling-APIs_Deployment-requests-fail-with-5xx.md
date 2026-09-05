# HTTP-5xx errors when API deployment is created successfully but requests fail
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm
- Fetched: 2026-09-05 01:38 CDT

# HTTP-5xx errors when API deployment is created successfully but requests fail

Find out how to troubleshoot HTTP-5xx errors when an API deployment is created successfully with the API Gateway service, but requests fail.

Having created an API deployment successfully, you might encounter HTTP-5xx errors when calling it.

## Invoking the API deployment fails with an HTTP-5xx error, and a "failed to parse pem cert chain" error is output to the log

When invoking an API deployment that has mutual TLS enabled, you might see the request fail with an HTTP-5xx error, and the following error output to the log:
```

```

This error occurs when the custom CA bundle in the trust store of the API gateway hosting the API deployment is not in the correct format.

To address this issue, make sure the custom CA bundle in the API gateway's trust store is in the correct format. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

## Invoking the API deployment fails with an HTTP-5xx error, and a "Client CA Bundle not present" error is output to the log

When invoking an API deployment that has mutual TLS enabled, you might see the request fail with an HTTP-5xx error, and the following error output to the log:
```

```

This error occurs when at least one mTLS-enabled API deployment is deployed on an API gateway, but a custom CA bundle has not been added to the API gateway's trust store.

To address this issue, do one of the following:
- Delete all mTLS-enabled API deployments from the API gateway.
- Edit all mTLS-enabled API deployments in the API gateway to disable mTLS support.
- Add a custom CA bundle to the API gateway's trust store.

For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

## Invoking the API deployment fails with an HTTP-5xx error, and an "Error in client certificate verification" error is output to the log

When invoking an API deployment that has mutual TLS enabled, you might see the request fail with an HTTP-5xx error, and the following error output to the log:
```

```

This error occurs when the custom CA bundle added to the API gateway's trust store has an invalid format. The log contains additional information about the failed request.

To address this issue, make sure the custom CA bundle added to the API gateway's trust store is in the correct format. Use traceback information from the log to fix this error. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

## Invoking the API deployment fails with a "Service Unavailable" message and a 503 error

When invoking an API deployment, you might see the request fail with an HTTP-503 error, and the following error message:
```

```

The message indicates that API Gateway is currently unable to handle the request, possibly because of insufficient capacity.

Note the following:
- If you continue to see this error, consider configuring API clients to increase the time interval between API deployment invocations (perhaps using a standard technique like jittered exponential backoff to add a degree of randomness to the interval).
- If the number of HTTP-503 errors is adversely affecting request/response performance, and it is operationally unacceptable to increase the time interval between API invocations,[Contact Us](https://support.oracle.com/)and ask for an increase in allocated CPU capacity. When you contact us, provide the OCID of the API gateway, a time period during which a high request throughput rate was handled successfully, and the target throughput rate that you want to achieve. We consider inquiries for CPU capacity increases on a case-by-case basis.
- If the message is displayed when an API deployment is invoked as the result of an action triggered by an event, additional attempts to invoke the API deployment will be retried automatically until the API deployment is successfully invoked. No intervention on your part is required.
- If you set up alarms that are triggered by API deployment error responses containing 503 error codes, you might see multiple notifications for which no intervention on your part is required.
- If the message continues to appear after an extended period of time,[Contact Us](https://support.oracle.com/)
