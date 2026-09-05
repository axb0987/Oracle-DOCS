# Renaming Key References
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rename_key_references.htm
- Fetched: 2026-09-05 02:35 CDT

# Renaming Key References

Learn how to rename a key reference created for an encryption key stored in an external key managmeent system.

After you create a key reference, you can rename it by accessing the Key Reference Details page.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rename_key_references.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rename_key_references.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rename_key_references.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault to see its details.
- In the Keys tab, select the name of a key reference to see its details.
- In the Key Reference Details page, select Edit Name .

Note  
  
You can update the key reference name, but not the external Key GUID. .
- Enter a new name.
- Select Save Changes .
- 

Use the[oci kms management key update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/update.html)command and required parameters to rename a key reference:

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/UpdateKey)API with the Management Endpoint to rename a key reference.

Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
