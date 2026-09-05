# Importing Key Material for an External Asymetric Key Version
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key_version.htm
- Fetched: 2026-09-05 02:35 CDT

# Importing Key Material for an External Asymetric Key Version

Learn how to import key material as a new external key version in the OCI Key Management service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key_version.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key_version.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key_version.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- In the key list, select Actions menu (three dots) for the key being rotated, and then select Rotate key . Note that importing external key material creates a new key version and rotates the key.
- In the Confirm dialog box, select the Import External Key Version option.
- Under External Key Data Source , provide the file that contains the wrapped key material.
- Select Rotate Key to complete the rotation.
- 

Use the[oci kms management key-version import](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key-version/import.html)command and required parameters to import key material for a new key version and rotate the target master encryption key:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ImportKeyVersion](https://docs.oracle.com/iaas/api/#/en/key/latest/KeyVersion/ImportKeyVersion)API with the Management Endpoint to import key material for a new key version and rotate the target master encryption key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
