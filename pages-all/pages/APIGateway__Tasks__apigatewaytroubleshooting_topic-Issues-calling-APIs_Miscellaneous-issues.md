# Miscellaneous errors when calling APIs
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Miscellaneous-issues.htm
- Fetched: 2026-09-05 01:38 CDT

# Miscellaneous errors when calling APIs

Find out how to troubleshoot miscellaneous errors when an API deployment is created successfully with the API Gateway service, but requests fail.

## Invoking the API deployment is successful but a "Base 64 Certificate Size greater than 8KB" warning is output to the log

When invoking an API deployment that has mutual TLS enabled, you might see the request handled successfully but the following warning output to the log:
```

```

The message is output to the log if the TLS certificate presented by the API client is greater than 8 KB when the certificate is Base64-encoded. If the Base64-encoded certificate is greater than 8 KB, the certificate is not stored as a`request.cert`context variable.

To address this issue, the API client must present a certificate that is less than 8 KB when Base64-encoded. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

## Invoking the API deployment fails with a "Connection closed due to excessive load" message

When invoking an API deployment, you might see bursts of SSL/TLS handshake errors, and the following error output to the log:
```

```

The message indicates that API Gateway is currently unable to handle the request, possibly because of insufficient capacity.

Note the following:
- If you continue to see this error, consider configuring API clients to increase the time interval between API deployment invocations (perhaps using a standard technique like jittered exponential backoff to add a degree of randomness to the interval).
- If the number of errors is adversely affecting request/response performance, and it is operationally unacceptable to increase the time interval between API invocations,[Contact Us](https://support.oracle.com/)and ask for an increase in allocated CPU capacity. When you contact us, provide the OCID of the API gateway, a time period during which a high request throughput rate was handled successfully, and the target throughput rate that you want to achieve. We consider inquiries for CPU capacity increases on a case-by-case basis.
- If the message is displayed when an API deployment is invoked as the result of an action triggered by an event, additional attempts to invoke the API deployment will be retried automatically until the API deployment is successfully invoked. No intervention on your part is required.
- If the message continues to appear after an extended period of time,[Contact Us](https://support.oracle.com/)
