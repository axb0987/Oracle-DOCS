# Disabling Key References
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_disabling_key_references.htm
- Fetched: 2026-09-05 02:34 CDT

# Disabling Key References

Lean how to disable key references in OCI External Key Management.

The "Disable" operation for a key and its key reference is a recoverable action, as the key and reference can be enabled again. In this respect, it differs from a Delete operation, which is an unrecoverable operation which destroys the key.

If an external key is disabled in the third-party external key manager, you can disable its key reference in OCI EKMS. As a result, the external key can no longer be used for cryptographic operations with Oracle data at rest.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_disabling_key_references.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_disabling_key_references.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_disabling_key_references.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault that has the key reference you're disabling.
- On the Keys tab, select the name of the a key reference you're disabling to view the key reference's details.
- Select Actions , then select Disable .
- Confirm that you want to disable the key reference.
-   

After disabling a key reference, all actions on the key reference gets disabled. However, on enabling it again, the actions become enabled.
- 

Use the[oci kms management key disable](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/disable.html)command with the Management Endpoint to disable a key reference:

Open a command prompt and run`oci kms management key disable`to disable a key reference:

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[DisableKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/DisableKey)API with the Management Endpoint to disable a key reference.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
