# Token Validation
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenValidation.htm
- Fetched: 2026-09-05 02:17 CDT

# Token Validation

Why do we validate tokens? When your web application checks credentials directly, it verifies that the username and password that are presented correspond to what you maintain. When using claims-based identity, you're outsourcing that job to an identity provider.

The responsibility shifts from verifying raw credentials to verifying that the requestor went through your preferred identity provider and successfully authenticated. The identity provider represents successful authentication by issuing a token. Before you can use the information or rely on it as an assertion that the user has authenticated, you must validate it.

OpenID Discovery Document

The OpenID Connect 1.0 protocol is a simple identity layer on top of the OAuth 2.0 protocol that requires the use of multiple endpoints for authenticating users and for requesting resources that include user information, tokens, and public keys. To help with discovering what these endpoints are that you need to use, OpenID Connect allows you to use a discovery document, which is a JSON document found at a well-known location. This discovery document contains key/value pairs that provide details about the OpenID Connect provider's configuration, including the URIs of the authorization, token, userinfo, and public keys endpoints. You can retrieve the discovery document for an IAM identity domain's OpenID Connect service from:`https://<domainURL>/.well-known/openid-configuration.`

See the[Oracle Identity Cloud Service OpenID Discovery docs.](http://docs.oracle.com/en/cloud/paas/identity-cloud/idcsa/api-Discovery-OpenID%20Discovery%20Docs.html)

## Validating Identity Tokens

An Identity (ID) Token is an integrity-secured, self-contained token (in JSON Web Token format) that contains claims about the end user. It represents an authenticated user's session. Therefore, the token must be validated before an application can trust the contents of the ID Token. For example, if a malicious attacker replayed a user's ID Token that they had captured earlier, the application should detect that the token has been replayed or was used after it had expired and deny the authentication.
The ID Token is defined in the OpenID Connect standard and is the primary extension that OpenID Connect makes to OAuth 2.0 to enable authentication. ID Tokens are sensitive and can be misused if intercepted. Ensure that these tokens are handled securely by sending them only over HTTPS and only by using POST data or within request headers. If you store them on your server, you must also store them securely.
- 

Verify that the value of the audience (`aud`) claim contains the application's`client_id`value. The`aud`(audience) claim may contain an array with more than one element. The ID Token must be rejected if the ID token doesn't list the client as a valid audience, or if it contains additional audiences that aren't trusted by the client.
- 

Verify that the current time is before the time represented by the expiry time (`exp`) claim.
- 
Verify that the ID Token is properly signed by the issuer. IAM identity domain-issued tokens are signed using one of the certificates found at the URI specified in the`jwks_uri`field of the discovery document.
- 

Retrieve the tenant's public certificate from the`SigningCert/jwk`endpoint (for example,`https://acme.identity.oraclecloud.com/admin/v1/SigningCert/jwk`).
Note  
  
Because identity domains change public keys infrequently, you can cache the public keys and, in the vast majority of cases, efficiently perform local validation. This requires retrieving and parsing certificates and making the appropriate crypto calls to check the signature:
- 

Use any JWT libraries available to validate, for example, Connect2id's Nimbus JWT Library for Java. See[JWT](http://jwt.io/)for a list of available libraries.
Note  
  
In case of signature validation failure, to prevent constant re-fetches in case of attacks with bogus tokens, the re-fetching/re-caching of the public key should be based on a time interval, such as 60 minutes, so that re-fetches only happen every 60 minutes.

Example
```

```

- 

Verify that the value of the Issuer Identifier (`iss`) claim exactly matches the value of the`iss`(issuer) claim:`https://<domainURL>/`

## Validating Access Tokens
Successful OAuth transactions require the identity domain OAuth Authorization Server to issue access tokens for use in authenticating an API call. An access token represents an authorization issued to the client application that contains credentials used to access protected OAuth resources. To validate an access token issued from the Authorization endpoint, the application client should do the following:
Note  
  
See the[Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AccessToken.htm)table.
- 

Verify that the access token is properly signed by the issuer.
- 

Retrieve the tenant's public certificate from the`SigningCert/jwk`endpoint (for example, https://acme.identity.oraclecloud.com/admin/v1/SigningCert/jwk).
Note  
  
Because identity domains change public keys infrequently, you can cache the public keys and, in the vast majority of cases, efficiently perform local validation. This requires retrieving and parsing certificates and making the appropriate crypto calls to check the signature:
- 

Use any JWT libraries available to validate, for example, Connect2id's Nimbus JWT Library for Java. See[JWT](http://jwt.io/)for a list of available libraries.
- 

Pass the certificate to the respective library's API, for example, using Nimbus SignedJWT API:
```

```

Note  
  
In case of signature validation failure, to prevent constant re-fetches in case of attacks with bogus tokens, the re-fetching/re-caching of the public key should be based on a time interval, such as 60 minutes, so that re-fetches only happen every 60 minutes.
- 

Verify that the value of the Issuer Identifier (`iss`) claim exactly matches the value of the`iss`(issuer) claim:`https://<domainURL>/`
- 

Verify that the access token has the audience (`aud`) claim as requested by the client. The value of the`aud`claim changes from scope to scope. The`aud`claim is an array if there are multiple audiences and is a string if there's only one audience.

The`aud`claim is the primary audience of the IAM identity domain App's resource server. If there are any secondary audiences defined in the IAM identity domain App, then they're also added as part of the`aud`claim. As part of the access token validation, the server must allow access if one of the values in the`aud`array makes sense to the resource server.
- 

Verify that the current time is before the time represented by the expiry time (`exp`) claim.
-
