# Details for API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_api_gateway.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for API Gateway

Logging details for API Gateway logs.

## Resources
- API deployment

## Log Categories

API value (ID): Console (Display Name) Description
Access Access Logs Access logs for an API deployment.
Execution Execution Logs Execution logs for an API deployment.

## Availability

API Gateway Access/Execution logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## API Deployment Access Log

API deployment access logs record a summary of every request and response that goes through the API gateway, matching a route on the API deployment. Each access log entry contains information about the request and response (time the request was received, server protocol, response status, and so on). For the complete list of fields, see[Contents of an Access Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_api_gateway.htm#details_for_api_gateway__section_uv3_4qj_5mb).

## Contents of an Access Log

Access logs appear as a value in the Log Data field. This value is JSON-formatted data with the following fields:

Field Example Description
httpMethod GET HTTP method derived from the request line.
requestUri /example/ Request URI derived from the request line.
serverProtocol HTTP/1.1 HTTP protocol derived from the request line.
bodyBytesSent 45 Total size of the response (in bytes) sent to the client.
gatewayId ocid1.apigateway.oc1.iad. &lt;unique_ID&gt; OCID of the API Gateway for the API deployment servicing the request.
httpUserAgent Apache-HttpClient/4.5.9 (Java/1.8.0_252) HTTP user agent for the request.
message GET /example/ HTTP/1.1 Request line received from the client.
opcRequestId FF7F0B8A32246FC7526AE45A2FA8D5CE/

A408784281BF81B0EE23596CE57CA93C/

C06F7DDDFC7C505FAA0566D8F2FE0BB2 Value of the opc-request-id HTTP header, or an internally generated request ID if none was specified in the request.
remoteAddr 138.1.55.172 IP address of the requesting client.
httpReferrer https://www.example.com The URL of the referral, if present.
requestDuration 0.016 Total time taken (in seconds, with millisecond precision), from when the gateway starts receiving request from the client, until it completes sending a response to the client.
status 404 Status code of the response from the gateway.
deploymentId ocid1.deployment.oc1.iad. &lt;unique_id&gt; OCID of the API deployment servicing the request.
gatewayDisplayName Example Gateway Display Name Display name of the API gateway for the API deployment servicing the request.

## Sample Access Log
```

```

## API Deployment Execution Log

API deployment execution logs record information about processing within the API gateway for an individual route, to help with troubleshooting and monitoring. Each execution log entry contains information (time the request was received, level to denote the severity of the log message, a message code, and so on). For the complete list of fields, see[Contents of an Execution Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_api_gateway.htm#details_for_api_gateway__section_vpg_qtj_5mb).

## Contents of an Execution Log

By default Log Level info is enabled. This value is JSON-formatted data with the following fields:

Field Example Description
code request.loopDetected Short code for the logging event encountered while running the request. For the complete list of message codes, see the "Log Codes" table[Log Codes](https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_api_gateway.htm#details_for_api_gateway__section_tj4_g5j_5mb).
gatewayId ocid1.apigateway.oc1.iad. &lt;unique_ID&gt; API gateway OCID for the API deployment servicing the request.
functionId ocid1.fnfunc.oc1.iad. &lt;unique_ID&gt; OCID of function that the API gateway invoked. This field is only present for function backends.
level WARN Log level for the execution log entry, whether INFO, WARN, or ERROR.
message A request loop has been detected - requests for this gateway are being directed back to this gateway. Execution message emitted while processing the request.
opcRequestId FF7F0B8A32246FC7526AE45A2FA8D5CE/

A408784281BF81B0EE23596CE57CA93C/

C06F7DDDFC7C505FAA0566D8F2FE0BB2 Value of the opc-request-id HTTP header, or an internally generated request ID if none was specified in the request.
configuredLimit 5 Number of requests to allow per configuredUnit. Either the rate limit, or the quota.
configuredUnit MINUTE Time period in which to allow the number of requests specified by configuredLimit. For rate limits, "SECOND". For quota, "MINUTE", "DAY", "HOUR", "WEEK", or "MONTH".
entitlementName Entitlement1 Name of the entitlement the request is using to access the API deployment.
limitingKey &lt;timestamp&gt;/ocid1.apigatewayusageplan.oc1.iad. &lt;unique_ID&gt; /&lt;entitlement-name&gt;/ocid1.apigatewaysubscriber.oc1.iad. &lt;unique_ID&gt; To calculate usage for rate limit and quota purposes, requests with the same key are counted together.
limitingResourceId ocid1.apigatewayusageplan.oc1.iad. &lt;unique_ID&gt; OCID of the usage plan used to access the API deployment.
limitingResourceName Gold-Usage-Plan Name of the usage plan used to access the API deployment.
secretId ocid1.secret.oc1.iad. &lt;unique_ID&gt; OCID of a vault secret the API gateway is attempting to retrieve.
secretVersion 1 Version number of a vault secret the API gateway is attempting to retrieve.
subscriberId ocid1.apigatewaysubscriber.oc1.iad. &lt;unique_ID&gt; OCID of the subscriber.
subscriberName Premium-subscriber Display name of the subscriber.
deploymentId ocid1.deployment.oc1.iad. &lt;unique_id&gt; OCID of the API deployment servicing the request.
gatewayDisplayName Example Gateway Display Name Display name of the API gateway for the API deployment servicing the request.

## Log Codes

Log Code Description
authentication.idpCallFailed An error occurred whilst calling the OAuth2 Identity Provider.
authentication.idpCallSuccess Successfully called the OAuth2 Identity Provider.
authentication.idpTokenExpiryNonNumeric The OAuth2 Identity Provider did not return a valid expiry.
authentication.validationFailurePolicyOAuth The OAuth2 Validation Failure Policy has been triggered.
authentication.validationFailurePolicyOAuthStepFailed An error occurred whilst performing the OAuth2 Validation Failure Policy steps.
authorization.unauthorizedRequest Authorization failed for the request.
customAuthentication.authenticationFailed Custom Authentication failed.
customAuthentication.cacheMiss The custom authorizer response was not found in the cache.
customAuthentication.failedFunctionInvocation Failed to invoke the Oracle Function.
customAuthentication.successfulAuthentication Custom Authentication successful.
customAuthentication.successfulFunctionInvocation Successfully invoked the Oracle Function.
customAuthentication.unexpectedResponse Unexpected response from the Oracle Function.
dynamicAuthentication.authenticationServerMatched The selected context variable value matched one of the authentication server rules.
dynamicAuthentication.defaultAuthenticationServerMatched The selected context variable value did not match any of the authentication server rules, but a default authentication server had been specified so that was used for authentication.
dynamicAuthentication.jwtTokenInvalid The selected context variable was request.auth[claimName] but an invalid JWT token was sent with the request.
dynamicAuthentication.jwtTokenNotFound The selected context variable was request.auth[claimName] but no JWT token was sent with the request.
dynamicAuthentication.noAuthenticationServerMatched The selected context variable value did not match any of the authentication server rules, and no default authentication server had been specified.
dynamicRouting.backendMatched The request matched a back end rule, and was routed to the associated back end.
dynamicRouting.backendRejected The request failed because the request did not match a back end rule, and no default rule was defined.
dynamicRouting.defaultBackendMatched The request did not match a back end rule, and so was routed to the back end associated with the default rule.
functionBackend.badGateway Received "Bad Gateway" when invoking the function in OCI Functions
functionBackend.badRequestHeaderValue Bad value for request header.
functionBackend.badRequestHeaders Bad request header.
functionBackend.badResponse Function returned faulty response. This indicates an improper formed response from the function.
functionBackend.internalServiceError Internal service error when invoking the function in OCI Functions
functionBackend.notFoundOrNotAuthorized Failed to invoke the function in OCI Functions due to 404 from OCI Functions service.
functionBackend.rateLimited Rate limited when invoking the function in OCI Functions
functionBackend.serviceUnavailable OCI Functions service unavailable.
functionBackend.successfulRequest Successful invocation of function in OCI Functions
functionBackend.timeout Invocation of function in OCI Functions timed out.
headerTransformation.badHeaderValue Bad value for request header.
headerTransformation.missingSetValues Missing value for the set transform policy.
headerTransformation.protectedHeaderTransformed The policy tried to transform a protected header.
httpBackend.formedBackendUrl The HTTP backend URL was formed dynamically using context variables.
httpBackend.requestError An error occurred making the request to the HTTP backend.
httpBackend.requestSent Request sent to the HTTP backend.
httpBackend.responseBodyError An error occurred whilst reading the response body from the HTTP backend.
httpBackend.responseReceived Response received from the HTTP backend.
httpBackend.urlInvalid The HTTP backend URL is not valid.
jwtAuthentication.authenticationFailed JWT Authentication failed.
jwtAuthentication.badJsonWebKeySet JSON Web Key Set is not valid.
jwtAuthentication.loadingJsonWebKeySet Loading the JSON Web Key Set.
jwtAuthentication.successfulAuthentication JWT Authentication successful.
logoutBackend.invalidAuthentication Logout path mismatch.
logoutBackend.logoutError An error occurred in the OAuth2 Logout Backend.
logoutBackend.redirectError The post logout redirect URL was not allowed.
mutualTls.clientCertificateInvalid The client certificate was missing or invalid.
mutualTls.clientCertificateSanInvalid The SANs contained within the client certificate failed validation.
queryParameterTransformation.badParameterValue Bad value for request query parameter.
rateLimiting.requestDenied The request was denied by the rate limiting policy.
rateLimiting.requestPermitted The request was permitted by the rate limiting policy.
request.bodyTooLarge The request body was too large.
request.clientCertConversionFailed The client certificate could not be converted to a string value.
request.clientEof A request could not be read due to a client error.
request.clientTimeout A request could not be read due to a client timeout.
request.internalServiceError Internal service error.
request.loopDetected A request loop condition has been detected, whereby requests for the gateway are being redirected to itself creating a cycle.
request.possibleLoopDetected A possible request loop condition has been detected, whereby requests for the gateway are being redirected to itself creating a cycle.
request.serviceUnavailable The gateway is currently unable to service the request.
requestValidation.validationError Request failed a validation policy.
requestValidation.validationPermitted Request passed a validation policy.
responseCache.backendResponseStorageAborted Backend response was not stored in the cache.
responseCache.backendResponseStoredInCache Backend response was stored in the cache.
responseCache.lookupAborted The response cache was not used.
responseCache.lookupResultNotFound A response was not found in the cache.
responseCache.lookupResultSuccess A response was read from the cache.
secretsClient.fetchFailure Failed to fetch client secret from secret service.
secretsClient.fetchSuccess Successfully fetched client secret from secret service.
secretsClient.unexpectedResponse Unexpected response from secret service while fetching client secret.
tokenAuthentication.authenticationFailed Token authentication failed.
tokenAuthentication.badDiscoveryEndpointResponse The remote discovery endpoint response is not valid.
tokenAuthentication.badIntrospectionResponse The token introspection response is not valid.
tokenAuthentication.badJsonWebKeySet JSON Web Key Set is not valid.
tokenAuthentication.loadingDiscoveryEndpointResponse Loading the remote discovery document.
tokenAuthentication.loadingJsonWebKeySet Loading the JSON Web Key Set.
tokenAuthentication.successfulAuthentication Token authentication successful.
usagePlans.eligibleNotEntitled The API deployment is not the target of an entitlement in any usage plan, even though the API deployment specification includes a usage plan request policy that specifies a client token.
usagePlans.requestBreachedButAllowed The request was allowed, even though the maximum number of requests specified by a usage plan entitlement was exceeded.
usagePlans.requestPermitted Request from a usage plan subscriber was allowed.
usagePlans.requestRejected Request from a usage plan subscriber was rejected.

## Sample Execution Logs
- Type: Request
- Scenario: Request Loop Detected
- Description: A request loop condition has been detected, whereby requests for the gateway are being redirected to itself creating a cycle.
- Example:
```

```
