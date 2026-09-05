# Assertion Grant Type
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm
- Fetched: 2026-09-05 02:16 CDT

# Assertion Grant Type

Use this grant type when you want to use an existing trust relationship expressed as an assertion and without a direct user approval step at the OAuth Authorization Server.

The following diagram displays the Assertion Grant Type flow.

In this OAuth flow:
- 
A user attempts to access a client application, sending a generated user assertion.
Note  
  
The process of how the assertion is acquired is out of scope for this explanation
- 

The client application requests an access token, and often a refresh token, by providing a user assertion or a third-party user assertion and client credentials.
- 

The Authorization Server returns the access token to the client application.
- 

The client application uses the access token in an API call to obtain protected data, such as a list of users.

Function Available
Requires client authentication Yes
Requires client to know user credentials No
Browser-based end user interaction

Note: The process to generate the assertion may involve user interaction. No
Can use an external Identity Provider for authentication Yes
Refresh token is allowed Yes
Access token is in the context of the end user

An access token will be in the context of the subject of the assertion, which may be an end user, a service, or the client itself. Maybe

See an example[Assertion Grant Type authorization flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm#AssertionClientSideAppAuth).

## Assertion Grant Type Authorization Flow Example

In this example flow, Example.com has subscribed to several Oracle Cloud PaaS and SaaS applications. Example.com users want to be able to access Oracle Cloud properties without having to go through the authorization process themselves (delegated authorization).
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
When you create an application using the Assertion grant type in the identity domain Console:
- 

Specify Mobile Application as the application type.
- 

Select Assertion as the grant type.

See[Assertion Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm)for more information on the Assertion grant type and an authorization flow diagram.

Authorization Flow
- 

A user attempts to access a client application (such as JCS).

The URL contains query parameters that indicate the type of access being requested. The SAML2 assertion is Base64 encoded and the recipient value in the SAML assertion must be one of the following:
- The issuer in the Issuer field of the OAuth Settings in the user interface.
- Or,`https://<domainURL>/`.
- Or, the value of`secure_saml_sp_sso_endpoint`in the discovery response. Example Request Using the Authorization Header
```

```

Example Request Using the Authorization Header Including Refresh Token in Request
```

```

Example Request Using a JWT Client Assertion
```

```

Example Request Using a JWT Client Assertion Including Refresh Token in Request
```

```

Example Request Using mTLS

To find out how to get the`secureDomainURL`, see[Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm).
```

```

- 

An Oracle Web Services Manager (client-side) agent intercepts the client application making a REST API call to the Resource Server (Fusion applications) to obtain an access token.
- 

The OAuth Authorization Server authenticates the client application based on the Authorization header or the assertion sent and returns an access token containing all applicable scopes based on the privileges represented by the application roles granted to the requesting client application.
-
