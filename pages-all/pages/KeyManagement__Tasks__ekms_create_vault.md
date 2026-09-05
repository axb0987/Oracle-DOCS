# Creating an External Key Management Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_vault.htm
- Fetched: 2026-09-05 02:34 CDT

# Creating an External Key Management Vault

Learn how to create a vault in OCI External Key Management.

To create a vault in KMS side, you need the following details:
- The external vault endpoint URL
- Private endpoint OCID
- Oauth metadata (IDCS URL, client application ID and client application secret)
Note  
  
You must associate the confidential client app to identity domain, and this app is bound to confidential resource app (external key management) for authorization

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_vault.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select External Key Management .
- On the External key Management home page, select Create Vault .
- On the Create Vault page, provide the following details:

- Name: Enter a name for the vault.
- Description: Provide a short description.
- Create in Compartment: Select a compartment for the OCI KMS vault.
- IDCS Account Name URL: Enter the authentication URL that you use to access the KMS service. The Console redirects to a sign in screen.
- Key Manager Vendor: Select a third-party vendor that deploys key management service.
- Client application ID: . Enter the OCI KMS client ID generated when you register the confidential client application in Oracle Identity Domain.
- Client application secret: Enter the Secret ID of the confidential client application registered in the Oracle Identity Domain.

Caution  
  
Rotating (changing) the IDCS client secret in the IDCS service is a disruptive operation. OCI doesn't support updating the client secret in an existing external vault resource. If you rotate the client secret in IDCS, the old secret stored in the external vault becomes invalid and all cryptographic operations fail for the vault.
- Private Endpoint compartment: Select the compartment of the private endpoint you want to use with the external key management vault.
- Private Endpoint: Select the private endpoint to use with the external key management vault.
- External Vault URL: Enter the vault URL that was generated when you created vault in external key management.
- Select Create Vault .
- 

Use the[oci kms management vault create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/create.html)command to create a new vault:

```

```

For example:
```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/CreateVault)API with the Management Endpoint to create an external vault.

Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
