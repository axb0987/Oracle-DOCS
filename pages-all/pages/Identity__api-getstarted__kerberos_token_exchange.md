# Token Exchange Grant Type: Exchanging a Kerberos Token for a UPST
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm
- Fetched: 2026-09-05 02:17 CDT

# Token Exchange Grant Type: Exchanging a Kerberos Token for a UPST

Use Kerberos token exchange where Kerberos is the authentication provider and you need to exchange Kerberos tokens for IAM tokens or principals to access OCI services. You exchange Kerberos tokens for OCI user principal session tokens (UPST) in IAM.

[Kerberos Token Terms](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#)

Term Description
Kerberos

A cross-platform authentication and single sign-on system. The Kerberos protocol provides mutual authentication between two entities relying on a shared secret (symmetric keys). Kerberos authentication requires a client, a server, and a trusted party to mediate between them called the Key Distribution Center (KDC).

The following is also required:
- 

A Principal: An identity for a user (a user is assigned a principal), or an identity for an application offering Kerberos services.
- 

A Realm: A Kerberos server environment, which can be a domain name such as`example.com`. Each Kerberos realm has at least one Web Services Security KDC.

The Kerberos Token profile of WS-Security allows business partners to use Kerberos tokens in service-oriented architectures (SOAs).
Kerberos Key Distribution Center (KDC) A third-party authentication server.
Active Directory (AD) A repository for the KDC server.
Keytab

A file that stores the actual encryption key that can be used instead of a password challenge for a specific principal. Keytab files are useful for noninteractive use cases.

Tip: The KDC admin tool can be used to create a keytab file. During keytab creation, the encryption type can be specified. Use the following encryption type:`aes256-cts-hmac-sha1-96`.
Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO)

Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO) is a GSSAPI "pseudo mechanism" used by client/server software to negotiate the choice of security technology.

Kerberos tickets are wrapped as part of the SPNEGO token so that the token works with HTTP based application layer.

SPNEGO Token Format and Details

The SPNEGO token format is defined in RFC 4178. The token is a serialized data structure that contains the following fields:
- `mechTypes`: A sequence of object identifiers (OID) that lists the supported authentication mechanisms.
- `mechToken`: An optimistic mechanism token. This is a token that's used to negotiate the actual authentication mechanism that will be used.
- `krb5Creds`: A Kerberos blob. This is a binary blob that contains the Kerberos authentication information.

The SPNEGO token is encoded in ASN.1. The following is an example of a SPNEGO token:
```

```

GSSAPI Generic Security Services Application Program Interface
IAM Token Exchange Service API IAM identity domain OAuth service:`/oauth2/v1/token`. The API accepts both standard OAuth based authentication headers/payload, and OCI Signatures. To learn how to use an OAuth client with an identity domain to access the REST APIs, see[Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm).
Identity Propagation Trust Configuration Use Identity Propagation Trust configurations to establish the trust between OCI Identity and an external identity provider and validate the external identity provider token and the mapping of the external identity provider's user identity with the user identity in IAM. Identity Propagation Trust also facilitates identity propagation from an external identity provider into OCI. The`/IdentityPropagationTrust`endpoint design is generic and works with any cloud provider. To create an Identity Propagation Trust configuration, see[Step 6: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-identity-propagation-trust-configuration).
Service User A user without interactive login privileges. These Service Users can be granted to groups and service roles. Applications can use these Service Users or the logged-in user can impersonate them to obtain a temporary UPST. Using a Service User is optional. For more information about using Service Users, see[Step 5: Use a Service User (Optional)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-service-user).
User Principal Session Token (UPST) An IAM generated token. Also known as a security token. It represents the authenticated Service User.

## Kerberos Token Exchange Steps

Use the following steps to exchange a Kerberos token for a UPST:
- [Step 1: Create a Vault and Add the Keytab File Contents](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-oci-vault-add-keytab)
- [Step 2: Create the Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__keytab-required-iam-policy)
- [Step 3: Create an Identity Domain Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-identity-domain-app-allow-token-exchange)
- [Step 4: Generate a SPNEGO Token For a Specific User Principal](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__generate_spnego_token)
- [Step 5: Use a Service User (Optional)](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-service-user)
- [Step 6: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__create-identity-propagation-trust-configuration)
- [Step 7: Get the OCI UPST](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#kerberos_token_exchange__get-oci-upst)

## Step 1: Create a Vault and Add the Keytab File Contents

Create a Vault and add the keytab file content as a base64-encoded string. Note: IAM doesn't store the keytab file in its file system.

Use the following steps as a guide:
- Create a Vault. See[Creating a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).
- Read the keytab content in Base64 format.
- Go to the Vault and store it as is, making sure to check Base64 as the Secret Type Template while creating secret. See[Creating a Secret in a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm).

## Step 2: Create the Required IAM Policy

Create an IAM policy in the tenancy to allow an identity domain resource to access Vault. This allows IAM to retrieve the keytab configuration from Vault. Use the following example as a guide:
```

```

## Step 3: Create an Identity Domain Application

Create an identity domain Confidential application. After you create the application, save the client id and the client secret in a secure location. See[Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../applications/add-confidential-application.htm).

## Step 4: Generate a SPNEGO Token For a Specific User Principal

- Use Java code to connect to the KDC Server and generate the SPNEGO token.
- Copy that SPNEGO token to form the token request.

Use the following Java code example as a guide:

```

```

## Step 5: Use a Service User (Optional)

A Service User is an identity domains User with the attribute`serviceUser`set to`true`.

Note  
  
Using a Service User is optional. If user impersonation will be used as part of the Trust configuration, then Service Users are needed. Otherwise, any other identity domain user is used. Only identity domain administrators can create, replace, update or delete a Service User. Other administrators may read Service Users and their attributes.

To use a Service User, create one without interactive login privileges. These Service Users can be granted to groups and service roles. Your applications can use these Service Users or the logged-in user can impersonate them to obtain a temporary UPST token.

Service Users have the following characteristics:
- Must have a userName . First name and last name isn't required.
- Can have an email address (Optional).
- Can be a member of groups and application roles.
- Can't have API keys.
- Can't use self-service endpoints.
- Can't have passwords and password policies don't apply.

Request Example: Create a Service User

The following shows an example of a request with the minimum attributes required to create a Service User.
```

```

Response Example: Create a Service User

The following shows an example of a response when creating a Service User.
```

```

## Step 6: Create an Identity Propagation Trust Configuration

The Identity Propagation Trust configuration is used to establish the trust between OCI Identity and the external Cloud providers, the validation of the Cloud provider token, and the mapping of the Cloud provider's user identity with the identity domains`service`user identity.

[Detailed Description of an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#)

Attribute Mandatory? Descriptions and Examples
name Yes

The name of the trust.
type Yes

The token type:
- spnego
- jwt
- saml
- aws-credential
issuer Yes

Use Issuer to help find the Trust identification. For example, if the SPNEGO token is generated using the service principal,`IAMSp`, then`IAMSp`is the issuer value.

Example:`IAMTokenExchangeServicePrincipal`
active Yes

If enabled,`true`.

If disabled,`false`.
oauthClients Yes

A list of OAuth Clients who are allowed to get tokens for a specific trusted partner.
Example:
```

```

allowImpersonation (make use of serviceUser) No

Boolean value. Specifies whether the resulting UPST should contain the authenticated user as the subject, or if it should impersonate a Service User in IAM.
impersonatingServiceUser

Yes, if`allowImpersonation`is set to`true`.

Specifies which resulting principal is going to impersonate based on the token claim name and the value conditions. You can:
- Allow a specific impersonating principal for all the identity provider (IdP) authenticated users.
- Set rules to define impersonation conditions:
- Based on the Token claim name
- Condition: contains (`co`) or equals (`eq`)
- Value:
- Can be a string.
- Array of values and complex/composite values aren't supported.
- With equals condition: wild card (*) is allowed .
- With contains condition: wild card (*) isn't supported .
- Impersonating principal.

Example:
- Rule:`"username" eq kafka*`
- Mapped Service User:`kafka`
- Result: All the authenticated users starting with the`kafka`prefix are impersonated with the IAM Service User`kafka`. The resulting UPST contains`kafka`as the authenticated user principal.

If impersonation is allowed, the resulting OCI security token (UPST), will have the original authenticated user related claim (`source_authn_prin`) as well to indicate on whose behalf impersonation is done.
- If subject claim name is configured , it will be used to extract that claim value.
- If subject claim name isn't configured , it defaults to`sub`in the incoming token. If`sub`claim itself isn't present, it's ignored. Evaluation stops with the first matched rule and the corresponding resulting principal is returned using the display name attribute. If no rules are matched, then the token request fails with errors.
keytab

Yes, if the token type is`SPNEGO`.

Retrieves the keytab configuration from Vault.
Important:
- 

The token exchange service retrieves the secret information based on the secret OCID and the secret version.
- 

If keytab is rotated in the KDC server, then you must update the secret information in the Identity Propagation Trust configuration.
- 

If keytab is rotated in Vault, then you must update the secret information in the Identity Propagation Trust configuration.

Request Example: Create an Identity Propagation Trust Configuration
The following shows an example of a request to create an Identity Propagation Trust configuration.
```

```

Response Example: Create an Identity Propagation Trust Configuration
The following shows an example of a response when creating an Identity Propagation Trust configuration.
```

```

## Step 7: Get the OCI UPST

[Detailed Description of the UPST Token Request Payload](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/kerberos_token_exchange.htm#)

Request Parameter Valid Value

`grant_type`

`'grant_type=urn:ietf:params:oauth:grant-type:token-exchange'`

`requested_token_type`

`'requested_token_type=urn:oci:token-type:oci-upst'`

`public_key`

`'public_key=<public-key-value>'`

The public key workflow:
- The workload generates a key pair.
- The public key is sent as part of token exchange request, which gets added as a claim,`jwk`, into the resulting UPST.
- The private key is used to generate the OCI signatures for the OCI native services API invocation along with the UPST.
- OCI services authentication validates the UPST, extracts the`jwk`claim from the UPST, and then uses it to validate OCI signature.

`subject_token_type`

`'subject_token_type=spnego'`

- spnego
- jwt
- saml
- aws-credential

`subject_token`

`'subject_token=<subject-token>'`

If the token type is:
- `spnego`: The opaque encrypted token.
- `jwt`or`saml`: The`jwt`or`saml`assertion value as is.
- `aws-credential`: The base64 encoded value of the AWS Credentials which appear in XML format.

`issuer`

Mandatory if the token type is`spnego`.

Example:

`IAMTokenExchangeServicePrincipal`

UPST Token Request Example: OCI Signature-based

The following shows an example OCI signature-based cURL request.
```

```

UPST Token Request Example: Identity Domain App-based

The following shows an example OCI identity domain app-based cURL request.
```

```
