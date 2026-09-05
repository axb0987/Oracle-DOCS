# Creating an Authorizer Function
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm
- Fetched: 2026-09-05 01:39 CDT

# Creating an Authorizer Function

Find out how to create multi-argument and single argument authorizer functions for use with API Gateway.

Depending on the functionality you require, you can write:
- (Recommended) A multi-argument authorizer function that accepts a user-defined, multi-argument access token comprising one or more elements of a request (see[Creating a Multi-Argument Authorizer Function (Recommended)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Multiargument_Authorizer_Function)). Note that multi-argument authorizer functions can accept single access tokens contained in a request header or query parameter.
- A single argument authorizer function that accepts a single-argument access token comprising a single value contained in a request header or query parameter (see[Creating a Single-Argument Authorizer Function](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Single-Argument_Authorizer_Function)).

## Creating a Multi-Argument Authorizer Function (Recommended)

To create an authorizer function that accepts a user-defined, multi-argument access token:
- 

Write code in the authorizer function that accepts JSON in the following format as input from API Gateway:

```

```

where:
- `"type": "USER_DEFINED"`indicates that the arguments and values being passed to the authorizer function are defined in the API deployment specification.
- `"<argument-n>"`is an argument name, corresponding to a user-defined argument name specified in the`parameters`section of the API deployment specification. For example,`"state"`,`"xapikey"`
- `"<context-variable-value>"`is the value of the context variable specified in the`parameters`section of the API deployment specification. For example, the value of the`request.query[state]`query parameter context variable, the value of the`request.headers[X-Api-Key]`header parameter context variable. Note that when passing multiple values to the authorizer function from request headers and query parameters,`"<context-variable-value>"`is passed to the authorizer function as an array. Also note that if the value for a context variable is not present in the original request to the API gateway, the context variable is not passed to the authorizer function.

For example, you might want the authorizer function to accept the values of the`request.query[state]`query parameter context variable and the`request.headers[X-Api-Key]`header parameter context variable as input from API Gateway. So, for example, if the values of the`request.query[state]`query parameter context variable and the`request.headers[X-Api-Key]`header parameter context variable are`california`and`abc123def456fhi789`respectively, the authorizer function must accept the following JSON input:

```

```

Note that if the`X-API-Key`header is not present in the original request to the API gateway, the`xapikey`context variable is not passed to the authorizer function at all (rather than being passed with a null value).
- 

Write code in the authorizer function that returns the following JSON to API Gateway as an HTTP 200 response when the user-defined, multi-argument access token has been successfully verified with an identity provider, and the identity provider has determined the token is valid:

```

```

where:
- `"active": true`indicates that the identity provider has determined that the access token originally passed to the authorizer function is valid. Note that this boolean field is optional, but defaults to`false`if not included in the JSON response.
- `"scope": ["<scopes>"]`is optionally the access scopes obtained by the authorizer function from the identity provider. Note that`["<scopes>"]`can be either a JSON array of comma-delimited strings, such as`["list:hello", "read:hello", "create:hello"]`, or a space-separated string such as`"list:hello read:hello create:hello"`. Note that this field is required if the authorization request policy's`type`property is set to`ANY_OF`.
- `"expiresAt": "<date-time>"`is optionally a date-time string in ISO-8601 format indicating when the access token originally passed to the authorizer function will expire. This value is used when determining how long to cache results after calling the authorizer function. You can cache results for a minimum of 60 seconds, and a maximum of 1 hour. Note that if this field is not included in the JSON response, or if`"<date-time>"`is invalid, results are cached for 60 seconds.
- `"context": {"<key>": "<value>", ... }`is an optional comma-delimited list of key-value pairs in JSON format to return to API Gateway. The authorizer function can return any key-value pair for use by the API deployment (for example, the username or email address of the end user). For more information about using the value in the key-value pair returned by an authorizer function as a context variable in an HTTP back end definition, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

For example:

```

```

When the authorizer function returns an HTTP 200 response and`active: true`in the JSON body of the response, API Gateway returns an HTTP 200 response to the API client.
- 

Write code in the authorizer function that returns the following JSON to API Gateway as an HTTP 200 response when the user-defined, multi-argument access token has been successfully verified with an identity provider, but the identity provider has determined the token is invalid:

```

```

where:
- `"active": false`indicates the identity provider has determined that the access token originally passed to the authorizer function is invalid. Note that this field is optional, but defaults to`false`if not present in the JSON response.
- `"wwwAuthenticate": "<directive>"`is optionally the value of the WWW-Authenticate header to be returned by the authorizer function if the access token is invalid, indicating the type of authentication that is required (such as Basic or Bearer). For example,`"wwwAuthenticate": "Bearer realm=\"example.com\""`. For more information, see[RFC 2617 HTTP Authentication: Basic and Digest Access Authentication](https://www.ietf.org/rfc/rfc2617.txt).

For example:

```

```

You can optionally include a`validationFailurePolicy`section in the API deployment specification to modify the response code, response message, and response headers that are returned to the API client. If you do not include a`validationFailurePolicy`section, API Gateway returns the WWW-Authenticate header in the response to the API client, along with a 401 status code. See[Notes on Validation Failure Policies and the Handling of Failed Authentication Responses from Multi-argument Authorizer Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Notes_on_Use_of_Multiargument_Authorizer_Function_and_Access_Tokens__notes-on-failed-authentication-responses).
- 

Write code in the authorizer function that returns an HTTP 5xx response if the token could not be verified with the identity provider (so it is not known whether the token is valid or invalid), or in the event of an error in the authorizer function or in OCI Functions.

When the authorizer function returns an HTTP 5xx response, API Gateway returns an HTTP 502 response to the API client. Any JSON in the body of the response is ignored.

## Creating a Single-Argument Authorizer Function

Note  
  
Oracle recommends the use of multi-argument authorizer functions rather than single-argument authorizer functions because of their additional versatility. Single-argument authorizer functions were provided in earlier releases, and continue to be supported. However, since multi-argument authorizer functions can also accept single-argument access tokens contained in request headers and query parameter, there is no reason to create new single-argument authorizer functions. Furthermore, single-argument authorizer functions are planned for deprecation in a future release.

To create an authorizer function that accepts a single-argument access token comprising a single value contained in a request header or query parameter:
- 

Write code in the authorizer function that accepts the following JSON input from API Gateway:

```

```

where:
- `"type": "TOKEN"`indicates that the value being passed to the authorizer function is an auth token.
- `"token": "<token-value>"`is the auth token being passed to the authorizer function.

For example:

```

```

- 

Write code in the authorizer function that returns the following JSON to API Gateway as an HTTP 200 response when the access token has been successfully verified with an identity provider, and the identity provider has determined the token is valid:

```

```

where:
- `"active": true`indicates that the identity provider has determined that the access token originally passed to the authorizer function is valid. Note that this boolean field is optional, but defaults to`false`if not included in the JSON response.
- `"scope": ["<scopes>"]`is optionally the access scopes obtained by the authorizer function from the identity provider. Note that`["<scopes>"]`can be either a JSON array of comma-delimited strings, such as`["list:hello", "read:hello", "create:hello"]`, or a space-separated string such as`"list:hello read:hello create:hello"`. Note that this field is required if the authorization request policy's`type`property is set to`ANY_OF`.
- `"expiresAt": "<date-time>"`is optionally a date-time string in ISO-8601 format indicating when the access token originally passed to the authorizer function will expire. This value is used when determining how long to cache results after calling the authorizer function. You can cache results for a minimum of 60 seconds, and a maximum of 1 hour. Note that if this field is not included in the JSON response, or if`"<date-time>"`is invalid, results are cached for 60 seconds.
- `"context": {"<key>": "<value>", ... }`is an optional comma-delimited list of key-value pairs in JSON format to return to API Gateway. The authorizer function can return any key-value pair for use by the API deployment (for example, the username or email address of an end user). For more information about using the value in the key-value pair returned by an authorizer function as a context variable in an HTTP back end definition, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

For example:

```

```

When the authorizer function returns an HTTP 200 response and`active: true`in the JSON body of the response, API Gateway returns an HTTP 200 response to the API client.

Note that the response from the single-argument authorizer function has the same format as a response from a multi-argument authorizer function (see[Creating a Multi-Argument Authorizer Function (Recommended)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Multiargument_Authorizer_Function)).
- 

Write code in the authorizer function that returns the following JSON to API Gateway as an HTTP 200 response when the access token has been successfully verified with an identity provider, but the identity provider has determined the token is invalid:

```

```

where:
- `"active": false`indicates the identity provider has determined that the access token originally passed to the authorizer function is invalid. Note that this field is optional, but defaults to`false`if not present in the JSON response.
- `"wwwAuthenticate": "<directive>"`is optionally the value of the WWW-Authenticate header to be returned by the authorizer function if the access token is invalid, indicating the type of authentication that is required (such as Basic or Bearer). For example,`"wwwAuthenticate": "Bearer realm=\"example.com\""`. For more information, see[RFC 2617 HTTP Authentication: Basic and Digest Access Authentication](https://www.ietf.org/rfc/rfc2617.txt).

For example:

```

```

API Gateway returns the WWW-Authenticate header in the response to the API client, along with a 401 status code.

Note that the response from the single-argument authorizer function has the same format as a response from a multi-argument authorizer function (see[Creating a Multi-Argument Authorizer Function (Recommended)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Multiargument_Authorizer_Function)).
- 

Write code in the authorizer function that returns an HTTP 5xx response if the token could not be verified with the identity provider (so it is not known whether the token is valid or invalid), or in the event of an error in the authorizer function or in OCI Functions.

When the authorizer function returns an HTTP 5xx response, API Gateway returns an HTTP 502 response to the API client. Any JSON in the body of the response is ignored.

For a related Developer Tutorial containing an example authorizer function, see[Functions: Validate an API Key with API Gateway](https://docs.oracle.com/iaas/Content/developer/functions/func-api-gtw-token/01-summary.htm)
