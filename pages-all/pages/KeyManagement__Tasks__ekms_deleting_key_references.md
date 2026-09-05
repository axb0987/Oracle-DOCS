# Deleting Key References
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_key_references.htm
- Fetched: 2026-09-05 02:34 CDT

# Deleting Key References

Learn how to delete a key reference in OCI External Key Management.

The delete operation for key references is a non-recoverable action. However, when you delete a key reference on KMS, this operation doesn't delete the actual key in the external key management system. OCI External Key management has a 7 day waiting period for deleting external key references to prevent accidental key reference deletion. When you schedule a key reference deletion, the key is put in a pending deletion state.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_key_references.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_key_references.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deleting_key_references.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault that has the key reference you're deleting.
- On the Keys tab, select the name of the a key reference you're deleting to view the key reference's details.
- Select Actions , then select Delete .
- In the Delete Key Reference dialog, confirm that you want to delete this key reference by entering the name of the key reference, then select a deletion date and time if you don't want to use the default 7 day wait period. If you select a custom date and time for deletion, it must be more than the minimum (default) period of 7 days from the current date and time.

Note  
  
OCI Key Management has a 7 day wait period for deleting a key reference. When you schedule a key reference for deletion, it goes to "pending deletion" state and all actions on the Key Reference details page are disabled. Note that deleting a key reference doesn't delete the external key. .
- 

Use the[oci kms management key schedule-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/schedule-deletion.html)command to delete a key reference:

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ScheduleKeyDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ScheduleKeyDeletion)API with the Management Endpoint to delete a key reference.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
