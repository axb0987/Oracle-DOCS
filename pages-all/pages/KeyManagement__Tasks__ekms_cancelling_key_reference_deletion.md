# Canceling the Scheduled Deletion of a Key Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_cancelling_key_reference_deletion.htm
- Fetched: 2026-09-05 02:34 CDT

# Canceling the Scheduled Deletion of a Key Reference

Learn how to cancel a scheduled key reference deletion in OCI External Key Management.

You can cancel the scheduled deletion of a key reference while the key reference is in the 7-day waiting period that starts when the deletion is requested as described in[Deleting Key References](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_key_references.htm). After the waiting period is over, External Key Management deletes the key reference, and the key reference can't be recovered. However, the encryption key stored in the external key management system isn't deleted by OCI.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_cancelling_key_reference_deletion.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_cancelling_key_reference_deletion.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_cancelling_key_reference_deletion.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault that has the key reference you're working with.
- On the Keys tab, select the name of the a key reference you're working with to view the key reference's details.
- Select Actions , then select Cancel Deletion .
- Confirm that you want to cancel the scheduled deletion of the key reference.

When you cancel a deletion, the key reference is set to the "Active" state. You can only cancel a scheduled deletion during the 7 day waiting period that starts when the deletion is scheduled.
- 

Use the[oci kms management key cancel-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/cancel-deletion.html)to cancel a key reference deletion.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CancelKeyDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/CancelKeyDeletion)API with the Management Endpoint to cancel deletion of a key reference.

Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
