# Deleting a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_delete_a_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Deleting a Key

Learn how to schedule the deletion of a master encryption key stored in an OCI vault.

OCI's Key Management service gives you the option of either[disabling](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_disable_a_key.htm)or deleting keys that you no longer use. While disabling a key provides the easiest path to restoring a key to service if the key is needed later, you might need to delete keys because of your organization's key lifecycle policy, or to free up quota in your[Key Management service limit](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Vault_Limits).

Because deleting a key is a destructive operation that could result in data that was encrypted with the key being inaccessible, OCI requires that you schedule the deletion with a wait period that you specify. You can either accept the default wait period of 30 days until deletion, or specify a shorter period, with 7 days being the minimum wait period. We recommend that you back up a key before you schedule it for deletion. With a backup, you can restore the key to the vault if you need to use the key later.

We recommend using service log data to analyze key usage and decide if deleting or disabling a key, when appropriate. Note that some keys might still be operationally important despite limited activity, and this must be considered along with usage data when making decision about deleting or disabling a key. See[Monitoring Key Usage](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys-usage.htm)for information on using OCI service logs to track key usage.

Important:
- When a key is in the Pending Deletion state, anything encrypted by that key immediately becomes inaccessible, including secrets. The key also can't be assigned or unassigned to any resources or otherwise updated. When the key is deleted, all key material and metadata is irreversibly destroyed. Before you delete a key, either assign a new key to resources currently encrypted by the key or preserve your data another way. To restore the use of a key before it's permanently deleted, you can cancel its deletion. See[Canceling a Master Encryption Key Deletion](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_cancel_the_deletion_of_a_key.htm)for more information.
- When your key is scheduled for deletion,[auto-rotation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm)temporarily suspended but not disabled for keys with this feature enabled. If the key deletion is canceled and the key returns to the Active state, the auto rotation setting that the key had before the scheduled deletion is restored.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_delete_a_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_delete_a_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_delete_a_key.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- From the Actions menu (three dots) at the end of the row entry for the key, select Delete Key .
- On the Confirm page, enter the key name in the Name field to confirm.
- Use the Select deletion date and Time fields to schedule when you want the Vault service to delete the key. By default, the service schedules keys for deletion 30 days from the current date and time. You can set a range between 7 days and 30 days. When you schedule the key for deletion, we recommend you to back up the key because all key management operations.
- Select Delete Key .
- 

Use the[oci kms management key schedule-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/schedule-deletion.html)command and required parameters to schedule the deletion of a key. By default, the deletion is schedule for 30 days from the time of the request. Use the optional`--time-of-deletion`parameter to schedule the deletion for a number of days between 7 and 30 from the time of the request. See the CLI Command Reference for more information:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ScheduleKeyDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ScheduleKeyDeletion)operation with the Management Endpoint to delete the vault key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
