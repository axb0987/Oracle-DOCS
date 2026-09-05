# Resource Owner Password Credentials Grant Type
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm
- Fetched: 2026-09-05 02:17 CDT

# Resource Owner Password Credentials Grant Type

Use this grant type when the resource owner has a trust relationship with the client, such as a computer OS or a highly privileged application, because the client must discard the password after using it to obtain the access token.

The following diagram displays the Resource Owner Password Credentials Grant Type flow.

In this OAuth flow:
- 

User clicks a link in the client application requesting access to protected resources.
- 

The client application requests the resource owner's username and password.
- 

The user signs in with their username and password.
- 

The client application exchanges those credentials for an access token, and often a refresh token, from the Authorization Server.
- 

The Authorization Server returns the access token to the client application.
- 

The client application uses the access token in an API call to obtain protected data, such as a list of users.

Function Available
Requires client authentication No
Requires client to have knowledge of user credentials Yes
Browser-based end-user interaction No
Can use an external Identity Provider for authentication No
Refresh token is allowed Yes
Access token is in the context of the end user Yes

See an example[Resource Owner Password Credentials Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm#ROWebServerAppAuth).

## Resource Owner Password Credentials Grant Type Authorization Flow Example

This authorization flow example walks you through obtaining an access token by using the resource owner's (user) credentials.

When you create an application using the Resource Owner grant type in the identity domain Console:
- 

Specify Trusted Application as the application type.
- 

Select Resource Owner as the grant type.
- 

Specify the Redirect URI, which is where responses to authentication requests are sent.

See[Resource Owner Password Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm)for more information on the Resource Owner Password Credentials grant type and an authorization flow diagram.

Authorization Flow
- 

A user clicks a link in the web server client application, requesting access to protected resources from a third-party web server application.
- 

The client application collects the user's username and password and requests an access token from the OAuth Authorization Server (AS).

The request URL contains query parameters that indicate the type of access being requested:

Example Request Using the Authorization Header
```

```

Example Request Using the Authorization Header Including Refresh Token in the Request
```

```

Example Request Using a JWT Client Assertion
```

```

Example Request Using a JWT Client Assertion Including Refresh Token in the Request
```

```

Example Request Using mTLS

To find out how to get the`secureDomainURL`, see[Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm).
```

```

- 

The OAuth Authorization Server returns the access token. The access token contains all applicable scopes based on the privileges represented by the identity domain application roles granted to the requesting client application and the user being specified by the client's request (if present).
Note  
  
If a request was made for an invalid scope, an error is returned instead of the access token.
-
