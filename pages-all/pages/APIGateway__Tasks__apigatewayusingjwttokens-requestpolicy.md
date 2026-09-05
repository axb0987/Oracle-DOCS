# Using a JWT_AUTHENTICATION Authentication Request Policy (no longer recommended)
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-requestpolicy.htm
- Fetched: 2026-09-05 01:39 CDT

# Using a JWT_AUTHENTICATION Authentication Request Policy (no longer recommended)

When using an authentication request policy of type JWT_AUTHENTICATION, before an end user can access an API deployment that uses JSON Web Tokens (JWTs) for authentication and authorization, they must obtain a JWT from an identity provider.
Note  
  

In earlier releases, you might have created authentication request policies of type JWT_AUTHENTICATION to use JWTs for authentication.

If you are creating new authentication request policies to use JWTs, we now recommend you create authentication request policies of type TOKEN_AUTHENTICATION instead (see[Using the Console to Add Token Authentication and Authorization Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usingconsole.htm)and[Editing a JSON File to Add Token Authentication and Authorization Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usinjson.htm)). We also recommend you migrate existing JWT_AUTHENTICATION request policies to TOKEN_AUTHENTICATION policies.

Note that existing JWT_AUTHENTICATION request policies are currently still supported. Also note that although you can create new JWT_AUTHENTICATION request policies by defining the API deployment specification in a JSON file (as described in the original instructions in this section), we recommend you create authentication request policies of type TOKEN_AUTHENTICATION instead.

When calling an API deployed on an API gateway, the API client provides the JWT as a query parameter or in the header of the request. The API gateway validates the JWT using a corresponding public verification key provided by the issuing identity provider. Using the API deployment's JWT_AUTHENTICATION authentication request policy, you can configure how the API gateway validates JWTs:
- You can configure the API gateway to retrieve public verification keys from the identity provider at runtime. In this case, the identity provider acts as the authorization server.
- You can configure the API gateway in advance with public verification keys already issued by an identity provider (referred to as 'static keys'), enabling the API gateway to verify JWTs locally at runtime without having to contact the identity provider. The result is faster token validation.

To add a new JWT_AUTHENTICATION authentication and authorization request policy to an API deployment specification in a JSON file:
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
- `"isAnonymousAccessAllowed": <true|false>`optionally indicates whether unauthenticated (that is, anonymous) end users can access routes in the API deployment specification. If you never want anonymous end users to be able to access routes, set this property to`false`. If you don't include this property in the`authentication`policy, the default of`false`is used. Note that if you do include this property and set it to`true`, you also have to explicitly specify every route to which anonymous access is allowed by setting the`type`property to`"ANONYMOUS"`in each route's`authorization`policy.
- `<issuer-url>`is the URL (or a text string) for an identity provider that is allowed in the issuer (`iss`) claim of a JWT to be used to access the API deployment. For example, to enable a JWT issued by OCI IAM with Identity Domains to be used to access the API deployment, enter`https://identity.oraclecloud.com/`. You can specify one or multiple identity providers (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `<"tokenHeader"|"tokenQueryParam">: <"<token-header-name>"|"<token-query-param-name>">`indicates whether it is a request header that contains the JWT (and if so, the name of the header), or a query parameter that contains the JWT (and if so, the name of the query parameter). Note that you can specify either`"tokenHeader": "<token-header-name>"`or`"tokenQueryParam": "<token-query-param-name>">`, but not both.
- `<tokenAuthScheme>`is the name of the authentication scheme to use if the JWT is contained in a request header. For example,`"Bearer"`.
- `<intended-audience>`is a value that is allowed in the audience (`aud`) claim of a JWT to identify the intended recipient of the token. For example, the audience could be, but need not be, the API gateway's hostname. You can specify one audience or multiple audiences (up to a maximum of five). See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).
- `"type": <"REMOTE_JWKS"|"STATIC_KEYS">`indicates how you want the API gateway to validate JWTs using public verification keys. Specify`REMOTE_JWKS`to configure the API gateway to retrieve up to ten public verification keys from the identity provider at runtime. Specify`STATIC_KEYS`to configure the API gateway with up to ten public verification keys already issued by an identity provider (enabling the API gateway to verify JWTs locally without having to contact the identity provider).
- 

`<public-key-config>`provides the details of JWT validation, according to whether you specified`"REMOTE_JWKS"`or`"STATIC_KEYS"`as the value of`"type":`as follows:
- 

If you specified`"type": "REMOTE_JWKS"`to configure the API gateway to validate JWTs by retrieving public verification keys from the identity provider at runtime, provide details as follows:

```

```

where:
- `"uri": "<uri-for-jwks>"`specifies the URI from which to retrieve the JSON Web Key Set (JWKS) to use to verify the signature on JWTs. For more information about the URI to specify, see[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm). Note the following:
- The URI must be routable from the subnet containing the API gateway on which the API is deployed.
- If the API gateway fails to retrieve the JWKS, all requests to the API deployment will return an HTTP 500 response code. Refer to the API gateway's execution log for more information about the error (see[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm)).
- Certain key parameters must be present in the JWKS to verify the JWT's signature (see[Key Parameters Required to Verify JWT Signatures](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-keyparams.htm)).
- The JWKS can contain up to ten keys.
- `"maxCacheDurationInHours": <cache-time>`specifies the number of hours (between 1 and 24) the API gateway is to cache the JWKS after retrieving it.
- `"isSslVerifyDisabled": <true|false>`indicates whether to disable SSL verification when communicating with the identity provider. Oracle recommends not setting this option to`true`because it can compromise JWT validation. API Gateway trusts certificates from multiple Certificate Authorities issued for OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta.

For example:

```

```

- 

If you specified`"type": "STATIC_KEYS"`, the details to provide depend on the format of the key already issued by the identity provider (regardless of format, you can specify up to ten keys):
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
- `verifyClaims`optionally specifies additional claim names and values for one or more additional claims to validate in a JWT (up to a maximum of ten).
- `"key": "<claim-name>"`is the name of a claim that can be, or must be, included in a JWT. The claim name you specify can be a reserved claim name such as the subject (`sub`) claim, or a custom claim name issued by a particular identity provider.
- `"values": ["<acceptable-value>", "<acceptable-value>"]`(optionally) indicates one or more acceptable values for the claim.
- `"isRequired": <true|false>`indicates whether the claim must be included in the JWT.

Note that any key names and values you enter are simply handled as strings, and must match exactly with names and values in the JWT. Pattern matching and other datatypes are not supported
- `maxClockSkewInSeconds: <seconds-difference>`optionally specifies the maximum time difference between the system clocks of the identity provider that issued a JWT and the API gateway. The value you specify is taken into account when the API gateway validates the JWT to determine whether it is still valid, using the not before (`nbf`) claim (if present) and the expiration (`exp`) claim in the JWT. The minimum (and default) is`0`, the maximum is`120`.

For example, the following`authentication`policy configures the API gateway with a public verification key already issued by an identity provider to validate the JWT in the Authorization request header:

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
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Example: Migrating a JWT_AUTHENTICATION Request Policy to a TOKEN_AUTHENTICATION Request Policy

This section shows an example of an existing JWT_AUTHENTICATION request policy migrated to a TOKEN_AUTHENTICATION policy.

One way to approach the migration is to create an empty TOKEN_AUTHENTICATION request policy, and then populate it with values from the JWT_AUTHENTICATION request policy

### Before Migration:

The original JWT_AUTHENTICATION request policy, before migration:

```

```

### After Migration:

The new TOKEN_AUTHENTICATION request policy populated with values from the original JWT_AUTHENTICATION request policy:
```

```
