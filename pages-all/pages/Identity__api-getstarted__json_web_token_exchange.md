# Token Exchange Grant Type: Exchanging a JSON Web Token for a UPST
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm
- Fetched: 2026-09-05 02:17 CDT

# Token Exchange Grant Type: Exchanging a JSON Web Token for a UPST

JWT-to-UPST token exchange allows federated identities (users or apps authenticated using IDCS or another identity provider) to securely access OCI services (OCI Control Plane) without managing OCI native users or API keys.
- JWT (JSON Web Token) : Issued by a trusted IdP such as external or OCI-native identity providers (IdPs), it contains signed claims about the user or service.
- UPST (User Principal Security Token) : A short-lived token OCI accepted as authentication for API access.
- The Token Exchange Endpoint validates the JWT, extracts claims, and issues a short lived UPST.

This allows users authenticated using external IdPs, such as Okta, Microsoft Entra ID, and others, or the OCI IdP itself, to gain access to OCI resources.

[JWT Token Terms](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#)

Term Description
IAM Token Exchange Service API IAM identity domain OAuth service:`/oauth2/v1/token`. The API accepts both standard OAuth based authentication headers/payload, and OCI Signatures. To learn how to use an OAuth client with an identity domain to access the REST APIs, see[Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm).
Identity Propagation Trust Configuration Use Identity Propagation Trust configurations to enable secure end-to-end identity propagation from an external identity provider (IdP) into Oracle Cloud Infrastructure (OCI). This mechanism allows OCI Identity to validate the external IdP's token and establish a trusted mapping between the external user's identity and an IAM user or service principal in OCI.

By sending the authenticated user's security context from the frontend (for example, an external IdP) to the backend services within OCI, identity propagation eliminates the need for generic or privileged accounts. It enhances security, enables detailed auditability of API calls, and supports advanced authentication scenarios. The`/IdentityPropagationTrust`API endpoint is cloud-agnostic and supports integrations with any cloud provider. To create an Identity Propagation Trust configuration, see[Step 4: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__create-identity-propagation-trust).
Service User A user without interactive sign in privileges. Service users can be granted to groups and service roles. Applications can use service users or logged-in users can impersonate them to obtain a temporary UPST. Using a service user is optional. For more information about using service users, see[Step 3: (Optional) Use a Service User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__use-service-user).
User Principal Session Token (UPST) An OCI IAM generated token that can be used to access OCI services (OCI Control Plane). A UPST is also known as a security token when you use it with SDK or Terraform. It represents the authenticated service user principal.

## Flow

Disclaimer: All product names, logos, and brands and logos are trademarks of their respective owners and used here for informational purposes only.

## JWT to UPST Token Exchange Steps

Use the following steps to exchange a JWT token for a UPST:
- [Step1: (Optional) Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__create-identity-domain)
- [Step 2: Create Identity Domain Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__create-applications)
- [Step 3: (Optional) Use a Service User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__use-service-user)
- [Step 4: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__create-identity-propagation-trust)
- [Step 5: Generating a Public Key](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__generate-public-key)
- [Step 6: Generate a JWT Token to exchange for UPST](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__generate-jwt-token)
- [Step 7: Get the OCI UPST](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__get-oci-upst)

## Step1: (Optional) Creating an Identity Domain

Create a new identity domain if it doesn't exist. See[Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../domains/to-create-new-identity-domain.htm).

## Step 2: Create Identity Domain Applications

An OAuth Client is a trusted application registered with Identity Cloud Service to authenticate and get access tokens using OAuth 2.0 flows. You use this client to:
- 

Obtain an access token to call IDCS Admin APIs.
- 

Federate app identity to exchange JWT for UPST.

See[Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../applications/add-confidential-application.htm). After you create the application, save the client id and the client secret in a secure location. You require two identity domain applications following Principle of Least Privilege (PoLP):
- An application with Identity Domain Administrator (IDA) App role. You use an access token generated using this app to perform operations on Identity Propagation Trust ([Step 4: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__create-identity-propagation-trust)) and service user ([Step 3: (Optional) Use a Service User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__use-service-user)).
- Another identity domain application without the Identity Domain Administrator App role, or any admin role. You use client credentials for this second identity domain application to invoke the token exchange API. You must authorize this application to be used with token exchange by configuring a client ID for the application in`IdentityPropagationTrust`.

Also, the application with elevated Identity Domain Administrator App role can perform JWT to UPST Token Exchange as well.

## Generating an Access Token with Identity Domain Administrator role

Use the application with Identity Domain Administrator App role defined to generate an access token. See[Generating Access Tokens](https://docs.oracle.com/en/cloud/paas/identity-cloud/idcsa/op-oauth2-v1-token-post.html). Use the access token generated to perform CRUD (Create, Replace, Update, Delete) operations on`IdentityPropagationTrusts`([Step 4: Create an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__create-identity-propagation-trust)) and service user ([Step 3: (Optional) Use a Service User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#jwt_token_exchange__use-service-user)).
Note  
  
Alternatively, you can generate a personal access token to use without creating applications. This offers the advantage of not leaving a confidential application with the Identity Domain Admin role. You must be signed in to the same domain where you're configuring the trust. For information on generating a personal access token, see[Generating an Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../usersettings/generate-personal-access-tokens.htm).

## Step 3: (Optional) Use a Service User

A service user is an identity domain user without interactive sign-in privileges. They have minimal privileges.

Service users can be granted to groups and apps. Applications can use service users or the signed in user can impersonate them to obtain a temporary UPST token.

Service users have the following characteristics:
- Must have a userName . First name and last name isn't required.
- Can have an email address (Optional).
- Can be a member of groups and application roles.
- Can't have API keys.
- Can't use self-service endpoints.
- Can't have passwords, and password policies don't apply.
Note  
  
Using a service user is optional. If user impersonation is used as part of the Trust configuration, then service users are needed. Otherwise, any other identity domain user is used. Only identity domain administrators can create, replace, update or delete a service user. Other administrators may read service users and their attributes.

Request Example: Create a Service User

The following shows an example of a request with the minimum attributes required to create a service user with the attribute`serviceUser`set to`true.`
```

```

Response Example: Create a Service User

The following shows an example of a response when creating a service user.
```

```

## Step 4: Create an Identity Propagation Trust Configuration

The Identity Propagation Trust configuration is used to establish the trust between OCI Identity and the external Cloud providers, the validation of the Cloud provider token, and the mapping of the Cloud provider's user identity with the identity domains`service`user identity.

[Detailed Description of an Identity Propagation Trust Configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#)

Attribute Mandatory? Descriptions and Examples
`name`Yes

The name of the trust.
`type`Yes

The token type: jwt
`issuer`Yes

Use unique issuer to help find the Trust identification.
`active`Yes

If enabled,`true`.

If disabled,`false`.
`oauthClients`Yes

A list of OAuth clients who are allowed to get tokens for a specific trusted partner.
Example:
```

```

`allowImpersonation`(make use of`serviceUser`) No

Boolean value. Specifies whether the resulting UPST should contain the authenticated user as the subject, or if it should impersonate a service user in IAM.
`impersonatingServiceUsers`

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
- Mapped service user:`kafka`
- Result: All the authenticated users starting with the`kafka`prefix are impersonated with the IAM service user`kafka`. The resulting UPST contains`kafka`as the authenticated user principal.

If impersonation is allowed, the resulting OCI security token (UPST), will have the original authenticated user related claim (`source_authn_prin`) as well to indicate on whose behalf impersonation is done.
- If subject claim name is configured , it is used to extract that claim value.
- If subject claim name isn't configured , it defaults to`sub`in the incoming token. If`sub`claim itself isn't present, it's ignored. Evaluation stops with the first matched rule and the corresponding resulting principal is returned using the display name attribute. If no rules are matched, then the token request fails with errors.
`publicCertificate`If the public key endpoint is not provided or not available with the provider. Ensure the public key is mandatory if a public key endpoint is not provided.
`publicKeyEndpoint`Either provide the public key API URL, or the public key must be uploaded as in the example that follows. The cloud provider's public key API. SAML and OIDC providers expose the API to retrieve the public key for signature validation.

Alternatively, store the public certificate in the configuration itself.

Request Example: Create an Identity Propagation Trust Configuration
The following shows an example of a request to create an Identity Propagation Trust configuration.
```

```

Response Example
```

```

Request Example: For`allowImpersonation`set to`false`Identity Propagation Trust Configuration
```

```

Request Example: Retrieving an Identity Propagation Trust Configuration
```

```

If`allowImpersonation`is set to "`true`" and`impersonationServiceUsers`is defined in the Identity Propagation Trust use the following request example.
```

```

Response Example
```

```

## Step 5: Generating a Public Key

Use the following commands in a terminal (Linux/macOS) or Git Bash on Windows:
```

```

After running these:
- 

`private_key.pem`is the private key, used to sign the JWT.
- 

`public_key.pem`is the public key, used by OCI to verify the JWT signature.
Note  
  
Keep the private key secure. Only share the public key with OCI.

## Step 6: Generate a JWT Token to exchange for UPST

Generate a JWT token with OCI's[Resource Owner Password Credentials Workflow](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csimg/resource-owner-password-credentials-workflow.html),[Client Credentials Workflow](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csimg/client-credentials-workflow.html)and[User Assertion Workflow](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csimg/user-assertion-workflow.html), or with any external IdPs such as Microsoft Entra ID, Google Firebase Authentication, AWS IAM Outbound Identity Federation, Okta, and others. The JWT token generated:
- 

Contains claims about the user or workload.
- 

Is signed by the IdP's private key so that OCI can verify its authenticity using the public key.
- 

Is exchanged at the OCI security token endpoint for a UPST.

## Step 7: Get the OCI UPST

JWT is exchanged at the OCI token exchange endpoint. The token endpoint decodes and verifies the JWT signature using the public key from trust configuration, validates issuer and matching claims as defined in the Identity Propagation Trust, and generates UPST.

The UPST generated received is used to access resources using OCI SDK/API.

[Detailed Description of the UPST Token Request Payload](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/json_web_token_exchange.htm#)

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

`'subject_token_type=jwt`
- `jwt`
`subject_token`

`'subject_token=<subject-token>'`

If the token type is:
- `jwt`or`assertion`the value as is.

UPST Token Request Example: Identity Domain App-based

The following shows an example OCI identity domain app-based cURL request.
```

```
