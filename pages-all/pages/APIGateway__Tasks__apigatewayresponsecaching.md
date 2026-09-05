# Caching Responses to Improve Performance
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm
- Fetched: 2026-09-05 01:38 CDT

# Caching Responses to Improve Performance

Find out how to use response caching request and response policies to reduce the number of requests sent to back-end services with API Gateway.

Typically, you'll want to avoid placing unnecessary load on back-end services to improve performance and reduce costs. One way to reduce that load is to cache responses to requests in case the responses can be re-used later. If similar requests are received, they can be satisfied by retrieving data from a response cache rather than sending the request to the back-end service.

The API Gateway service can integrate with an external cache server that you already have access to, such as a Redis or KeyDB server. You can configure API gateways managed by the API Gateway service to:
- Store data in the cache server that has been returned by a back-end service in response to an original request.
- Retrieve previously stored data from the cache server in response to a later request that is similar to the original request, without sending the later request to the back-end service.

To configure an API gateway for response caching, you:
- enable response caching on the API gateway (see[Enabling Response Caching on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#enablingresponsecaching))
- set up response caching for individual routes in the API gateway using request policies and response policies (see[Adding Response Caching Request and Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#addingresponsecachingpolicies))

You can set up response caching by:
- using the Console
- editing a JSON file

## How Does Response Caching Work?

When you have enabled an API gateway for response caching, the API gateway analyzes requests from API clients to routes that have response caching policies. The API gateway attempts to match a new request with previous similar requests for which responses are already stored in the cache server. The API gateway stores responses in the cache server for GET, HEAD, and OPTIONS requests, provided the responses have an HTTP status code of 200, 204, 301, or 410. Note that the API gateway uses the response caching request and response policies that you set up, and ignores any cache-control headers (if present) in the request or the response.

To uniquely identify responses in the cache server, the API gateway uses cache keys derived from the GET, HEAD, and OPTIONS requests that elicited the responses. By default, a cache key comprises:
- the URL of the request that elicited the response (excluding any query parameters in the URL)
- the HTTP method (one of GET, HEAD, or OPTIONS)
- the OCID of the API deployment that received the request

To more closely match cached responses with particular requests, you can optionally customize cache keys by adding the values of one or more context variables from the request to the cache key (see[Notes about Customizing Cache Keys](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_hmg_dbz_cpb)).

What happens next depends on whether the API gateway is able to match the new GET, HEAD, or OPTIONS request with a response from a previous similar request:
- If the API gateway finds a matching cache key in the cache server, the API gateway retrieves the corresponding response data from the cache server and sends it to the API client as the response.
- If the API gateway doesn't find a matching cache key in the cache server, the API gateway forwards the request to the back-end service. When the back-end service returns a response, the API gateway both sends the response to the API client and also stores the response in the cache server with a new cache key.
The API gateway adds an additional header to responses to GET, HEAD, and OPTIONS requests to routes that have response caching policies. The additional response header,`X-Cache-Status`, indicates whether the response has been retrieved from the cache server as follows:
- `X-Cache-Status: HIT`indicates a matching cache key was found in the cache server, so the response has been retrieved from the cache server.
- `X-Cache-Status: MISS`indicates no matching cache key was found in the cache server, so the response has come from the back-end service.
- `X-Cache-Status: BYPASS`indicates the cache server was not checked, so the response has come from the back-end service. Reasons for not checking the cache server include problems communicating with the cache server, and configuration settings that prevent responses for specific requests being retrieved from the cache server.

Tip: If you don't want responses to contain the additional`X-Cache-Status`header, use a header transformation response policy to remove it (see[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm)).

## Notes about Response Caching and Security

To ensure that data on the cache server is stored and accessed securely:
- You set up the API gateway to authenticate with the cache server using credentials saved as a secret in a vault in the Vault service.
- You can specify whether to set up a secure connection over TLS (formerly SSL) between the API gateway and a TLS-enabled cache server, and whether to verify TLS certificates. Note that only certificates signed by public certificate authorities are currently verified.
- You can specify an expiry time to ensure that cached data is not stored for an overly long period, and that stale data is not returned from the cache server in response to a later request.
- You can limit the request URLs that match cache keys by customizing cache keys to include one or more parameters present in request URLs (see[Notes about Customizing Cache Keys](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_hmg_dbz_cpb)).
- You can specify not to cache responses for requests that include credentials (see[Notes about Caching Responses for Requests Containing Credentials (Private Caching)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_ll5_bbz_cpb)).

Note that it is your responsibility to ensure that the cache server itself is configured correctly to secure the data stored on it. Specifically, Oracle strongly recommends you do not reuse an existing cache server. Instead, Oracle recommends you set up a new cache server solely for API gateway response caching, and restrict access to the cache server to just API gateways.

## Notes about Caching Responses for Requests Containing Credentials (Private Caching)

Requests can include authorization headers that contain the credentials to authenticate an API client with a back-end service. The credentials typically provide access to data that is private to an individual or organization. For example, a request authorization header containing an authentication token could be used to elicit a response containing bank account information. The existence of authorization headers in a request is an indication that the response might be of a sensitive nature and only to be shared with those allowed to see it.

Similarly, if you have used authorizer functions for authentication and authorization, an authentication policy identifies a header or query parameter in a request that contains an access token (see[Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)). The existence in a request of the header or query parameter identified in an authentication policy is also an indication that the response might be of a sensitive nature and only to be shared with those allowed to see it.

Caching responses for requests that contain authorization headers, or that contain a header or query parameter identified in an authentication policy, is referred to as 'private caching'. Although private caching can speed up responses to similar requests in future, it does have the potential to compromise data security. Therefore, to avoid security breaches, private caching is disabled by default. However, on a route-by-route basis, you can enable private caching.

If you do decide to enable private caching, we recommend you customize the cache key to isolate responses so each response is only returned to those allowed to see it. For example:
- Add the value of the request authorization header, or the value of the header or query parameter identified in an authentication policy, to the cache key as a context variable from a context table.
- If you have used authorizer functions or JWTs for authentication and authorization, add the value of a context variable that identifies the request principal (such as`sub`or`principalId`) to the cache key from the`request.auth`context table. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).

A cached response with a value in its cache key for a context variable will only be returned in response to a request that has a matching value.

It is your responsibility to specify a cache key addition that provides sufficient isolation between cached responses. See[Notes about Customizing Cache Keys](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_hmg_dbz_cpb).

## Notes about Customizing Cache Keys

Responses stored in the cache server are uniquely identified by a cache key. By default, a cache key is derived from the URL of the request that elicited the response (excluding any context variables present in the request), the HTTP method, and the OCID of the API deployment. To more closely match cached responses with particular requests, you can optionally customize cache keys by adding the values of one or more context variables from the request to the cache key. If you decide to enable private caching for requests that contain authorization headers, or that contain a header or query parameter identified in an authentication policy, we recommend you add their values as context variables to the cache key.

To specify the context variable values to add to the cache key, use the format`<context-table-name>.[<key>]`where:
- `<context-table-name>`is one of`request.query`,`request.headers`, or`request.auth`
- `<key>`is one of:
- a query parameter name included in the request to the API
- a header name included in the request to the API
- an authentication parameter name returned by an authorizer function or contained in a JWT token
- the`Host`header field in the request to the API

For example:
- To add the value of the`X-Username`context variable to a cache key when it is included in a request header, specify`request.headers[X-Username]`as a cache key addition.
- To add the request principal (the person or application sending the request) to a cache key when it is included as the`sub`claim in a JWT token, specify`request.auth[sub]`as a cache key addition.
- To add the value of the`Authorization`header to a cache key, specify`request.headers[Authorization]`as a cache key addition.
- To add the value of an access token returned by an authorizer function and contained in a header named`X-Custom-Auth`to a cache key, specify`request.headers[X-Custom-Auth]`as a cache key addition.
- To add the value of the`Host`header field included in the the request to a cache key, specify`request.host`.

For more information about context variables, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

## Prerequisites for Response Caching

Before you can enable response caching for an API gateway:
- A cache server that implements the RESP protocol (such as Redis or KeyDB) must have been set up already, and must be available.
- The API gateway's subnet must be able to access the cache server.
- The cache server must be hosted on a single cache server host, and not distributed across multiple instances in a cluster.
- You must have already stored the credentials to authenticate with the cache server as a secret in a vault in the Vault service (see[Creating a Secret in a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm)), and you must know the OCID and version number of the secret. When specifying the contents of the secret, use the format`{"username":"<cache-server-username>", "password":"<cache-server-password>"}`. Note that specifying a username is optional. For example:

```

```

- You must have already set up a policy to give API gateways in a dynamic group permission to access the secret in the Vault service that contains the credentials to authenticate with the cache server (see[Create a Policy to Give API Gateways Access to Credentials Stored as Secrets in the Vault Service](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy-5)).

## Enabling Response Caching on an API Gateway

You can enable response caching on an API gateway using the Console or by editing a JSON file.

### Using the Console to Enable and Configure Response Caching

To enable and configure response caching for an API gateway using the Console:
- 

Create or update an API gateway using the Console.

For more information, see[Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the Advanced options section of the Create gateway dialog, select Enable response caching and:
- Specify Cache server options, as follows:
- Host: The host name of the cache server. For example,`"cache.example.com"`.
- Port number: The port number on the cache server. For example,`6379`.
- Specify Cache server credentials options, as follows:
- Vault: The name of the vault in the Vault service that contains the credentials to log into the cache server, from the list of vaults in the specified compartment.
- Vault Secret: The name of the secret in the specified vault that contains the credentials to log into the cache server, from the list of vault secrets in the specified compartment.
- Vault Secret Version Number: The version of the secret to use.
- Specify Cache server connection settings options, as follows:
- Use SSL/TLS in requests: Whether the cache server is TLS-enabled, and therefore whether to set up a secure connection between the API gateway and the cache server over TLS (formerly SSL).
- Verify SSL/TLS certificate: Whether the API gateway verifies the cache server's TLS (formerly SSL) certificate. Note that only certificates signed by public certificate authorities are currently verified.
- Connect Timeout in milliseconds: How long to wait before abandoning an attempt to connect to the cache server, in milliseconds. If the API gateway cannot connect to the cache server within this time, the API gateway does not retrieve previously cached data from the cache server, and does not write new data to the cache server for potential future reuse.
- Send Timeout in milliseconds: How long to wait before abandoning an attempt to write data to the cache server, in milliseconds. If the API gateway cannot send data to the cache server within this time, a response is not cached for potential future reuse.
- Read Timeout in milliseconds: How long to wait before abandoning an attempt to read data from the cache server, in milliseconds. If the API gateway cannot retrieve data from the cache server within this time, the API gateway sends a request to the back-end service instead.
- Select Create or Update to create or update the API gateway.

### Using the CLI and a JSON File to Enable and Configure Response Caching

To enable and configure response caching for an API gateway using the CLI and a JSON file:
- 

Using your preferred JSON editor, create a cache configuration file in the format:

```

```

where:
- `"type" : "EXTERNAL_RESP_CACHE"`indicates that response caching is to be enabled. If not set, the default is`"type" : "NONE"`, indicating that response caching is disabled.
- `"host" : "<cache-server-hostname>"`is the host name of the cache server. For example,`"host" : "cache.example.com"`.
- `"port" : <port-number>`is the port number on the cache server. For example,`"port" : 6379`.
- `"authenticationSecretId" : "<secret-ocid>"`is the OCID of the secret defined in a vault in the Vault service that contains the credentials to log into the cache server. For example,`"authenticationSecretId" : "ocid.oc1.sms.secret.aaaaaa______gbdn"`
- `"authenticationSecretVersionNumber" : <secret-version-number>`is the version of the secret to use. For example,`"authenticationSecretVersionNumber" : 1`
- `"isSSLEnabled" : <true|false>`indicates whether the cache server is TLS-enabled, and therefore whether to set up a secure connection between the API gateway and the cache server over TLS (formerly SSL). If not set, the default is`false`
- `"isSSLVerifyDisabled" : <true|false>`indicates whether the API gateway verifies the cache server's TLS (formerly SSL) certificate. Note that only certificates signed by public certificate authorities are currently verified. If not set, the default is`false`
- `"connectTimeoutInMs" : <milliseconds>`indicates how long to wait before abandoning an attempt to connect to the cache server, in milliseconds. If the API gateway cannot connect to the cache server within this time, the API gateway does not retrieve previously cached data from the cache server, and does not write new data to the cache server for potential future reuse. If not set, the default is`1000`. For example,`"connectTimeoutInMs" : 1500`
- `"readTimeoutInMs" : <milliseconds>`indicates how long to wait before abandoning an attempt to read data from the cache server, in milliseconds. If the API gateway cannot retrieve data from the cache server within this time, the API gateway sends a request to the back-end service instead. If not set, the default is`1000`. For example,`"readTimeoutInMs" : 250`
- `"sendTimeoutInMs" : <milliseconds>`indicates how long to wait before abandoning an attempt to write data to the cache server, in milliseconds. If the API gateway cannot send data to the cache server within this time, responses are not cached for potential future reuse. If not set, the default is`1000`. For example,`"sendTimeoutInMs" : 1250`

For example:

```

```

- Save the cache configuration file with a name of your choice. For example,`resp-cache-config.json`
- Use the cache configuration file when you create or update an API gateway using the CLI:
- To create a new API gateway with response caching enabled, follow the CLI instructions in[Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm)and set the`--response-cache-details`parameter to the name and location of the cache configuration file. For example:

```

```

- To update an existing API gateway to enable response caching or change response caching settings, follow the CLI instructions in[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm)and set the`--response-cache-details`parameter to the name and location of the cache configuration file. For example:

```

```

## Adding Response Caching Request and Response Policies

You can add response caching request and response policies to API deployment specifications using the Console or by editing a JSON file. Note that you must enable response caching on an API gateway for the request and response policies to take effect.

### Using the Console to Add Response Caching Request and Response Policies

To add response caching request and response policies to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

Select Next and specify authentication options on the Authentication page.

For more information about authentication options, see[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- 

Select Next to enter details for individual routes in the API deployment on the Routes page.
- 

On the Routes page, select the route for which you want to specify response caching request and response policies.
- 

Select Show response caching policies .
- Select Enable caching for this route and specify the response caching options that apply to this particular route:
- TTL (Time To Live) for cached responses in seconds: How long cached data is available in the cache server for this particular route.
- Cache key additions: One or more context variables to add to the default cache key to more closely associate a cached response with a particular request. For example,`request.headers[X-Username]`. You can select from a list of commonly-used context variables, or enter a context variable of your choice. Do not precede the context variable with a $ symbol or enclose it within curly brackets (as you would do if you were adding the context variable to a URL in an API deployment specification in a JSON file). For more information, see[Notes about Customizing Cache Keys](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_hmg_dbz_cpb).
- If you want to cache responses for requests that contain an authorization header, or that contain a header or query parameter identified in an authentication policy, select the Cache responses with authorization headers option.

Note that caching responses for such requests might compromise data security. For more information, see[Notes about Caching Responses for Requests Containing Credentials (Private Caching)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_ll5_bbz_cpb).
- Select Update .
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

### Editing a JSON File to Add Response Caching Request and Response Policies

To add response caching to a particular route, you have to add both a request policy and a response policy.

To add the response caching request and response policy to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add response caching, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

To specify the response caching request and response policy that applies to an individual route:
- 

Insert both a`requestPolicies`section and a`responsePolicies`section after the backend section for the route to which you want the policy to apply. For example:

```

```

- Add the following`responseCacheLookup`request policy to the new`requestPolicies`section to apply to the route:

```

```

where:
- `"type": "SIMPLE_LOOKUP_POLICY"`is the type of response caching to implement. Only`"SIMPLE_LOOKUP_POLICY"`is currently supported.
- `"isEnabled": true`indicates that response caching is enabled for the route. If you want to temporarily disable response caching, set`"isEnabled": false`. If not specified, the default is`true`.
- `"isPrivateCachingEnabled": <true|false>`indicates whether to cache responses for requests that contain an authorization header, or that contain a header or query parameter identified in an authentication policy. Note that caching responses for such requests might compromise data security. If not specified, the default is`false`indicating that responses for such requests are not cached. For more information, see[Notes about Caching Responses for Requests Containing Credentials (Private Caching)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_ll5_bbz_cpb).
- `"cacheKeyAdditions": [<list-of-context-variables>]`is an optional comma-separated list of context variables to add to the default cache key to more closely associate a cached response with a particular request. For example,`"cacheKeyAdditions": ["request.headers[Accept]"]`. Do not precede the context variable with a $ symbol or enclose it within curly brackets (as you would do if you were adding the context variable to a URL in an API deployment specification in a JSON file). For more information, see[Notes about Customizing Cache Keys](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayresponsecaching.htm#Response_Caching__section_hmg_dbz_cpb).
- Add the following`responseCacheStorage`response policy to the new`responsePolicies`section to apply to the route:

```

```

where:
- `"type": "FIXED_TTL_STORE_POLICY"`is the type of response cache in which to store responses. Only`"FIXED_TTL_STORE_POLICY"`is currently supported.
- `"timeToLiveInSeconds": <seconds>`specifies how long cached data is available in the cache server for this particular route. For example,`"timeToLiveInSeconds": 300`

For example:

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
