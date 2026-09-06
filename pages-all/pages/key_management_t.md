# Key Management Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#dcoc-content-body)

## Key Management Common Types

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_LOCATION_T Type

Backup upload location

Syntax
```

```

Fields

Field Description

`destination`

(required) 'Backup location destination: BUCKET - Uploading or downloading backup via object store bucket PRE_AUTHENTICATED_REQUEST_URI - Uploading or downloading backup via a PreAuthenticated object store URI'

Allowed values are: 'BUCKET', 'PRE_AUTHENTICATED_REQUEST_URI'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_KEY_DETAILS_T Type

The details of the Key that you wish to backup.

Syntax
```

```

Fields

Field Description

`backup_location`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_LOCATION_BUCKET_T Type

Object storage bucket details to upload or download the backup

Syntax
```

```

`dbms_cloud_oci_key_management_backup_location_bucket_t`is a subtype of the`dbms_cloud_oci_key_management_backup_location_t`type.

Fields

Field Description

`namespace`

(required)

`bucket_name`

(required)

`object_name`

(required)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_LOCATION_URI_T Type

PreAuthenticated object storage URI to upload or download the backup

Syntax
```

```

`dbms_cloud_oci_key_management_backup_location_uri_t`is a subtype of the`dbms_cloud_oci_key_management_backup_location_t`type.

Fields

Field Description

`uri`

(required)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_VAULT_DETAILS_T Type

The details of the Vault that you wish to backup.

Syntax
```

```

Fields

Field Description

`backup_location`

(optional)

`is_include_keys`

(optional) A Boolean value that indicates whether the Keys should be included during backing up the Vault.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_CHANGE_KEY_COMPARTMENT_DETAILS_T Type

The deatils of the compartment that you wish to move the Key.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that you want to move the key to.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_CHANGE_VAULT_COMPARTMENT_DETAILS_T Type

The details of the compartment you wish to move the Vault.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the vault to.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_EKMS_PRIVATE_ENDPOINT_DETAILS_T Type

Information needed to create EKMS private endpoint resource

Syntax
```

```

Fields

Field Description

`subnet_id`

(required) The OCID of subnet in which the EKMS private endpoint is to be created

`compartment_id`

(required) Compartment identifier.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`display_name`

(required) Display name of the EKMS private endpoint resource being created.

`external_key_manager_ip`

(required) External private IP to connect to from this EKMS private endpoint

`ca_bundle`

(required) CABundle to validate TLS certificate of the external key manager system in PEM format

`port`

(optional) The port of the external key manager system

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_SHAPE_T Type

The cryptographic properties of a key.

Syntax
```

```

Fields

Field Description

`algorithm`

(required) The algorithm used by a key's key versions to encrypt or decrypt. Only AES algorithm is supported for `External` keys.

Allowed values are: 'AES', 'RSA', 'ECDSA'

`length`

(required) The length of the key in bytes, expressed as an integer. Supported values include the following: - AES: 16, 24, or 32 - RSA: 256, 384, or 512 - ECDSA: 32, 48, or 66

`curve_id`

(optional) Supported curve IDs for ECDSA keys.

Allowed values are: 'NIST_P256', 'NIST_P384', 'NIST_P521'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_REFERENCE_T Type

A reference to the key on external key manager.

Syntax
```

```

Fields

Field Description

`external_key_id`

(required) ExternalKeyId refers to the globally unique key Id associated with the key created in external vault in CTM

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_KEY_DETAILS_T Type

The details of the key that you want to create.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where you want to create the master encryption key.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`key_shape`

(required)

`protection_mode`

(optional) The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default, a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported. A protection mode of `EXTERNAL` mean that the key persists on the customer's external key manager which is hosted externally outside of oracle. Oracle only hold a reference to that key. All cryptographic operations that use a key with a protection mode of `EXTERNAL` are performed by external key manager.

Allowed values are: 'HSM', 'SOFTWARE', 'EXTERNAL'

`external_key_reference`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_OAUTH_METADATA_T Type

Authorization details required to get access token from IDP for accessing protected resources.

Syntax
```

```

Fields

Field Description

`idcs_account_name_url`

(required) Base URL of the IDCS account where confidential client app is created.

`client_app_id`

(required) ID of the client app created in IDP.

`client_app_secret`

(required) Secret of the client app created in IDP.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_MANAGER_METADATA_T Type

Metadata required for accessing External Key manager

Syntax
```

```

Fields

Field Description

`oauth_metadata`

(required)

`external_vault_endpoint_url`

(required) URI of the vault on external key manager.

`private_endpoint_id`

(required) OCID of private endpoint created by customer.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_VAULT_DETAILS_T Type

The details of the vault that you want to create.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where you want to create this vault.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`external_key_manager_metadata`

(optional)

`vault_type`

(required) The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.

Allowed values are: 'VIRTUAL_PRIVATE', 'DEFAULT', 'EXTERNAL'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_VAULT_REPLICA_DETAILS_T Type

Creates a vault replica.

Syntax
```

```

Fields

Field Description

`replica_region`

(required) The region in the realm to which the vault need to be replicated to

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_DECRYPT_DATA_DETAILS_T Type

The details of the encrypted data that you want to decrypt.

Syntax
```

```

Fields

Field Description

`associated_data`

(optional) Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associated data must be fewer than 4096 characters.

`ciphertext`

(required) The encrypted data to decrypt.

`key_id`

(required) The OCID of the key used to encrypt the ciphertext.

`logging_context`

(optional) Information that provides context for audit logging. You can provide this additional data as key-value pairs to include in audit logs when audit logging is enabled.

`key_version_id`

(optional) The OCID of the key version used to encrypt the ciphertext.

`encryption_algorithm`

(optional) The encryption algorithm to use to encrypt or decrypt data with a customer-managed key. `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP). `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash and uses OAEP.

Allowed values are: 'AES_256_GCM', 'RSA_OAEP_SHA_1', 'RSA_OAEP_SHA_256'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_DECRYPTED_DATA_T Type

The response to a request to decrypt the encrypted data.

Syntax
```

```

Fields

Field Description

`plaintext`

(required) The decrypted data, expressed as a base64-encoded value.

`plaintext_checksum`

(required) The checksum of the decrypted data.

`key_id`

(optional) The OCID of the key used to encrypt the ciphertext.

`key_version_id`

(optional) The OCID of the key version used to encrypt the ciphertext.

`encryption_algorithm`

(optional) The encryption algorithm to use to encrypt and decrypt data with a customer-managed key `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP). `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash and uses OAEP.

Allowed values are: 'AES_256_GCM', 'RSA_OAEP_SHA_1', 'RSA_OAEP_SHA_256'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_DELETE_VAULT_REPLICA_DETAILS_T Type

Deletes a vault replica

Syntax
```

```

Fields

Field Description

`replica_region`

(required) The region in the realm on which the replica should be deleted

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EKMS_PRIVATE_ENDPOINT_T Type

EKMS private endpoint created in customer subnet used to connect to external key manager system

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable

`compartment_id`

(required) Compartment Identifier.

`subnet_id`

(required) Subnet Identifier

`display_name`

(required) EKMS Private Endpoint display name

`time_created`

(required) The time the EKMS private endpoint was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time the EKMS private endpoint was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(required) The current state of the EKMS private endpoint resource.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.

`external_key_manager_ip`

(required) Private IP of the external key manager system to connect to from the EKMS private endpoint

`port`

(optional) The port of the external key manager system

`ca_bundle`

(optional) CABundle to validate TLS certificate of the external key manager system in PEM format

`private_endpoint_ip`

(optional) The IP address in the customer's VCN for the EKMS private endpoint. This is taken from subnet

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EKMS_PRIVATE_ENDPOINT_SUMMARY_T Type

EKMS private endpoints summary

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable

`subnet_id`

(required) Subnet Identifier

`compartment_id`

(required) Identifier of the compartment this EKMS private endpoint belongs to

`time_created`

(required) The time the EKMS private endpoint was created. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`time_updated`

(optional) The time the EKMS private endpoint was updated. An[RFC3339](https://tools.ietf.org/html/rfc3339)formatted datetime string.

`display_name`

(required) Mutable name of the EKMS private endpoint

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(required) The current state of the EKMS private endpoint resource.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_ENCRYPT_DATA_DETAILS_T Type

The details of the plaintext data that you want to encrypt.

Syntax
```

```

Fields

Field Description

`associated_data`

(optional) Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associated data must be fewer than 4096 characters.

`key_id`

(required) The OCID of the key to encrypt with.

`logging_context`

(optional) Information that provides context for audit logging. You can provide this additional data as key-value pairs to include in the audit logs when audit logging is enabled.

`plaintext`

(required) The plaintext data to encrypt.

`key_version_id`

(optional) The OCID of the key version used to encrypt the ciphertext.

`encryption_algorithm`

(optional) The encryption algorithm to use to encrypt and decrypt data with a customer-managed key. `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP). `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash and uses OAEP.

Allowed values are: 'AES_256_GCM', 'RSA_OAEP_SHA_1', 'RSA_OAEP_SHA_256'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_ENCRYPTED_DATA_T Type

The response to a request to encrypt the plaintext data.

Syntax
```

```

Fields

Field Description

`ciphertext`

(required) The encrypted data.

`key_id`

(optional) The OCID of the key used to encrypt the ciphertext.

`key_version_id`

(optional) The OCID of the key version used to encrypt the ciphertext.

`encryption_algorithm`

(optional) The encryption algorithm to use to encrypt and decrypt data with a customer-managed key. `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP). `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash and uses OAEP.

Allowed values are: 'AES_256_GCM', 'RSA_OAEP_SHA_1', 'RSA_OAEP_SHA_256'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_ERROR_T Type

The desciption of Error message.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXPORT_KEY_DETAILS_T Type

The details of the key that you want to wrap and export.

Syntax
```

```

Fields

Field Description

`key_id`

(required) The OCID of the master encryption key associated with the key version you want to export.

`key_version_id`

(optional) The OCID of the specific key version to export. If not specified, the service exports the current key version.

`algorithm`

(required) The encryption algorithm to use to encrypt exportable key material from a software-backed key. Specifying `RSA_OAEP_AES_SHA256` invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the RSA public wrapping key provided along with the request, creating a wrapped temporary AES key. The temporary AES key is also used to wrap the exportable key material. The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing concatenated blob output that jointly represents them. Specifying `RSA_OAEP_SHA256` means that the software key is wrapped by the RSA public wrapping key provided along with the request.

Allowed values are: 'RSA_OAEP_AES_SHA256', 'RSA_OAEP_SHA256'

`public_key`

(required) The PEM format of the 2048-bit, 3072-bit, or 4096-bit RSA wrapping key in your possession that you want to use to encrypt the key.

`logging_context`

(optional) Information that provides context for audit logging. You can provide this additional data as key-value pairs to include in the audit logs when audit logging is enabled.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXPORTED_KEY_DATA_T Type

The response to a request to export key material.

Syntax
```

```

Fields

Field Description

`key_version_id`

(required) The OCID of the key version.

`key_id`

(required) The OCID of the master encryption key associated with this key version.

`time_created`

(required) The date and time this key version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

`vault_id`

(required) The OCID of the vault that contains this key version.

`encrypted_key`

(required) The base64-encoded exported key material, which is encrypted by using the public RSA wrapping key specified in the export request.

`algorithm`

(required) The encryption algorithm to use to encrypt exportable key material from a key that persists on the server (as opposed to a key that persists on a hardware security module and, therefore, cannot be exported). Specifying RSA_OAEP_AES_SHA256 invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the RSA public wrapping key provided along with the request, creating a wrapped temporary AES key. The temporary AES key is also used to wrap the exportable key material. The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing concatenated blob output that jointly represents them. Specifying RSA_OAEP_SHA256 means that the exportable key material is wrapped by the RSA public wrapping key provided along with the request.

Allowed values are: 'RSA_OAEP_AES_SHA256', 'RSA_OAEP_SHA256'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_OAUTH_METADATA_SUMMARY_T Type

Summary about authorization to be returned to the customer as a response.

Syntax
```

```

Fields

Field Description

`idcs_account_name_url`

(required) Base URL of the IDCS account where confidential client app is created.

`client_app_id`

(required) ID of the client app created in IDP.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_MANAGER_METADATA_SUMMARY_T Type

Summary about metadata of external key manager to be returned to the customer as a response.

Syntax
```

```

Fields

Field Description

`vendor`

(optional) Vendor of the external key manager.

`external_vault_endpoint_url`

(required) URL of the vault on external key manager.

`private_endpoint_id`

(required) OCID of the private endpoint.

`oauth_metadata_summary`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_REFERENCE_DETAILS_T Type

Key reference data to be returned to the customer as a response.

Syntax
```

```

Fields

Field Description

`external_key_id`

(required) ExternalKeyId refers to the globally unique key Id associated with the key created in external vault in CTM.

`external_key_version_id`

(required) Key version ID associated with the external key.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_VERSION_REFERENCE_T Type

A reference to key version on external key manager.

Syntax
```

```

Fields

Field Description

`external_key_version_id`

(optional) Key version ID associated with the external key.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_GENERATE_KEY_DETAILS_T Type

The details of the key that you want to encrypt or decrypt data.

Syntax
```

```

Fields

Field Description

`associated_data`

(optional) Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associated data must be fewer than 4096 characters.

`include_plaintext_key`

(required) If true, the generated key is also returned unencrypted.

`key_id`

(required) The OCID of the master encryption key to encrypt the generated data encryption key with.

`key_shape`

(required)

`logging_context`

(optional) Information that provides context for audit logging. You can provide this additional data by formatting it as key-value pairs to include in audit logs when audit logging is enabled.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_GENERATED_KEY_T Type

The reponse to the regeuest to generate the key to encrypt or decrypt the data.

Syntax
```

```

Fields

Field Description

`ciphertext`

(required) The encrypted data encryption key generated from a master encryption key.

`plaintext`

(optional) The plaintext data encryption key, a base64-encoded sequence of random bytes, which is included if the[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)request includes the `includePlaintextKey` parameter and sets its value to \"true\".

`plaintext_checksum`

(optional) The checksum of the plaintext data encryption key, which is included if the[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)request includes the `includePlaintextKey` parameter and sets its value to \"true\".

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_WRAPPED_IMPORT_KEY_T Type

The details of the wrapped import Key.

Syntax
```

```

Fields

Field Description

`key_material`

(required) The key material to import, wrapped by the vault's RSA public wrapping key and base64-encoded.

`wrapping_algorithm`

(required) The wrapping mechanism to use during key import. `RSA_OAEP_AES_SHA256` invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the vault's RSA public wrapping key, creating a wrapped temporary AES key. The temporary AES key is also used to wrap the private key material. The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing concatenated blob output that jointly represents them. `RSA_OAEP_SHA256` means that the exportable key material is wrapped by the vault's RSA public wrapping key.

Allowed values are: 'RSA_OAEP_SHA256', 'RSA_OAEP_AES_SHA256'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_IMPORT_KEY_DETAILS_T Type

The details of the Key that you wish to import.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains this key.

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`

`display_name`

(required) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`key_shape`

(required)

`wrapped_import_key`

(required)

`protection_mode`

(optional) The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default, a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.

Allowed values are: 'HSM', 'SOFTWARE'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_IMPORT_KEY_VERSION_DETAILS_T Type

The details of the KeyVersion that you wish to import.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`wrapped_import_key`

(required)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_REPLICA_DETAILS_T Type

Key replica details

Syntax
```

```

Fields

Field Description

`replication_id`

(optional) ReplicationId associated with a key operation

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_T Type

The logical entities that represent one or more key versions, each of which contains cryptographic material.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains this master encryption key.

`current_key_version`

(required) The OCID of the key version used in cryptographic operations. During key rotation, the service might be in a transitional state where this or a newer key version are used intermittently. The `currentKeyVersion` property is updated when the service is guaranteed to use the new key version for all subsequent encryption operations.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the key.

`key_shape`

(required)

`protection_mode`

(optional) The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default, a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported. A protection mode of `EXTERNAL` mean that the key persists on the customer's external key manager which is hosted externally outside of oracle. Oracle only hold a reference to that key. All cryptographic operations that use a key with a protection mode of `EXTERNAL` are performed by external key manager.

Allowed values are: 'HSM', 'SOFTWARE', 'EXTERNAL'

`lifecycle_state`

(required) The key's current lifecycle state. Example: `ENABLED`

Allowed values are: 'CREATING', 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION', 'UPDATING', 'BACKUP_IN_PROGRESS', 'RESTORING'

`time_created`

(required) The date and time the key was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property indicating when to delete the key, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the vault that contains this key.

`restored_from_key_id`

(optional) The OCID of the key from which this key was restored.

`replica_details`

(optional)

`is_primary`

(optional) A Boolean value that indicates whether the Key belongs to primary Vault or replica vault.

`external_key_reference_details`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_SUMMARY_T Type

The details of the Key.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the key.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the key.

`lifecycle_state`

(required) The key's current lifecycle state. Example: `ENABLED`

Allowed values are: 'CREATING', 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION', 'UPDATING', 'BACKUP_IN_PROGRESS', 'RESTORING'

`time_created`

(required) The date and time the key was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the vault that contains the key.

`protection_mode`

(optional) The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default, a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported. A protection mode of `EXTERNAL` mean that the key persists on the customer's external key manager which is hosted externally outside of oracle. Oracle only hold a reference to that key. All cryptographic operations that use a key with a protection mode of `EXTERNAL` are performed by external key manager.

Allowed values are: 'HSM', 'SOFTWARE', 'EXTERNAL'

`algorithm`

(optional) The algorithm used by a key's key versions to encrypt or decrypt data.

Allowed values are: 'AES', 'RSA', 'ECDSA'

`external_key_reference_details`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_VERSION_REPLICA_DETAILS_T Type

KeyVersion replica details

Syntax
```

```

Fields

Field Description

`replication_id`

(optional) ReplicationId associated with a key version operation

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_VERSION_T Type

The details of the KeyVersion associated with the Key.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains this key version.

`id`

(required) The OCID of the key version.

`key_id`

(required) The OCID of the key associated with this key version.

`public_key`

(optional) The public key in PEM format. (This value pertains only to RSA and ECDSA keys.)

`lifecycle_state`

(optional) The key version's current lifecycle state. Example: `ENABLED`

Allowed values are: 'CREATING', 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION'

`origin`

(optional) The source of the key material. When this value is `INTERNAL`, Key Management created the key material. When this value is `EXTERNAL`, the key material was imported from an external source.

Allowed values are: 'INTERNAL', 'EXTERNAL'

`time_created`

(required) The date and time this key version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: \"2018-04-03T21:10:29.600Z\"

`time_of_deletion`

(optional) An optional property indicating when to delete the key version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the vault that contains this key version.

`restored_from_key_version_id`

(optional) The OCID of the key version from which this key version was restored.

`replica_details`

(optional)

`is_primary`

(optional) A Boolean value that indicates whether the KeyVersion belongs to primary Vault or replica Vault.

`external_key_reference_details`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_VERSION_SUMMARY_T Type

The details of the KeyVersion.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains this key version.

`id`

(required) The OCID of the key version.

`key_id`

(required) The OCID of the master encryption key associated with this key version.

`lifecycle_state`

(optional) The key version's current lifecycle state. Example: `ENABLED`

Allowed values are: 'CREATING', 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION'

`origin`

(required) The source of the key material. When this value is INTERNAL, Key Management created the key material. When this value is EXTERNAL, the key material was imported from an external source.

Allowed values are: 'INTERNAL', 'EXTERNAL'

`time_created`

(required) The date and time this key version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property to indicate when to delete the key version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the vault that contains this key version.

`external_key_reference_details`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_REPLICA_DETAILS_T Type

Details of replication status

Syntax
```

```

Fields

Field Description

`l_region`

(optional) The replica region

`status`

(optional) Replication status associated with a replicationId

Allowed values are: 'REPLICATING', 'REPLICATED'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_REPLICA_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_key_management_replica_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_REPLICATION_STATUS_DETAILS_T Type

Details of replication status across all replica regions

Syntax
```

```

Fields

Field Description

`replica_details`

(optional) Replica Details.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_RESTORE_KEY_FROM_OBJECT_STORE_DETAILS_T Type

The details of the backup location from which you want to restore the Key.

Syntax
```

```

Fields

Field Description

`backup_location`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_RESTORE_VAULT_FROM_OBJECT_STORE_DETAILS_T Type

The details of the backup location from which you want to restore the Vault.

Syntax
```

```

Fields

Field Description

`backup_location`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_SCHEDULE_KEY_DELETION_DETAILS_T Type

Details for scheduling key deletion.

Syntax
```

```

Fields

Field Description

`time_of_deletion`

(optional) An optional property to indicate when to delete the vault, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. The specified time must be between 7 and 30 days from when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_SCHEDULE_KEY_VERSION_DELETION_DETAILS_T Type

Details for scheduling key version deletion.

Syntax
```

```

Fields

Field Description

`time_of_deletion`

(optional) An optional property to indicate when to delete the key version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. The specified time must be between 7 and 30 days from the time when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_SCHEDULE_VAULT_DELETION_DETAILS_T Type

Details for scheduling vault deletion.

Syntax
```

```

Fields

Field Description

`time_of_deletion`

(optional) An optional property indicating when to delete the vault, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. The specified time must be between 7 and 30 days from the time when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_SIGN_DATA_DETAILS_T Type

The details of the message that you want to sign.

Syntax
```

```

Fields

Field Description

`message`

(required) The base64-encoded binary data object denoting the message or message digest to sign. You can have a message up to 4096 bytes in size. To sign a larger message, provide the message digest.

`key_id`

(required) The OCID of the key used to sign the message.

`key_version_id`

(optional) The OCID of the key version used to sign the message.

`message_type`

(optional) Denotes whether the value of the message parameter is a raw message or a message digest. The default value, `RAW`, indicates a message. To indicate a message digest, use `DIGEST`.

Allowed values are: 'RAW', 'DIGEST'

`signing_algorithm`

(required) The algorithm to use to sign the message or message digest. For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with different hashing algorithms. For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms. When you pass a message digest for signing, ensure that you specify the same hashing algorithm as used when creating the message digest.

Allowed values are: 'SHA_224_RSA_PKCS_PSS', 'SHA_256_RSA_PKCS_PSS', 'SHA_384_RSA_PKCS_PSS', 'SHA_512_RSA_PKCS_PSS', 'SHA_224_RSA_PKCS1_V1_5', 'SHA_256_RSA_PKCS1_V1_5', 'SHA_384_RSA_PKCS1_V1_5', 'SHA_512_RSA_PKCS1_V1_5', 'ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_SIGNED_DATA_T Type

The response to a request to sign the message.

Syntax
```

```

Fields

Field Description

`key_id`

(required) The OCID of the key used to sign the message.

`key_version_id`

(required) The OCID of the key version used to sign the message.

`signature`

(required) The base64-encoded binary data object denoting the cryptographic signature generated for the message or message digest.

`signing_algorithm`

(required) The algorithm to use to sign the message or message digest. For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with different hashing algorithms. For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms. When you pass a message digest for signing, ensure that you specify the same hashing algorithm as used when creating the message digest.

Allowed values are: 'SHA_224_RSA_PKCS_PSS', 'SHA_256_RSA_PKCS_PSS', 'SHA_384_RSA_PKCS_PSS', 'SHA_512_RSA_PKCS_PSS', 'SHA_224_RSA_PKCS1_V1_5', 'SHA_256_RSA_PKCS1_V1_5', 'SHA_384_RSA_PKCS1_V1_5', 'SHA_512_RSA_PKCS1_V1_5', 'ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_UPDATE_EKMS_PRIVATE_ENDPOINT_DETAILS_T Type

Information needed to modify EKMS private endpoint resource

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of EKMS private endpoint resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_UPDATE_KEY_DETAILS_T Type

The details of the Key that you wish to update.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_UPDATE_VAULT_DETAILS_T Type

The details of the Vault that you wish to update.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_REPLICA_DETAILS_T Type

Vault replica details

Syntax
```

```

Fields

Field Description

`replication_id`

(optional) ReplicationId associated with a vault operation

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_T Type

The logical entity where the Vault service creates and durably stores keys.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains this vault.

`crypto_endpoint`

(required) The service endpoint to perform cryptographic operations against. Cryptographic operations include[Encrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/EncryptedData/Encrypt),[Decrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/DecryptedData/Decrypt), and[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)operations.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the vault.

`lifecycle_state`

(required) The vault's current lifecycle state. Example: `DELETED`

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION', 'UPDATING', 'BACKUP_IN_PROGRESS', 'RESTORING'

`management_endpoint`

(required) The service endpoint to perform management operations against. Management operations include \"Create,\" \"Update,\" \"List,\" \"Get,\" and \"Delete\" operations.

`time_created`

(required) The date and time this vault was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property to indicate when to delete the vault, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`vault_type`

(required) The type of vault. Each type of vault stores the key with different degrees of isolation and has different options and pricing.

Allowed values are: 'VIRTUAL_PRIVATE', 'DEFAULT', 'EXTERNAL'

`restored_from_vault_id`

(optional) The OCID of the vault from which this vault was restored, if it was restored from a backup file. If you restore a vault to the same region, the vault retains the same OCID that it had when you backed up the vault.

`wrappingkey_id`

(required) The OCID of the vault's wrapping key.

`replica_details`

(optional)

`is_primary`

(optional) A Boolean value that indicates whether the Vault is primary Vault or replica Vault.

`external_key_manager_metadata_summary`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_REPLICA_SUMMARY_T Type

Summary of vault replicas

Syntax
```

```

Fields

Field Description

`crypto_endpoint`

(optional) The vault replica's crypto endpoint

`management_endpoint`

(optional) The vault replica's management endpoint

`l_region`

(optional) Region to which vault is replicated to

`status`

(optional) Status of the Vault

Allowed values are: 'CREATING', 'CREATED', 'DELETING', 'DELETED'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_SUMMARY_T Type

The details of the Vault.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains a particular vault.

`crypto_endpoint`

(required) The service endpoint to perform cryptographic operations against. Cryptographic operations include[Encrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/EncryptedData/Encrypt),[Decrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/DecryptedData/Decrypt), and[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)operations.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name for a vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a vault.

`lifecycle_state`

(required) A vault's current lifecycle state. Example: `ACTIVE`

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION', 'UPDATING', 'BACKUP_IN_PROGRESS', 'RESTORING'

`management_endpoint`

(required) The service endpoint to perform management operations against. Management operations include \"Create,\" \"Update,\" \"List,\" \"Get,\" and \"Delete\" operations.

`time_created`

(required) The date and time a vault was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`vault_type`

(required) The type of vault. Each type of vault stores keys with different degrees of isolation and has different options and pricing.

Allowed values are: 'VIRTUAL_PRIVATE', 'EXTERNAL', 'DEFAULT'

`external_key_manager_metadata_summary`

(optional)

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_USAGE_T Type

The details of the number of Keys and KeyVersions usage in a Vault.

Syntax
```

```

Fields

Field Description

`key_count`

(required) The number of keys in this vault that persist on a hardware security module (HSM), across all compartments, excluding keys in a `DELETED` state.

`key_version_count`

(required) The number of key versions in this vault that persist on a hardware security module (HSM), across all compartments, excluding key versions in a `DELETED` state.

`software_key_count`

(optional) The number of keys in this vault that persist on the server, across all compartments, excluding keys in a `DELETED` state.

`software_key_version_count`

(optional) The number of key versions in this vault that persist on the server, across all compartments, excluding key versions in a `DELETED` state.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VERIFIED_DATA_T Type

The response to a request to verify the message.

Syntax
```

```

Fields

Field Description

`is_signature_valid`

(required) A Boolean value that indicates whether the signature was verified.

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_VERIFY_DATA_DETAILS_T Type

The details of the message that you want to verify.

Syntax
```

```

Fields

Field Description

`key_id`

(required) The OCID of the key used to sign the message.

`key_version_id`

(required) The OCID of the key version used to sign the message.

`signature`

(required) The base64-encoded binary data object denoting the cryptographic signature generated for the message.

`message_type`

(optional) Denotes whether the value of the message parameter is a raw message or a message digest. The default value, `RAW`, indicates a message. To indicate a message digest, use `DIGEST`.

Allowed values are: 'RAW', 'DIGEST'

`message`

(required) The base64-encoded binary data object denoting the message or message digest to sign. You can have a message up to 4096 bytes in size. To sign a larger message, provide the message digest.

`signing_algorithm`

(required) The algorithm to use to sign the message or message digest. For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with different hashing algorithms. For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms. When you pass a message digest for signing, ensure that you specify the same hashing algorithm as used when creating the message digest.

Allowed values are: 'SHA_224_RSA_PKCS_PSS', 'SHA_256_RSA_PKCS_PSS', 'SHA_384_RSA_PKCS_PSS', 'SHA_512_RSA_PKCS_PSS', 'SHA_224_RSA_PKCS1_V1_5', 'SHA_256_RSA_PKCS1_V1_5', 'SHA_384_RSA_PKCS1_V1_5', 'SHA_512_RSA_PKCS1_V1_5', 'ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512'

### DBMS_CLOUD_OCI_KEY_MANAGEMENT_WRAPPING_KEY_T Type

The public RSA wrapping key associated with the vault

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains this key.

`id`

(required) The OCID of the key.

`lifecycle_state`

(required) The key's current lifecycle state. Example: `ENABLED`

Allowed values are: 'CREATING', 'ENABLING', 'ENABLED', 'DISABLING', 'DISABLED', 'DELETING', 'DELETED', 'PENDING_DELETION', 'SCHEDULING_DELETION', 'CANCELLING_DELETION', 'UPDATING', 'BACKUP_IN_PROGRESS', 'RESTORING'

`public_key`

(required) The public key, in PEM format, to use to wrap the key material before importing it.

`time_created`

(required) The date and time the key was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the vault that contains this key.

- [Key Management Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-7E751719-1928-4C6A-9E89-6878D48271B7)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-372B8F0F-2F34-4E66-9B01-4A0EC54D0549)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-3174B6B9-2104-4542-909E-D5625FA9A538)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-9BB20887-364B-493C-9E00-7156A23467C8)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_LOCATION_BUCKET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-6C8FF722-1AA8-45E9-87E8-C3B85D75AE7E)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_LOCATION_URI_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-32A238E0-0427-421A-9D97-06FDE6683043)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_BACKUP_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-E043ED29-E414-4020-A3B9-5DBC4423F96C)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_CHANGE_KEY_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-A55579CA-4A8D-4BFC-9A62-0A44FE000E3F)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_CHANGE_VAULT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-C77EBA33-B624-4A2B-A951-2BDFD470F2F0)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_EKMS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-4E30D7B6-33FA-4723-89E7-2A8433870E13)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-FDD4133C-6441-4E73-A1C9-CA2B9DD49519)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-87C69042-F20B-411B-B0DC-9ECF1AC3200B)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-5B6D590B-4CE5-4EC8-933B-D6A6B2C798B5)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_OAUTH_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-A8F47D31-41CB-4164-B466-00C9664518CE)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_MANAGER_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-19F0C0D8-8539-42C1-9547-1D0C5EA78CE9)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-F840D384-A9FD-433A-A066-05E4BC3743C8)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_CREATE_VAULT_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-4B0C6778-D46C-44AD-8542-135002C4C981)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_DECRYPT_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-0774947E-5FA3-4EF2-9DA4-68013C390512)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_DECRYPTED_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-5EA48319-EC7E-41F8-BC66-F016DB5159B7)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_DELETE_VAULT_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-72E80385-DBB2-4D3A-824E-511692CAD7E6)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EKMS_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-974281AD-4839-450D-8294-36A44C7FDA72)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EKMS_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-B432D6D3-C736-49AB-A6F3-19C625EF7701)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_ENCRYPT_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-856E6CE6-FC9C-4966-B2E8-0A65D16EC97E)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_ENCRYPTED_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-42520FDE-E4AE-4638-94BA-A0078A4226AC)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-3E741252-E56E-4A46-8E25-3E426212A32D)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXPORT_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-2FD4C021-B79C-4F18-9D40-2E9BEA98EDB5)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXPORTED_KEY_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-877DE362-74C5-46E4-BFFF-1700517121EC)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_OAUTH_METADATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-22451BEF-AB8E-4ABA-A81C-7895134736E0)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_MANAGER_METADATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-D887DD6C-BE93-4A1B-AEA2-5C0E7A2C9E31)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_REFERENCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-0EEFD67C-58F5-4696-BC84-49A669489578)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_EXTERNAL_KEY_VERSION_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-4E4FAC8F-CFEF-4FE8-B5E4-325C04DC8FB3)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_GENERATE_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-B59D513E-E3C3-4A01-BB9D-0D8E079AFB38)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_GENERATED_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-0EE11B0A-ECDC-4D02-9E46-C765587026F9)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_WRAPPED_IMPORT_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-41B3D29E-5F23-49DF-82B7-355F69E1C45E)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_IMPORT_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-83C8A389-A386-4548-858D-FF36AF5C8AEA)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_IMPORT_KEY_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-1087D587-06F8-4076-BA9D-2D52CD2E434E)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-9F2C7D68-A7F9-4C3D-AE31-B3265D8A0100)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-21B60C8B-657C-4C78-9A40-986EF1F0C29B)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-89AC71D3-D5CC-4905-94CF-3FC31F7BF9B7)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_VERSION_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-619694D0-C288-4F2E-ACFF-F05344BDBEEB)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-CD063FDA-CC31-48F1-8137-7EAC0CCDF10D)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_KEY_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-36B50B1D-4BFA-414E-AB8A-15CAE966BFEF)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-F187849A-99DC-446B-AA11-1F1DF013C6DB)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_REPLICA_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-3D1E5D03-B75D-4D02-841D-DF2C76E78D10)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_REPLICATION_STATUS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-777A7E84-7E8D-4F0B-9830-E441E4BAD626)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_RESTORE_KEY_FROM_OBJECT_STORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-6C9E0A19-3FDF-4FB5-BAE8-E32E2F4AAB10)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_RESTORE_VAULT_FROM_OBJECT_STORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-B9565A49-48A7-40B2-93B1-1A16290DC7BB)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_SCHEDULE_KEY_DELETION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-B15874D7-F618-4063-86B2-DF414D4813B5)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_SCHEDULE_KEY_VERSION_DELETION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-D30CEC66-0D4B-41FD-BBB0-C7BFDE919CBF)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_SCHEDULE_VAULT_DELETION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-2CD4FEF7-097F-41D3-961D-591DE1F6B6B3)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_SIGN_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-DF6D4466-527A-4E85-938D-ACD3ACFB2407)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_SIGNED_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-F82B57EB-3C30-4D22-ACEA-AE1734A8ADFC)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_UPDATE_EKMS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-2F32C61C-0356-4731-9A6F-25AF05CF7FF3)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_UPDATE_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-84A462A2-B282-4C5B-BAA5-9FD748A412C3)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_UPDATE_VAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-4C4A6204-553D-4965-994E-8F62063A6D9A)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_REPLICA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-892AEFE7-57BD-4B6D-B4E0-FA80F634EFEB)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-23E184EE-E62A-4F70-A41E-7D01205DC488)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_REPLICA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-B368B951-2303-488B-A8BA-55228FDA6AD3)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-FA1FBCC0-0D6F-4283-8722-9205AE4499DF)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VAULT_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-1AD3212B-F1E5-4196-9740-BE0AF65463C8)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VERIFIED_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-499732F4-86BA-43BE-B28F-FCB5D15D0582)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_VERIFY_DATA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-61FD4927-E973-42DE-A582-F9CE06254360)
- [DBMS_CLOUD_OCI_KEY_MANAGEMENT_WRAPPING_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/key_management_t.html#ADSDK-GUID-6D45A244-3716-4582-8A62-972DAA445D92)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
