# Verifying Signed Data Using an Encryption Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_verify_signed_data_by_using_your_Vault_master_encryption_key.htm
- Fetched: 2026-09-05 02:36 CDT

# Verifying Signed Data Using an Encryption Key

Learn how to verify signed data with an encryption key using the CLI or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_verify_signed_data_by_using_your_Vault_master_encryption_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_verify_signed_data_by_using_your_Vault_master_encryption_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/usingkeys_topic-To_verify_signed_data_by_using_your_Vault_master_encryption_key.htm#)
- 

This task isn't available in the OCI Console.
- 

Note  
  
You can only use RSA or ECDSA asymmetric keys to digitally sign data and verify signed data. AES keys do not support the asymmetric vault cryptography required to sign data or to verify signed data.

Use the[oci kms crypto verified-data verify](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/crypto/verified-data/verify.html)command and required parameters to verify the integrity of signed data:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[Verify](https://docs.oracle.com/iaas/api/#/en/key/latest/VerifiedData/Verify)API with the Cryptographic Endpoint to verify a digital signature created with a master encryption key.

Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
