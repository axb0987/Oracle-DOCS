# Authentication provider call failures surface as HTTP 500
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-authentication_provider_call_failures_http-500.htm
- Fetched: 2026-09-05 01:39 CDT

# Authentication provider call failures surface as HTTP 500

Find out how to troubleshoot authentication provider call failures that return HTTP 500 errors when calling APIs, having successfully created API gateways and API deployments with the API Gateway service.

When API Gateway returns HTTP 500 during authentication, the request might fail before it reaches the back-end service. In this case, review the configured identity-provider call path.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

A client receives an HTTP`500`response on a route that uses token authentication.
- 

The back-end service does not show a matching request for the failed API call.
- 

The failure occurs during token introspection, discovery, or remote JSON Web Key Set (JWKS) validation.
- 

The failure occurs only on routes that depend on an external identity provider.

## Possible Causes

This issue typically has one of the following causes:
- 

The configured`introspection_endpoint`, discovery endpoint, or JWKS endpoint returns HTTP`500`or another unexpected response.
- 

API Gateway cannot connect to the identity-provider endpoint because the connection times out or is refused.
- 

The identity provider returns a response that API Gateway cannot parse.
- 

The authentication policy references the wrong provider endpoint.
- 

The client credentials configured for token introspection are incorrect or not accepted by the identity provider.

## Review the Failing Authentication Request

Use the failing request to confirm where the error occurs:
- 

In the access log, find the request and note the`opcRequestId`value.
- 

Confirm that the client-visible response status is HTTP`500`.
- 

Search the execution log for the same`opcRequestId`value.
- 

Confirm whether the execution log reports`authentication.idpCallFailed`.

If the execution log reports`authentication.idpCallFailed`, troubleshoot the identity-provider call path before you troubleshoot the back-end route.

## Review the Authentication Policy

Review the authentication policy for provider endpoint and credential issues:
- 

Confirm that the discovery, JWKS, or introspection endpoint URI in the deployment specification or Console points to the intended identity provider.
- 

If the log message identifies`introspection_endpoint`, verify that endpoint before you review other provider endpoints.
- 

Confirm that the configured client ID and client secret are valid for the introspection endpoint.
- 

Confirm that the identity provider returns valid JSON in the format expected by the selected authentication policy.

## Review Log Messages

Review the execution log for messages that identify the failed provider call:
- 

`authentication.idpCallFailed`
- 

`Unexpected response from the introspection_endpoint uri: <uri>, received (500, Server Error).`
- 

`Unable to connect to the introspection_endpoint uri: <uri>, TIMEOUT. Make sure that the URI is accessible on the subnet of the gateway.`
- 

`Unable to connect to the introspection_endpoint uri: <uri>, CONNECTION_REFUSED. Make sure that the URI is accessible on the subnet of the gateway.`
- 

`Unable to parse response from Identity Provider`

These messages help you identify whether the failure is caused by provider availability, network reachability, or an invalid provider response.

## Fix Authentication Provider Call Failures

Apply the resolution that matches the failure that you identified:
- 

If the provider endpoint URI is incorrect, update the discovery, JWKS, or introspection endpoint in the authentication policy.
- 

If the identity provider returns HTTP`500`, resolve the provider-side error before you investigate the issue as an API Gateway defect.
- 

If the provider response cannot be parsed, update the identity provider to return valid JSON in the expected format.
- 

If the introspection credentials are incorrect, update the configured client credentials.
- 

If the provider endpoint times out or refuses the connection, test the endpoint from a compute instance that uses the same network path as the gateway subnet. Then fix the firewall, route table, security rule, or provider endpoint configuration that blocks the connection.

## Verify Authentication Provider Calls

After you update the provider configuration or network path, verify that authentication succeeds:
- 

Send the same API request again.
- 

Confirm that the request no longer returns HTTP`500`during authentication.
- 

Confirm that the execution log no longer shows`authentication.idpCallFailed`for the request.
- 

Confirm that the request reaches the expected back-end service when the token is valid.

## For More Information

For more information, see:
- 

[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm)
- 

[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)
- 

[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)
