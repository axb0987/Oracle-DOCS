# Validating Tokens to Add Authentication and Authorization to API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm
- Fetched: 2026-09-05 01:39 CDT

# Validating Tokens to Add Authentication and Authorization to API Deployments

You can add authentication and authorization functionality to an API gateway by having the API gateway itself validate the tokens included in a request (as described in this topic). Alternatively, you can have the API gateway pass a multi-argument or single-argument access token included in a request to an authorizer function deployed on OCI Functions for validation (as described in[Passing Tokens to Authorizer Functions to Add Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction.htm)).

To have the API gateway itself validate the token included in a request, you create an authentication request policy of type TOKEN_AUTHENTICATION. The tokens you use to control access to APIs are often, but not always, JSON Web Tokens (JWTs).

When using a TOKEN_AUTHENTICATION policy, you enable an API deployment to use tokens for authentication and authorization by including two different kinds of request policy in the API deployment specification:
- An authentication request policy for the entire API deployment that specifies the use of tokens, including how to validate them and whether unauthenticated end users can access routes in the API deployment.
- An authorization request policy for each route that specifies the operations an end user is allowed to perform, optionally based on values specified for the`scope`claim of a JWT.

You can add authentication and authorization request policies to an API deployment specification by:
- [Using the Console.](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usingconsole.htm)
- [Editing a JSON file.](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usinjson.htm)
Note  
  

In earlier releases, you created authentication request policies of type JWT_AUTHENTICATION to use JWTs for authentication. Existing JWT_AUTHENTICATION authentication request policies are still supported (see[Notes about the use of JWT_AUTHENTICATION request policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm#Using_JSON_Web_Tokens_JWTs_to_Add_Authentication_and_Authorization_to_API_Deployments__Notes-about-JWT_AUTHENTICATION-request-policies)). However, if you are creating new authentication request policies to authenticate JWTs, we recommend you create authentication request policies as TOKEN_AUTHENTICATION policies. Using TOKEN_AUTHENTICATION policies enables you to:
- Validate both JWT tokens and non-JWT tokens.
- Validate tokens using an identity provider to obtain an introspection endpoint.
- Specify validation failure policies, including the generation of a new JWT token in the event of an invalid or missing JWT token in the original request.

## What happens during token authentication?

When an API gateway receives a request from an API client and you have specified a token authentication policy, the API gateway locates a token (for example, in a token header) and uses that token.

You specify how the API gateway validates the token it has obtained by defining the token authentication policy's validation policy to be one of the following types:
- OAuth 2.0 introspection endpoint: Specify this type of validation policy if you want the API gateway to validate a JWT or non-JWT token with the introspection endpoint of an identity provider. You have to specify the Discovery URL of the identity provider from which to obtain the introspection endpoint. In this case, the API gateway passes the client credentials (the client id, along with the client secret retrieved from the Vault service) to the identity provider to validate the token. The token is validated without the use of public keys. To make future validation faster, you can specify that you want the API gateway to cache the response from the introspection endpoint, for between 1 hour (the default) and 24 hours. If you're defining the API deployment specification in a JSON file and you want this behavior, include a validation policy of type`REMOTE_DISCOVERY`.
- Remote JWKS: Specify this type of validation policy if you want the API gateway to use public verification keys retrieved from an identity provider at runtime to verify a JWT. In this case, the API gateway contacts the identity provider to verify the JWT. The identity provider acts as the authorization server. If you're defining the API deployment specification in a JSON file and you want this behavior, include a validation policy of type`REMOTE_JWKS`.
- Static keys: Specify this type of validation policy if you want the API gateway to use public verification keys already issued by an identity provider (referred to as 'static keys') to verify a JWT. In this case, the API gateway can verify the JWT locally at runtime without having to contact the identity provider. The result is faster token validation. If you're defining the API deployment specification in a JSON file and you want this behavior, include a validation policy of type`STATIC_KEYS`

If validation succeeds, the API gateway routes the request to the appropriate API endpoint.

If validation fails due to an invalid or missing token in the original request, you specify the API gateway behavior by defining the token authentication policy's validation failure policy to be one of the following types:
- Default (HTTP 401 Unauthorized): Specify this type of validation failure policy if you want the API gateway to return an HTTP-401 response to the API client. This is the default response. If you're defining the API deployment specification in a JSON file and you want this behavior, simply don't include a validation failure policy.
- Custom response: Specify this type of validation failure policy if you want the API gateway to return an alternative response (a modified response) to the API client, instead of an HTTP-401 response. If you're defining the API deployment specification in a JSON file and you want this behavior, include a validation failure policy of type`MODIFY_RESPONSE`.
- OAuth 2.0: Specify this type of validation failure policy if you want the API gateway to obtain a new and valid JWT token from the identity provider for GET requests (having first securely stored the original request query parameters). For PUT requests and POST requests, you can specify a relative path in the current API deployment to which to redirect API clients.

Using this type of validation failure policy, you can also configure the following back ends:
- Login back end: Optionally specify a static login redirect path to identify a route in the API deployment specification that uses a login back end. The identity provider redirects API clients to this path as part of the authentication flow, and the API gateway then redirects API clients back to the route that they originally requested. See[Adding Login as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingloginbackends.htm).
- Logout back end: Optionally specify a logout path to identify a route in the API deployment specification that uses a logout back end. The API gateway removes associated session cookies, revokes tokens by calling the identity provider's end session endpoint, and redirects to an allowed post-logout URL. See[Adding Logout as an API Gateway Back End](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogoutbackends.htm).

If you're defining the API deployment specification in a JSON file and you want OAuth 2.0 validation failure behavior, include a validation failure policy of type`OAUTH2`.

Note that validation failure policies of type OAuth 2.0 currently support only the OpenID Connect authorization flow, and only JWT token generation (see[Notes about OAuth 2.0 and OpenID Connect](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm#Using_JSON_Web_Tokens_JWTs_to_Add_Authentication_and_Authorization_to_API_Deployments__section_oath2_openidconnect)). In the case of the OpenID Connect authorization flow, two tokens named`id_token`(always JWT-encoded) and`access_token`(can be JWT-encoded) are returned. The API gateway saves the token values in the`request.auth[id_token]`and`request.auth[access_token]`context variables, along with custom claims in the`request.auth[id_token_claims][<claim-name>]`and`request.auth[access_token_claims][<claim-name>]`context variables respectively (see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm)). On receipt of the new`id_token`JWT token, the API gateway saves the token values in the request context. If you have not configured a static login redirect path, the API gateway continues processing the API client’s original request using the token. If you have configured a static login redirect path, the API client returns from the identity provider to the route that uses the login back end. The API gateway then uses the saved intermediate request details to redirect the API client back to the route that the API client originally requested.

The location from which the API gateway obtains a token depends on both the type of validation policy (one of OAuth 2.0 introspection endpoint , Remote JWKS , or Static keys ) and the type of validation failure policy (one of Default (HTTP 401 Unauthorized) , Custom response , or OAuth 2.0 ), as follows:
- If you specify both a validation policy of type OAuth 2.0 introspection endpoint and a validation failure policy of type OAuth 2.0 , the API gateway initially attempts to obtain the token from one or other of the following:
- If you selected the Use cookies for session option in the validation failure policy, from a session cookie.
- Otherwise, from the X-APIGW-TOKEN header in the request.

If the API gateway cannot obtain a token from the initial location, the API gateway obtains the token from the request header or query parameter you specify in the token authentication policy.

If token validation is subsequently successful and you selected the Use cookies for session option, the API gateway stores the generated token as a non-human-readable string in a session cookie. If the API client makes a subsequent request, the token is obtained from the session cookie. To prevent CSRF attacks, when the generated token is stored in a session cookie, the API gateway also returns a CSRF token in an X-CSRF-TOKEN response header (see[Notes about Cross-Site Request Forgery (CSRF) Protection](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens.htm#Using_JSON_Web_Tokens_JWTs_to_Add_Authentication_and_Authorization_to_API_Deployments__section_csrf_protection)).
- If you do not specify both a validation policy of type OAuth 2.0 introspection endpoint and a validation failure policy of type OAuth 2.0 , the API gateway obtains the token from the request header or query parameter you specify in the token authentication policy.

## Notes about JSON Web Tokens (JWTs)

The tokens you use to control access to APIs are typically JSON Web Tokens (JWTs). A JWT is a JSON-based access token sent in an HTTP request from an API client to a resource. JWTs are issued by identity providers. API Gateway supports the use of any OAuth2-compliant identity provider, such as OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0, and Okta. If a JWT is required to access a resource, the resource validates the JWT with an authorization server using a corresponding public verification key, either by invoking a validation end-point on the authorization server or by using a local verification key provided by the authorization server.

A JWT comprises:
- A header, which identifies the type of token and the cryptographic algorithm used to generate the signature.
- A payload, containing claims about the end user's identity, and the properties of the JWT itself. A claim is a key value pair, where the key is the name of the claim. A payload is recommended (although not required) to contain certain reserved claims with particular names, such as expiration time (`exp`), audience (`aud`), issuer (`iss`), and not before (`nbf`). A payload can also contain custom claims with user-defined names.
- A signature, to validate the authenticity of the JWT (derived by base64 encoding the header and the payload).

When using JWTs to control access to APIs, you can specify that reserved claims in the JWT's payload must have particular values before the API gateway considers the JWT to be valid. By default, API gateways validate JWTs using the expiration (`exp`), audience (`aud`), and issuer (`iss`) claims, along with the not before (`nbf`) claim if present. You can also specify acceptable values for custom claims. See[Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm).

When a JWT has been validated, the API gateway extracts claims from the JWT's payload as key value pairs and saves them as records in the`request.auth`context table for use by the API deployment. For example, as context variables for use in an HTTP back end definition (see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm)). If the JWT's payload contains the`scope`claim, you can use the claim's values in authorization request policies for individual routes to specify the operations an end user is allowed to perform.

## Notes about OAuth 2.0 and OpenID Connect

The OAuth 2.0 protocol enables the safe retrieval of secure resources while protecting client credentials. OAuth 2.0 is a flexible and secure protocol that relies on SSL (Secure Sockets Layer) to ensure data between web servers and browsers remain private. Although OAuth 2.0 is different from JWT, and used for different purposes, OAuth 2.0 and JWT are compatible. Since the OAuth2 protocol does not specify the format of tokens, JWTs can be incorporated into the usage of OAuth2. For more information about OAuth 2.0, see the[OAuth 2.0 documentation](https://oauth.net/2/).

OpenID Connect is a simple identity layer on top of the OAuth 2.0 protocol. Using OpenID Connect enables API gateways to verify the identity of an API client based on authentication performed by an authorization server. OpenID Connect also enables API gateways to obtain basic profile information about the API client. For more information about OpenID Connect, see the[OpenID Connect documentation](https://openid.net/connect/).

## Notes about Cross-Site Request Forgery (CSRF) Protection

An attacker can mount a CSRF attack by exploiting the existence of a browser cookie to cause a user to submit an unintended command to a web application, such as an API gateway. If the application determines the user has already been authenticated successfully because of the browser cookie's existence, the application executes the command with potentially damaging consequences.

When you define a validation policy of type OAuth 2.0 introspection endpoint and a validation failure policy of type OAuth 2.0 , you specify how an API gateway stores a new JWT token it has obtained using the OpenID Connect authorization flow:
- Select the Use cookies for session option if you want to store the new JWT token in a session cookie. To prevent potential CSRF attacks, when the API gateway stores the token in a session cookie, it also returns a CSRF token in an X-CSRF-TOKEN response header. Subsequent mutation requests to the API gateway (such as POST, PUT, and DELETE requests, but not GET requests) must include the CSRF token in an X-CSRF-TOKEN request header, in addition to the JWT token in the session cookie that is included automatically.

Note that the API gateway also stores the CSRF token in the`request.auth[apigw_csrf_token]`context variable. If the API client is unable to read the initial X-CSRF-TOKEN response header for some reason, you can include the`request.auth[apigw_csrf_token]`context variable in a header transformation response policy to add a response header containing the CSRF token to every response returned to the API client. This approach ensures the API client can successfully extract the CSRF token from the response header for inclusion in subsequent X-CSRF-TOKEN mutation request headers it sends to the API gateway. Here's an example of a suitable header transformation response policy:
```

```

For more information about header transformation response policies, see[Adding Header Transformation Response Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaymodifyingresponsesrequests-addingresponsetransforms.htm).
- Do not select the Use cookies for session option if you do not want to store the new JWT token in a session cookie. Instead, the API gateway returns a non-human-readable token in an X-APIGW-TOKEN response header. Subsequent requests to the API gateway must include the same token in an X-APIGW-TOKEN request header.

For more information about CSRF, search online.

## Notes about the use of JWT_AUTHENTICATION request policies

In earlier releases, you might have created authentication request policies of type JWT_AUTHENTICATION to use JWTs for authentication.

If you are creating new authentication request policies to use JWTs, we now recommend you create authentication request policies of type TOKEN_AUTHENTICATION instead (see[Using the Console to Add Token Authentication and Authorization Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usingconsole.htm)and[Editing a JSON File to Add Token Authentication and Authorization Request Policies](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-usinjson.htm)). We also recommend you migrate existing JWT_AUTHENTICATION request policies to TOKEN_AUTHENTICATION policies.

Note that existing JWT_AUTHENTICATION request policies are currently still supported. Also note that although you can create new JWT_AUTHENTICATION request policies (as described in the original instructions in the section[Using a JWT_AUTHENTICATION Authentication Request Policy (no longer recommended)](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-requestpolicy.htm)
