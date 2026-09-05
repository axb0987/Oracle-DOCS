# Adding Authentication and Authorization Request Policies for Multi-Argument Access Tokens and Authorizer Functions (Recommended)
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Authentication and Authorization Request Policies for Multi-Argument Access Tokens and Authorizer Functions (Recommended)

Add request policies to provide authentication and authorization using user-defined, multi-argument access tokens and multi-argument authorizer functions.

You can add request policies by:
- [using the Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Using_the_Console_to_Add_Multiargument_Authorizer_Function_Authentication_Request_Policies)
- [editing a JSON file](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Editing_a_JSON_File_to_Add_Multiargument_Authorizer_Function_Authentication_Request_Policies)

## Using the Console to Add Request Policies for Multi-Argument Authentication and Authorization

To add authentication and authorization request policies for multi-argument access tokens to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- Select Next to display the Authentication page.
- 

Select Single Authentication to specify that you want to use a single authentication server for all requests.

These instructions assume you want to use a single authentication server. Alternatively, if you want to use multiple authentication servers, select Multi-Authentication and follow the instructions in[Using the Console to Add Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm#apigatewayaddingmultipleauthorizationservers_topic-Using_the_Console).
- 

Select or deselect Enable anonymous access to specify whether unauthenticated (that is, anonymous) end users can access routes in the API deployment.

By default, this option is not selected. If you never want anonymous users to be able to access routes, don't select this option. Note that if you do select this option, you also have to explicitly specify every route to which anonymous access is allowed by selecting Anonymous as the Authorization type in each route's authorization policy.
- Select Authorizer function from the Authentication type option list.
- Specify the multi-argument authorizer function to use to authenticate the multi-argument access token:
- Oracle Functions application: The name of the application in OCI Functions that contains the authorizer function. You can select an application from a different compartment.
- Oracle Function: The name of the authorizer function in OCI Functions.
- Select Multi-argument authorizer function to specify that you want to pass one or more elements of a request as an access token to an authorizer function that can accept multi-argument access tokens.
- In the Function arguments panel, specify one or more context variables providing values to pass to the authorizer function as arguments with argument names you enter:
- Specify a context variable providing a value to pass to the authorizer function as an argument:
- Context table: Select the context table containing the context variable from the list:
- `request.query`context table, containing query parameter names and values included in the request
- `request.headers`context table, containing header names and values included in the request
- `request.cert`context table, containing a Base64-encoded version of the certificate presented by an API client and successfully validated during an mTLS handshake
- `request.host`context table, containing the name of the host to which the request was sent (extracted from the`Host`header field in the request)
- `request.body`context table, containing the body of the request
- Header name or Query param name: If you selected the`request.headers`or`request.params`context table, enter the name of the header or query parameter that you want to pass to the authorizer function. For example,`X-Api-Key`,`state`.
- Argument name: Enter the name of the argument to which to assign the value of the context variable. The argument is passed to the authorizer function. The argument name you enter must correspond to the argument name that the authorizer function expects to receive.
- Specify additional context variables and arguments as required (select Another argument if necessary).
- 

Optionally, customize how to cache the response from a multi-argument authorizer function:
- Select Advanced options .

The Function results caching panel shows which arguments are present in the cache key. The cache key uniquely identifies the cached response returned from the authorizer function, using arguments and argument values passed in the original authentication request. By default, all arguments and argument values (except for an argument with a value from the`request.body`context table) you specified to pass to the authorizer function are used to create the cache key.
- To add or remove arguments from the cache key, select Edit .
- Select or deselect the arguments passed to authorizer function to include or exclude them from the cache key.

See[Notes on the Caching of Multi-argument Authorizer Function Results](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Notes_on_Use_of_Multiargument_Authorizer_Function_and_Access_Tokens__notes-on-caching).
- 

Optionally, customize how to handle a failed authentication response from a multi-argument authorizer function by setting up a validation failure policy:
- Select Advanced options .

The Custom response for failed auth. panel shows the HTTP status code and message body to return to the API client if the authorizer function cannot authenticate the request. By default, the API gateway sends an HTTP 401 status code and the`WWW-Authenticate`header in the response. See[Notes on Validation Failure Policies and the Handling of Failed Authentication Responses from Multi-argument Authorizer Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Notes_on_Use_of_Multiargument_Authorizer_Function_and_Access_Tokens__notes-on-failed-authentication-responses).
- Specify a status code (and an optional message body) to return to the API client if the authorizer function cannot authenticate the request:
- HTTP status code: Enter an alternative HTTP status code (for example,`500`). Alternatively, you can include a context variable to return the code returned by the authorizer function. For example, if the authorizer function returns a response code in the`responseCode`parameter, specify`request.auth[responseCode]`.
- Message body: Enter a message body. For example,`Unfortunately, authentication failed.`The message body can include any context variable (except for`request.body`). For example,`Unfortunately, authentication failed ${request.auth[my-auth-variable]}`.
- 

Optionally, modify the headers of the response that the API gateway returns to the API client by selecting Advanced options and specifying a header transformation response policy:
- 

To limit the headers included in a response, specify:
- Action: Filter.
- Type: Either Block to remove from the response the headers you explicitly list, or Allow to only allow in the response the headers you explicitly list (any other headers are removed from the response).
- Header names: The list of headers to remove from the response or allow in the response (depending on the setting of Type ). The names you specify are not case-sensitive, and must not be included in any other transformation response policies for the route (with the exception of items you filter as allowed). For example,`User-Agent`.
- 

To change the name of a header included in a response (whilst keeping its original value), specify:
- Action: Rename.
- Header name: The original name of the header that you are renaming. The name you specify is not case-sensitive, and must not be included in any other transformation response policies for the route. For example,`X-Username`.
- New header name: The new name of the header you are renaming. The name you specify is not case-sensitive (capitalization might be ignored), and must not be included in any other transformation response policies for the route (with the exception of items in`ALLOW`lists). For example,`X-User-ID`.
- 

To add a new header to a response (or to change or retain the values of an existing header already included in a response), specify:
- Action: Set.
- 

Behavior: If the header already exists, specify what to do with the header's existing value:
- Overwrite , to replace the header's existing value with the value you specify.
- Append , to append the value you specify to the header's existing value.
- Skip , to keep the header's existing value.
- Header name: The name of the header to add to the response (or to change the value of). The name you specify is not case-sensitive, and must not be included in any other transformation response policies for the route (with the exception of items you filter as allowed). For example,`X-Api-Key`.
- Values: The value of the new header (or the value to replace or append to an existing header's value, depending on the setting of Behavior ). You can specify multiple values. The value you specify can be a simple string, or can include context variables (except for`request.body`) enclosed within`${...}`delimiters. For example,`"value": "zyx987wvu654tsu321"`.

For more information about header transformation response policies, see[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm)
- 

Select Next to enter details for individual routes in the API deployment on the Routes page.
- 

Select Add route and specify the first route in the API deployment that maps a path and one or more methods to a back-end service:
- 

Path: A path for API calls using the listed methods to the back-end service. Note that the route path you specify:
- is relative to the deployment path prefix
- must be preceded by a forward slash ( / ), and can be just that single forward slash
- can contain multiple forward slashes (provided they are not adjacent), and can end with a forward slash
- can include alphanumeric uppercase and lowercase characters
- can include the special characters`$ - _ . + ! * ' ( ) , % ; : @ & =`
- can include parameters and wildcards (see[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm))
- Methods: One or more methods accepted by the back-end service, separated by commas. For example,`GET, PUT`.
- 

Add a single backend or Add multiple backends : Whether to route all requests to the same back end, or to route requests to different back ends according to context variable and rules you enter.

These instructions assume you want to use a single back end, so select Add a single backend . Alternatively, if you want to use different back ends, select Add multiple backends and follow the instructions in[Using the Console to Add Dynamic Back End Selection to an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm#apigatewaydynamicroutingbasedonrequest_topic-Using_the_Console_to_Add_Dynamic_Backend_Selection_to_an_API_Deployment_Specification).
- Backend type: The type of the back-end service, as one of:
- HTTP: For an HTTP back end, you also need to specify a URL, timeout details, and whether to disable SSL verification (see[Adding an HTTP or HTTPS URL as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusinghttpbackend.htm)).
- Oracle Functions: For an OCI Functions back end, you also need to specify the application and function (see[Adding a Function in OCI Functions as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm)).
- Stock response: For a stock response back end, you also need to specify the HTTP status code, the content in the body of the response, and one or more HTTP header fields (see[Adding Stock Responses as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingstockresponses.htm)).
- Logout : For a logout back end, you also need to specify a list of allowed URLs to which a request can be redirected to revoke tokens, and optionally data to pass to the logout URL (see[Adding Logout as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogoutbackends.htm)).
- 

To specify an authorization policy that applies to an individual route, select Show route request policies , select the Add button beside Authorization , and specify:
- 

Authorization type: How to grant access to the route. Specify:
- Any: Only grant access to end users that have been successfully authenticated, provided the authorizer function has also returned one of the access scopes you specify in the Add allowed scope field. In this case, the authentication policy's Enable anonymous access option has no effect.
- Anonymous: Grant access to all end users, even if they have not been successfully authenticated by the authorizer function. In this case, you must have selected the authentication policy's Enable anonymous access option.
- Authentication only: Only grant access to end users that have been successfully authenticated by the authorizer function. In this case, the authentication policy's Enable anonymous access option has no effect.
- Add allowed scope: If you selected Any as the Authorization type , enter a comma-delimited list of one or more strings that correspond to access scopes returned by the authorizer function. Access will only be granted to end users that have been successfully authenticated if the authorizer function returns one of the access scopes you specify. For example,`read:hello`
Note  
  

If you don't include an authorization policy for a particular route, access is granted as if such a policy does exist and Authorization type is set to Authentication only . In other words, regardless of the setting of the authentication policy's Enable anonymous access option:
- only authenticated end users can access the route
- all authenticated end users can access the route regardless of access scopes returned by the authorizer function
- anonymous end users cannot access the route
- Select Create , and then select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Request Policies for Multi-Argument Authentication and Authorization

To add authentication and authorization request policies for multi-argument access tokens to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add authentication and authorization functionality, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

At a minimum, the API deployment specification will include a`routes`section containing:
- A path. For example,`/hello`
- One or more methods. For example,`GET`
- A definition of a back end. For example, a URL, or the OCID of a function in OCI Functions.

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

Add an`authentication`request policy that applies to all routes in the API deployment specification:
- 

Insert a`requestPolicies`section before the`routes`section, if one doesn't exist already. For example:

```

```

- 

Add the following`authentication`policy to the new`requestPolicies`section.

```

```

where:
- `<type-value>`is the authentication type. To use an authorizer function for authentication, specify`CUSTOM_AUTHENTICATION`.
- `"isAnonymousAccessAllowed": <true|false>`optionally indicates whether unauthenticated (that is, anonymous) end users can access routes in the API deployment specification. If you never want anonymous end users to be able to access routes, set this property to`false`. If you don't include this property in the`authentication`policy, the default of`false`is used. Note that if you do include this property and set it to`true`, you also have to explicitly specify every route to which anonymous access is allowed by setting the`type`property to`"ANONYMOUS"`in each route's`authorization`policy.
- `<function-ocid>`is the OCID of the authorizer function deployed to OCI Functions.
- `<argument-n>`is the name of the argument to which to assign the value of one, and only one, context variable. The argument is passed to the authorizer function. The argument name you enter must correspond to the argument name that the authorizer function expects to receive. You can include multiple argument-context variable pairs.
- `<context-variable>`is a context variable the value of which you want assign to the corresponding argument.`<context-variable>`must be in the format`<context-table-name>`or`<context-table-name>[<key>]`, where`<context-table-name>`is one of :
- `request.query`, a context table containing query parameter names and values included in the request. If you want to specify a query parameter, you have to specify both the`request.query`context table, and the name of the query parameter as the key, in the format`request.query[<query-parameter-name>]`. For example,`request.query[state]`
- `request.headers`, a context table containing header names and values included in the request. If you want to specify a header, you have to specify both the`request.headers`context table, and the name of the header as the key, in the format`request.headers[<header-name>]`. For example,`request.headers[X-Api-Key]`
- `request.cert`context table, containing a Base64-encoded version of the certificate presented by an API client and successfully validated during an mTLS handshake
- `request.host`, a context table containing the name of the host to which the request was sent (extracted from the`Host`header field in the request)
- `request.body`, a context table containing the body of the request.
- `"cacheKey": ["<cache-key-argument-n>", "<cache-key-argument-n>"]`optionally restricts the cache key to using just the arguments you specify. The cache key uniquely identifies the cached response returned from the authorizer function, using arguments and argument values passed in the original authentication request. By default, all arguments and argument values (except for an argument with a value from the`request.body`context table) in the`parameters: {…}`list are used to create the cache key. An argument you specify for`<cache-key-argument-n>`must be one of the arguments in the`parameters: {…}`list. See[Notes on the Caching of Multi-argument Authorizer Function Results](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Notes_on_Use_of_Multiargument_Authorizer_Function_and_Access_Tokens__notes-on-caching).
- Optionally, add a`validationFailurePolicy`to the`authentication`policy section:

```

```

where:
- `"validationFailurePolicy": {…}`optionally enables you to change the HTTP status code, message body, and headers in the response to the API client if the authorizer function cannot authenticate a request. By default, the API gateway sends an HTTP 401 status code and the`WWW-Authenticate`header in the response. See[Notes on Validation Failure Policies and the Handling of Failed Authentication Responses from Multi-argument Authorizer Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Notes_on_Use_of_Multiargument_Authorizer_Function_and_Access_Tokens__notes-on-failed-authentication-responses).
- `<policy-type>`is the type of validation failure policy. To modify the response, specify`MODIFY_RESPONSE`.
- `"responseCode": "<alternative-response-code>"`specifies an alternative HTTP status code. For example,`"responseCode": "500"`. Alternatively, you can include a context variable to return the code returned by the authorizer function. For example, if the authorizer function returns a response code in the`responseCode`parameter, specify`"request.auth[responseCode]"`.
- `"responseMessage": "<custom-message-body>"`specifies content to include in the message body. For example,`"responseMessage": "Unfortunately, authentication failed."`. The message body can include any context variable (except for`request.body`). For example,`"responseMessage": "Unfortunately, authentication failed ${request.auth[my-auth-variable]}"`.
- `"headerTransformations": {<valid-header-transformation-response-policy>}`is a valid header transformation response policy. See[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm).
- 

Add an`authorization`request policy for each route in the API deployment specification:
- 

Insert a`requestPolicies`section after the first route's`backend`section, if one doesn't exist already. For example:

```

```

- 

Add the following`authorization`policy to the`requestPolicies`section:

```

```

where:
- 

`"type": <"AUTHENTICATION_ONLY"|"ANY_OF"|"ANONYMOUS">`indicates how to grant access to the route:
- `"AUTHENTICATION_ONLY"`: Only grant access to end users that have been successfully authenticated. In this case, the`"isAnonymousAccessAllowed"`property in the API deployment specification's`authentication`policy has no effect.
- `"ANY_OF"`: Only grant access to end users that have been successfully authenticated, provided the authorizer function has also returned one of the access scopes you specify in the`allowedScope`property. In this case, the`"isAnonymousAccessAllowed"`property in the API deployment specification's`authentication`policy has no effect.
- `"ANONYMOUS"`: Grant access to all end users, even if they have not been successfully authenticated. In this case, you must explicitly set the`"isAnonymousAccessAllowed"`property to`true`in the API deployment specification's`authentication`policy.
- `"allowedScope": [ "<scope>" ]`is a comma-delimited list of one or more strings that correspond to access scopes returned by the authorizer function. In this case, you must set the`type`property to`"ANY_OF"`(the`"allowedScope"`property is ignored if the`type`property is set to`"AUTHENTICATION_ONLY"`or`"ANONYMOUS"`). Also note that if you specify more than one scope, access to the route is granted if any of the scopes you specify is returned by the authorizer function.

For example, the following request policy defines a`/hello`route that only allows authenticated end users with the`read:hello`scope to access it:

```

```

- Add an`authorization`request policy for all remaining routes in the API deployment specification.
Note  
  

If you don't include an`authorization`policy for a particular route, access is granted as if such a policy does exist and the`type`property is set to`"AUTHENTICATION_ONLY"`. In other words, regardless of the setting of the`isAnonymousAccessAllowed`property in the API deployment specification's`authentication`policy:
- only authenticated end users can access the route
- all authenticated end users can access the route regardless of access scopes returned by the authorizer function
- anonymous end users cannot access the route
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Notes on the Use of Multi-argument Authorizer Functions and Access Tokens

### Notes on the Caching of Multi-argument Authorizer Function Results

When using authorizer functions, the API gateway internally caches the response from the authorizer function by default. Caching the response enables the response to be re-used later to respond to a similar authentication request, without calling the authorizer function again.

To uniquely identify a cached response returned by an authorizer function for an authentication request, the API gateway uses a cache key derived from the arguments and argument values passed to the authorizer function that elicited the response. If the argument and argument values of a subsequent authentication request match a cache key, the cached response is used instead of calling the authorizer function unnecessarily.

In the case of multi-argument authorizer functions, by default all arguments and argument values (except for an argument with a value from the`request.body`context table) passed to the authorizer function are used to create the cache key. However, you can customize the arguments and argument values used to create the cache key, so the cache key only includes the arguments and argument values you specify. Note that if you do remove arguments and argument values from the cache key, you might introduce the risk of an incoming invalid authentication request matching the cache key of a previous response to a successfully authenticated request. Only remove arguments from the cache key if you are sure the arguments play no role in authenticating the request.

### Notes on Validation Failure Policies and the Handling of Failed Authentication Responses from Multi-argument Authorizer Functions

When using a multi-argument authorizer function, you can define a validation failure policy. A validation failure policy enables you to customize the HTTP status code, message, and response headers that the API gateway sends to an API client in the event of a failed authentication response from a multi-argument authorizer function.

A multi-argument authorizer function must return an HTTP 200 response (with the JSON body of the response containing`"active": false`and a`WWW-Authenticate`header) if an access token has been successfully verified with an identity provider, but the identity provider has determined the token is invalid,

If the authorizer function returns an HTTP 200 response with`"active": false`in the response body, by default the API gateway sends an HTTP 401 status code to the API client (along with the`WWW-Authenticate`header in the response). However, you can define a validation failure policy to specify a different HTTP status code to return, and to specify a custom message to return in the response body.

You can also include a header transformation response policy within a validation failure policy to modify the header of the response that the API gateway returns to the API client. By including a header transformation response policy within a validation failure policy you can:
- limit the headers included in a response
- change the name of a header included in a response (whilst keeping its original value)
- add a new header to a response (or change or retain the values of an existing header already included in a response)

For more information about adding a validation failure policy, see[Editing a JSON File to Add Request Policies for Multi-Argument Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Editing_a_JSON_File_to_Add_Multiargument_Authorizer_Function_Authentication_Request_Policies).

## Example Deployment Specification Using Multi-Argument Access Tokens

The following API deployment specification defines:
- An authentication request policy that calls a multi-argument authorizer function to perform authentication.
- An authorization request policy that specifies what authenticated end-users can do.

```

```

The authentication request policy in this API deployment specification:
- Specifies the multi-argument authorizer function to call to perform authentication and defines the`xapikey`,`referer`,`state`,`city`,`cert`,`body`, and`host`arguments to pass to the authorizer function. The values of these arguments are obtained from context variables that have values from the original request.
- Defines a custom cache key to uniquely identify the cached response returned from the authorizer function. Rather than use the default cache key (which includes all arguments sent to the authorizer function, and is recommended), this authentication request policy specifies that the cache key is to comprise just the values of the`xapikey`and`referrer`arguments passed to the authorizer function.
- Includes a validation failure policy that modifies the default validation failure response to replace the default HTTP 401 status code with the value of the`request.auth[responseCode]`context variable. The`request.auth[responseCode]`context variable has the value of an authentication parameter (in this case, named`responseCode`) returned by the authorizer function. Similarly, the default validation failure message is replaced with a custom message string (`"Unfortunately, authentication failed."`).
- Includes a header transformation request policy within the validation failure policy that adds the`location`header to the validation failure response. The`location`header is given the value of the`request.auth[location]`context variable, which has the value of an authentication parameter (in this case, named`location`) returned by the authorizer function. The header transformation request policy also removes headers named`topSecret`from the response.

The authorization request policy in this API deployment specification only allows end users authenticated by the authorizer function and with the`read:hello`scope to access the`/hello`
