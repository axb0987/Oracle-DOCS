# Using the Console to Add Token Authentication and Authorization Request Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usingconsole.htm
- Fetched: 2026-09-05 01:39 CDT

# Using the Console to Add Token Authentication and Authorization Request Policies

Add authentication and authorization request policies to an API deployment specification using the Console.
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- Select Next to display the Authentication page.
- 

Select Single Authentication to specify that you want to use a single authentication server for all requests.

These instructions assume you want to use a single authentication server. Alternatively, if you want to use multiple authentication servers, select Multi-Authentication and follow the instructions in[Using the Console to Add Multiple Authentication Servers to the same API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmultipleauthenticationservers.htm#apigatewayaddingmultipleauthorizationservers_topic-Using_the_Console).
- 

Select or deselect Enable anonymous access to specify whether unauthenticated (that is, anonymous) end users can access routes in the API deployment.

By default, this option is not selected. If you never want anonymous users to be able to access routes, don't select this option. Note that if you do select this option, you also have to explicitly specify every route to which anonymous access is allowed by selecting Anonymous as the Authorization Type in each route's authorization policy.
- Select Token Authentication from the Authentication type option list and specify:
- Token location: Whether tokens are contained in a request header or a query parameter.
- 

Authentication token details: Depending on whether tokens are contained in a request header or a query parameter, specify:
- Token header name: and Authentication scheme: If tokens are contained in a request header, enter the name of the header (for example`Authorization`), and the HTTP authentication scheme (only`Bearer`is currently supported).
- Token parameter name: If tokens are contained in a query parameter, enter the name of the query parameter.
- Specify how you want the API gateway to validate tokens:
- 

If you want the API gateway to validate both JWT tokens and non-JWT tokens with an OAuth 2.0 authorization server's introspection endpoint using client credentials (including a client secret retrieved from a vault in the Vault service), select OAuth 2.0 introspection endpoint from the Type list and specify:
- Client ID: The client ID to send to the introspection endpoint. You obtain a client ID by creating and registering a client application with the authorization server. For example,`5hsti38yhy5j2a4tas455rsu6ru8yui3wrst4n1`. See[Prerequisites for Token Authentication](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-prerequisites.htm).
- Vault: The name of a vault in the Vault service that contains the client secret to send to the introspection endpoint, from the list of vaults in the specified compartment. You obtain a client secret by creating and registering a client application with the authorization server. See[Prerequisites for Token Authentication](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-prerequisites.htm).
- Vault secret in &lt;compartment name&gt;: The name of a vault secret that contains the client secret to send to the introspection endpoint, from the list of vault secrets in the specified compartment.
- Vault secret version number: The version of the vault secret that contains the client secret to send to the introspection endpoint.
- Discovery URL: The well-known URL of the authorization server from which the API gateway is to obtain authorization metadata endpoints. For example,`https://my-idp/oauth2/default/.well-known/openid-configuration`.

Note the URL must be routable from the subnet containing the API gateway on which the API is deployed.
- Maximum cache duration in hours: The number of hours (between 1 and 24) the API gateway is to cache the response from the introspection endpoint.
- Max clock skew in seconds: (Optional) The maximum time difference between the system clocks of the authorization server that issued a token and the API gateway. The value you enter here is taken into account when the API gateway validates a JWT to determine whether it is still valid, using the not before (`nbf`) claim (if present) and the expiration (`exp`) claim in the JWT. The minimum (and default) is`0`, the maximum is`120`.
- Disable SSL verification: Whether to disable SSL verification when communicating with the authorization server. By default, this option is not selected. Oracle recommends not selecting this option because it can compromise token validation. API Gateway trusts certificates from multiple Certificate Authorities issued for OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta.
- 

If you want the API gateway to validate JWTs by retrieving public verification keys from the identity provider at runtime, select Remote JWKS from the Type list and specify:
- 

JWKS URI: The URI from which to retrieve the JSON Web Key Set (JWKS) to use to verify the signature on JWTs. For example, https://www.somejwksprovider.com/oauth2/v3/certs. For more information about the URI to specify, see[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).

Note the following:
- 

The URI must be routable from the subnet containing the API gateway on which the API is deployed.
- If the API gateway fails to retrieve the JWKS, all requests to the API deployment will return an HTTP 500 response code. Refer to the API gateway's execution log for more information about the error (see[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)).
- Certain key parameters must be present in the JWKS to verify the JWT's signature (see[Key Parameters Required to Verify JWT Signatures](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-keyparams.htm)).
- The JWKS can contain up to ten keys.
- Maximum cache duration in hours: The number of hours (between 1 and 24) the API gateway is to cache the JWKS after retrieving it.
- Max clock skew in seconds: (Optional) The maximum time difference between the system clocks of the authorization server that issued a token and the API gateway. The value you enter here is taken into account when the API gateway validates a JWT to determine whether it is still valid, using the not before (`nbf`) claim (if present) and the expiration (`exp`) claim in the JWT. The minimum (and default) is`0`, the maximum is`120`.
- Disable SSL verification: Whether to disable SSL verification when communicating with the identity provider. By default, this option is not selected. Oracle recommends not selecting this option because it can compromise JWT validation. API Gateway trusts certificates from multiple Certificate Authorities issued for OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta.
- 

If you want the API gateway to validate JWTs with public verification keys already issued by an identity provider (enabling the API gateway to verify JWTs locally without having to contact the identity provider), select Static keys from the Type list and specify up to ten static keys:
- Key ID: The identifier of the static key used to sign the JWT. The value must match the`kid`claim in the JWT header. For example,`master_key`.
- 

Key format: The format of the static key, as either a JSON Web Key or a PEM-encoded Public Key.
- 

JSON web key: If the static key is a JSON Web Key, paste the key into this field.

For example:
```

```

Note that certain parameters must be present in the static key to verify the JWT's signature (see[Key Parameters Required to Verify JWT Signatures](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-keyparams.htm)). Also note that`RSA`is currently the only supported key type (`kty`).
- 

PEM-encoded public key: If the static key is a PEM-encoded public key, paste the key into this field. For example:
```

```

Note that the`-----BEGIN PUBLIC KEY-----`and`-----END PUBLIC KEY-----`markers are required.
- Another key: Select to add additional keys (up to a maximum of ten).
- (Optional) Specify additional details for JWT token validation:
- 

In the Issuers section, specify values that are allowed in the issuer (`iss`) claim of a JWT being used to access the API deployment:
- Allowed issuers: Specify the URL (or a text string) for an identity provider that is allowed in the issuer (`iss`) claim of a JWT to be used to access the API deployment. For example, to enable a JWT issued by OCI IAM with Identity Domains to be used to access the API deployment, enter`https://identity.oraclecloud.com/`. See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- Another issuer: Select to add additional identity providers (up to a maximum of five).
- 

In the Audiences section, specify values that are allowed in the audience (`aud`) claim of a JWT being used to access the API deployment :
- Allowed audiences: Specify a value that is allowed in the audience (`aud`) claim of a JWT to identify the intended recipient of the token. For example, the audience could be, but need not be, the API gateway's hostname. See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- Another audience: Select to add additional audiences (up to a maximum of five).
- 

Claims validation: (Optional) In addition to the values for the audience`aud`and issuer`iss`claims that you already specified, you can specify names and values for one or more additional claims to validate in a JWT. Note that any key names and values you enter are simply handled as strings, and must match exactly with names and values in the JWT. Pattern matching and other datatypes are not supported.
- Claim is required: Specify whether the claim in the Claim key field must be included in the JWT.
- Claim key: (Optional) Specify the name of a claim that can be, or must be, included in a JWT. If the claim must be included in the JWT, select Required . The claim name you specify can be a reserved claim name such as the subject (`sub`) claim, or a custom claim name issued by a particular identity provider.
- Claim values: (Optional) Specify an acceptable value for the claim in the Claim key field. Select the plus sign (+) to enter another acceptable value. If you specify one or more acceptable values for the claim, the API gateway validates that the claim has one of the values you specify.

Note that you can specify a claim in a JWT without specifying a value for it. To do so, enter the claim's name in the Claim key field, leave the Claim values field blank, and set Claim is required as appropriate.
- Specify how you want the API gateway to handle a failed authentication response (returned after an unsuccessful attempt to validate a missing or invalid token) by setting up a validation failure policy:
- If you want the API gateway to send an HTTP 401 status code and the`WWW-Authenticate`header in the response (the default response to a missing or invalid token), select Default (HTTP 401 Unauthorized) .
- 

If you want the API gateway to use an OpenID Connect authorization flow to obtain a new JWT access token, select OAuth 2.0 . Note that this option is only available if you selected OAuth 2.0 introspection endpoint from the Validation Type list earlier. Specify:
- Scopes: One or more access scopes to include in a`scope`claim sent to the authorization server. To use the OpenID Connect authorization flow, you must include`openid`as one of the scopes. For example,`openid`,`email:read`,`profile`.
- Response type: The type of response required from the authorization flow. Enter`code`as the response type.
- Fallback redirect path: (optional) A relative path in the current API deployment to which to redirect API clients if the original request was a PUT request or a POST request. For example,`/home`

If the original request was a GET request, request processing resumes with a new JWT access token, so a fallback path is not used.
- Logout path: (optional) A relative path to a logout back end in the current API deployment. The path you specify must match the route path defined for the logout back end. For example,`/revoke`

An API client can call the logout back end to revoke tokens. A call to the logout back end can include a post-logout URL as a query parameter named`postLogoutUrl`. See[Adding Logout as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogoutbackends.htm).
- 

Login path: (optional) A relative path to a login back end in the current API deployment. The path you specify must match the route path defined for the login back end (that is, the value must exactly match a route with a Backend type of Login ). For example,`/auth/callback`

The identity provider redirects API clients to the login back end as part of the authentication flow. See[Adding Login as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingloginbackends.htm).
- Response expiry in hours: (optional) The length of time to cache the JWT token generated by the authorization flow. The default is 1 hour.
- Use OAuth2 introspection endpoint client credentials: Specify whether to use the same client details that you previously specified for the OAuth 2.0 introspection endpoint to obtain a new JWT access token (which is usually the case). If you do not want to use the details you previously specified, enter different client details to use to obtain a new JWT access token from the authorization server, as follows:
- Client ID: The client ID to send to the introspection endpoint. For example,`5hsti38yhy5j2a4tas455rsu6ru8yui3wrst4n1`
- Vault: The name of a vault in the Vault service that contains the client secret to send to the introspection endpoint, from the list of vaults in the specified compartment.
- Vault secret: The name of the vault secret that contains the client secret to send to the introspection endpoint, from the list of vault secrets in the specified compartment. .
- Vault secret version number: The version of the vault secret that contains the client secret to send to the introspection endpoint.

You can optionally choose to store in cookies the tokens and values obtained during OpenID authorization flows, by selecting Advanced options and selecting:
- Use PKCE: (optional) Specify whether to use PKCE (Proof Key for Code Exchange) for additional security. PKCE is an OAuth 2.0 security extension to prevent CSRF (Cross-Site Request Forgery) and authorization code injection attacks. PKCE is not a replacement for a client secret, and PKCE is recommended even if a client secret is used. For more information about PKCE, see the[OAuth 2.0 documentation](https://oauth.net/2/).
- Use cookies for session: (optional) Specify how to store newly generated JWT tokens as non-human-readable strings at the end of an OpenID Connect authorization flow:
- Select this option if you want to store the new JWT token in a session cookie. To prevent potential CSRF attacks, when the API gateway stores the token in a session cookie, it also returns a CSRF token in an X-CSRF-TOKEN response header. Subsequent requests to the API gateway (apart from GET requests) must include the CSRF token in an X-CSRF-TOKEN request header, in addition to the JWT token in the session cookie that is included automatically.
- Do not select this option if you do not want to store the new JWT token in a session cookie. Instead, the API gateway returns a non-human-readable token in an X-APIGW-TOKEN response header. Subsequent requests to the API gateway must include the same token in an X-APIGW-TOKEN request header.

See[Notes about Cross-Site Request Forgery (CSRF) Protection](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm#Using_JSON_Web_Tokens_JWTs_to_Add_Authentication_and_Authorization_to_API_Deployments__section_csrf_protection)
- Use cookies for intermediate steps: (optional) Specify how to store authorization flow intermediate step values (for example, request parameters). Select this option to store the values in browser cookies. Deselect this option to store the values with the API gateway.
- If you want to customize the response to an unsuccessful attempt to validate a missing or invalid token, select Custom response , and specify a status code (and an optional message body) to return to the API client:
- HTTP status code: Enter an alternative HTTP status code. For example,`500`.
- Message body: Enter a message body. For example,`Unfortunately, authentication failed.`The message body can include any context variable (except for`request.body`).
- Optionally, modify the headers of the response that the API gateway returns to the API client by specifying a header transformation response policy. For more information about header transformation policies, see[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm).
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
- Login: For a login back end, you define a static route to which the identity provider redirects API clients as part of the authentication flow. The route path must exactly match the login path specified in the OAuth 2.0 validation failure policy. See[Adding Login as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingloginbackends.htm).
- 

To specify an authorization policy that applies to an individual route, select Show route request policies , select the Add button beside Authorization , and specify:
- 

Authorization Type: How to grant access to the route. Specify:
- Any: Only grant access to end users that have been successfully authenticated, provided the JWT has a`scope`claim that includes at least one of the access scopes you specify in the Allowed Scope field. In this case, the authentication policy's Enable anonymous access option has no effect.
- Anonymous: Grant access to all end users, even if they have not been successfully authenticated using the JWT. In this case, you must have selected the authentication policy's Enable anonymous access option.
- Authentication only: Only grant access to end users that have been successfully authenticated using the JWT. In this case, the authentication policy's Enable anonymous access option has no effect.
- Allowed Scope: If you selected Any as the Authorization Type , enter a comma-delimited list of one or more strings that correspond to access scopes in the JWT. Access will only be granted to end users that have been successfully authenticated if the JWT has a`scope`claim that includes one of the access scopes you specify. For example,`read:hello`
Note  
  

If you don't include an authorization policy for a particular route, access is granted as if such a policy does exist and Authorization Type is set to Authentication only . In other words, regardless of the setting of the authentication policy's Enable anonymous access option:
- only authenticated end users can access the route
- all authenticated end users can access the route regardless of access scopes in the JWT's`scope`claim
- anonymous end users cannot access the route
- Select Create , and then select Next to review the details you entered for the API deployment.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
