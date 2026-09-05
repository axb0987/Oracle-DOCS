# Adding CORS support to API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding CORS support to API Deployments

Find out how to use a request policy to add CORS support to API deployments with API Gateway.

Web browsers typically implement a "same-origin policy" to prevent code from making requests against a different origin to the one from which the code was served. The intention of the same-origin policy is to provide protection from malicious web sites. However, the same-origin policy can also prevent legitimate interactions between a server and clients of a known and trusted origin.

Cross-Origin Resource Sharing (CORS) is a cross-origin sharing standard to relax the same-origin policy by allowing code on a web page to consume a REST API served from a different origin. The CORS standard uses additional HTTP request headers and response headers to specify the origins that can be accessed.

The CORS standard also requires that for certain HTTP request methods, the request must be "pre-flighted". Before sending the actual request, the web browser sends a pre-flight request to the server to determine whether the methods in the actual request are supported. The server responds with the methods it will allow in an actual request. The web browser only sends the actual request if the response from the server indicates that the methods in the actual request are allowed. The CORS standard also enables servers to notify clients whether requests can include credentials (cookies, authorization headers, or TLS client certificates).

For more information about CORS, see resources available online including those from[W3C](https://www.w3.org/TR/cors/)and[Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

Using the API Gateway service, you can enable CORS support in the APIs you deploy to API gateways. When you enable CORS support in an API deployment, HTTP pre-flight requests and actual requests to the API deployment return one or more CORS response headers to the API client. You set the CORS response header values in the API deployment specification.

You use request policies to add CORS support to APIs (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)). You can apply a CORS request policy globally to all routes in an API deployment specification, or just to particular routes.

You can add a CORS request policy to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add CORS Request Policies

To add a CORS request policy to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the API Request Policies section of the Basic information page, select the Add button beside CORS and specify:
- Origins: An origin that is allowed to access the API deployment. For example,`https://oracle.com`. Select Another origin to enter second and subsequent origins.
- Methods: One or more methods that are allowed in the actual request to the API deployment. For example,`GET, PUT`.
- Headers: Optionally, an HTTP header that is allowed in the actual request to the API deployment. For example,`opc-request-id`or`If-Match`. Select Another header to enter second and subsequent headers.
- Exposed headers: Optionally, an HTTP header that API clients can access in the API deployment's response to an actual request. For example,`ETag`or`opc-request-id`. Select Another header to enter second and subsequent headers.
- Max age in seconds: Optionally, an integer value indicating how long (in delta-seconds) the results of a preflight request can be cached by a browser. If you don't specify a value, the default is`0`.
- Enable allow credentials: Whether the actual request to the API deployment can be made using credentials (cookies, authorization headers, or TLS client certificates). By default, this option is not selected.

To find out how the different fields in the CORS request policy map onto different CORS response headers, see[How a CORS Request Policy Maps to a CORS Response](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm#corsfields).
- 

Select Update .
- 

Select Next to specify authentication options on the Authentication page.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to enter details for individual routes in the API deployment on the Routes page. To specify CORS request policies that apply to an individual route, select Show route request policies , select the Add button beside CORS , and specify:
- Origins: An origin that is allowed to access the route. For example,`https://oracle.com`. Select Another origin to enter second and subsequent origins.
- Methods: One or more methods that are allowed in the actual request to the route. For example,`GET, PUT`.
- Headers: Optionally, an HTTP header that is allowed in the actual request to the route. For example,`opc-request-id`or`If-Match`. Select Another header to enter second and subsequent headers.
- Exposed headers: Optionally, an HTTP header that API clients can access in the API deployment's response to an actual request. For example,`ETag`or`opc-request-id`. Select Another header to enter second and subsequent headers.
- Max age in seconds: Optionally, an integer value indicating how long (in delta-seconds) the results of a preflight request can be cached by a browser. If you don't specify a value, the default is`0`.
- Enable allow credentials: Whether the actual request to the route can be made using credentials (cookies, authorization headers, or TLS client certificates). By default, this option is not selected.

To find out how the different fields in the CORS request policy map onto different CORS response headers, see[How a CORS Request Policy Maps to a CORS Response](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm#corsfields).
- Select Update , and then select Next to review the details you entered for the API deployment and for individual routes.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add CORS Request Policies

To add a CORS request policy to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add CORS support, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

To specify a CORS request policy that applies globally to all the routes in an API deployment:
- 

Insert a`requestPolicies`section before the`routes`section, if one doesn't exist already. For example:

```

```

- 

Add the following`cors`policy to the new`requestPolicies`section to apply globally to all the routes in an API deployment:

```

```

where:
- `"allowedOrigins": [<list-of-origins>]`is a required comma-separated list of origins that are allowed to access the API deployment. For example`, "allowedOrigins": ["*", "https://oracle.com"]`
- `"allowedMethods": [<list-of-methods>]`is an optional comma-separated list of HTTP methods that are allowed in the actual request to the API deployment. For example,`"allowedMethods": ["*", "GET"]`
- `"allowedHeaders": [<list-of-implicit-headers>]`is an optional comma-separated list of HTTP headers that are allowed in the actual request to the API deployment. For example,`"allowedHeaders": ["opc-request-id", "If-Match"]`
- `"exposedHeaders": [<list-of-exposed-headers>]`is an optional comma-separated list of HTTP headers that API clients can access in the API deployment's response to an actual request. For example,`"exposedHeaders": ["ETag", "opc-request-id"]`
- `"isAllowCredentialsEnabled": <true|false>`is either`true`or`false`, indicating whether the actual request to the API deployment can be made using credentials (cookies, authorization headers, or TLS client certificates). If not specified, the default is`false`.
- `"maxAgeInSeconds": <seconds>`is an integer value, indicating how long (in delta-seconds) the results of a preflight request can be cached by a browser. If not specified, the default is`0`.

For example:

```

```

To find out how the different fields in the CORS request policy map onto different CORS response headers, see[How a CORS Request Policy Maps to a CORS Response](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm#corsfields).
- 

To specify a CORS request policy that applies to an individual route:
- 

Insert a`requestPolicies`section after the backend section for the route to which you want the policy to apply. For example:

```

```

- Add the following`cors`policy to the new`requestPolicies`section to apply to just this particular route:

```

```

where:
- `"allowedOrigins": [<list-of-origins>]`is a required comma-separated list of origins that are allowed to access the API deployment. For example`, "allowedOrigins": ["*", "https://oracle.com"]`
- `"allowedMethods": [<list-of-methods>]`is an optional comma-separated list of HTTP methods that are allowed in the actual request to the API deployment. For example,`"allowedMethods": ["*", "GET"]`
- `"allowedHeaders": [<list-of-implicit-headers>]`is an optional comma-separated list of HTTP headers that are allowed in the actual request to the API deployment. For example,`"allowedHeaders": ["opc-request-id", "If-Match"]`
- `"exposedHeaders": [<list-of-exposed-headers>]`is an optional comma-separated list of HTTP headers that API clients can access in the API deployment's response to an actual request. For example,`"exposedHeaders": ["ETag", "opc-request-id"]`
- `"isAllowCredentialsEnabled": <true|false>`is either`true`or`false`, indicating whether the actual request to the API deployment can be made using credentials (cookies, authorization headers, or TLS client certificates). If not specified, the default is`false`.
- `"maxAgeInSeconds": <seconds>`is an integer value, indicating how long (in delta-seconds) the results of a preflight request can be cached by a browser. If not specified, the default is`0`.

For example:

```

```

To find out how the different fields in the CORS request policy map onto different CORS response headers, see[How a CORS Request Policy Maps to a CORS Response](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingcorssupport.htm#corsfields).
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## How a CORS Request Policy Maps to a CORS Response

The different fields in a CORS request policy map onto different CORS response headers as shown in the table:

Field Maps to CORS response header Included in response to pre-flight request Included in response to actual request Notes
`allowed Origins`[Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)Yes Yes

Required?: Yes

Datatype: string[]

Default: n/a

Used to return a comma-separated list of origins that are allowed to access the API deployment.

Only one origin is allowed by the CORS specification, so in the case of multiple origins the client origin needs to be dynamically checked against the list of allowed values. Values "*" and "null" are allowed.
`allowed Methods`[Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods)Yes No

Required?: No

Datatype: string[]

Default: empty list

Used to return a comma-separated list of HTTP methods that are allowed in the actual request to the API deployment.

The default of Access-Control-Allow-Methods is to allow through all simple methods, even on preflight requests.
`allowed Headers`[Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers)Yes No

Required?: No

Datatype: string[]

Default: empty list

Used to return a comma-separated list of HTTP headers that are allowed in the actual request to the API deployment.
`exposed Headers`[Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers)No Yes

Required?: No

Datatype: string[]

Default: empty list

Used to return a comma-separated list of HTTP headers that clients can access in the API deployment's response to an actual request. This list of HTTP headers is in addition to the CORS-safelisted response headers.
`isAllow Credentials Enabled`[Access-Control-Allow-Credentials](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)Yes Yes

Required?: No

Datatype: boolean

Default:`false`

Used to return`true`or`false`, indicating whether the actual request to the API deployment can be made using credentials (cookies, authorization headers, or TLS client certificates).

To allow requests to be made with credentials, set`isAllowCredentialsEnabled`to`true`.
`maxAge InSeconds`[Access-Control-Max-Age](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age)Yes No Required?: No

Datatype: integer

Default:`0`Used to indicate how long (in delta-seconds) the results of a preflight request can be cached by a browser. Ignored if set to`0`
