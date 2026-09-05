# Access Grant Types
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm
- Fetched: 2026-09-05 02:17 CDT

# Access Grant Types

The most important step for an application in the OAuth flow is how the application receives an access token (and optionally a refresh token). A grant type is the mechanism used to retrieve the token. OAuth defines several different access grant types that represent different authorization mechanisms.

Applications can request an access token to access protected endpoints in different ways, depending on the type of grant type specified in the client application. A grant is a credential representing the resource owner's authorization to access a protected resource. Trusted applications (such as backend services) may request access tokens directly on behalf of users. This is an OAuth two-legged authorization flow. OAuth web applications typically need to first validate the user's identity and optionally obtain the user's consent. This is an OAuth three-legged authorization flow.

For example, when using the Resource Owner grant type, the resource owner's password credentials (username and password) can be used directly as an authorization grant to obtain an access token. When using the Client Credentials grant type, the client authenticates with the OAuth service, and then requests an access token. When using the Assertion grant, a user assertion is sent along with the client information when requesting access.
Note  
  
Although you can associate more than one grant type with an application, we recommended that you select only what your application needs to use. Each grant type that you add means that the application can talk to identity domains using any of those grant types. But, the application chooses at runtime, which grant type to use.

## mTLS Client Authentication Enforcement

mTLS Client Authentication is enforced for all grant types if the token request comes through the secure transport layer (mTLS). See the details in the following paragraphs:
- If the token request comes through a secure transport layer (mTLS), the OAuth service checks both the certificate validation and the OAuth grant, for example, client credentials, user password, and so on.
- Even if the grant (client credentials, user password) is correct, if the certificate isn't correct or doesn't match the configuration in the client profile, the token request is rejected. Likewise, the token request is rejected when the certificate is correct, but the main grant of the client credentials or user password is incorrect.

## Get the secureDomainURL for mTLS
- Go to the details page for the domain in and find the domain URL. For example,
```

```

- Add /.well-known/idcs-configuration after .com in the domain URL and go to the domain configuration page.
- The URL at`secure_token_endpoint`is the`secureDomainURL`.

## More about Grant Types
Select a link for more information on each of these grant types:
- 

[Authorization Code Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AuthCodeGT.htm)
- 

[Resource Owner Password Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ROPCGT.htm)
- 

[Client Credentials Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CCGT.htm)
- 

[Assertion Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AssertGT.htm)
- 

[Implicit Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ImplicitGT.htm)
- 

[Refresh Token Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RefreshGT.htm)
- 

[Token Exchange Grant Type](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/token_exchange_grant_type.htm)
- [Token Exchange Grant Type Two-Legged Authorization Flow Example](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/token_exchange_grant_type_two_legged.htm)
- [Token Exchange Grant Type: Exchanging a Kerberos Token for a UPST](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm)
- [Token Exchange Grant Type: Exchanging a JSON Web Token for a UPST](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm)
