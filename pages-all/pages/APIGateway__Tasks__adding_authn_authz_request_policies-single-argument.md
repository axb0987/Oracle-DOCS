# Adding Authentication and Authorization Request Policies for Single-Argument Access Tokens and Authorizer Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-single-argument.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Authentication and Authorization Request Policies for Single-Argument Access Tokens and Authorizer Functions

Add request policies to provide authentication and authorization using single-argument access tokens and single-argument authorizer functions.

You can add request policies by:
- [using the Console](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-single-argument.htm#usingconsole)
- [editing a JSON file](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-single-argument.htm#usngjson)
Note  
  
Oracle recommends the use of multi-argument authorizer functions rather than single-argument authorizer functions because of their additional versatility. Single-argument authorizer functions were provided in earlier releases, and continue to be supported. However, since multi-argument authorizer functions can also accept single-argument access tokens contained in request headers and query parameter, there is no reason to create new single-argument authorizer functions. Furthermore, single-argument authorizer functions are planned for deprecation in a future release.

## Using the Console to Add Request Policies for Single-Argument Authentication and Authorization

To add authentication and authorization request policies for single-argument access tokens to an API deployment specification using the Console:
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
- Specify the single-argument authorizer function to use to authenticate the single-argument access token:
- Oracle Functions application: The name of the application in OCI Functions that contains the authorizer function. You can select an application from a different compartment.
- Function Name: The name of the authorizer function in OCI Functions.
- Select Single-argument authorizer function to specify that you want to pass a single-argument access token in a header or query parameter to a single-argument authorizer function.
- In the Access token panel, identify the access token to use for authentication:
- Token location: Select Header or Query parameter to specify the location of the access token in the request.
- Token header name or Token parameter name: Depending on the location of the access token, enter the name of the header or query parameter containing the access token.
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

Add a single backend or Add multiple backends : Whether to route all requests to the same back end, or to route requests to different backends according to context variable and rules you enter.

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

## Editing a JSON File to Add Request Policies for Single-Argument Authentication and Authorization

To add authentication and authorization request policies for single-argument access tokens to an API deployment specification in a JSON file:
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
- `<"tokenHeader"|"tokenQueryParam">: <"<token-header-name>"|"<token-query-param-name>">`indicates whether it is a request header that contains the access token (and if so, the name of the header), or a query parameter that contains the access token (and if so, the name of the query parameter). Note that you can specify either`"tokenHeader": "<token-header-name>"`or`"tokenQueryParam": "<token-query-param-name>">`, but not both.

For example, the following`authentication`policy specifies an OCI function that will validate the access token in the Authorization request header:

```

```

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
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
