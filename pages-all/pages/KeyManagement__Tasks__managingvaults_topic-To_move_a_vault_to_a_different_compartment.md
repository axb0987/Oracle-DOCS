# Moving a Vault to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_move_a_vault_to_a_different_compartment.htm
- Fetched: 2026-09-05 02:36 CDT

# Moving a Vault to a Different Compartment

Learn how to move an OCI vault to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_move_a_vault_to_a_different_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_move_a_vault_to_a_different_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_move_a_vault_to_a_different_compartment.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- From the Actions menu (three dots) for the vault, select Move Resource .
- Select the destination compartment and then select Move Resource .
- 

Use the[oci kms management vault change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/change-compartment.html)command and required parameters to move a vault to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ChangeVaultCompartment](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/ChangeVaultCompartment)API with the KMSVAULT API endpoint to move a vault to another compartment.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
