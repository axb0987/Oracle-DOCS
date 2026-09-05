# Deleting a Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_delete_a_vault.htm
- Fetched: 2026-09-05 02:36 CDT

# Deleting a Vault

Learn how to delete an OCI vault.
Note  
  
When you delete a vault, the vault and all its associated keys go into a pending deletion state until the waiting period expires. By default, this wait period is set as 30 days, but it can be set from a minimum of 7 days up to a maximum of 30 days. When a vault is deleted, all its associated keys are also deleted. If replication is configured, deleting a vault in the source region also deletes the vault and any keys in the vault in the destination region.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_delete_a_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_delete_a_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_delete_a_vault.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- From the Actions menu (three dots) for the vault, select Delete Vault.
- In the Confirm dialog box, enter the name of the vault, and then select the date and time that you want the vault to be deleted.
- Select Delete Vault .
- 

Use the[oci kms management vault schedule-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/schedule-deletion.html)command and required parameters to delete a vault:

```

```

When you delete a vault, the vault and all its associated keys go into a pending deletion state until the waiting period expires. By default, this is 30 days, but can be set from a minimum of 7 days up to a maximum of 30 days. When a vault is deleted, all its associated keys are also deleted. If replication is configured, deleting a vault in the source region also deletes the vault and any keys in the vault in the destination region.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ScheduleVaultDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/ScheduleVaultDeletion)API with the KMSVAULT endpoint to delete a vault replica.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
