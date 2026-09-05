# Token validation fails because token claims do not match the deployment policy
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-token_validation_fails_token_claims_do_not_match.htm
- Fetched: 2026-09-05 01:39 CDT

# Token validation fails because token claims do not match the deployment policy

Find out how to troubleshoot token validation claim mismatches when calling APIs, having successfully created API gateways and API deployments with the API Gateway service.

If API Gateway rejects a request during token validation, the token claims might not match the authentication policy for the deployment. The token can be present and well formed, but validation still fails if the issuer, audience, expiry time, or required custom claims do not match the route policy.

## Issue Symptoms

You might see one or more of the following symptoms:
- The request is rejected during authentication, even though the request includes a token that is properly formatted.
- The token payload appears valid after you decode it, but API Gateway still denies the request.
- Authentication fails with claim validation errors for the`aud`,`iss`,`exp`, or required custom claim value.
- The same application succeeds with one token and fails with another token from a different issuer, audience, or environment.

## Possible Causes

This issue can have one or more of the following causes:
- The token's`aud`claim does not match the audience that is configured for the deployment.
- The token's`iss`claim does not match the configured issuer.
- The authentication policy requires a custom claim that is missing from the token.
- The authentication policy requires a custom claim value that does not match the token.
- The token is expired, or the token time values fall outside the configured clock-skew allowance.
- For discovery-based or introspection-based validation, the returned claim set does not satisfy the deployment policy.

## Review the Authentication Policy

Review the authentication policy for the route that handled the request and verify the following settings:
- `authentication.audiences`contains the audience that the token was issued for.
- `authentication.issuers`contains the identity provider that issued the token.
- `verifyClaims`includes only the claims and values that the route must enforce.
- `maxClockSkewInSeconds`accounts for the expected time difference between the token issuer and the systems that validate the request.

If the failure is time-related, compare the token's`exp`value with the current UTC time and the configured clock-skew allowance.

## Review Log Messages

Review the API Gateway execution log in Logging for the failing request. Use the request ID from the response to find the matching log entry.

Look for authentication failure events such as the following events:
- `jwtAuthentication.authenticationFailed`
- `tokenAuthentication.authenticationFailed`

Then review the log message for the failed claim validation. The message can identify the claim or value that did not satisfy the policy.
- `Validation failed for 'exp' claim.`
- `JWT token not issued by the configured issuers.`
- `JWT token not issued for the configured audience.`
- `JWT token missing required claim '<claim>'.`
- `JWT token does not have the expected claim value for '<claim>'.`

## Validate the Token Claims

Use the validation method that matches the token type.

For a JSON Web Token (JWT), decode the payload and compare the relevant claims with the deployment configuration. Check the`aud`,`iss`,`exp`, and required custom claim values.

```

```

For an opaque token, call the configured introspection endpoint directly. Compare the returned`aud`,`iss`,`exp`, and custom claim values with the API Gateway deployment policy.

```

```

Validate the token against the exact deployment and route configuration that handled the failing request.

## Fix Claim Mismatches

Apply the fix that matches the failed validation check:
- If the audience is wrong, update`authentication.audiences`or use a token that was issued for the expected audience.
- If the issuer is wrong, update`authentication.issuers`or use a token from the expected identity provider.
- If a required custom claim is missing, update the token issuance process or update`verifyClaims`to match the intended requirement.
- If a required custom claim has the wrong value, correct the token claim value or update the expected value in`verifyClaims`.
- If the token is expired, retry the request with a valid token.
- If the failure is caused by clock skew, adjust`maxClockSkewInSeconds`only when the time difference is expected and acceptable for your security requirements.

## Verify Token Validation

After you update the policy or retry the request with a corrected token, verify the result:
- Send the same request again.
- Confirm that the deployment accepts the request.
- Confirm that the execution log no longer shows the claim-validation failure.

## For More Information

For more information, see:
- [Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm)
- [Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)
- [Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)
