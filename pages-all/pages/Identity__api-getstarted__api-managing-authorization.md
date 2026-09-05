# Managing Authorization Using the API
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm
- Fetched: 2026-09-05 02:17 CDT

# Managing Authorization Using the API

The identity domains REST API supports both token-based authorization and OCI request signatures. For security reasons, the identity domains REST API isn't accessible using only the username and password that you use to sign in to the identity domain. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.

identity domains REST API use the OAuth 2.0 protocol for authentication and authorization and support these common authorization scenarios:
- 

Web server
- 

Mobile
- 

JavaScript applications

The Authorization section discusses the OAuth 2.0 scenarios that identity domains support.

This section contains the following topics:
- [Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm#registering_a_client_application)
- [Security Recommendations](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm#SecurityChecklist)
- [Scopes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Scopes.htm)
- [Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm)
- [Supported Tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedTokens.htm)
- [Token Validation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenValidation.htm)
- [Working with AppRoles](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/working_with_app_roles.htm)
- [Authentication and On-Demand MFA API HTTP Status Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIStatusCodes.htm)
- [Authentication and On-Demand MFA API Error Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIErrorCodes.htm)

## Registering a Client Application

An application must be registered as an OAuth 2 Client using the identity domain. OAuth clients are HTTP clients that can get and then use an access token.

Complete the following steps to use an OAuth client to access identity domains REST API:
- 

Sign in to the identity domain using the username and password found in your Welcome email.
- 

Create an OAuth client application and make note of the client ID and client secret.
Note  
  
When you configure the OAuth client application, select the application roles that you want to assign to the application. This enables your application to access the REST APIs that each of those assigned application roles can access. Each application role has scopes assigned to it that define an even more fine-grain level of access to API operations. For example, select Identity Domain Administrator from the list. All REST API operations available to the identity domain administrator will be accessible to the application.
- 

Use the client ID and client secret to request an access token from the IAM OAuth Service.
- 

Include the access token in the appropriate HTTP header when you make REST API calls.

More Information
- For more information on registering a client application, see[Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/register-client-app.htm).
- 

For more information on grant types, see[Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm).
- 

To walk through the steps yourself, see[Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm).
- 

For a list of all available endpoint operations and the application roles required to access them, see[AppRole Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm).
- 

For a list of which AppRoles can be granted to both clients and users and which can only be granted to clients, see[AppRoles That Can Be Granted to Clients and Users](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AppRoleClientsUsers.htm).

## Security Recommendations

To securely integrate your applications with identity domains using OAuth, you must implement security controls recommended by the standard.

The security controls may be considered mandatory or optional depending on your application confidentiality, integrity, and availability requirements.
A secure OAuth integration requires:
- 

Security controls implemented across all OAuth participants, which includes the Authorization Server ( IAM), the Resource Owner (user), the Client, and the Resource Server applications
- 

Confidentiality of key information: code, access_token, refresh_token, client credentials, and user credentials
- 

Server authentication established between OAuth participants (to avoid impersonation attacks)
- 

Proper information validation for any request (especially for JSON Web Token (JWT) access tokens)
- 

Use of tokens with minimal scopes and timeout (to reduce the exposure in case of disclosure and to support the token revocation)
- 

Use of typical information security principles such as least privilege

### Resources

For more information about OAuth security, access the following links:
- 

[The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
- 

[OAuth 2.0 Threat Model and Security Considerations](https://tools.ietf.org/html/rfc6819)
- 

[JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519)
- 

[JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://tools.ietf.org/html/rfc7523)
Note  
  
We recommend that you monitor security proactively so that you can quickly identify new security threats.

### Security Recommendations Checklist

This page lists the most relevant security recommendations as a checklist, so that you can validate your application security and address the security items according to your expectations.

### Encryption
- 

Use TLS in Client and Resource Server Applications

The use of TLS with all applications provides confidentiality in communications between identity domain, resource owners, client applications, and resource server applications. This prevents eavesdropping during transmission of the authorization code, access tokens, refresh tokens, client credentials, and user credentials, and preventing replay attacks.
- 

Establish Server Authentication (HTTPS with Trusted CA Validation)

Server authentication allows clients, resource servers, and resource owners to establish communication between themselves and with an identity domain after verifying the public certificate against the trusted CA.

If the server fails to provide a trusted certificate (provided by a trusted CA and with a matching hostname), the communication is considered a man-in-the-middle attack.

Server authentication prevents spoofing, proxying, man-in-the-middle, and phishing attacks to capture authorization codes, access tokens, client credentials, and user credentials.
- 

Consider Using a Trusted Assertion with Identity Domains

Critical security clients can use a client assertion with key cryptography (instead of a client secret) for authentication.
- 

Protect the Redirect URI with HTTPS and Trusted CA Validation

HTTPS and using trusted CA validation prevents authorization "code" phishing and user session impersonation.

### Administration
- 

Configure Applications Following the Least Privilege Principle

Applications should be configured in an identity domain with only the minimum rights needed for their operation.

Narrowing down the scope, flows, grant types, and operations improves the security posture and reduces the impact of a compromised application.
- 

Provide a Meaningful Name and Description for Applications

The application information appears for users under the My Apps and the consent pages.

The use of meaningful application names and descriptions may prevent users from making mistakes during consent authorization and also contributes to better audit reporting.
- 

Provide a Meaningful Description for Scopes

The scope description appears on the consent page. Explaining the scope, which the user is about to grant, in an understandable way prevents the user from making mistakes during authorization and contributes to better audit reporting.
- 

Avoid Scopes Provided Without Consent

To leverage transparency and rely on the resource owner, provide scopes without permission only when a scope is mandatory, and the user must not be able to deny it.
- 

Reduce the Access Token Time Out and Use Refresh Tokens

Identity domains support JWT, an access token that can be validated in resource servers without checking the token in the identity domain. Because of this, access tokens with long duration can't be easily revoked.

To implement timely revocation, you can configure the access token with a short lifetime, and then use the refresh token for requesting new access tokens. To perform a timely revocation, you need to revoke the refresh token.
- 

Rotate the Application's Client Secrets

For security critical implementations, implement a client secret rotation. This reduces the risk of getting a compromised client secret explored.

### Resource Owner (User)
- 

Keep the Resource Owner Informed

Scope use with consent provides transparency to the resource owner and prevents applications from requesting scopes that aren't required.
- 

User Awareness

Teach users how to protect their credentials and identify client, resource server application, and identity domain legitimacy (especially when authentication and consent pages appear). This reduces the risk of phishing attacks and the compromise of user credentials.

### Application Development
- 

Protect Codes, Access Tokens, Refresh Tokens, and Client Credentials

Applications must preserve the confidentiality of codes, access tokens, refresh tokens, and client credentials. When you develop the application, consider the following measures (among other application security measures):
- 

Don't store codes (use the code only during runtime to obtain the access token)
- 

Keep access tokens in transient memory and limit their grants
- 

Store refresh tokens and client credentials in secure places that can be accessed only by the application
- 

Protect the Redirect URL

The redirect URL (from where the identity domain retrieves the authorization code) is considered a key component for OAuth security. Be careful when you define this URL to avoid threats such as cross site request forgery and denial of service.
- 

Read Tokens from the Native Apps File System

Attackers may try to get file system access on the device and read the refresh tokens using a malicious application. To reduce this risk, store secrets in secure storage and use device lock to prevent unauthorized device access.
- 

Implement Controls for Cloned and Stolen Devices with Native Apps

To reduce risks when a device with Native Apps gets cloned or stolen, use device lock to prevent unauthorized access and revoke refresh tokens.
- 

Validate Application Security Prior to Publication

Test the application and its hosting environment security before publishing the application to reduce vulnerabilities. Threats related to application hosting and development aren't addressed by identity domains. These threats include but aren't limited to indirect access to application databases and storage, select-jacking, cross-site scripting, script/SQL injection, and information confidentiality flows on the application.
- 

Apply Least Privilege During Scope Request

Client applications should request tokens that contain only scopes that it will possibly or actually use.

The use of the`urn:opc:idm:__myscopes__ scope`, although convenient, may retrieve more tokens than needed by the client application.

A token with extensive scopes can increase the security impact when a token is compromised.

See[Scopes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Scopes.htm)for information about using the scope parameter and an access token to grant different levels of access to identity domains.
- 

Validate JWT Tokens

When receiving an access token (JWT) from any party (except the identity domain server in a direct request from your application), validate the JWT following the[JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://tools.ietf.org/html/rfc7523)and the[JWT](https://tools.ietf.org/html/rfc7519)RFCs.

See[Token Validation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenValidation.htm)for more information on how to validate the token.
Note  
  
Resource servers must process information only after the entire JWT validation is performed.
- 

Receive JWT Tokens Properly

Resource server applications must receive the access token using only the`Authorization: bearer <token>`header to avoid threats related to parameter caching.
- 

Implement 2-Way TLS Between Client and Resource Server Applications

For security critical applications, you can implement a 2-way TLS between client and resource server applications to reduce the risk of denial of service (DoS) and impersonation attacks.

Don't write applications that collect authentication information directly from users.
- 

Prevent Select-Jacking

For newer browsers, avoid iFrames during authorization by enforcing the use of the`X-FRAME-OPTIONS`header.

For older browsers, JavaScript frame-busting techniques can be used but may not be effective in all browsers.
- 

Avoid the Use of Resource Owner Password Credentials
The resource owner flow allows a client to request an access token using an end user's ID, password, and the client's own credentials. This grant type presents a higher risk because:
- 

It's in charge of collecting the user credentials on the client application (maintains the UID/password anti-pattern).
- 

Doesn't present a consent screen for scope requests.

Except for migration reasons, avoid the use of this grant type.
- 

Use the`Cache-Control="no-store"`Header

This header minimizes the risk of not protecting authenticated content and leaking confidential data in HTTP proxies.
- 

Avoid Requests with Sensitive Information Sent Using URL Parameters

The URL parameters (used on GET requests) can be logged in any component between applications such as application logs, proxy servers, firewalls, and network edge components.

Identity domains implement alternative search REST endpoints using POST that addresses this risk. See the[Query Parameters](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISQueryParameters.htm)
