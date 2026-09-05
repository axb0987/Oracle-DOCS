# Backing up a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_key.htm
- Fetched: 2026-09-05 02:31 CDT

# Backing up a Key

Learn how to back up a master encryption key.

The backup a key feature is only available for keys in virtual private vaults. You can monitor the progress of the backup operation through the work request for the backup. See[Using the Console to View Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_back_up_a_key.htm#)
- 

This task can't be performed using the OCI Console.

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select the name of the Master Encryption Key to view the details for the key.
- Select Actions, then select Back Up Key.

- Select a source: export a backup to either an Existing Object Storage Bucket (recommended) or a preauthenticated Object Storage URL for an bucket that you can write to.
- Do one of the following, depending on what you chose in the previous step:
- Select a bucket from the drop down menu. If needed, you can change the compartment to find a bucket in a different compartment. Then, specify the Backup Name . Avoid entering confidential information.
- Select Object Storage URL , and then provide a preauthenticated URL for an object.
- When you're finished, select Back Up Key . (Note the compartment so that you can restore this resource to the same compartment later.)
- 

Use the[oci kms management key backup](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/backup.html)command and required parameters to back up a key:

```

```

See[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information on using JSON input with this command.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[BackupKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/BackupKey)API with the Management Endpoint to back up a key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
