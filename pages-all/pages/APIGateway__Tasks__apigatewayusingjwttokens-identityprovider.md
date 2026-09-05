# Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-identityprovider.htm
- Fetched: 2026-09-05 01:39 CDT

# Identity Provider Details to Use for iss and aud Claims, and for the JWKS URI

The identity provider that issued the JSON Web Token (JWT) determines the allowed values you have to specify for the issuer (`iss`) and the audience (`aud`) claims in the JWT. Which identity provider issued the JWT also determines the URI from which to retrieve the JSON Web Key Set (JWKS) to verify the signature on the JWT.

Note that regardless of identity provider, a JWKS can contain a maximum of ten keys.

Use the following table to find out what to specify for JWTs issued by the OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Okta, and Auth0 identity providers.

Identity Provider

Issuer (`iss`) claim

Audience (`aud`) claim

Format of URI from which to retrieve the JWKS
OCI IAM with Identity Domains https://identity.oraclecloud.com

Customer-specific.

See[Managing Applications](https://docs.oracle.com/iaas/Content/Identity/applications/overview.htm)in the[OCI IAM with Identity Domains documentation](https://docs.oracle.com/iaas/Content/Identity/applications/overview.htm).

https://&lt;tenant-base-url&gt;/admin/v1/SigningCert/jwk
IDCS https://identity.oraclecloud.com/

Customer-specific.

See[Validating Access Tokens](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/TokenValidation.html)in the[Oracle Identity Cloud Service documentation](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/TokenValidation.html).

https://&lt;tenant-base-url&gt;/admin/v1/SigningCert/jwk

To obtain the JWKS without logging in to Oracle Identity Cloud Service, see[Change Default Settings](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/change-default-settings.html)in the[Oracle Identity Cloud Service documentation](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/change-default-settings.html).
Okta https://&lt;your-okta-tenant-name&gt;.com

Customer-specific.

The audience configured for the Authorization Server in the Okta Developer Console. See[Additional validation for access tokens](https://developer.okta.com/code/dotnet/jwt-validation/#additional-validation-for-access-tokens)in the[Okta documentation](https://developer.okta.com/code/dotnet/jwt-validation/#additional-validation-for-access-tokens).

https://&lt;your-okta-tenant-name&gt;.com/oauth2/&lt;auth-server-id&gt; /v1/keys

See the[Okta documentation](https://developer.okta.com/docs/reference/api/oidc/#keys).
Auth0 https://&lt;your-account-name&gt;.auth0.com/

Customer-specific.

See[Audience](https://auth0.com/docs/glossary)in the[Auth0 documentation](https://auth0.com/docs/glossary)
