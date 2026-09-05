# Editing a JSON File to Add Token Authentication and Authorization Request Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usinjson.htm
- Fetched: 2026-09-05 01:39 CDT

# Editing a JSON File to Add Token Authentication and Authorization Request Policies

Add authentication and authorization request policies to an API deployment specification in a JSON file.
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

Insert a`requestPolicies`section before the`routes`section (if one doesn't exist already) to create an`authentication`request policy that applies to all routes in the API deployment specification. For example:

```

```

- 

Add the`authentication`request policy as follows

```

```

where:
- `"authentication": {"type": "TOKEN_AUTHENTICATION"...`specifies that you want to use tokens for authentication.
- `<"tokenHeader"|"tokenQueryParam">: <"<token-header-name>"|"<token-query-param-name>">`indicates whether it is a request header that contains the token (and if so, the name of the header), or a query parameter that contains the token (and if so, the name of the query parameter). Note that you can specify either`"tokenHeader": "<token-header-name>"`or`"tokenQueryParam": "<token-query-param-name>">`, but not both. For example,`"tokenHeader": "Authorization"`
- `<tokenAuthScheme>`is the name of the authentication scheme to use if the token is contained in a request header. For example,`"Bearer"`.
- `"isAnonymousAccessAllowed": <true|false>`optionally indicates whether unauthenticated (that is, anonymous) end users can access routes in the API deployment specification. If you never want anonymous end users to be able to access routes, set this property to`false`. If you don't include this property in the`authentication`policy, the default of`false`is used. Note that if you do include this property and set it to`true`, you also have to explicitly specify every route to which anonymous access is allowed by setting the`type`property to`"ANONYMOUS"`in each route's`authorization`policy.
- `maxClockSkewInSeconds: <seconds-difference>`optionally specifies the maximum time difference between the system clocks of the identity provider that issued a JWT and the API gateway. The value you specify is taken into account when the API gateway validates the JWT to determine whether it is still valid, using the not before (`nbf`) claim (if present) and the expiration (`exp`) claim in the JWT. The minimum (and default) is`0`, the maximum is`120`.
- `"validationPolicy": {<validation-policy-config>}`specifies a validation policy to validate tokens, as described in the following steps.
- If you want the API gateway to validate both JWT tokens and non-JWT tokens with an OAuth 2.0 authorization server's introspection endpoint using client credentials (including a client secret retrieved from a vault in the Vault service), add the following validation policy to the empty`validationPolicy`section:
```

```

where:
- `"validationPolicy": {"type": "REMOTE_DISCOVERY"...}`specifies that you want to validate tokens with an OAuth 2.0 authorization server's introspection endpoint using client credentials (including a client secret retrieved from a vault in the Vault service).
- `clientDetails": {"type": "CUSTOM"...}`specifies details of the client secret to retrieve from a vault in the Vault service:
- `"clientId": "<client-id>"`specifies the client ID to send to the introspection endpoint. You obtain a client ID by creating and registering a client application with the authorization server. For example,`5hsti38yhy5j2a4tas455rsu6ru8yui3wrst4n1`. See[Prerequisites for Token Authentication](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-prerequisites.htm).
- `"clientSecretId": "<secret-ocid>"`specifies the OCID of the vault secret that contains the client secret to send to the introspection endpoint. For example,`ocid1.vaultsecret.oc1.iad.amaaaaaa______cggit3q`
- `"clientSecretVersionNumber": <secret-version-number>`specifies the version of the vault secret that contains the client secret to send to the introspection endpoint. For example,`1`
- `"uri": "<well-known-uri>"`specifies the well-known URL of an authorization server from which the API gateway is to obtain authorization metadata endpoints. For example,`https://my-idp/oauth2/default/.well-known/openid-configuration`. Note the URL must be routable from the subnet containing the API gateway on which the API is deployed.
- `"isSslVerifyDisabled": <true|false>`indicates whether to disable SSL verification when communicating with the authorization server. Oracle recommends not setting this option to`true`because it can compromise JWT validation. API Gateway trusts certificates from multiple Certificate Authorities issued for OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta.
- `"maxCacheDurationInHours": <cache-time>`specifies the number of hours (between 1 and 24) the API gateway is to cache the response from the introspection endpoint.
- `"additionalValidationPolicy": {"issuers": ...}`specifies additional details for token validation:
- `<issuer-url>`is the URL (or a text string) for an authorization server that is allowed in the issuer (`iss`) claim of a JWT to be used to access the API deployment. For example, to enable a JWT issued by OCI IAM with Identity Domains to be used to access the API deployment, specify`https://identity.oraclecloud.com/`. You can specify one or multiple authorization servers (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `<intended-audience>`is a value that is allowed in the audience (`aud`) claim of a JWT to identify the intended recipient of the token. For example, the audience could be, but need not be, the API gateway's hostname. You can specify one audience or multiple audiences (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `"verifyClaims": {...}`optionally specifies additional claim names and values for one or more additional claims to validate in a JWT (up to a maximum of ten):
- `"key": "<claim-name>"`is the name of a claim that can be, or must be, included in a JWT. The claim name you specify can be a reserved claim name such as the subject (`sub`) claim, or a custom claim name issued by a particular authorization server.
- `"values": ["<acceptable-value>", "<acceptable-value>"]`(optionally) indicates one or more acceptable values for the claim.
- `"isRequired": <true|false>`indicates whether the claim must be included in the JWT.

Note that any key names and values you enter are simply handled as strings, and must match exactly with names and values in the JWT. Pattern matching and other datatypes are not supported

For example, the following`authentication`policy configures the API gateway to validate a token in the Authorization request header using client credentials (including a client secret retrieved from a vault in the Vault service) passed to an OAuth 2.0 introspection endpoint):

```

```

- 

If you want the API gateway to validate JWTs by retrieving public verification keys from the identity provider at runtime, add the following validation policy to the empty`validationPolicy`section:

```

```

where:
- `"validationPolicy": {"type": "REMOTE_JWKS"...`specifies that you want to configure the API gateway to retrieve up to ten public verification keys from the identity provider at runtime.
- `"uri": "<uri-for-jwks>"`specifies the URI from which to retrieve the JSON Web Key Set (JWKS) to use to verify the signature on JWTs. For more information about the URI to specify, see[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm). Note the following:
- The URI must be routable from the subnet containing the API gateway on which the API is deployed.
- If the API gateway fails to retrieve the JWKS, all requests to the API deployment will return an HTTP 500 response code. Refer to the API gateway's execution log for more information about the error (see[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)).
- Certain key parameters must be present in the JWKS to verify the JWT's signature (see[Key Parameters Required to Verify JWT Signatures](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-keyparams.htm)).
- The JWKS can contain up to ten keys.
- `"isSslVerifyDisabled": <true|false>`indicates whether to disable SSL verification when communicating with the identity provider. Oracle recommends not setting this option to`true`because it can compromise JWT validation. API Gateway trusts certificates from multiple Certificate Authorities issued for OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta.
- `"maxCacheDurationInHours": <cache-time>`specifies the number of hours (between 1 and 24) the API gateway is to cache the JWKS after retrieving it.
- `"additionalValidationPolicy": {"issuers": ...}`specifies additional details for token validation:
- `<issuer-url>`is the URL (or a text string) for an identity provider that is allowed in the issuer (`iss`) claim of a JWT to be used to access the API deployment. For example, to enable a JWT issued by OCI IAM with Identity Domains to be used to access the API deployment, enter`https://identity.oraclecloud.com/`. You can specify one or multiple identity providers (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `<intended-audience>`is a value that is allowed in the audience (`aud`) claim of a JWT to identify the intended recipient of the token. For example, the audience could be, but need not be, the API gateway's hostname. You can specify one audience or multiple audiences (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `verifyClaims`optionally specifies additional claim names and values for one or more additional claims to validate in a JWT (up to a maximum of ten).
- `"key": "<claim-name>"`is the name of a claim that can be, or must be, included in a JWT. The claim name you specify can be a reserved claim name such as the subject (`sub`) claim, or a custom claim name issued by a particular identity provider.
- `"values": ["<acceptable-value>", "<acceptable-value>"]`(optionally) indicates one or more acceptable values for the claim.
- `"isRequired": <true|false>`indicates whether the claim must be included in the JWT.

Note that any key names and values you enter are simply handled as strings, and must match exactly with names and values in the JWT. Pattern matching and other datatypes are not supported

For example, the following`authentication`policy configures the API gateway to validate the JWT in the Authorization request header by retrieving public verification keys from the identity provider at runtime:

```

```

- 

If you want the API gateway to validate JWTs with public verification keys already issued by an identity provider (enabling the API gateway to verify JWTs locally without having to contact the identity provider), add the following validation policy to the empty`validationPolicy`section:

```

```

where:
- `"validationPolicy": {"type": "STATIC_KEYS"...`specifies that you want to configure the API gateway with up to ten public verification keys already issued by an identity provider (enabling the API gateway to verify JWTs locally without having to contact the identity provider).
- `"keys": [{<key-config>}]`specify the identifier of the static key used to sign the JWT. The details to provide depend on the format of the key already issued by the identity provider (regardless of format, you can specify up to ten keys):
- 

If the static key is a JSON Web Key, specify`"format": "JSON_WEB_KEY"`, specify the identifier of the static key used to sign the JWT as the value of the`"kid"`parameter, and provide values for other parameters to verify the JWT's signature.

For example:

```

```

Note that certain parameters must be present in the static key to verify the JWT's signature (see[Key Parameters Required to Verify JWT Signatures](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-keyparams.htm)). Also note that`RSA`is currently the only supported key type (`kty`).
- 

If the static key is a PEM-encoded public key, specify`"format": "PEM"`, specify the identifier of the static key used to sign the JWT as the value of`"kid"`, and provide the key as the value of`"key"`.

For example:

```

```

Note that the`-----BEGIN PUBLIC KEY-----`and`-----END PUBLIC KEY-----`markers are required.
- `"isSslVerifyDisabled": <true|false>`indicates whether to disable SSL verification when communicating with the identity provider. Oracle recommends not setting this option to`true`because it can compromise JWT validation. API Gateway trusts certificates from multiple Certificate Authorities issued for OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta.
- `"maxCacheDurationInHours": <cache-time>`specifies the number of hours (between 1 and 24) the API gateway is to cache the JWKS after retrieving it.
- `"additionalValidationPolicy": {"issuers": ...}`specifies additional details for token validation:
- `<issuer-url>`is the URL (or a text string) for an identity provider that is allowed in the issuer (`iss`) claim of a JWT to be used to access the API deployment. For example, to enable a JWT issued by OCI IAM with Identity Domains to be used to access the API deployment, enter`https://identity.oraclecloud.com/`. You can specify one or multiple identity providers (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `<intended-audience>`is a value that is allowed in the audience (`aud`) claim of a JWT to identify the intended recipient of the token. For example, the audience could be, but need not be, the API gateway's hostname. You can specify one audience or multiple audiences (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `verifyClaims`optionally specifies additional claim names and values for one or more additional claims to validate in a JWT (up to a maximum of ten).
- `"key": "<claim-name>"`is the name of a claim that can be, or must be, included in a JWT. The claim name you specify can be a reserved claim name such as the subject (`sub`) claim, or a custom claim name issued by a particular identity provider.
- `"values": ["<acceptable-value>", "<acceptable-value>"]`(optionally) indicates one or more acceptable values for the claim.
- `"isRequired": <true|false>`indicates whether the claim must be included in the JWT.

Note that any key names and values you enter are simply handled as strings, and must match exactly with names and values in the JWT. Pattern matching and other datatypes are not supported

For example, the following`authentication`policy configures the API gateway with a public verification key already issued by an identity provider to validate the JWT in the Authorization request header:

```

```

- (Optional) You can specify how you want the API gateway to handle a failed authentication response (returned after an unsuccessful attempt to validate a missing or invalid token) by setting up a validation failure policy:
- If you want the API gateway to send an HTTP 401 status code and the`WWW-Authenticate`header in the response (the default response to a missing or invalid token), do not define a validation failure policy.
- 

If you want the API gateway to use an OpenID Connect authorization flow to obtain a new JWT access token, define a validation failure policy of type`OAUTH2`. Note that this option is only available if you specified a`validationPolicy`of type`REMOTE_DISCOVERY`earlier. Specify:

```

```

where:
- `"scopes": ["<scope>", "<scope"]`specifies one or more access scopes to include in a`scope`claim sent to the authorization server. To use the OpenID Connect authorization flow, you must include`openid`as one of the scopes. For example,`"scopes": ["openid", "email:read", "profile"]`
- `clientDetails": {...}`specifies the client details to use to obtain a new JWT access token from the authorization server, as follows:
- `"type": "<VALIDATION_BLOCK|CUSTOM>"`specifies whether to use the same, or different, client details to those specified in the earlier`validationPolicy`. If you want to use the same client details as before (which is usually the case), specify`"type": "VALIDATION_BLOCK"`and do not provide additional details. If you want to use different client details, specify`"type": "CUSTOM"`and set values for`"clientId"`,`"clientSecretId"`, and`"clientSecretVersionNumber"`.
- `"clientId": "<client-id>"`specifies the client ID to send to the introspection endpoint. Only used if`"type": "CUSTOM"`. For example,`5hsti38yhy5j2a4tas455rsu6ru8yui3wrst4n1`
- `"clientSecretId": "<secret-ocid>"`specifies the OCID of the vault secret that contains the client secret to send to the introspection endpoint. Only used if`"type": "CUSTOM"`. For example,`ocid1.vaultsecret.oc1.iad.amaaaaaa______cggit3q`
- `"clientSecretVersionNumber": <secret-version-number>`specifies the version of the vault secret that contains the client secret to send to the introspection endpoint. Only used if`"type": "CUSTOM"`. For example,`1`
- `"sourceUriDetails": {"type": "VALIDATION_BLOCK"}`specifies that you want to use the same URL as that specified in the earlier`validationPolicy`as the well-known URL of an authorization server from which the API gateway is to obtain authorization metadata endpoints.
- `"maxExpiryDurationInHours": <number-of-hours>`specifies the length of time to cache the JWT token generated by the authorization flow. The default is 1.
- `"useCookiesForSession": <true|false>`specifies how to store newly generated JWT tokens as non-human-readable strings at the end of an OpenID Connect authorization flow:
- Set this option to`true`if you want to store the new JWT token in a session cookie. To prevent potential CSRF attacks, when the API gateway stores the token in a session cookie, it also returns a CSRF token in an X-CSRF-TOKEN response header. Subsequent requests (apart from GET requests) must include the CSRF token in an X-CSRF-TOKEN request header, in addition to the JWT token in the session cookie that is included automatically.
- Set this option to`false`if you do not want to store the new JWT token in a session cookie. Instead, the API gateway returns a non-human-readable token in an X-APIGW-TOKEN response header. Subsequent requests to the API gateway must include the same token in an X-APIGW-TOKEN request header.

See[Notes about Cross-Site Request Forgery (CSRF) Protection](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm#Using_JSON_Web_Tokens_JWTs_to_Add_Authentication_and_Authorization_to_API_Deployments__section_csrf_protection)
- `"useCookiesForIntermediateSteps": <true|false>`specifies how to store authorization flow intermediate step values (for example, request parameters). Set this option to`true`to store the values in browser cookies. Set this option to`false`to store the values with the API gateway.
- `"usePkce": <true|false>`specifies whether to use PKCE (Proof Key for Code Exchange) for additional security. PKCE is an OAuth 2.0 security extension to prevent CSRF (Cross-Site Request Forgery) and authorization code injection attacks. PKCE is not a replacement for a client secret, and PKCE is recommended even if a client secret is used. For more information about PKCE, see the[OAuth 2.0 documentation](https://oauth.net/2/).
- `"responseType": "code"`specifies the type of response required from the authorization flow. Specify`code`as the response type.
- `"fallbackRedirectPath": "/home"`optionally specifies a relative path in the current API deployment to which to redirect API clients if the original request was a PUT request or a POST request. For example,`/home`.

If the original request was a GET request, request processing resumes with a new JWT access token, so a fallback path is not used.
- `"logoutPath": "<revoke-path>"`optionally specifies a relative path to a logout back end in the current API deployment. The path you specify must match the route path defined for the logout back end. For example,`"logoutPath": "/revoke"`.

An API client can call the logout back end to revoke tokens. A call to the logout back end can include a post-logout URL as a query parameter named`postLogoutUrl`. See[Adding Logout as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogoutbackends.htm).
- `"loginPath": "<login-path>"`optionally specifies a relative path to a login back end in the current API deployment. The path you specify must match the route path defined for the login back end (that is, the value must exactly match a route with a`<backend-type>`of`OAUTH2_LOGIN_BACKEND`). For example,`"loginPath": "/auth/callback"`. The identity provider redirects API clients to the login back end as part of the authentication flow. See[Adding Login as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingloginbackends.htm).

For example:

```

```

- If you want to customize the response to an unsuccessful attempt to validate a missing or invalid token, define a validation failure policy of type`MODIFY_RESPONSE`, and specify a status code (and an optional message body) to return to the API client, as follows:

```

```

where:
- `responseCode`: specifies an alternative HTTP status code. For example,`500`.
- `responseMessage`: (optionally) specifies a message body. For example,`Unfortunately, authentication failed.`The message body can include any context variable (except for`request.body`).
- `responseTransformations`: (optionally) modifies the headers of the response that the API gateway returns to the API client by specifying a header transformation response policy. For more information about header transformation policies, see[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm).

For example:

```

```

- 

Add an`authorization`request policy for each route in the API deployment specification:
- 

Insert a`requestPolicies`section after the first route's`backend`section, if one doesn't exist already. For example:

```

```

- 

Add the following`authorization`policy to the new`requestPolicies`section:

```

```

where:
- 

`"type": <"AUTHENTICATION_ONLY"|"ANY_OF"|"ANONYMOUS">`indicates how to grant access to the route:
- `"AUTHENTICATION_ONLY"`: Only grant access to end users that have been successfully authenticated. In this case, the`"isAnonymousAccessAllowed"`property in the API deployment specification's`authentication`policy has no effect.
- `"ANY_OF"`: Only grant access to end users that have been successfully authenticated, provided the JWT's`scope`claim includes one of the access scopes you specify in the`allowedScope`property. In this case, the`"isAnonymousAccessAllowed"`property in the API deployment specification's`authentication`policy has no effect.
- `"ANONYMOUS"`: Grant access to all end users, even if they have not been successfully authenticated. In this case, you must explicitly set the`"isAnonymousAccessAllowed"`property to`true`in the API deployment specification's`authentication`policy.
- `"allowedScope": [ "<scope>" ]`is a comma-delimited list of one or more strings that correspond to access scopes included in the JWT's`scope`claim. In this case, you must set the`type`property to`"ANY_OF"`(the`"allowedScope"`property is ignored if the`type`property is set to`"AUTHENTICATION_ONLY"`or`"ANONYMOUS"`). Also note that if you specify more than one scope, access to the route is granted if any of the scopes you specify is included in the JWT's`scope`claim.

For example, the following request policy defines a`/hello`route that only allows authenticated end users with the`read:hello`scope to access it:

```

```

- Add an`authorization`request policy for all remaining routes in the API deployment specification.
Note  
  

If you don't include an`authorization`policy for a particular route, access is granted as if such a policy does exist and the`type`property is set to`"AUTHENTICATION_ONLY"`. In other words, regardless of the setting of the`isAnonymousAccessAllowed`property in the API deployment specification's`authentication`policy:
- only authenticated end users can access the route
- all authenticated end users can access the route regardless of access scopes in the JWT's`scope`claim
- anonymous end users cannot access the route
- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
