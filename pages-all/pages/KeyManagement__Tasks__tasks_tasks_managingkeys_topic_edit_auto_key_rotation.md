# Enabling and Updating Auto Key Rotation
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm
- Fetched: 2026-09-05 02:36 CDT

# Enabling and Updating Auto Key Rotation

Learn about enabling automatic key rotation, and about updating automatic rotation settings for keys that already have this feature enabled.
Note  
  
This feature is available only for virtual private vaults.

You can update automatic key rotation settings to do the following:
- Enable automatic rotation for keys that don't have this feature enabled
- Update the date on which the next rotation happens
- Update the rotation interval (the number of days, between 60 and 365, that pass before a key is rotated)

## Manual Key Rotation

See[Rotating a Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm)for information on manually rotating an encryption key. See[Key Versions &amp; Rotations](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts__key-versions-and-rotations-section)in the the[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts)topic for an overview of key rotation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- In the Key Information tab, select Actions , then select Edit auto-rotation settings .
- In the Edit auto-rotation settings page, update the following as needed:

- Auto rotation: Select this checkbox to enable auto rotation.
- Start date: Use this field to select the date that auto rotation begins for your key.
- Rotation interval: Specify the number of days between rotations. You can enter a value between 60 and 365 days.
- Select Update .
- 

Use the[oci kms management key update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/update.html)command and required parameters to edit the auto rotation settings of keys in virtual private vaults.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/UpdateKey)API with the Management Endpoint to update automatic key rotation settings for a virtual private vault key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
