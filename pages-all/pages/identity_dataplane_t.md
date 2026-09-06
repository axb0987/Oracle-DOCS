# Identity Dataplane Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#dcoc-content-body)

## Identity Dataplane Common Types

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CLAIM_T Type

Syntax
```

```

Fields

Field Description

`key`

(required) The key of the claim.

`value`

(required) The value of the claim.

`issuer`

(optional) The issuer of the claim.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CLAIM_TBL Type

Nested table type of dbms_cloud_oci_identity_dataplane_claim_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PRINCIPAL_T Type

Syntax
```

```

Fields

Field Description

`subject_id`

(required) The user's OCID.

`tenant_id`

(required) The tenancy OCID.

`claims`

(required) The set of claims for this principal.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PERMISSION_T Type

Syntax
```

```

Fields

Field Description

`p`

(required) The name of the permission.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CONTEXT_VARIABLE_T Type

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the variable.

`value`

(required) The value of the variable.

`l_type`

(required) The type of the variable.

Allowed values are: 'STRING', 'NUMBER', 'ENTITY', 'BOOLEAN', 'LIST'

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CONTEXT_VARIABLE_TBL Type

Nested table type of dbms_cloud_oci_identity_dataplane_context_variable_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PERMISSION_CONTEXT_T Type

Syntax
```

```

Fields

Field Description

`permission`

(required) The permission context.

`variables`

(required) The set of variables in this permission context.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PERMISSION_CONTEXT_TBL Type

Nested table type of dbms_cloud_oci_identity_dataplane_permission_context_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHORIZATION_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`request_id`

(required) The id of this request. It is a GUID.

`user_principal`

(required) The user principal object

`svc_principal`

(required) The service principal object for service to service calls.

`service_name`

(required) The name of the service that is making this authorization request

`context`

(required) A set of permission contexts

`policy_hash`

(required) The hash of cached policy on the caller service side. If this is different than what Identity has, it will send the most recent policy statements.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ACCESSIBLE_COMPARTMENT_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`authorization_request`

(required) The authorization request.

`compartment_ids`

(required) The list of compartment ids.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMPARTMENT_METADATA_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment id.

`access_level`

(required) The access level.

Allowed values are: 'accessible', 'visible', 'inaccessible'

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMPARTMENT_METADATA_TBL Type

Nested table type of dbms_cloud_oci_identity_dataplane_compartment_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ACCESSIBLE_COMPARTMENT_RESPONSE_T Type

Syntax
```

```

Fields

Field Description

`compartments_metadata`

(required) The compartments metadata.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHORIZATION_REQUEST_TBL Type

Nested table type of dbms_cloud_oci_identity_dataplane_authorization_request_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ASSOCIATION_AUTHORIZATION_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`requests`

(required) The list of authorization requests.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTH_SERVICE_USER_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The id of the compartment.

`tenant_id`

(required) The id of the tenant.

`id`

(required) The user's Oracle ID (OCID).

`name`

(required) The name of the user.

`display_name`

(required) The display name of the user.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATE_CLIENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`request_headers`

(required) The signed headers of the original caller's request.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATE_CLIENT_RESULT_T Type

Syntax
```

```

Fields

Field Description

`principal`

(optional) The original caller's resolved principal object if the authentication succeeds, null otherwise.

`error_message`

(optional) If the authentication fails for the original caller (not failing authentication of the calling service, in which case we return 401), we return a 200, but with null principal and an error message

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATE_USER_RESULT_T Type

See ValidAuthenticateUserResult, BadUserStateAuthenticateUserResult, UserNotFoundAuthenticateUserResult, TenantNotFoundAuthenticateUserResult

Syntax
```

```

Fields

Field Description

`tenant_input`

(required) The tenant name.

`user_input`

(required) The user name.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PASSWORD_POLICY_T Type

Password policy, currently set for the given compartment.

Syntax
```

```

Fields

Field Description

`minimum_password_length`

(optional) Minimum password length required.

`is_uppercase_characters_required`

(optional) At least one uppercase character required.

`is_lowercase_characters_required`

(optional) At least one lower case character required.

`is_numeric_characters_required`

(optional) At least one numeric character required.

`is_special_characters_required`

(optional) At least one special character required.

`is_username_containment_allowed`

(optional) User name is allowed to be part of the password.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATION_POLICY_T Type

Authentication policy, currently set for the given compartment

Syntax
```

```

Fields

Field Description

`password_policy`

(optional) Password policy.

`compartment_id`

(optional) Compartment OCID.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_TENANT_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The tenant's Oracle ID (OCID).

`name`

(required) The name of the tenancy.

`service_namespace`

(optional) The service namespace.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_USER_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The user's Oracle ID (OCID).

`name`

(required) The name of the user.

`is_otp`

(required) If the provided password is a one-time password.

`is_mfa_activated`

(required) If mfa is activated.

`is_mfa_verified`

(required) If the user has been mfa verified.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATION_PRINCIPAL_T Type

Syntax
```

```

Fields

Field Description

`tenant`

(required) The tenancy object.

`l_user`

(required) The user object.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATION_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`user_name`

(required) The user name

`password`

(required) The password

`tenant_name`

(required) The name of the tenancy

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_BAD_USER_STATE_AUTHENTICATE_USER_RESULT_T Type

Syntax
```

```

Fields

Field Description

`tenant_input`

(required) The tenant name.

`user_input`

(required) The user name.

`resolved_tenant_id`

(required) The resolved tenant id.

`resolved_user_id`

(required) The resolved user id.

`user_state`

(required) The bad user state.

Allowed values are: 'USER_BLOCKED', 'USER_DISABLED', 'ONE_TIME_PASSWORD_EXPIRED', 'PASSWORD_INVALID'

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CLIENT_CREDENTIALS_RESPONSE_T Type

Syntax
```

```

Fields

Field Description

`access_token`

(required) The access token.

`token_type`

(required) The token type.

`expires_in`

(required) The amount of time until the token expires.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMMON_PRINCIPAL_T Type

Syntax
```

```

Fields

Field Description

`tenant`

(required) The tenant.

`l_user`

(required) The user.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ENTITY_STATUS_T Type

Syntax
```

```

Fields

Field Description

`status`

(required) The entity status.

`inactive_bit_mask`

(required) A bit mask showing the reason why the entity is inactive: - bit 0: ACTIVE - bit 1: SUSPENDED - bit 2: DISABLED - bit 3: BLOCKED - bit 4: LOCKED

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMPARTMENT_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the compartment.

`name`

(required) The name of the compartment.

`display_name`

(required) The display name of the compartment.

`full_name`

(required) The full name of the compartment.

`parent_compartment_id`

(required) The id of the parent compartment.

`status`

(required) The status of the compartment.

`property_map`

(required) The extended properties.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COST_TRACKING_TAG_T Type

Syntax
```

```

Fields

Field Description

`tag_namespace_id`

(required) The tag namespace id.

`tag_namespace_name`

(required) The tag namespace name.

`tag_definition_id`

(required) The tag definition id.

`tag_definition_name`

(required) The tag definition name.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CREDENTIAL_AUTHENTICATOR_INFO_T Type

Syntax
```

```

Fields

Field Description

`raw_credential`

(required) The raw credential.

`user_id`

(required) The id of the user.

`tenant_id`

(required) The id of the tenant.

`user_name`

(required) The name of the user.

`tenant_name`

(required) The name of the tenant.

`credential_identifier`

(required) The credential identifier.

`credential_list`

(required) The credential list.

`service`

(required) The name of the service that is making this authorization request.

`client_id`

(required) The id of the client.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_DERIVED_KEY_RESPONSE_T Type

Syntax
```

```

Fields

Field Description

`signing_key`

(required) The derived key.

`principal`

(required) The principal.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_FILTER_GROUP_MEMBERSHIP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`principal`

(required) A resolved principal object

`group_ids`

(required) An array of group or dynamic group Ids the resolved principal potentially belongs to.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_FILTER_GROUP_MEMBERSHIP_RESULT_T Type

Syntax
```

```

Fields

Field Description

`principal`

(required) Return passed-in resolved principal object

`group_ids`

(required) An array of group or dynamic group Ids which present the intersection between the passed-in group/dynamic-group and the actual group/dynamic-group the resovled principal belongs to.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_GENERATE_SCOPED_ACCESS_TOKEN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`scope`

(required) Scope definition for the scoped access token

`public_key`

(required) A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will be put inside the security token by the auth service after successful validation of the certificate.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_GENERATE_USER_SECURITY_TOKEN_DETAILS_T Type

Request parameters in body for obtaining a user principal session token (UPST) for self.

Syntax
```

```

Fields

Field Description

`public_key`

(required) The user-owned public key in PEM format that corresponds to the RSA key pair used for signing requests. The user also owns the corresponding private key. This public key will be put inside the user security token by the auth service after successful validation of the request.

`session_expiration_in_minutes`

(optional) User session expiration in minutes to which the requested user principal session token (UPST) is bounded. Valid values are from 5 to 60 for all realms.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_IDENTITY_PROVIDER_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The id of the provider.

`name`

(required) The name of the provider.

`tenant_name`

(required) The name of the tenant.

`tenant_id`

(required) The id of the tenant.

`redirect_uri`

(required) The SAML endpoint where user will be redirected.

`signing_certificate`

(required) The signing certificate of the provider.

`protocol`

(required) The type of the provider.

Allowed values are: 'SAML2'

`service_provider_entity_id`

(required) The id of the service provider entity.

`force_authentication`

(required) Whether to force authentication.

`authn_context_class_refs`

(required) Authentication context class refs.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_JWK_T Type

Syntax
```

```

Fields

Field Description

`n`

(required) The modulus.

`e`

(required) The exponent.

`kid`

(required) The key id.

`use`

(required) The key use.

`alg`

(required) The algorithm.

`kty`

(required) The key type.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ON_BEHALF_OF_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`request_headers`

(required) The signed headers of the customer call.

`target_service_name`

(required) The name of the target service.

`obo_token`

(optional) If you have an obo token already, exchange that for a new obo token.

`expiration`

(optional) A duration for which the obo token is requested to be valid.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PASSWORD_RESET_AUTHENTICATION_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`user_id`

(required) The id of the user

`password_reset_token`

(required) The password reset token

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_REFRESH_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`current_token`

(required) The current security token that is to be renewed.

`new_public_key`

(optional) An optional new public for the new token. If not supplied, currentToken's public key will be used.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_RESOURCE_PRINCIPAL_SESSION_TOKEN_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`resource_principal_token`

(required) The resource principal token.

`service_principal_session_token`

(required) The service principal session token.

`session_public_key`

(required) The session public key.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_SECURITY_TOKEN_T Type

Syntax
```

```

Fields

Field Description

`token`

(required) The security token, signed by auth service

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_TENANT_NOT_FOUND_AUTHENTICATE_USER_RESULT_T Type

Syntax
```

```

Fields

Field Description

`tenant_input`

(required) The tenant name.

`user_input`

(required) The user name.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THICK_AUTHORIZATION_RESPONSE_T Type

Syntax
```

```

Fields

Field Description

`policy`

(required) The policy string related to the request

`policy_cache_duration`

(required) The duration of how long this policy should be cached. Note that the type is of type java.time.Duration, not string.

`groups`

(required) The policy string related to the request.

`group_membership_cache_duration`

(required) The duration of how long the user's group membership should be cached. Note that the type is of type java.time.Duration, not string.

`flush_all_caches`

(optional) If set to true, the SDK should clear the caches.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THIN_AUTHORIZATION_RESPONSE_T Type

Syntax
```

```

Fields

Field Description

`authorization_request`

(required) The policy string related to the request.

`decision_cache_duration`

(required) The duration of how long this decision should be cached. Note that the type is of type java.time.Duration, not string.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THIN_AUTHORIZATION_RESPONSE_TBL Type

Nested table type of dbms_cloud_oci_identity_dataplane_thin_authorization_response_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THIN_ASSOCIATION_AUTHORIZATION_RESPONSE_T Type

Syntax
```

```

Fields

Field Description

`responses`

(required) The authorization responses.

`association_result`

(required) The association verification result.

Allowed values are: 'FAIL_UNKNOWN', 'FAIL_BAD_REQUEST', 'FAIL_MISSING_ENDORSE', 'FAIL_MISSING_ADMIT', 'SUCCESS'

`decision_cache_duration`

(optional) The decision cache duration.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_USER_NOT_FOUND_AUTHENTICATE_USER_RESULT_T Type

Syntax
```

```

Fields

Field Description

`tenant_input`

(required) The tenant name.

`user_input`

(required) The user name.

`resolved_tenant_id`

(required) The resolved tenant id.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_VALID_AUTHENTICATE_USER_RESULT_T Type

Syntax
```

```

Fields

Field Description

`tenant_input`

(required) The tenant name.

`user_input`

(required) The user name.

`resolved_principal`

(required) The resolved principal.

### DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_X509_FEDERATION_REQUEST_T Type

Syntax
```

```

Fields

Field Description

`certificate`

(required) The x509 certificate of the service instance, issued by his CA.

`public_key`

(required) A temporary public key, owned by the service. The service also owns the corresponding private key. This public key will be put inside the security token by the auth service after successful validation of the certificate.

`intermediate_certificates`

(optional) An array of intermediate certificates to form the chain from the leaf certificate to the root CA. If auth service already has the intermediate certificate(s), then this is not required.

- [Identity Dataplane Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-F5CA2257-8897-4992-B01F-B3415831A12B)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-AF389E26-A197-46F3-A8A6-7561FA9AA3DB)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CLAIM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-D13E9E3B-AF60-44A1-AE0C-A28A5B7C4C05)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CLAIM_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-EE57EC04-3D22-470B-938B-A35F5F7A1373)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PRINCIPAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-B9D08270-BD84-4B30-B82B-664B3400DD58)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PERMISSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-0CAEDC39-892C-4FD3-84D9-8BFA3735172C)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CONTEXT_VARIABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-0D6D91EF-BD29-4FDE-8A38-3FCA718D32DF)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CONTEXT_VARIABLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-E22D746D-F562-4D3D-94A8-64B165FADC2B)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PERMISSION_CONTEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-D34F297D-9672-4645-BFC9-3E1BE6C4D14C)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PERMISSION_CONTEXT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-0E312C83-1447-4632-A038-F4C5EF1FED87)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHORIZATION_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-6E92BC47-FF09-4056-AE8B-4AB125BD7EF2)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ACCESSIBLE_COMPARTMENT_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-550DF987-1F61-44DC-971B-8E74A7F16685)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMPARTMENT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-445463BF-D86F-44D0-99B4-E3780B6BDAA3)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMPARTMENT_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-8F2A452A-E18B-44FF-A725-71B3D971D768)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ACCESSIBLE_COMPARTMENT_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-FD98430C-659E-4683-A5E4-1E95053713AB)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHORIZATION_REQUEST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-2B5260E9-ADE9-4E1F-A0D2-00D5CF971B9A)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ASSOCIATION_AUTHORIZATION_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-55B80E10-9FD3-4D38-9104-C8202A10370A)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTH_SERVICE_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-AE053AC3-EFF7-4C6E-9235-81EBC4AEBBCD)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATE_CLIENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-64D49744-3442-4DD1-AF47-45CC40433D15)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATE_CLIENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-64DE4F78-E109-4C21-A19F-98A0D875DAA4)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATE_USER_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-2B4071F8-7AC6-43AF-8069-FE008732A7C1)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PASSWORD_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-97A8B890-A895-4BFB-9D85-9FA99A78C15D)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-FC17F5FF-3A9C-418C-B28E-88EFE0495FD8)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_TENANT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-AAE24508-1482-410D-807E-CB66698D0C9B)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-C6A67821-024B-46FE-BE30-5648F5B20997)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATION_PRINCIPAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-99AB79FD-0804-4C2F-8C87-E14EE72A64D4)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_AUTHENTICATION_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-3D18A6BD-4BC0-496C-957E-5D690DEC7F2A)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_BAD_USER_STATE_AUTHENTICATE_USER_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-8140370D-B081-49A4-B29B-F582DDA51C52)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CLIENT_CREDENTIALS_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-64C8E967-5063-4B5E-89E5-03717CDA0FC3)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMMON_PRINCIPAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-DC04DB0E-5FB9-4C56-A9B3-172629651766)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ENTITY_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-8E0A6A94-C5A6-4F53-B832-87FB08CB4547)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COMPARTMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-9DDB9F16-7473-4156-B94B-6ACCECE55C0E)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_COST_TRACKING_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-DEB435E2-5E58-418E-8E45-93B2DC061103)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_CREDENTIAL_AUTHENTICATOR_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-951C26E3-705C-4BA9-BC70-87F592E2E216)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_DERIVED_KEY_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-DF5E93CB-27A1-4188-A18D-CF60A1427700)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-50ED4CE2-AB47-44E0-B9D6-B86BF3067434)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_FILTER_GROUP_MEMBERSHIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-6D5605ED-6099-45C7-89F5-5263FA0CACDC)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_FILTER_GROUP_MEMBERSHIP_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-E0B821D8-6095-445E-AA06-02341650841B)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_GENERATE_SCOPED_ACCESS_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-5ED59830-28D4-4C29-A395-08F9080E1453)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_GENERATE_USER_SECURITY_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-5339E4DB-EA91-446E-BF2D-F561014B9057)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_IDENTITY_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-9028D913-F7B2-43C3-846D-00C2C8BD1E89)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_JWK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-362CE29A-02AC-4938-ACFB-32B07B4A65FA)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_ON_BEHALF_OF_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-FFFA3080-3C04-49F5-ACB5-DF06A8B9EF68)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_PASSWORD_RESET_AUTHENTICATION_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-BA9CDF99-FB10-4EEC-A592-FFB99D0EDC16)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_REFRESH_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-3F1E418F-BDDB-453D-A131-8ED0F411DD73)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_RESOURCE_PRINCIPAL_SESSION_TOKEN_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-4F45D371-3D9E-4277-8434-37D396A59B41)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_SECURITY_TOKEN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-3659B9D4-D04D-411B-9E66-E65C8CE9C08E)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_TENANT_NOT_FOUND_AUTHENTICATE_USER_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-A3C09BB9-F27E-4CD7-88B2-682E5544750E)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THICK_AUTHORIZATION_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-AC62A33F-2621-4AC4-AE98-8595B0BEFEF6)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THIN_AUTHORIZATION_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-1CFBF058-C6A8-493A-92A5-48324211E23C)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THIN_AUTHORIZATION_RESPONSE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-39458E65-B078-4AEF-8317-3E7A9592B494)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_THIN_ASSOCIATION_AUTHORIZATION_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-E86BF8AA-A617-415F-9614-8CDEA242D3A6)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_USER_NOT_FOUND_AUTHENTICATE_USER_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-C918213D-CB04-4F6D-BDE0-75F1CE524882)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_VALID_AUTHENTICATE_USER_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-C98094C6-3E94-4F8A-98E8-1D8BB3F74897)
- [DBMS_CLOUD_OCI_IDENTITY_DATAPLANE_X509_FEDERATION_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_dataplane_t.html#ADSDK-GUID-90C1C46D-25BD-4666-B81E-5BA65E31DD28)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
