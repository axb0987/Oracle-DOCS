# Rotating a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Rotating a Key

Learn how to rotate a key by creating a new key version.

When you create a new key version of a master encryption key, the KMS service rotates the key version in use for the key. The service can generate the key material for the new key version, or you can import your own key material. When importing a key you must use a wrapping key to wrap the key material. However, you can't create, delete or rotate a wrapping key. For more information about key rotation, see[Key Versions &amp; Rotations](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts__key-versions-and-rotations-section)in the the[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts)topic.

## Automatic Key Rotation

For keys created in virtual private vaults, you can enable automatic key rotation. See the[Automatic Key Rotation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts__automatic-key-rotation-overview-section)section of the[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts)topic for details. This option can be enabled during key creation, or enabled after a key is created. See[Enabling and Updating Auto Key Rotation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm)for instructions on updating auto-rotation settings, and[Creating a Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm)for instructions on creating a new key with automatic rotation enabled.

## Manual Key Rotation

Use the instructions in the following sections to manually rotate a key using the Console, CLI, or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- In the key list, select Actions menu (three dots) and then select Rotate key .
- In the Confirm dialog box, enable Import External key version to import the key materials and key versions and allow Key Management Service to use a copy of it.
- Select Rotate Key.

Note  
  
Cryptographic operations involving objects that were encrypted with the previous version of this key continue to use the older key version. You can re-encrypt those objects with the current key version if you prefer
- 

use the[oci kms management key-version create](https://docs.oracle.com/iaas/tools/oci-cli/3.50.3/oci_cli_docs/cmdref/kms/management/key-version/create.html)command and required parameters to rotate a key.

```

```

Cryptographic operations involving objects that were encrypted with the previous version of this key will continue to use the older key version. You can re-encrypt those objects with the current key version if you prefer.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateKeyVersion](https://docs.oracle.com/iaas/api/#/en/key/latest/KeyVersion/CreateKeyVersion)API with the Management Endpoint to rotate a master encryption key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
