# Viewing Key Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm
- Fetched: 2026-09-05 02:35 CDT

# Viewing Key Details

Learn how to get the details information for a master encryption key.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select the key's name. The OCI Console displays the following information in the Key Information tab:

- OCID: The unique, Oracle-assigned ID of the key.
- Created: The date and time when you initially created the key.
- Compartment: The unique, Oracle-assigned ID of the compartment that contains the key.
- Protection Mode: Where the key is stored and processed, whether on a hardware security module (HSM) or on a server (software).
- Vault: The unique, Oracle-assigned ID of the vault that contains the key.
- Key Version: The unique, Oracle-assigned ID of the key version.
- Algorithm: The encryption algorithm used by the key.
- Length: The number of bits in the key length (for AES keys and RSA keys).
- Curve ID: The curve ID of the key (ECDSA keys only) .
- Auto rotation: (Virtual private vault keys only) Indicates whether auto rotation is enabled or disabled for the key.
- Last successful auto rotation: (Virtual private vault keys only) The date and time of the last successful auto rotation for the key.
- Next auto rotation: (Virtual private vault keys only) The date and time when the key is eligible for the next scheduled rotation.

Select the Versions tab to see information on the key's key versions.
- 

Use the[oci kms management key get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/get.html)command and required parameters to get the details of a master encryption key:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/GetKey)API with the Management Endpoint to get the details of a master encryption key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
