# Supported Tokens
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedTokens.htm
- Fetched: 2026-09-05 02:17 CDT

# Supported Tokens

A token is used to make security decisions to authorize a user and to store tamper-proof information about a system entity in an identity domain.

Identity domains support JSON Web Tokens (JWT). A JWT is a JSON-based open standard[(RFC 7519)](https://tools.ietf.org/html/rfc7519)that defines a compact and self-contained way for securely sending information between parties as a JSON object. This information can be verified and trusted because it's digitally signed. JSON Web Tokens consist of three parts separated by periods`(xxxx.yyyy.zzzz)`:
- 

Header . Consists of two parts: the type of token (JWT) and the hashing algorithm being used, such as SHA256
- 

Payload . Contains the claims (the token data)
- 

Signature . Consists of the encoded token header and the encoded payload signed with the identity domain private key. The signature is used to verify that the sender of the JWT is who it says it's and ensures that the message wasn't changed along the way.

Identity domains support three different tokens: identity token, access token, and client assertion.

To access detailed information on each supported token, select any of the following links:
- 

[Identity Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedTokens.htm#IdentityToken)
- 

[Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm)
- 

[Client/User JWT Assertion](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ClientAssertion.htm)

For information about token expiration go to:
- [Token Expiry Table](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenExpiryTable.htm)
- [Specifying a Custom Access Token Expiration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm#customexpiry)

## Identity Token

An Identity Token is an integrity-secured, self-contained token (in JSON Web Token (JWT) format) that's defined in the OpenID Connect standard containing claims about the end user. The Identity Token is the primary extension that OpenID Connect makes to OAuth 2.0 to enable authentication in an identity domain.

The Identity Token JWT consists of three components, a header, a payload, and the digital signature. Following the JWT standard, these three sections are Base64URL encoded and separated by periods.
Note  
  
OpenID Connect requests must contain the`openid`scope value.

OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It allows an IAM identity domain client application (registered as an OAuth 2 client with client ID and client secret) to verify the identity of the end user based on the authentication performed by an Authorization Server (AS), and to obtain basic profile information about the end user in an interoperable, REST-like manner. OpenID Connect allows clients of all types, including web-based, mobile, and JavaScript clients to request and receive information about authenticated sessions and end users. See[OpenID Connect](http://openid.net/connect/)for more information.

Name Value
`amr`Authentication Methods References. JSON array of strings that are identifiers for authentication methods used in the authentication. For example, values might indicate that both password and OTP authentication methods were used.
`at_hash`OAuth 2 Access Token hash value.
`aud`Identifies recipients for which this ID Token is intended. Must be the OAuth 2.0`client_id`(per the[OpenID Connect specification).](http://openid.net/specs/openid-connect-core-1_0.html#IDToken)This is the OAuth client name (app.name) that's making the request.`Aud`also contains the IAM identity domain Issuer, thereby turning the token type ( IT ) into an IAM identity domain User Assertion.
`authn_strength*`The value returned by Cloud SSO indicating Authentication Strength from AuthN Context.
`auth_time`The time (UNIX epoch time) when Cloud SSO actually authenticated the user (in seconds, coming from AuthN Context).
`azp`Authorized party. The party to which the ID Token was issued. If present, it MUST contain the OAuth 2.0 Client ID of this party. This claim is only needed when the ID Token has a single audience value and that audience is different than the authorized party. It may be included even when the authorized party is the same as the sole audience. The azp value is a case-sensitive string that contains a StringOrURI value.
`exp`The expiration time (UNIX epoch time) on or after which the ID Token must not be accepted for processing. This value must be same as the`session_exp.`
`iat`The time (UNIX epoch time) when the JWT was created (in seconds). UNIX Epoch Time is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in Coordinated Universal Time (UTC) until the date/time.
`iss`The principal that issued the token:`https://<domainURL>`
`jti`The server-generated unique identifier for the JWT ID.
`nonce`The string value used to associate a client session with an ID Token and to mitigate replay attacks. This value is provided by Cloud Gate.
`session_exp*`The time (UNIX epoch time) when the Cloud SSO session expires (seconds, must be the same SSO's session expiration in AuthN context).
`sid`The session ID from Cloud SSO (255 maximum ASCII characters) from AuthN Context.
`sub`Identifies the user. The subject identifier is locally unique, never reassigned, and is intended to be consumed by the client: User Login ID (255 maximum ASCII characters). This is the user's login ID from AuthN Context.
`sub_mappingattr*`The attribute used to find the sub in the ID store.
`tok_type*`Identifies the token type:`IT`
`user_displayname*`The User Display Name (255 maximum ASCII characters) from AuthN Context.
`user_csr*`Indicates ( true ) that the user is a Customer Service Representative (CSR).
`user_id*`The user's IAM identity domain GUID from AuthN Context.
`user_lang*`The user's preferred language.
`user_locale*`The user's locale.
`user_tenantname*`The User Tenant Name (255 maximum ASCII characters). Tenant's GUID is specifically not saved in the token
`user_tz*`
