# HTTP-4xx errors when API deployment is created successfully but requests fail
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Gateway-requests-fail-with-4xx.htm
- Fetched: 2026-09-05 01:38 CDT

# HTTP-4xx errors when API deployment is created successfully but requests fail

Find out how to troubleshoot HTTP-4xx errors when an API deployment is created successfully with the API Gateway service, but requests fail.

Having created an API deployment successfully, you might encounter HTTP-4xx errors when calling it.

## Invoking the API deployment fails with an HTTP-4xx error, and a "Client certificate is invalid for this gateway" error is output to the log

When invoking an API deployment that has mutual TLS enabled, you might see the request fail with an HTTP-4xx error, and the following error output to the log:
```

```

This error occurs when the API gateway hosting the API deployment cannot verify the certificate presented by the API client.

To address this issue, confirm that the certificate presented by the API client can be validated using a custom CA bundle specified for the API gateway. For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

## Invoking the API deployment fails with an HTTP-4xx error, and a "SAN validation failure" error is output to the log

When invoking an API deployment that has mutual TLS enabled, you might see the request fail with an HTTP-4xx error, and the following error output to the log:
```

```

This error occurs when the API gateway hosting the API deployment can verify the certificate presented by the API client, but the certificate's Subject Alternative Names/Common Names (SANs/CNs) fields contain none of the allowed SAN/CN values specified in the API deployment's mTLS request policy.

To address this issue, do one of the following:
- Change the allowed SAN/CN list in the mTLS request policy to include the SAN/CN values in the certificate presented by the API client.
- Change the certificate presented by the API client to include SAN/CN values from the allowed SAN/CN list in the mTLS request policy.

For more information, see[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm)
