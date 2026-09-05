# OCI service API calls fail after being proxied through API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-service_api_calls_fail_after_proxied.htm
- Fetched: 2026-09-05 01:39 CDT

# OCI service API calls fail after being proxied through API Gateway

Find out how to troubleshoot OCI service API calls that fail after being proxied through a gateway, having successfully created API gateways and API deployments with the API Gateway service.

OCI service API calls can fail after API Gateway proxies them, even when the same calls succeed when sent directly to the OCI service. This issue often occurs because the target OCI service validates a request signature that no longer matches the request that the service receives.

Many OCI service APIs validate a signature over the final request target, host, method, body, and selected headers. If API Gateway changes any signed value while proxying the request, the target OCI service can reject the request.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

A client can call the OCI service directly, but the same call fails when routed through API Gateway.
- 

A request that uses OCI API key signing or another OCI request-signing flow fails only when routed through the gateway.
- 

The proxied request returns an authorization or signature validation error from the target OCI service.
- 

Calls to an OCI service endpoint, such as Generative AI or another OCI API that expects signed OCI requests, fail after API Gateway proxies the request.

## Possible Causes

This issue can occur for the following reasons:
- 

The client signs the original request for the API Gateway endpoint instead of the final OCI service endpoint.
- 

The`Host`header that the target OCI service receives differs from the`host`value that was used to create the signature.
- 

The signed`(request-target)`value does not match the final request path and method.
- 

Required signing headers, such as`date`,`host`, or`x-content-sha256`, do not match the final outbound request.
- 

API Gateway can forward headers, but it does not recalculate OCI request signatures for generic proxied OCI service calls.

## Review Signature Requirements

Confirm whether the target OCI service requires OCI request signing. Then compare the client request with the request that the target OCI service receives.

Review the following request details:
- 

Inspect the client request`Authorization`header.
- 

Confirm whether the`Authorization`header starts with`Signature`.
- 

Identify the headers that are included in the signed header list.
- 

Confirm whether the signature was created for the final target URI, HTTP method, and request body that the OCI service receives.

If the request is signed for the API Gateway hostname and path instead of the final OCI service endpoint, the OCI service rejects the request.

## Review Signed Headers

Review the signed request for headers that OCI request signing commonly uses:
- 

`Authorization`
- 

`date`
- 

`host`
- 

`x-content-sha256`
- 

`content-type`
- 

`content-length`

If the target OCI service validates request signatures, the signed values must match the final outbound request exactly.

Capture the API Gateway response and record the returned`opc-request-id`. Use the request ID to correlate the failing proxied call with logs and service-side diagnostics.

## Fix OCI Service Proxy Calls

Use a design that signs the request that the OCI service receives. Do not rely on header forwarding alone to make a signed OCI service request valid after proxying.

Use the fix that matches your integration pattern:
- 

If the target OCI service requires a signed request, sign the final outbound request outside API Gateway.
- 

If API Gateway must front the integration, place a component behind API Gateway that generates the correct OCI-signed request to the target service. For this pattern, a Functions back end is often a workable approach because the function can call the OCI service with its own OCI authentication flow.

## Understand Header Forwarding Limits

API Gateway can forward headers, but forwarded headers do not repair OCI request signature mismatches.

Passing the original`Authorization`header unchanged is not sufficient when one or more of the following values change:
- 

The final`host`value.
- 

The final request path.
- 

The signed header set.
- 

The body hash that the target OCI service validates.

## Verify OCI Service Proxy Calls

After you change the integration design, verify that the proxied request succeeds.

Use the following checks:
- 

Send the request through the updated request path.
- 

Confirm that the target OCI service accepts the request.
- 

Confirm that the request is signed for the final OCI service endpoint instead of the API Gateway endpoint.
- 

Confirm that the returned`opc-request-id`no longer corresponds to a signature or authorization failure.

## For More Information

For more information, see:
- 

[Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm)
- 

[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)
- 

[Adding a Function in OCI Functions as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm)
- 

[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)
