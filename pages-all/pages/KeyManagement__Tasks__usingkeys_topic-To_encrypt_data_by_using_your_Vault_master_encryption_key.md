# Encrypting Data
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_encrypt_data_by_using_your_Vault_master_encryption_key.htm
- Fetched: 2026-09-05 02:36 CDT

# Encrypting Data

Learn how to encrypt data with an encryption key using either the CLI or the API. Note that this operation can't be performed in the OCI Console.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_encrypt_data_by_using_your_Vault_master_encryption_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_encrypt_data_by_using_your_Vault_master_encryption_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_encrypt_data_by_using_your_Vault_master_encryption_key.htm#)
- 

This task isn't available in the OCI Console.
- 

Use the[oci kms crypto encrypt](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/crypto/encrypt.html)command to encrypt data. If you don't specify an encryption algorithm using the`--encryption-algorithm`parameter, an AES key is used by default.
Note  
  
You can use either AES symmetric keys or RSA asymmetric keys to encrypt or decrypt data. ECDSA keys don't support vault cryptography required to encrypt or decrypt data. To encrypt data by using an RSA asymmetric key, if the key has been rotated and has a key version identifier, you must also provide the`--key-version-id`of the key. To decrypt the data, you must provide the same`--key-version-id`. The need to track key versions exists because, unlike symmetric keys, an asymmetric key's ciphertext doesn't contain the information that the service needs for decryption purposes.

RSA keys

Note that the`--encryption-algorithm`parameter must be included in the command for RSA keys. To encrypt data with an RSA key, use the following command. If you haven't rotated the key, you don't need the`--key-version-id`flag:

```

```

Example 1: RSA key, encryption algorithm`RSA_OAEP_SHA_256`

```

```

Example 2: RSA key, encryption algorithm`RSA_OAEP_SHA_1`

```

```

AES keys

```

```

Example: AES key with`AES_256_GCM`algorithm

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[Encrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/EncryptedData/Encrypt)API with the Cryptographic Endpoint to encrypt data.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
