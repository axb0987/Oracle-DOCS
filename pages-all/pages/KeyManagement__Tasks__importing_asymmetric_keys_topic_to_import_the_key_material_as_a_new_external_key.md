# Importing Key Material for an External Asymmetric Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Importing Key Material for an External Asymmetric Key

Learn how to import key material as a new external key in the OCI Key Management service.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- In the Create Key dialog box, select a compartment from the Create in Compartment list. (Keys can exist outside the compartment the vault is in.)
- Select Protection Mode , and then select HSM . You can't import key material for keys protected by software.
- Select Name , and then enter a name to identify the key. Avoid entering confidential information.
- Select Key Shape: Algorithm , and select RSA .
- Select Key Shape: Length , and then select the key length, in bits. For RSA keys, the Vault service supports keys that are exactly 2048 bits, 3072 bits, or 4096 bits in length.
- Select the Import External Key option.
- Select Wrapping Algorithm , and then select RSA_OAEP_AES_SHA256 (RSA-OAEP with a SHA-256 with a temporary AES key).
- Under External Key Data Source , provide the file that contains the wrapped RSA key material.
-   

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- When you're finished, select Create Key .
- 

Use the[oci kms management key import](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/import.html)command and required parameters to import an external key into an OCI vault:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ImportKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ImportKey)API with the Management Endpoint to import an external key into an OCI vault.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
