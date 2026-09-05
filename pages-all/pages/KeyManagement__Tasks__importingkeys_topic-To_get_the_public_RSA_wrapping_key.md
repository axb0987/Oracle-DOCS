# Getting the Public RSA Wrapping Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys_topic-To_get_the_public_RSA_wrapping_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Getting the Public RSA Wrapping Key

Learn how to get a public RSA wrapping key.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys_topic-To_get_the_public_RSA_wrapping_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys_topic-To_get_the_public_RSA_wrapping_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys_topic-To_get_the_public_RSA_wrapping_key.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select Create Key under Master Encryption Keys .
- Enable Import external key to see the wrapping key information.
- Select the PUBLIC KEY----- copy icon (two overlapping squares) to view and copy the public RSA wrapping key.
- Save the copied wrapping key, and then continue[Applying RSA-OAEP to Wrap the Key Material for a Symmetric Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys_topic-To_apply_RSAOAEP_to_wrap_the_key_material.htm).
- 

Use the[oci kms management wrapping-key get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/wrapping-key/get.html)command to get details about the public RSA wrapping key associated with the vault in the endpoint.:

```

```

After you get the public wrapping key, wrap the AES key material by[applying RSA-OAEP](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importingkeys_topic-To_apply_RSAOAEP_to_wrap_the_key_material.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetWrappingKey](https://docs.oracle.com/iaas/api/#/en/key/latest/WrappingKey/GetWrappingKey)API with the Management Endpoint to get the public RSA wrapping key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
