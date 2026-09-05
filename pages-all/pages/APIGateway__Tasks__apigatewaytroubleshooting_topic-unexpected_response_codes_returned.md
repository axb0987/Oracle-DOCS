# Unexpected response codes are returned through API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-unexpected_response_codes_returned.htm
- Fetched: 2026-09-05 01:39 CDT

# Unexpected response codes are returned through API Gateway

Find out how to troubleshoot unexpected HTTP response codes returned through a gateway when calling APIs, having successfully created API gateways and API deployments with the API Gateway service.

When a client receives an unexpected HTTP response code through API Gateway, first determine whether API Gateway or the back-end service returned the response. API Gateway can proxy a response from the back-end service, return an error when the back-end call fails, or return an authentication error before the request reaches the back-end service.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

The client receives an unexpected`302`,`500`,`502`,`504`, or similar response through the gateway.
- 

The response code does not match the response that you expect from the API deployment.
- 

The`Location`header or status code does not match the response that you expect from the API deployment.
- 

The gateway team and the back-end service team cannot determine which component returned the response.

## Possible Causes

Unexpected response codes can occur for the following reasons:
- 

The back-end service returned the response, and API Gateway proxied that response to the client.
- 

API Gateway returned an error because it could not complete the back-end call.
- The response came from the authentication path before API Gateway routed the request to the back-end service.
- 

The back-end service returned a redirect that contains an internal URL, a private host name, or an unexpected host header value.
- 

A timeout, TLS failure, DNS failure, or connection failure was interpreted as a response-code issue.

## Capture Response Details

Send the request again and capture the following response details:
- 

The client-visible HTTP status code.
- 

The`opc-request-id`response header.
- 

Response headers that affect routing or redirects, such as`Location`,`Host`,`Forwarded`, and`X-Forwarded-Host`.
- 

The gateway endpoint, request path, HTTP method, and time of the request.

## Review Access and Execution Logs

Use the`opc-request-id`value to review the access log and execution log for the same request:
- 

In Logging, open the access log and execution log for the API Gateway deployment.
- 

In the access log, review the client-visible`status`value.
- 

In the execution log, review the`code`and`message`fields.
- 

In the deployment specification or Console, verify the`backend.url`value, the`routes.path`value, and any request header transformations that the back-end service requires.

## Determine the Source of the Response

Compare the client response, access log, and execution log to identify the component that returned the response:
- 

If the execution log contains an authentication provider error, such as`authentication.idpCallFailed`, the request failed on the authentication path before it reached the back-end service.
- 

If the execution log contains a back-end call failure, such as`DNS_NXDOMAIN`,`CONNECTION_REFUSED`,`CONNECTION_TIMEOUT`,`TIMEOUT`, or`HANDSHAKE_FAILED`, API Gateway returned the error because it could not complete the back-end call.
- 

If the client-visible`status`value is`302`, review the`Location`header. If the header contains the back-end service internal URL, the redirect came from the back-end service.
- 

If many requests show the same back-end response pattern, review API Gateway metrics. The`BackendHttpResponses`metric includes the`backendHttpStatusCode`and`backendHttpStatusCategory`dimensions.

## Resolve Unexpected Response Codes

Apply the resolution that matches the source of the response:
- 

If the back-end service returned the response, troubleshoot the back-end application, redirect logic, or error handling.
- 

If the back-end service uses request headers to build redirects or response links, configure the deployment to forward the required headers.
- 

If API Gateway returned an error because of a connectivity, DNS, timeout, or TLS issue, troubleshoot the back-end call path.
- 

If the authentication path returned the response, review the identity provider, authentication policy, selector configuration, and token validation settings.
- 

If the response includes an unexpected redirect, update the back-end service to generate client-visible URLs, or use header transformations so the back-end service receives the expected host and forwarding headers.

## Verify Response Codes

After you fix the response source, verify the API call again:
- 

Send the same request to the gateway endpoint.
- 

Confirm that the returned status code matches the expected response from the API deployment.
- 

Confirm that redirects use client-visible URLs when the API is expected to redirect the client.
- 

Confirm that the access log and execution log show the expected request path and response source.
- 

If you use API Gateway metrics, confirm that the`BackendHttpResponses`dimensions show the expected back-end response category.

## For More Information

For more information, see:
- 

[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)
- 

[Transforming Incoming Requests and Outgoing Responses](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests.htm)
- 

[API Gateway Metrics](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Reference/apigatewaymetrics.htm)
- 

[Details for API Gateway Logging](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_api_gateway.htm)
- 

[HTTP-5xx errors when API deployment is created successfully but requests fail](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm)
