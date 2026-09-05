# External KMS Vendor API Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Reference/ekms-vendor-api.htm
- Fetched: 2026-09-05 02:31 CDT

# External KMS Vendor API Reference

Find information about the vendor API for OCI External Key Management.
Important  
  

This API reference information is for hardware security module (HSM) vendors, and is not for regular users of the OCI External Key Management service. See[Developing with Key and Secret Management](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Reference/developing-with-vault.htm)for information on the customer APIs for OCI Key Management.

## The OCI External Key Management Resource Model

This section details the OCI and third-party resources in the External Key Management resource model. For more details on External Key Management in OCI, see[Key and Secret Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Reference/../Concepts/keyoverview.htm#concepts)and[External Key Management Service](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Reference/../Tasks/external_key_management.htm).

OCI's Key Management Service (KMS) uses the following resources when users store and manage keys in an external hardware security module (HSM).

### Vaults

OCI vaults are logical entities in the customer's OCI environment where the Key Management Service creates and durably stores vault keys or key references. Customers using External Key Management create vaults of the type "external" to store references to keys located in an external HSM. The vault is the top-level resource for the customer when managing keys. Inside the vault are OCI Key References and Key Reference Versions.

### Third-party Keys

Customers using OCI External Key Management create and store keys in an third-party HSM interface. OCI External Key Management considers these to be "third-party keys," because they're not generated or stored by Oracle, and therefore aren't resources within the OCI customer environment. But they're a part of the resource model because OCI External Key Management maps references to these keys to handle cryptographic operation requests.

Each third-party key has a key ID (GUID) created by the external system. Customers use the key ID and key details (key type and shape) to create a key reference in OCI External Key Management. Third-party keys contain one or more key versions.

### Key References for Third-party Keys

In OCI Key Management, customers create references to third-party keys using the key ID and key details (key type and shape). OCI Key Management stores the key mapping details and key metadata, and not the actual key material. Customers interact with these key references in their OCI environment.

Creation of a key reference in OCI doesn't create a key in the third-party HSM. Similarly, the deletion of a key reference in OCI doesn't delete the third-party key in the HSM. OCI KMS uses the key reference for handling cryptographic operation requests, and cryptographic operations happen in the external HSM. Key references store information about current and retired key reference versions.

### Key Reference Versions for Third-party Keys

Each third-party key is automatically assigned a key version in the HSM. When a customer rotates an third-party key, the HSM generates a new key version. Customers take the version ID of the rotated key and use it to rotate the key reference in OCI Key Management so that OCI Key Management can send cryptographic operation requests to the correct third-party key version.

## Vendor API Operations

HSM vendors implement the OCI External Key Management (External KMS) vendor API to support External KMS features. The API offers the following operations:

Operation API name Description
Get vault metadata`GetVaultMetadata`Gets the metadata of a vault.
Encrypt data`Encrypt`Encrypts data using a specified external key version, or if no version is specified, the latest version of a specified key.
Decrypt data`Decrypt`Encrypts data using a specified external key version, or if no version is specified, the latest version of a specified key.
Get key metadata`GetKeyMetadata`Gets the metadata associated with the latest version of a specified key.
Get key version metadata`GetKeyVersionMetadata`Gets the metadata associated with a specified key version.
Generate random byes`GenerateRandomBytes`Generates random bytes.

## Vendor API Reference

Expand the Vendor API reference in this section for complete API details.

[Vendor API Reference](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Reference/ekms-vendor-api.htm#)

```

```

## Error Code Reference

Input Error Vendor API Expected response from external HSM vendor
customer provides wrong hold your own key (hyok) vault ID`vaults/{vaultId}/metadata``{"code":"404","message":"Error in getting OCI vault"}`
hyok vault is disabled in external key manager`vaults/{vaultId}/metadata``{"code":"403","message":"xxxxxxxx"}`
customer provides wrong hyok key`keys/{keyId}/metadata``{"code":"404","message":"Invalid key details provided"}`
hyok key is disabled`keys/{keyId}/metadata``{"code":"403","message":"xxxxxxxx"}`
customer provides wrong hyok key version`/keyVersions/{keyVersionId}/metadata``{"code":"404","message":"Invalid Key details"}`
customer tries to encrypt or decrypt when hyok key is disabled in external key manager

`keys/{keyId}/encrypt`

`keys/{keyId}/decrypt``{"code":"403","message":"OCI key is not in Active state to perform the operation."}`
customer tries to encrypt or decrypt when hyok key is deleted in external key manager

`keys/{keyId}/encrypt`

`keys/{keyId}/decrypt``{"code":"404","message":"Invalid key details provided"}`
customer tries to provide tampered or invalid cipher text during decrypt call`keys/{keyId}/decrypt``{"code":"400","message":"Bad Request: illegal base64 data at input byte 4"}`
customer provides cipher text that was encrypted using a different hyok key`keys/{keyId}/decrypt``{"code":"400","message":"Error in decryption: [NCERRCryptoOperationFailed: Cryptographic operation failed in cipher operation]: AEAD decrypt final failed"}`
customer tires to provide invalid initialization vector (IV) or tag during decrypt call`keys/{keyId}/decrypt``{"code":"400","message":"Error in decryption: [NCERRCryptoOperationFailed: Cryptographic operation failed in cipher operation]: AEAD decrypt final failed"}`
customer tries to provide invalid additional authenticated data (AAD) in the payload`/keys/{keyId}/generateRandomBytes``{"code":"400","message":"Bad Request: illegal base64 data at input byte 8"}`
customer tries to generate random bytes when hyok key is disabled in external key manager`/keys/{keyId}/generateRandomBytes``{"code":"403","message":"Key is in disabled state."}`
