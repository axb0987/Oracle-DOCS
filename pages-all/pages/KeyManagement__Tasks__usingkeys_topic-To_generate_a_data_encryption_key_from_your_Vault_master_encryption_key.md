# Generating a Data Encryption Key from a Master Encryption Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_generate_a_data_encryption_key_from_your_Vault_master_encryption_key.htm
- Fetched: 2026-09-05 02:36 CDT

# Generating a Data Encryption Key from a Master Encryption Key

Learn how to generate a data encryption key from a master encryption key using the CLI or API.
Important  
  

- Ensure that when you create a data encryption key, the data encryption key has equal or greater encryption strength to that of the master encryption key used to create it.
- You can only use AES symmetric keys to generate data encryption keys. You can't generate data encryption keys using any other algorithm.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_generate_a_data_encryption_key_from_your_Vault_master_encryption_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_generate_a_data_encryption_key_from_your_Vault_master_encryption_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_generate_a_data_encryption_key_from_your_Vault_master_encryption_key.htm#)
- 

This task isn't available in the OCI Console.
- 

Open a command prompt and run`oci kms crypto generate-data-encryption-key`to generate a data encryption key that you can then use to encrypt and decrypt data:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Use the[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)API with the Cryptographic Endpoint to generate a data encryption key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
