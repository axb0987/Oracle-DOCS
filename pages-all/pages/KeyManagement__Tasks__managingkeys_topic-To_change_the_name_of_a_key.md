# Renaming a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_change_the_name_of_a_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Renaming a Key

Learn how to update a master encryption key to change its name.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_change_the_name_of_a_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_change_the_name_of_a_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_change_the_name_of_a_key.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select the name of key to see the key details displayed in the Key Information tab.
- Select the Actions button.
- Select Edit Name .
- Enter a new name, then select Update .
- 

Use the[oci kms management key update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/update.html)command and required parameters to edit a key's name:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/UpdateKey)API with the Management Endpoint to change a key's name.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
