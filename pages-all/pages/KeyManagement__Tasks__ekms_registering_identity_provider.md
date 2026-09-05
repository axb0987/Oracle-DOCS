# Registering Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_registering_identity_provider.htm
- Fetched: 2026-09-05 02:35 CDT

# Registering Identity Provider

Register Identity Provider in the third-party KMS for validating JSON Web Token (JWT).

OCI EKM ensures vendor neutrality by using OAuth2, the industry-standard protocol, to sign cryptographic operation requests using customer-granted access tokens. All cryptographic requests are transmitted securely over a dedicated, encrypted connection to the third-party KMS network. Upon receiving the request, the third-party KMS validates the authenticity by verifying the OAuth2 JSON Web Tokens (JWTs) token using JSON Web Key Set (JWKS), a well-Known endpoint issued by OCI Identity Cloud Service.

For OCI EKMS to securely communicate with the third-party KMS, you must register JWKS URL and Confidential resource app credentials for validating with JWT.

If you're a Thales CipherTrust Manager (CM) user, see[Register JWT Issuer in Thales CipherTrust Manager (CM)](https://thalesdocs.com/ctp/cm/latest/reference/cckmapi/ora-ext-apis/index.html#register-jwt-issue-on-cipher-trust-manager)in the Thales documentation for information on registering a JWT issuer. Thales users can use the following steps to register:
- 

Go to your domain in OCI Console and find the Domain URL . See[Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm)for instructions.

A domain URL looks like the following example:
```

```

- 

Add /.well-known/idcs-configuration after .com and navigate to this URL. For example
```

```

-
