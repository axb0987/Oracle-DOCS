# Canceling a Vault Deletion
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_cancel_the_deletion_of_a_vault.htm
- Fetched: 2026-09-05 02:36 CDT

# Canceling a Vault Deletion

Learn how to cancel the scheduled deletion of a vault.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_cancel_the_deletion_of_a_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_cancel_the_deletion_of_a_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_cancel_the_deletion_of_a_vault.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- Select Cancel Deletion from the Actions menu (three dots) in the row for the vault.
- To confirm, select Cancel Deletion .
- 

Use the[oci kms management vault cancel-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/cancel-deletion.html)command and required parameters to cancel the pending deletion of a vault:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CancelVaultDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/CancelVaultDeletion)API with the KMSVAULT API endpoint to cancel the scheduled deletion of a vault in OCI.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
