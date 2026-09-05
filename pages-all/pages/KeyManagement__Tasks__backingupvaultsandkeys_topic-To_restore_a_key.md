# Restoring a key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_key.htm
- Fetched: 2026-09-05 02:32 CDT

# Restoring a key

Learn how to restore a vault key from a backup.

The restore a key feature is only available for keys in virtual private vaults. You can monitor the progress of the restore operation through the work request for the restore. See[Using the Console to View Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_restore_a_key.htm#)
- 

- On the Master Encryption Keys list page, select Restore Key . If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select a source. You can import a key backup from the following sources: an Object Storage bucket, a preauthenticated Object Storage URL, or a file on your local machine or a mapped network location.
- Do one of the following, depending on what you chose in the previous step:

- Select a bucket from the dropdown menu. If needed, you can change the compartment to find a bucket in a different compartment, then use the Select a file menu to select the name of the file containing the backup of your key.
- Select Object Storage URL , and then provide a preauthenticated URL for the file in OCI Object Storage that contains your key backup..
- Using Upload a file , drag a file or select one from your local machine or a mapped network location to import a file containing a backup of a key.
- When you're finished, select Restore Key .
- 

Use the[oci kms management key restore](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/restore.html)command and required parameters to restore a key from Object Storage:

```

```

Use the[oci kms management key restore-from-file](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/restore-from-file.html)command and required parameters to restore a key from a file:

```

```

See[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information on using JSON input with this command.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[RestoreKeyFromFile](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/RestoreKeyFromFile)API or the[RestoreKeyFromObjectStore](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/RestoreKeyFromObjectStore)API with the Management Endpoint to restore a key from a backup.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
