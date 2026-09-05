# Forwarded and host-related headers sent to HTTP backends do not match backend expectations
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-forwarded_headers_do_not_match.htm
- Fetched: 2026-09-05 01:39 CDT

# Forwarded and host-related headers sent to HTTP backends do not match backend expectations

Find out how to troubleshoot forwarded and host-related headers sent to HTTP backends when calling APIs, having successfully created API gateways and API deployments with the API Gateway service.

Use this topic to troubleshoot forwarded and host-related headers that an HTTP back end receives through API Gateway. Header values can affect redirects, URL generation, access-control logic, and application routing.

API Gateway adds some forwarding headers, preserves some client-supplied values, appends values to some header chains, and rewrites the`Host`header for the back-end target. Verify the headers that the back end receives before you change application logic or deployment configuration.

## Issue Symptoms

You might see one or more of the following symptoms:
- 

The back-end service expects`Forwarded: host=<client-hostname>`, but the value is missing.
- 

The back-end service receives only`Forwarded: for=...`entries.
- 

The back-end service receives the back-end target hostname in the`Host`header instead of the client-facing hostname.
- 

Redirects, generated URLs, or host-based access-control logic work differently after the API is placed behind API Gateway.
- 

The back-end service receives multiple`Forwarded`or`X-Forwarded-For`values, and the application handles only one value.

## Possible Causes

Forwarded and host header mismatches can occur for the following reasons:
- 

The application expects`Forwarded: host=...`or`Forwarded: proto=...`, but API Gateway adds only a`for=...`entry by default.
- 

The application reads the`Host`header, but API Gateway rewrites that header for the back-end target.
- 

The application expects a single forwarding value, but the request contains a forwarding chain.
- 

The deployment does not include a request header transformation that passes the client-facing host to the back end.

## Understand Forwarded Header Behavior

For HTTP back ends, API Gateway adds request headers that contain client IP information.

The request to the back end can include the following headers:
- 

`X-Real-IP`
- 

`Forwarded`
- 

`X-Forwarded-For`
- 

`User-Agent: Oracle API Gateway`

The default`Forwarded`value is a`for=...`entry. API Gateway does not automatically add`host=...`or`proto=...`values to the`Forwarded`header.

If the client sends existing forwarding headers, API Gateway preserves those values and appends its own client IP information. The back end can therefore receive a chain of`Forwarded`or`X-Forwarded-For`values.

## Understand Host Header Behavior

For HTTP back ends, the`Host`header in the request to the back end is not the original client-facing host by default. API Gateway rewrites the`Host`header for the back-end target.

If the application needs the client-facing host, configure a request header transformation that copies the incoming`Host`value into a header that the application reads. For example, use the`request.host`context variable to copy the incoming host to`X-Forwarded-Host`or to an application-specific header.

Do not rely on the back-end request`Host`header to preserve the external hostname.

## Review Received Headers

Repeat the request through API Gateway and inspect the headers that the back end receives.

Review the following header values:
- 

The back-end visible`Forwarded`header.
- 

The back-end visible`X-Forwarded-For`header.
- 

The back-end visible`Host`header.
- 

The back-end visible`X-Forwarded-Host`header, if the route uses that header.
- 

Any custom header that the deployment creates from the incoming`Host`value.

If possible, use a temporary endpoint that echoes request headers. The echoed response shows the header values that arrived at the back end.

## Review the Deployment Configuration

Review the API deployment configuration in API Gateway to identify the matching route and any request header transformations on that route.

Confirm the following configuration values:
- 

The`backend.url`value for the route.
- 

The`routes.path`value that matched the request.
- 

The request header transformations on the matching route.

If the back end depends on the client-facing hostname, confirm that the route copies the incoming`Host`value into a header that the back end can read.

If the back end depends on`Forwarded: host=...`, confirm that your own header strategy sets that value. Do not assume that API Gateway creates the value automatically.

## Fix Forwarded and Host Header Issues

Apply the fix that matches the header value that the back end requires:
- 

If the back end can use`X-Forwarded-Host`, configure the route to send that header and update the application to read it.
- 

If the back end needs the client-facing host in a custom header, create a request header transformation from the incoming`Host`value.
- 

If the back end expects`Forwarded: host=...`, update the application to use the headers that API Gateway provides, or add an explicit header strategy that the application can consume.
- 

If the back end parses only one`Forwarded`or`X-Forwarded-For`value, update the application to handle a forwarding chain.

## Verify Forwarded and Host Headers

After you update the deployment or application logic, repeat the request and verify the result.

Confirm the following results:
- 

The back end receives the expected client-facing host value in the configured header.
- 

The back end handles multiple`Forwarded`or`X-Forwarded-For`values correctly.
- 

Redirects, generated URLs, and host-based logic use the expected hostname and scheme.
- 

Host-based access-control logic returns the expected response.

## For More Information

For more information, see:
- 

[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)
- 

[Transforming Incoming Requests and Outgoing Responses](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests.htm)
- 

[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm)
- 

[Miscellaneous errors when calling APIs](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Miscellaneous-issues.htm)
