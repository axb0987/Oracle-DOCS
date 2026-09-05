# HTTPS backend TLS handshake fails
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-https_backend_tls_handshake_fails.htm
- Fetched: 2026-09-05 01:39 CDT

# HTTPS backend TLS handshake fails

Find out how to troubleshoot HTTPS backend TLS handshake failures when creating API deployments with the API Gateway service.

When an API deployment uses an HTTPS back end, a TLS handshake failure can stop the request before the back-end service processes any HTTP traffic. The failure usually means that API Gateway cannot validate the certificate chain or TLS configuration that the back end presents.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

The back-end URL is correct, but the request fails before the back-end service processes the HTTP request.
- 

The execution log shows the`httpBackend.requestError`log code.
- 

The execution-log message ends with`HANDSHAKE_FAILED`.
- 

Requests fail when the back-end service uses a private certificate authority (CA), custom CA bundle, or certificate chain that API Gateway does not trust.

## Possible Causes

HTTPS back-end TLS handshake failures usually have one of the following causes:
- 

The back-end certificate expired, is incomplete, or is invalid.
- 

The back-end certificate chain is missing an intermediate certificate.
- 

The certificate chain uses a CA that is not in the API Gateway trust store.
- 

The back-end TLS listener is misconfigured, including unsupported or incorrect TLS settings.
- 

The TLS session fails before API Gateway can send the HTTP request to the back end.

## Review Log Messages

Repeat the request through API Gateway, and then review the execution log for the same request.

Use the following command to repeat the request:
- 

`curl -i https://<gateway-hostname>/<deployment-path-prefix>/<api-route-path>`

In Logging, check the following log details:
- 

Capture the`opc-request-id`for the failed request.
- 

Open the execution log for the same request.
- 

Confirm whether the log code is`httpBackend.requestError`.
- 

Confirm whether the message ends with`HANDSHAKE_FAILED`.

The following log message indicates that the TLS handshake failed before the gateway sent the HTTP request to the back end:
- 

`An error occurred whilst sending request to https://<backend-url>: HANDSHAKE_FAILED`

## Review the HTTPS Back End Configuration

Review the route and back-end configuration for the failed request.
- 

Confirm that`backend.url`points to the expected HTTPS back end.
- 

Confirm that the back-end listener presents a complete certificate chain.
- 

If the back end uses a private CA or custom CA bundle, confirm that the API gateway trust store includes the required CA or CA bundle.
- 

Confirm that the TLS listener configuration matches the HTTPS back-end and trust-store requirements for the API deployment.

## Validate the HTTPS Back End Directly

From a system that can reach the back end directly, test the HTTPS listener outside API Gateway.

Use the following command to inspect the TLS handshake:
- 

`curl -v <backend-url>`

Review the direct test results for the following details:
- 

The certificate chain that the back-end listener presents.
- 

The certificate expiration dates and host name coverage.
- 

The TLS protocol and cipher configuration.
- 

Any certificate validation errors that occur before the HTTP request is sent.

## Fix HTTPS Back-End TLS Issues

Apply the fix that matches the problem that you found.
- 

If the back-end certificate expired, is incomplete, or is invalid, replace or correct the certificate chain.
- 

If the certificate chain is missing an intermediate certificate, configure the back-end listener to present the full chain.
- 

If the back end uses a private CA or custom CA bundle, add the required CA or CA bundle to the API gateway trust store.
- 

If the back-end listener uses incorrect TLS settings, update the listener configuration and retry the request.
- 

If the execution log shows`httpBackend.requestError`with`HANDSHAKE_FAILED`, troubleshoot the HTTPS listener before you change the API Gateway route configuration.

## Verify HTTPS Back-End Connectivity

After you correct the TLS configuration, verify that the API deployment can reach the HTTPS back end.
- 

Send the same request through API Gateway.
- 

Confirm that the execution log no longer shows`httpBackend.requestError`with`HANDSHAKE_FAILED`.
- 

Confirm that the back-end service receives and processes the HTTP request.

## For More Information

For more information, see:
- 

[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)
- 

[Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm)
- 

[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm)
- 

[HTTP-5xx errors when API deployment is created successfully but requests fail](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm)
