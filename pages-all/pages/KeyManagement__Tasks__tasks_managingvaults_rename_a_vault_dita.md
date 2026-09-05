# Renaming a Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_rename_a_vault_dita.htm
- Fetched: 2026-09-05 02:36 CDT

# Renaming a Vault

Learn how to update a vault's details. Note that you can't change the vault type after the vault is created.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_rename_a_vault_dita.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_rename_a_vault_dita.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_managingvaults_rename_a_vault_dita.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- Select the name of the vault to open its details page.
- Select Actions to see a list of actions you can perform on the vault.
- Select Edit Name .
- Enter a new name for the vault and then select Update
- 

Use the[oci kms management vault update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/update.html)command and required parameters to rename a vault:
```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/UpdateVault)API with the KMSVAULT endpoint to rename a vault.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
