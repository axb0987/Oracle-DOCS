# API Gateway Internal Limits
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/apigatewaylimits.htm
- Fetched: 2026-09-05 01:37 CDT

# API Gateway Internal Limits

Find out about the API Gateway internal limits, their default values, and whether you can change them.

## API Gateway Resource Limits

This table describes internal limits enforced by the API Gateway service on API gateway resources.

Limit Description Default Limit Value Can you change it?
Number of API gateways Maximum number of active API gateways per tenant.

(Shown as Gateway Count in the Console.)

50 (Monthly or Annual Universal Credits)

5 (Pay-as-You-Go or Promo) Yes,[contact us](https://support.oracle.com/).
Number of CA bundles per API gateway Maximum total number of CA bundles from the Certificates service that can be specified across all APIs deployed on an API gateway. 2 CA bundles per API gateway Yes,[contact us](https://support.oracle.com/).
Number of CAs per API gateway Maximum total number of CAs from the Certificates service that can be specified across all APIs deployed on an API gateway. 5 CAs per API gateway Yes,[contact us](https://support.oracle.com/).
Client certificate verification depth Maximum number of CA certificates that can be traversed in a certificate chain to validate a TLS certificate presented by an API client. 3 No.
Backend TLS certificate verification depth Maximum number of CA certificates in the certificate chain that issued the backend TLS certificate. 3 No.

## API Deployment Resource Limits

This table describes internal limits enforced by the API Gateway service on API deployment resources.

Limit Description Default Limit Value Can you change it?
Number of API deployments Maximum number of active API deployments per gateway. 20 No
Number of routes per API deployment Maximum number of routes defined inside the API deployment specification. 50 No
Path prefix length Maximum length of path for API deployment. 255 characters No
Route pattern length Maximum length of path for a route in an API deployment. 2,000 characters No
API deployment specification Size Maximum length of json encoded API deployment specification in bytes. 2 MB No
Stock Response - header length Maximum length of UTF-8 encoded json of stock response headers. 4096 bytes No
Stock Response - header name length Maximum length of a stock response header name. 1024 bytes No
Stock Response - header value length Maximum length of a stock response header value. 4096 bytes No
Stock Response - number of headers Maximum number of stock response headers. 50 No
Stock Response - body size Maximum body size in UTF-8 bytes. 4096 bytes No
Stock Response - request body size Maximum body size of a request to a stock response back end. 20 MB No
CORS Policy - number of headers Maximum number of CORS allowed/exposed headers. 50 No
CORS Policy - number of allowed methods Maximum number of CORS allowed methods. 50 No
Number of allowed subject alternative names inside client certificate per deployment Maximum number of SANs allowed inside client certificate specified as part of client mTLS. 10 Yes,[contact us](https://support.oracle.com/).
Number of routing backends defined per route Maximum number of routing backends allowed per route. 100 Yes,[contact us](https://support.oracle.com/).
Number of unique static key values defined per routing backend Maximum number of unique static key values allowed per routing backend. 100 Yes,[contact us](https://support.oracle.com/).
Number of authentication servers defined per deployment Maximum number of authentication servers defined per API deployment. 100 Yes,[contact us](https://support.oracle.com/).
Number of unique static key values defined per authentication server Maximum number of unique static key values defined per authentication server. 100 Yes,[contact us](https://support.oracle.com/).
Number of key-value pairs in parameters Maximum number of key-value pairs passed to multi-argument authorizer functions. 10 No
Number of values in cache key Maximum number of values for forming cache key for caching authentication response. 10 No
Number of Post Logout Urls Maximum number of allowed post-logout URLs per logout back end. 10 Yes,[contact us](https://support.oracle.com/).

## API Gateway Certificate Resource Limits

This table describes internal limits enforced by the API Gateway service on API Gateway certificate resources.

Limit Description Default Limit Value Can you change it?
Leaf Certificate - maximum length Maximum length of the leaf certificate. 4096 bits No
Intermediate Certificates - maximum length Maximum combined length of any intermediate certificates. 10240 bits No
Private key- maximum length Maximum private key size. 4096 bits No
Private key - minimum length Minimum private key size. 2048 bits No

## HTTP Back End Resource Limits

This table describes internal limits enforced by the API Gateway service on HTTP back ends.

Limit Description Default Limit Value Can you change it?
Connect timeout Maximum configurable HTTP back end connect timeout in seconds. 60.0 seconds Yes, by changing the timeout setting in the API deployment specification to between 1.0 and 75.0 seconds (see[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/../Tasks/apigatewayusinghttpbackend.htm)).
Read timeout Maximum configurable HTTP back end read timeout in seconds. 10.0 seconds Yes, by changing the timeout setting in the API deployment specification to between 1.0 and 300.0 seconds (see[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/../Tasks/apigatewayusinghttpbackend.htm)).
Send timeout Maximum configurable HTTP back end send timeout in seconds. 10.0 seconds Yes, by changing the timeout setting in the API deployment specification to between 1.0 and 300.0 seconds (see[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Reference/../Tasks/apigatewayusinghttpbackend.htm)).

## API Gateway Invocation Limits

This table describes internal limits enforced by the API Gateway service on API gateway invocations.

Limit Description Default Limit Value Can you change it?
Simultaneous connections per IP address

Maximum number of simultaneous HTTPS connections to an API gateway:
- from a single IPv4 address
- from an IPv6 /64 prefix range 1000 No
Request body size Maximum request body size. 20 MB No
Request header read timeout Time between reads of request header bytes. 15 seconds No
Request body read timeout Time between reads of request body bytes. 15 seconds No
Response body read timeout Time between sends of response body bytes. 15 seconds No
Maximum header size Maximum length of header (including method, URI, and headers). 8 KB No
Function request body size Maximum body size of a request to a function back end. 6 MB No
Maximum cached response size Maximum size of a single cached response. 50 MB No

## SDK Resource Limits

This table describes internal limits enforced by the API Gateway service on SDK resources.

Limit Description Default Limit Value Can you change it?
Number of SDKs per tenancy Maximum number of SDKs per tenancy.

(Shown as SDK Artifact Count in the Console.) 500 SDKs No
SDK maximum size Maximum size of any one SDK. 50 MB No
SDK creation limit Maximum number of requests to create SDKs. 1 request per minute No
SDK list limit Maximum number of requests to list SDKs. 100 requests per minute (20 requests per second) No
SDK download limit Maximum number of requests to download SDKs. 4 requests per minute No
SDK deletion limit Maximum number of requests to delete SDKs. 4 requests per minute No
SDK update limit Maximum number of requests to update SDKs. 1 request per minute No
SDK list language limit Maximum number of requests to list the available languages for generating SDKs. 100 requests per minute (20 requests per second) No

## Usage Plan and Subscriber Resource Limits

This table describes internal limits enforced by the API Gateway service on usage plan resources and subscriber resources.

Limit Description Default Limit Value Can you change it?
Number of usage plans per tenant Maximum number of usage plans per tenant. 20 No
Number of subscribers per tenant Maximum number of subscribers per tenant. 1,000 No
Usage plan size Maximum length of JSON-encoded usage plan definition in bytes. 1 MB No
Subscriber size Maximum length of JSON-encoded subscriber definition in bytes. 4 KB No
Number of clients per subscriber Maximum number of clients per subscriber. 5 No
Number of entitlements per usage plan Maximum number of entitlements per usage plan. 200 No
Number of targets per entitlement Maximum number of targets per entitlement. 200 No
Number of route names per entitlement target Maximum number of route names per entitlement target. 50 No
Number of usage plans per subscriber Maximum number of usage plans per subscriber. 10 No

## API Limits

This table describes internal limits enforced by the API Gateway service on API resources.

Limit Description Default Limit Value Can you change it?
Number of API resources Maximum number of API resources.

(Shown as API Count in the Console.) 100 No
