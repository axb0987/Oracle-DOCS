# Refresh Token Grant Type
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RefreshGT.htm
- Fetched: 2026-09-05 02:17 CDT

# Refresh Token Grant Type

Use this grant type when you want a refresh token issued along with the access token. The refresh token is used to obtain a new access token without requiring the user to reauthenticate.

To refresh a token, the access token must have been requested with a grant type that supports refresh tokens, such as Authorization Code, Resource Owner Password Credentials, and Assertion. A request is then made to the token endpoint with the`grant_type`parameter set to`refresh_token.`
Note  
  
This grant type doesn't influence authorization flows.

Select a link to view a cURL example that includes a refresh token in the request:
- 

[Authorization Code Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm#ACWebServerAppAuth)
- 

[Resource Owner Password Credentials Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm#ROWebServerAppAuth)
- 

[Assertion Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm#AssertionClientSideAppAuth)

See a cURL example that uses the[Refresh Token Grant Type Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RefreshGT.htm#RTAuthFlow)

## Refresh Token Grant Type Authorization Flow Example

This authorization flow example walks you through obtaining a new access token without requiring the user to reauthenticate.

Be sure to select the refresh token grant type when specifying a grant type that supports refresh tokens, such as[Authorization Code Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm),[Resource Owner Password Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm), or[Assertion Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm).

See[Refresh Token Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RefreshGT.htm)for more information on the Refresh Token grant type.

When an application makes a request to an identity domain to obtain an access token, the request URL contains query parameters that indicate the type of access being requested.

Example Request Using the Authorization Header
```

```

Example Request Using a JWT Client Assertion
```

```

Example Request Using a Public Client
```

```

Example Request Using mTLS

To find out how to get the`secureDomainURL`, see[Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm).
```

```
