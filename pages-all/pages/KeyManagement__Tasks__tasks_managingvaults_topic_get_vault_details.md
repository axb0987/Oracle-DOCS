# Getting a Vault's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_topic_get_vault_details.htm
- Fetched: 2026-09-05 02:36 CDT

# Getting a Vault's Details

Learn how to get the an OCI vault's details.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_topic_get_vault_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_topic_get_vault_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_topic_get_vault_details.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- From the list of vaults in the compartment, select a vault name to see its details.
The Vault Information section displays the following vault details:
- Compartment: The name of the compartment that contains the vault.
- OCID: The unique, Oracle-assigned ID of the vault.
- Created: The date and time when you initially created the vault.
- HSM Key Version Usage: The total number of key versions across all HSM-protected keys that the vault contains.
- Virtual Private: The vault is a virtual private type.
- Crytographic Endpoint: The service endpoint to perform cryptographic operations such encrypt, decrypt and so forth.
- Management Endpoint: The service endpoint to perform management operations such as "create, get,list, delete and so forth.
- 

Use the[oci kms management vault get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/get.html)command and required parameters to get a vault's details information:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/GetVault)API with the KMSVAULT API endpoint to get a vault's details information.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
