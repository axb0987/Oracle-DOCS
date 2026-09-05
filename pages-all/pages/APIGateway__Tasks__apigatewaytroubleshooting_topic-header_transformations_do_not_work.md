# Header transformations do not work as expected
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-header_transformations_do_not_work.htm
- Fetched: 2026-09-05 01:39 CDT

# Header transformations do not work as expected

Find out how to troubleshoot header transformations that do not add, replace, or rename headers as expected when creating API deployments with the API Gateway service.

If API Gateway does not add, replace, or rename a header as expected, first check whether the route and policy configuration make the required context value available to the transformation. The transformation also might target a protected header, produce an invalid header value, or use an`ifExists`setting that keeps the existing header value.

## Issue Symptoms

You might see one or more of the following symptoms:
- The back-end service does not receive the header that you expect API Gateway to add.
- The header is present, but the value is empty or unchanged.
- The header transformation appears to be configured correctly, but the request that is sent to the back-end service does not include the expected header change.

## Possible Causes

This issue can have one or more of the following causes:
- The route uses an`ANONYMOUS`authorization policy, so API Gateway does not populate`request.auth[...]`values for the route.
- The header transformation tries to modify a protected request header or protected response header that API Gateway does not transform.
- The transformation expression renders an invalid value or does not produce a usable value.
- The`ifExists`setting keeps the original header unchanged.

## Review the Route Configuration

Review the route that handled the request and verify the following details:
- The request matched the expected route.
- The route uses the expected`requestPolicies.authentication`setting.
- The route includes the expected transformation in the`requestPolicies.headerTransformations`section or the`responsePolicies.headerTransformations`section.
- The transformation depends on`request.auth[...]`only when the route performs authentication.
- The target header is not a protected request header or protected response header that API Gateway refuses to transform.

If the transformation uses an expression such as`${request.auth[access_token_claims][claim1]}`, the route must use an authorization policy that performs authentication. When a route uses the`ANONYMOUS`authorization policy, API Gateway does not authenticate the request and does not populate`request.auth[...]`values.

## Review the Route and Logs
- In the Console, open the API deployment that handled the request.
- Review the matching route, authentication policy, and header transformation policy.
- Send the same request again to create a new failing example.
- In OCI Logging, open the API Gateway access log and execution log for the deployment.
- Use the request ID from the response to find the same request in both logs.
- In the execution log, review the request for header transformation errors.

## Review Log Messages

Review the execution log for the failing request. The following log entries can identify why the API gateway skipped or rejected the transformation:
- `headerTransformation.protectedHeaderTransformed`: The policy tried to transform a protected header.
- `headerTransformation.badHeaderValue`: The rendered header value contained unsupported characters or was otherwise invalid.
- `headerTransformation.missingSetValues`: The transformation expression did not produce a valid value, so API Gateway skipped the header update.

## Fix Header Transformations

Use the fix that matches the cause that you found:
- If the transformation depends on token claims, change the route to use an authenticated authorization policy, such as`AUTHENTICATION_ONLY`, instead of`ANONYMOUS`.
- If the request depends on token claims, send the request again with a valid token and verify that token validation succeeds.
- If the transformation targets a protected header, update the policy to use a different header.
- If the expression renders an invalid or empty result, update the expression so that the expression produces a valid header value.
- If the result appears unchanged, review the`ifExists`setting.`SKIP`keeps an existing header unchanged, and`APPEND`adds values without replacing the original header.

## Verify Header Transformations

After you update the route or policy, verify that the header transformation works as expected:
- Send the same request again.
- Verify that the back-end service receives the expected header and value.
- Verify that the execution log does not show the header transformation errors described in this topic.

## For More Information

For more information, see:
- [Transforming Incoming Requests and Outgoing Responses](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests.htm)
- [Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm)
- [Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm)
- [Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)
