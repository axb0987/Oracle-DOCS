# Authorization Code Grant Type
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm
- Fetched: 2026-09-05 02:16 CDT

# Authorization Code Grant Type

Use this grant type when you want to obtain an authorization code by using an authorization server as an intermediary between the client application and the resource owner using identity domains.

The following diagram displays the Authorization Code Grant Type flow.
In this OAuth flow:
- 

A user clicks a link in a web server client application, requesting access to protected resources.
- 

The client application redirects the browser to the authorization endpoint`oauth2/v1/authorize`with a request for an authorization code.
- 

The Authorization Server returns an authorization code to the client application through a browser redirect after the resource owner gives consent.
- 

The client application then exchanges the authorization code for an access token, and often a refresh token.
- 

The Authorization Server returns the access token to the client application.
- 
The client application uses the access token in an API call to obtain protected data.
Note  
  
Resource owner credentials are never exposed to the client.

Function Available
Requires client authentication No
Requires client to know user credentials No
Browser-based end-user interaction Yes
Can use an external Identity Provider for authentication Yes
Refresh token is allowed Yes
Access token is in the context of the end user Yes

See an example[Authorization Code Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm#ACWebServerAppAuth).

## Authorization Code Grant Type Authorization Flow Example

This authorization flow example walks you through an OpenID Connect login request using an authorization code.

This flow is a three-legged OAuth flow, which refers to scenarios in which the application calls the identity domain APIs on behalf of end users, and in which user consent is sometimes required. This flow shows how to configure Federated Single Sign-On between an identity domain and a custom application using OAuth 2.0 and OpenID Connect.

When you create an app using the Authorization Code grant type in the identity domain Console:
- 

Specify Trusted Application as the type of application.
- 

Select Authorization Code as the grant type.
- 

Specify the Redirect URI, which is where responses to authentication requests are sent.
- 

Optionally, select the Refresh Token grant type to return a refresh token with the access token.

See[Authorization Code Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm)for more information on the Authorization Code grant type and an authorization flow diagram.

Authorization Flow
- 

A user clicks a link in the web server client application (Customer Quotes), requesting access to protected resources.
- 

The Customer Quotes app redirects the browser to the identity domain authorization endpoint`(oauth2/v1/authorize)`with a request for an authorization code.
The request URL contains query parameters that indicate the type of access being requested.
Note  
  
A nonce value is a cryptographically strong random string that you use to prevent intercepted responses from being reused.

Example Request: Confidential/Trusted Client
```

```

Example Request: Confidential/Trusted Client Including Refresh Token in Request
```

```

Example Request: Public Client
```

```

Example Request Using PKCE
```

```

- 

The identity domain receives the request and identifies that the Customer Quotes app (identified by its`client_id`) is requesting an authorization code to get more information about the resource owner (scope`openid).`
- 

If the user isn't already logged in, IAM challenges the user to authenticate. IAM checks the user's credentials.
- 
If the login is successful, IAM redirects the browser to the Customer Quotes application with an authorization code.
Note  
  
If the user doesn't authenticate, an error is returned rather than the authorization code.
- 

The Customer Quotes application extracts the authorization code and makes a request to an identity domain to exchange the authorization code for an access token.

Request Example: Confidential/Trusted Client
```

```

Request Example: Public Client
```

```

Example Request Using PKCE
```

```

Example Request Using mTLS

To find out how to get the`secureDomainURL`, see[Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm).
```

```

- 

IAM validates the grant and user data associated with the code (`client_id, client_secret`, and the authorization code).
- 

An[Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm)and an[Identity Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedTokens.htm#IdentityToken)are returned. The access token contains information about which scopes the Customer Quotes application can request on behalf of the user. The application can use this token when requesting APIs on behalf of the user.

The Identity Token is retrieved only when you request the`openid`scope. This token contains identification information about the user and is used for federated authentication.
- 

The Customer Quotes application processes the`id_token`and then extracts the user's information returned from IAM.
-
