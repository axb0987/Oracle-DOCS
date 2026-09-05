# Backing up a Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_vault.htm
- Fetched: 2026-09-05 02:32 CDT

# Backing up a Vault

Learn how to back up an OCI vault and its keys.
The backup feature is only available for virtual private vaults. You can monitor the progress of the backup operation through the work request for the backup. See[Using the Console to View Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_vault.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- Select the name of the vault to open its details page.
- On the vault's details page, select Actions , then select Back Up Vault .
- Select a source: export a backup to either an Existing Object Storage Bucket (recommended) or a preauthenticated Object Storage URL for an bucket that you can write to.
- Do one of the following, depending on what you chose in the previous step:
- Select a bucket from the drop down menu. If needed, you can change the compartment to find a bucket in a different compartment. Then, specify the Backup Name . Avoid entering confidential information.
- Select Object Storage URL , and then provide a preauthenticated URL for an object.
- Optionally, to back up only the vault without any keys, select the Back up vault metadata only checkbox.
- When you're finished, select Back Up Vault . (Note the compartment so that you can restore this resource to the same compartment later.)
- 

Use the[oci kms management vault backup](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/backup.html)command and required parameters to restore a key:

```

```

See[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information on using JSON input with this command.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[BackupVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/BackupVault)API with the Management Endpoint to back up a vault.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/)
