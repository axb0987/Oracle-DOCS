# Restoring Vault from a Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_vault.htm
- Fetched: 2026-09-05 02:32 CDT

# Restoring Vault from a Backup

Learn how to restore a vault from a backup.

The restore vault feature is only available for virtual private vaults. You can monitor the progress of the restore operation through the work request for the restore. See[Using the Console to View Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_vault.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- Select the name of the value to view its details.
- Select Actions , then select Update Vault from Backup .
- Select a backup source. You can import a vault backup from the following sources: an Object Storage bucket, a preauthenticated Object Storage URL, or a file on your local machine or a mapped network location.
- Do one of the following, depending on what you chose in the previous step:

- Select a bucket. If needed, you can change the compartment to find a bucket in a different compartment. Then, select the file containing the vault backup.
- Select the Object Storage URL option, then provide a preauthenticated URL. Include the backup's file name.
- Using Upload a File , drag a file or select one from your local machine or a mapped network location.
- When you're finished, select Update Vault .
- 

Use the[oci kms management vault restore](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/restore.html)command to restore a vault from OCI Object Storage.

```

```

Use the[oci kms management vault restore-from-file](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/restore-from-file.html)command to restore a vault from an encrypted file.

```

```

- 

Use the[RestoreVaultFromFile](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/RestoreVaultFromFile)API or the[RestoreVaultFromObjectStore](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/RestoreVaultFromObjectStore)API with the Management Endpoint to restore a vault from a backup.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
