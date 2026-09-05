# Dynamic authentication selector configuration is invalid, or a multi-auth deployment later fails to match requests to an authentication server
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-dynamic_authentication_selector_configuration_is_invalid.htm
- Fetched: 2026-09-05 01:39 CDT

# Dynamic authentication selector configuration is invalid, or a multi-auth deployment later fails to match requests to an authentication server

Find out how to troubleshoot dynamic authentication selector errors and request-matching failures in multi-auth configurations when creating API deployments with the API Gateway service.

If an API deployment uses multiple authentication servers and selects between them dynamically, failures can occur at deployment time or at runtime. At deployment time, API Gateway can reject an invalid selector configuration. At runtime, API Gateway can accept the deployment but fail to match a request to an authentication server.

## When This Happens

You might see one or both of the following symptoms:
- 

API Gateway rejects the deployment with an`Invalid Dynamic Authentication Selector`error.
- 

The deployment is created successfully, but some requests later return`401 Unauthorized`because no authentication server matches the request.

The issue often occurs in deployments that use different authentication methods for different request patterns, such as API key authentication for one route pattern and OAuth2 authentication for another route pattern.

## How Dynamic Authentication Works

A dynamic authentication deployment uses the`selectionSource.selector`value to decide which authentication server handles each request. For each request, API Gateway resolves the selector value from the request and compares that value with the configured authentication server keys.

Use one of the following supported selector forms:
- 

`request.auth[<key>]`
- 

`request.path[<key>]`
- 

`request.query[<key>]`
- 

`request.headers[<key>]`
- 

`request.subdomain[<key>]`
- 

`request.host`

After API Gateway resolves the selector value, it selects the matching authentication server. If no authentication server key matches, API Gateway uses the default authentication server if one is configured. Otherwise, the request fails with`401 Unauthorized`.

## Part 1: Deployment Creation Fails Because the Selector Is Invalid

This failure occurs when the selector expression is invalid and the deployment cannot be created.

What This Looks Like

The deployment is rejected with the following error:
- 

`Invalid Dynamic Authentication Selector`

Why This Happens

The selector expression must use a supported selector form and valid selector syntax. The following selector examples are invalid:
- 

`random`
- 

`request.header[]]`
- 

`request.path[path1]*request.path[path2]`

These configuration errors must be fixed before the deployment can be created or updated.

Path Selector Requirement

If you use`request.path[<key>]`, the`<key>`value must be the name of a path parameter that is defined in the route.

The following route and selector use the same path parameter name:
- 

Route:`/DMPServices/{serviceType}`
- 

Selector:`request.path[serviceType]`

The`request.path[/]`selector is not valid because`/`is not a path-parameter name.

How to Fix It

Use the following checks to fix invalid selector syntax:
- 

Replace the invalid selector with one of the supported selector forms.
- 

If you use`request.path[<key>]`, define the same named path parameter in the route.
- 

If the request pattern is not based on a stable path parameter, use a header or query-parameter selector instead.

## Part 2: Deployment Succeeds, but Requests Later Fail with No Matching Authentication Server

This failure occurs at runtime. The deployment configuration is valid, but an incoming request does not produce a selector value that matches any configured authentication server.

What This Looks Like

At runtime, requests fail with the following message:
- 

`Request unauthorized as no authentication server matched the request and no default is specified`

The message means that API Gateway reached the deployment but could not select an authentication server for the request.

Why This Happens

The failure usually occurs because the selector value is present on the first request but missing from later requests. For example, the initial request might include a query parameter that selects the authentication server, while later requests for`.js`files,`.css`files, images, or API calls omit that query parameter.

If no default authentication server is configured, a request that does not include a matching selector value fails with`401 Unauthorized`.

## How Cookies and OAuth2 State Fit In

Cookies and the OAuth2`state`parameter can help preserve session or flow information, but they do not replace the runtime selector requirement for ordinary follow-up requests.

Query-Parameter Selector Problems

A query-parameter selector can fail when the initial request includes the selector value but later requests omit it. For example, browser requests for assets such as`.js`files,`.css`files, and images often do not include the same query parameters as the initial request.

During the OAuth2 redirect or callback step, API Gateway can use the OAuth2`state`parameter to recover the authentication server that was used for that flow. After the callback, ordinary follow-up requests still must match the deployment authentication-selection behavior.

How to Choose a Better Selector

Use a selector value that is present on every request that must be authenticated consistently. The following selector types are often more reliable than a query-parameter selector:
- 

A request header, using`request.headers[<key>]`.
- 

A stable path parameter, using`request.path[<key>]`.
- 

The host name, using`request.host`, if host-based authentication selection is required.

For browser-based applications, a request header is often more reliable than a query parameter because follow-up requests can include the same header consistently.

How to Fix Runtime Matching Failures

Use the following checks to fix runtime authentication-server matching failures:
- 

If the selector uses a query parameter that is not present on later requests, change the selector to a stable request value, such as a header or path parameter.
- 

If some requests are expected to omit the selector value, configure an appropriate default authentication server.
- 

If the selector uses a path parameter, confirm that later requests include the same path parameter.
- 

If your application uses cookies, use them for session continuity only. Do not rely on cookies alone to select the authentication server for ordinary follow-up requests.

## What to Check

For a deployment that is already active, compare the request that succeeds with the request that fails. Confirm the following details:
- 

The selector configured in`selectionSource`.
- 

The selector value that is resolved from the successful request.
- 

The selector value that is resolved from the failed request.
- 

Whether the selector value is present in both requests.
- 

Whether an authentication server key matches each resolved selector value.
- 

Whether a default authentication server is configured.

## What to Look for in Logs

Use execution logs to identify the failure mode:
- 

`Invalid Dynamic Authentication Selector`indicates a deployment configuration problem.
- 

`Request unauthorized as no authentication server matched the request and no default is specified`indicates a runtime request-matching problem.

Troubleshoot these failure modes separately. A valid deployment configuration can still fail at runtime if later requests do not include a matching selector value.

## Verify the Fix

After you correct the selector or authentication server mapping, verify the deployment and request flow:
- 

Re-create or update the deployment if the selector configuration changed.
- 

Send the initial request again.
- 

Send the follow-up requests that previously failed.
- 

Confirm that API Gateway no longer rejects the deployment for selector syntax.
- 

Confirm that runtime requests no longer fail because no authentication server matched the request.

## For More Information

For more information, see:
- 

[Adding Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm)
- 

[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm)
- 

[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)
- 

[Miscellaneous errors when calling APIs](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Miscellaneous-issues.htm)
