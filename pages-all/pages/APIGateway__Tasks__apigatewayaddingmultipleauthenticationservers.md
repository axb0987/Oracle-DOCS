# Adding Multiple Authentication Servers to the same API Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Multiple Authentication Servers to the same API Deployment

A common requirement is to authenticate requests sent to the same API deployment in different ways. For example, you might want an incoming request from one API client to be sent to an authorizer function for authentication. Whereas, you might want a JSON Web Token (JWT) included in an incoming request from a different API client to be validated with an identity provider. For convenience, these different types of authentication and authorization (authorizer function, JWT authentication) are referred to as 'authentication servers'.
To meet the requirement to authenticate requests sent to an API deployment in different ways, you can define multiple authentication servers for the same API deployment. The authentication servers you set up can be of the same type or a different type. You can specify the following types of authentication server:
- authorizer functions (for more information about authorizer functions, see[Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm))
- JSON Web Tokens (JWTs) validated with an identity provider (see[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)).

When defining multiple authentication servers for the same API deployment, you create rules to enable the API gateway to dynamically select which authentication server to use to authenticate requests, based on an element in the original request.

To enable the API gateway to dynamically select the correct authentication server, you use the following context variables to capture elements of the request:
- `request.auth[<key>]`where`<key>`is the name of a claim contained in a JWT token.
- `request.headers[<key>]`where`<key>`is the name of a header included in the request to the API.
- `request.host`as the name of the host to which the original request was sent.
- `request.path[<key>]`where`<key>`is the name of a path parameter defined in the API deployment specification.
- `request.query[<key>]`where`<key>`is the name of a query parameter included in the request to the API.
- `request.subdomain[<key>]`where`<key>`is the trailing part of the host name to ignore when capturing the leading part of the host name to which the original request was sent.

Note that if a context variable has multiple values, only the first value is used when selecting the authentication server. For more information about context variables, see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm).

You can set up multiple authentication servers for the same API deployment in an API deployment specification by:
- Using the Console.
- Editing a JSON file.

## Notes about authentication server rule matching

When creating the rules to determine which authentication server to use, you can specify how closely the context variable value must match a given value for the request to be routed to a particular authentication server. You can require an exact match, or you can specify a value starting with, or ending with, a wildcard. The API gateway evaluates the rules in the order you specify (exact match rules first, followed by wildcard rules), and uses the first matching rule. You can also specify a default rule to use if the context variable value does not match any authentication server rules. If no rule is specified as the default and the context variable value in an incoming request does not match any authentication server rules, the request returns an error. The order of precedence for determining which authentication server rule (and hence which authentication server) to use can be summarized as:
- If the context variable value exactly matches a rule's value, use that rule.
- Otherwise, if the context variable value matches a rule's value that starts or ends with a wildcard, use the first rule containing a wildcard that matches.
- Otherwise, if a rule is specified as the default rule, use that rule.
- Otherwise, return a`401 Unauthorized`error response.

## Using the Console to Add Multiple Authentication Servers to the same API Deployment

To add multiple authentication servers for the same API deployment to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- Select Next to display the Authentication page.
- Select Multi-Authentication to specify that you want authentication requests routed to different authentication servers, according to the context variable and rules you enter:
- From the Selector list, select the context table (containing the context variable) to use when determining the authentication server to which to send the authentication request, as follows:
- Auth: Use the value of a claim contained in a JWT (and saved in the`request.auth`context table) to determine the authentication server. Note that if you select Auth , you must specify authentication servers of type Token Authentication (for JSON Web Token (JWTs)) for all authentication server rules in the API deployment. If you select Auth from the Selector list, also note that the location of the JWTs must be the same for all the Token Authentication authentication servers (either the same request header and authorization scheme, or the same query parameter).
- Headers: Use the value of a header from the original request (and saved in the`request.headers`context table) to determine the authentication server.
- Host: Use the name of the host to which the original request was sent (extracted from the host field of the Host header in the request, and saved in the`request.host`context table) to determine the authentication server.
- Path: Use a path parameter from the original request (and saved in the`request.path`context table) to determine the authentication server.
- Query params: Use the value of a query parameter from the original request (and saved in the`request.query`context table) to determine the authentication server.
- Subdomain: Use the leading part of the host name to which the original request was sent (just that part of the host name not specified as the key, and saved in the`request.subdomain`context table) to determine the authentication server. Note that the key is the trailing part of the host name to not use.
- Depending on the context table you select, enter the name of the key to use when determining the authentication server to which to send the authentication request.
- Select Add policy to enter a rule for the context variable that, if met, routes the authentication request to the authentication server you define.
- Enter details for the authentication server rule as follows:
- Name: Enter a name for the authentication server rule. Use the name you enter to identify the authentication server when referring to logs and metrics. The name must be unique across all authentication server rules defined for the API deployment.
- Match type: Specify how closely the context variable value must match a value you enter in order for the request to be routed to this authentication server. Select Any of if the context variable must exactly match the value in the Values field. Select Wildcard if the context variable must match a value in the Expression field that contains wildcards. Value-matching is case-insensitive if you select Any of , and case-sensitive if you select Wildcard .
- Values: (Displayed if you selected Any of in the Match type field.) Specify a value (or multiple values in a comma-separated list) that the context variable must exactly match. Note that the match is case-insensitive if you selected Any of . Also note that values must be unique within a single authentication server rule, and across all authentication server rules defined for the API deployment.
- Expression: (Displayed if you selected Wildcard in the Match type field) Specify a value starting with, or ending with, a wildcard that the context variable must match. Use the`*`(asterisk) wildcard to indicate zero or more characters, and/or the`+`(plus sign) wildcard to indicate one or more characters. Note that the match is case-sensitive if you selected Wildcard . Note that you cannot include more than one wildcard in a value, and you cannot include a wildcard in the middle of a value.
- Make default: Specify whether to use the authentication server defined for this rule if no other authentication server rules match the context variable value. You can only specify one authentication server rule as the default for an API deployment. If no rule is marked as the default and the context variable value in an incoming request does not match any authentication server rules defined for an API deployment, the request returns a`401 Unauthorized`error response.
- 

Select or deselect the Enable anonymous access checkbox to specify whether unauthenticated (that is, anonymous) end users can access routes in the API deployment.

By default, this option is not selected. If you never want anonymous users to be able to access routes, don't select this option. Note that if you do select this option, you also have to explicitly specify every route to which anonymous access is allowed by selecting Anonymous as the Authorization Type in each route's authorization policy.
- Enter details for the authentication server as follows:
- In the Authentication type field, select Token Authentication or Authorizer function as the authentication server to which to route the authentication request if the rule you entered is met.

Note that if you selected Auth from the Selector list, you must select Token Authentication as the type of authentication server. If you selected Auth from the Selector list, also note that the location of the JWTs must be the same for all the Token Authentication authentication servers (either the same request header and authorization scheme, or the same query parameter).
- Enter details for the authentication server you selected. The details to enter will depend on the authentication server type you selected:
- For a Token Authentication authentication server, see[Using the Console to Add Token Authentication and Authorization Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usingconsole.htm).
- For an Authorizer function authentication server, specify the name of the authorizer function, the application in OCI Functions that contains it, and then select either Multi-argument authorizer function or Single-argument authorizer function . For more information, see:
- [Using the Console to Add Request Policies for Multi-Argument Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Using_the_Console_to_Add_Multiargument_Authorizer_Function_Authentication_Request_Policies)
- [Using the Console to Add Request Policies for Single-Argument Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-single-argument.htm#usingconsole)
- Select Create to create the authentication server and associated rule.
- Optionally, select Add policy again to define additional authentication servers and associated rules.
- Select Next to enter details for individual routes in the API deployment on the Routes page.
- Select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add Multiple Authentication Servers to the same API Deployment

To add multiple authentication servers for the same API deployment to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)) in the format:

```

```

where:
- `"dynamicAuthentication"`specifies that you want the API gateway to dynamically select which authentication server to use to authenticate requests, based on an element in the request.
- `"selector": "<context-table-key>"`specifies the context table (and key, if appropriate) from which to obtain the context variable value that determines the authentication server to send authentication requests to, as follows:
- `request.auth[<key>]`Use the value of a claim contained in a JSON Web Token (JWT) to determine the authentication server.`<key>`is the name of the claim. For example,`request.auth[tenant]`. Note that if you specify`request.auth[<key>]`, you must specify authentication servers of type`JWT_AUTHENTICATION`for all authentication server rules in the API deployment. If you specify`request.auth[<key>]`, also note that the location of the JWTs must be the same for all the authentication servers (either the same request header and authorization scheme, or the same query parameter).
- `request.headers[<key>]`Use the value of a header from the original request to determine the authentication server.`<key>`is the header name. For example,`request.headers[Accept]`
- `request.host`Use the name of the host to which the original request was sent (extracted from the host field of the Host header in the request) to determine the authentication server.
- `request.path[<key>]`Use a path parameter from the original request to determine the authentication server.`<key>`is the path parameter name. For example,`request.path[region]`
- `request.query[<key>]`Use the value of a query parameter from the original request to determine the authentication server.`<key>`is the query parameter name. For example,`request.query[state]`
- `request.subdomain[<key>]`Use the leading part of the host name to which the original request was sent (just that part of the host name not specified as the key) to determine the authentication server. Note that`<key>`is the trailing part of the host name to not use. For example,`request.subdomain[example.com]`
- `"type": "SINGLE"`specifies that you want to use a single context variable to dynamically select the authentication server.
- `"key": {...}`specifies the rule that must be met to send a request to the authentication server specified by`"authenticationServerDetail": {…}`.
- `"type": "<ANY_OF|WILDCARD>"`specifies how closely the value of the context variable identified by`<context-table-key>`must match the value you enter for`<context-variable-value>`in order for the request to be sent to the authentication server specified by`"authenticationServerDetail": {…}`. Specify`ANY_OF`if the value of the context variable identified by`<context-table-key>`must exactly match the value you specify for`<context-variable-value>`. Specify`WILDCARD`if the value of the context variable identified by`<context-table-key>`must match a value containing wildcards that you specify for`<context-variable-value>`. Value-matching is case-insensitive if you specify`ANY_OF`, and case-sensitive if you specify`WILDCARD`.
- `<context-variable-value>`is a value that possibly matches the value of the context variable identified by`<context-table-key>`. You can include multiple`"<context-variable-value>"`entries in the`values:[...]`array, separated by commas. The request is sent to the authentication server specified by`"authenticationServerDetail": {…}`if the values match, as follows:
- If you specified`"type": "ANY_OF"`, the values must match exactly. Note that values must be unique within a single authentication server rule, and across all authentication server rules defined for an API deployment. Value-matching is case-insensitive if you specified`ANY_OF`.
- If you specified`"type": "WILDCARD"`, you can specify a value for`<context-variable-value>`that starts with, or ends with, a wildcard. Use the`*`(asterisk) wildcard to indicate zero or more characters, and/or the`+`(plus sign) wildcard to indicate one or more characters. Note that you cannot include more than one wildcard in a value, and you cannot include a wildcard in the middle of a value. Value-matching is case-sensitive if you specified`WILDCARD`. For example, if you want a request from an API client that can accept an xml response (as indicated in the Accept header of the request) to be routed to a particular authentication server, you might specify:
- `"selector": "request.headers[Accept]"`
- `"type": "ANY_OF"`
- `"values": ["application/xml"]`
- `"isDefault": "<true|false>"`is an optional boolean value (either`true`or`false`) indicating whether to use the authentication server for this rule if no other authentication server rules match the context variable value. If not specified,`"isDefault": "false"`is assumed. You can only specify one authentication server rule as the default for an API deployment. If no rule is marked as the default and the context variable value in an incoming request does not match any authentication server rules defined for an API deployment, the request returns a`401 Unauthorized`error response.
- `"name": "<rule-name>"`specifies a name for the rule. Use this name to identify the authentication server when referring to logs and metrics. The name must be unique across all authentication server rules defined for the API deployment.
- `"type": "<authentication-server-type>"`specifies the type of the authentication server. Valid values are`JWT_AUTHENTICATION`, and`CUSTOM_AUTHENTICATION`. Note that if you specified`request.auth[<key>]`, you must specify authentication servers of type`JWT_AUTHENTICATION`for all authentication server rules in the API deployment. If you specified`request.auth[<key>]`, also note that the location of the JWTs must be the same for all the authentication servers (either the same request header and authorization scheme, or the same query parameter).
- `"<auth-server-attribute-name>": "<auth-server-attribute-value>"`are attributes and attribute values for the type of authentication server you specified. The attributes and attribute values to enter will depend on the type of authentication server type you specified:
- for a`JWT_AUTHENTICATION`authentication server, see[Editing a JSON File to Add Token Authentication and Authorization Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usinjson.htm)
- for a`CUSTOM_AUTHENTICATION`authentication server, see:
- [Editing a JSON File to Add Request Policies for Multi-Argument Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-multi-argument.htm#apigatewayusingauthorizerfunction_topic-Editing_a_JSON_File_to_Add_Multiargument_Authorizer_Function_Authentication_Request_Policies)
- [Editing a JSON File to Add Request Policies for Single-Argument Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/adding_authn_authz_request_policies-single-argument.htm#usngjson)

For example, the following API deployment specification includes dynamic authentication server selection that handles authentication requests based on the value of the`vehicle-type`query parameter passed in the request. For a more detailed explanation of this example, see[Example 1: Select JWT or serverless function as authentication server using a query parameter (including wildcard selection and default)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm#apigatewayaddingmultipleauthenticationservers_topic-Examples__section_JWT_or_function_auth_server_example).

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Examples

### Example 1: Select JWT or serverless function as authentication server using a query parameter (including wildcard selection and default)

In this example, the API gateway determines the authentication server to which to send the authentication request based on the value of the`vehicle-type`query parameter passed in the request. If the`vehicle-type`query parameter has the value`car`, the JWT in the authorization header of the request is validated by retrieving public verification keys from the`https://recommend-app.eu.auth0.com`identity provider. If the`vehicle-type`query parameter has a value that starts with`mini`, an authentication request is sent to a serverless function in OCI Functions for processing. If the`vehicle-type`query parameter value is neither`car`nor`mini*`, the API gateway assumes by default that there is a JWT in the authorization header of the request and attempts to validate it by retrieving public verification keys from the`https://recommend-app.eu.auth0.com`identity provider:

```

```

### Example 2: Select JWT authentication server using claims from JWT tokens

In this example, the API gateway determines the authentication server to which to send the authentication request based on the`tenant`claim in a JWT token passed in the Authorization header of the request. Two example JWT tokens follow the API deployment specification:
```

```

When authenticating a request that has the following JWT token in the Authorization header, the API gateway retrieves the JSON Web Key Set (JWKS) to verify the signature from`https://car.us.auth0.com/.well-known/jwks.json`.
```

```

When authenticating a request that has the following JWT token in the Authorization header, the API gateway retrieves the JSON Web Key Set (JWKS) to verify the signature from`https://truck.us.auth0.com/.well-known/jwks.json`.
```

```
