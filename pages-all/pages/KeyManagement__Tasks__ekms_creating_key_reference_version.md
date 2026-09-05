# Creating Key Reference Version
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_key_reference_version.htm
- Fetched: 2026-09-05 02:34 CDT

# Creating Key Reference Version

Learn how to create a key reference version for an encryption key stored in an external key management system.

Use this operation to retire the current key reference version and create a new key reference version.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_key_reference_version.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_key_reference_version.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_key_reference_version.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault that has the key reference you want to work with.
- In the Keys tab, select a key reference.
- In the Key Reference Versions tab, select Rotate Key Reference .
- On the Rotate Key Reference page, enter the key rotation version ID.
- Select Rotate Key Reference .

A new entry is added to the Version table and the rotation status is set as "Enabled."
- 

Use the[oci kms management key-version create](https://docs.oracle.com/iaas/tools/oci-cli/3.50.3/oci_cli_docs/cmdref/kms/management/key-version/create.html)command to create a key reference version.

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateKeyVersion](https://docs.oracle.com/iaas/api/#/en/key/latest/KeyVersion/CreateKeyVersion)API with the Management Endpoint to create a new key reference version for an external key in External Key Management.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
