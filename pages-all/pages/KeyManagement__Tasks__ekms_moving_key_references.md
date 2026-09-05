# Moving Key References
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_moving_key_references.htm
- Fetched: 2026-09-05 02:34 CDT

# Moving Key References

Learn how to move a key reference from one compartment to another compartment in OCI External Key Management.

You can move key reference from the existing compartment to another compartment in the same region.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_moving_key_references.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_moving_key_references.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_moving_key_references.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault that has the key reference you're moving.
- On the Keys page, select the name of the a key reference you're moving.
- Select Actions , then select Move Resource .
- Select a compartment to which you want to move the resource.
- Select Move resource .

The resource is moved to the new compartment.
- 

Use the[oci kms management key change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/change-compartment.html)command to move key reference to a different compartment:

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ChangeKeyCompartment](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ChangeKeyCompartment)API with the Management Endpoint to change compartment of the key reference.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
