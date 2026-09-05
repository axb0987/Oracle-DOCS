# Retrieving the Public Key for an Asymmetric Master Encryption Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_view_the_public_key_of_an_asymmetric_key.htm
- Fetched: 2026-09-05 02:36 CDT

# Retrieving the Public Key for an Asymmetric Master Encryption Key

Learn how to retrieve the public key of an RSA or ECDSA key.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_view_the_public_key_of_an_asymmetric_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_view_the_public_key_of_an_asymmetric_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_view_the_public_key_of_an_asymmetric_key.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select the name of the key
- In the list of key versions, find the key for which you want to view the public key, select the Actions menu (three dots) , and then select View Public Key .
- Do one of the following:

- 

To copy the contents of the public key, select Copy . The contents of the public key are copied to your clipboard.
- 

To download the public key, select Download . The file is automatically downloaded to your local computer.
- When you're finished, select Close .
- 

Use the[oci kms management key-version get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key-version/get.html)command to retrieve the public key of an asymmetric key.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetKeyVersion](https://docs.oracle.com/iaas/api/#/en/key/latest/KeyVersion/GetKeyVersion)API with the Management Endpoint to get the public key in PEM format for RSA and ECDSA keys.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
