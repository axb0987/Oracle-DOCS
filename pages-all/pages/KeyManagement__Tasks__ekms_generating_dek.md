# Generating a Data Encryption Key (DEK)
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_generating_dek.htm
- Fetched: 2026-09-05 02:34 CDT

# Generating a Data Encryption Key (DEK)

Learn how to generate a data encryption key using the API.

Use the[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)API with the Cryptographic Endpoint to generate a data encryption key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
