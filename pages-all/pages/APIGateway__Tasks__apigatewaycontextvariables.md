# Adding Context Variables to Policies and HTTP Back End Definitions
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding Context Variables to Policies and HTTP Back End Definitions

Find out how to use parameters in API calls using API Gateway context variables.

Calls to APIs deployed on an API gateway typically include parameters that you'll want to use when defining the following in API deployment specifications:
- request policies and response policies
- HTTP and HTTPS back ends

To enable you to use parameters included in API calls, the API Gateway service saves the values of the following types of parameter in temporary 'context tables':
- Path parameters you define in the API deployment specification are saved in records in the`request.path`table. See[Adding Path Parameters and Wildcards to Route Paths](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingparamswildcards.htm).
- Query parameters included in the call to the API are saved in records in the`request.query`table.
- Header parameters included in the call to the API are saved in records in the`request.headers`table.
- Authentication parameters returned by an authorizer function or contained in a JSON Web Token (JWT) are saved in records in the`request.auth`table. See[Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)and[Validating Tokens to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm)respectively.
- Certificate parameters (a Base64-encoded version of the certificate presented by an API client and successfully validated during an mTLS handshake) are saved in records in the`request.cert`table. See[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).
- The name of the host to which a request was sent (extracted from the`Host`header field in the request) is saved in the`request.host`table. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm)and[Dynamically Selecting API Gateway Back Ends Based on Request Elements](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm).
- The leading part of the host name to which the original request was sent is saved in the`request.subdomain`table. See[Adding Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm)[Dynamically Selecting API Gateway Back Ends Based on Request Elements](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm).
- The OCID of a usage plan to which the API client is subscribed is saved in the`request.usage_plan`table. See[Dynamically Selecting API Gateway Back Ends Based on Request Elements](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydynamicroutingbasedonrequest_topic.htm).
- The body of the request is saved in the`request.body`table (solely for use by multi-argument authorizer functions). See[Creating a Multi-Argument Authorizer Function (Recommended)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Creating_an_Authorizer_Function.htm#apigatewayusingauthorizerfunction_topic-Creating_a_Multiargument_Authorizer_Function).

Each record in a context table is identified by a unique key.

When defining request and response policies, and HTTP and HTTPS back ends, you can reference the value of a parameter in a context table using a 'context variable'. A context variable has the format`<context-table-name>[<key>]`where:
- `<context-table-name>`is one of`request.path`,`request.query`,`request.headers`,`request.auth`,`request.cert`, or`request.host`
- `<key>`is one of:
- a path parameter name defined in the API deployment specification
- a query parameter name included in the request to the API
- a header name included in the request to the API
- an authentication parameter name returned by an authorizer function or contained in a JWT token
- the name`[client_base64]`, representing a successfully validated, Base64-encoded, certificate presented by an API client during an mTLS handshake
- the trailing part of the host name to ignore (when capturing the leading part of the host name to which the original request was sent)
- the name of a host to which the request was sent (extracted from the`Host`header field in the request)

If you want to include the context variable within a string in the API deployment specification (for example, in the url property of an HTTP back end definition), use the format`${<context-table-name>[<key>]}`.

For example, the`request.path[region]`context variable in the example below returns the value of the record identified by the`region`key in the`request.path`context table.

```

```

Note the following:
- A single record is created in the context table for each discrete parameter in an HTTP request. If the HTTP request includes two (or more) parameters of the same type and with the same name, the value of each parameter with that name is saved in the same record in the context table and identified by the same key. However, only the first value in the context table record can be substituted in place of a context variable. When adding a context variable for which multiple values can exist in the context table record and you want the first value in the context table record to be substituted in place of the context variable, add the context variable to the API deployment specification in the format`${<context-table-name>[<key>]}`
- If a parameter value includes special characters that have been encoded, the encoding is preserved when the value is saved in the context table. When the value is substituted for a context variable, the encoded value is substituted in place of the context variable. For example, if San José is included in a query parameter as`San+José`, the encoded version is what will be substituted in place of the context variable for that query parameter.
- If a context variable key does not exist in the specified context table, an empty string is substituted in place of the context variable.
- If a context variable key contains a dot, the dot is treated as any other character. It is not treated as an indicator of a parent-child relationship between the strings either side of it.
- If a path parameter includes a wildcard (for example,`generic_welcome*`), the path parameter without the wildcard is used as the key.
- 

You can include a context variable as a path segment in the URL property of an HTTP back end definition, but not as a query parameter. For example:
- 

You can use the`request.query[state]`context variable as a path segment in the URL property, as shown in the following valid HTTP back end definition:

```

```

- 

You cannot use the`request.query[state]`context variable as a query parameter in the URL property, as shown in the following invalid HTTP back end definition:

```

```

If you do want to pass a context variable as a query parameter, use a query parameter transformation request policy rather than including the context variable as a query parameter in the URL property (see[Adding Query Parameter Transformation Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingqueryparamtransformrequestpolicies.htm)).

## Examples

The examples in this section assume the following API deployment definition and basic API deployment specification in a JSON file:

```

```

Note the examples also apply when you're defining an API deployment specification using dialogs in the Console.

### Example 1: Query path parameter in a definition

You can define a path parameter in the API deployment specification, and then use it elsewhere in the API deployment specification as a context variable.

This example creates a path parameter,`region`, and uses it in a context variable`request.path[region]`in the HTTP back end definition.

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather/west`resolves to`https://api.weather.gov/west`.

### Example 2: Different types of context variable in the same definition

You can include different types of context variable in the same definition in the API deployment specification.

This example uses the following in the HTTP back end definition:
- a path parameter context variable,`request.path[region]`
- a query parameter context variable,`request.query[state]`

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather/west?state=california`resolves to`https://api.weather.gov/west/california`.

### Example 3: Multiple context variables of the same type in the same definition

You can include the same type of context variable multiple times in the same definition.

This example uses the following in the HTTP back end definition:
- a path parameter context variable,`request.path[region]`
- two query parameter context variables,`request.query[state]`and`request.query[city]`

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather/west?state=california&city=fremont`resolves to`https://api.weather.gov/west/california/fremont`.

### Example 4: Multiple values for the same parameter

It is often valid for an HTTP request to include the same query parameter multiple times. The API Gateway service saves the value of each parameter with the same name to the same record in the context table. However, in the API deployment specification, it's typically the case that only a single value can be substituted for a context variable. In these situations, you can indicate that only the first value recorded in the context table for a key is substituted in place of a context variable by enclosing the context variable within`${...}`.

For example, a valid request like`"https://<gateway-hostname>/marketing/weather/west?state=california&city=fremont&city=belmont"`has two occurrences of the`city`query parameter. On receipt of the HTTP request, the API Gateway service writes both values of the`city`query parameter (`fremont`and`belmont`) to the same record in the`request.query`table. When the definition of an HTTP back end includes`${request.query[city]}`, only the first value in the record is substituted in place of the context variable.

This example uses the following in the HTTP back end definition:
- a path parameter context variable,`request.path[region]`
- two query parameter context variables,`request.query[state]`and`request.query[city]`

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather/west?state=california&city=fremont&city=belmont`resolves to`https://api.weather.gov/west/california/fremont`. Note that only`fremont`(as the first value in the`request.query`context table record identified by the`city`key) is substituted for the`request.query[city]`context variable.

### Example 5: Parameter value includes encoded special characters

If an HTTP request includes special characters (for example, the character é, the space character) that have been encoded, the value is stored in the context table in its encoded form. When the value from the context table is substituted for a context variable, the encoding is preserved.

This example uses the following in the HTTP back end definition:
- a path parameter context variable,`request.path[region]`
- a query parameter context variable,`request.query[city]`

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather/west?city=San+José`resolves to`https://api.weather.gov/west/california/San+José`.

### Example 6: Header parameters in a definition

You can include values passed in the headers of a request as context variables in a definition. If the request includes a header, the value of the header is stored in the`request.headers`table, and the name of the header is used as the key.

This example uses the following in the HTTP back end definition:
- a path parameter context variable,`request.path[region]`
- a header parameter context variable,`request.headers[X-Api-Key]`

```

```

In this example, a request like`https://<gateway-hostname>/marketing/weather/west`included an`X-Api-Key`header with the value`abc123def456fhi789`. The request resolves to`https://api.weather.gov/west/abc123def456fhi789`.

### Example 7: Authentication parameters in a definition

You can include values returned from an authorizer function or contained in a JWT token as context variables in a definition:
- An authorizer function validates the token passed by an API client when calling the API Gateway service. The authorizer function returns a response that includes information such as the validity of the authorization, information about the end user, access scope, and a number of claims in key-value pairs. Depending on the authorization token, the information might be contained within the token, or the authorizer function might invoke end-points provided by the authorization server to validate the token and to retrieve information about the end user. When the API Gateway service receives a key-value pair from the authorizer function, it saves the key-value pair in the`request.auth`table as an authentication parameter.
- A JWT token can optionally include a custom claim named`scope`, comprising a key-value pair. When the JWT token has been validated, the API Gateway service saves the key-value pair in the`request.auth`table as an authentication parameter.

In the case of the OpenID Connect authorization flow, two tokens named`id_token`(always JWT-encoded) and`access_token`(can be JWT-encoded) are returned. The API Gateway service saves the token values in the`request.auth[id_token]`and`request.auth[access_token]`context variables, along with custom claims in the`request.auth[id_token_claims][<claim-name>]`and`request.auth[access_token_claims][<claim-name>]`context variables respectively.

This example uses the key-value pair returned by an authorizer function as the authentication parameter context variable`request.auth[region]`in the HTTP back end definition.

```

```

Assume an authorizer function`ocid1.fnfunc.oc1.phx.aaaaaaaaac2______kg6fq`validates the token passed by an API client in a call to the API Gateway service. The authorizer function returns a response to the API Gateway service that includes the region associated with the end user as a key-value pair, and also the authenticated end user's access scope. When the API Gateway service receives the key-value pair, it saves the key-value pair in the`request.auth`table as an authentication parameter.

In this example, a request like`https://<gateway-hostname>/marketing/weather`is made by an end user jdoe using an API client. The authorizer function validates the token passed by the API client in the request, and also determines that jdoe has the`"weatherwatcher"`access scope. The authorizer function identifies that jdoe is associated with the west region. The authorizer function returns jdoe's access scope to the API Gateway service, along with the region associated with jdoe. The API Gateway service saves the region associated with jdoe as an authentication parameter. The HTTP back end definition specifies that end users with the`"weatherwatcher"`access scope are allowed to access the HTTP back end. The API Gateway service uses the value of the authentication parameter context variable`request.auth[region]`in the request. The request resolves to`https://api.weather.gov/west`.

### Example 8: TLS certificate parameter in a definition

You can include a Base64-encoded version of the TLS certificate presented by an API client during an mTLS handshake as a context variable in a definition. The Base64-encoded version of the TLS certificate is stored in the`request.cert`table, with the name`client_base64`used as the key. See[Adding mTLS support to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm).

This example uses the following in the HTTP back end definition:
- the certificate context variable,`request.cert[client_base64]`

```

```

In this example, a header named`certificate-header`
