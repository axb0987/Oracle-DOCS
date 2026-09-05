# Viewing a Key Version
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managing-keys-get-key-version.htm
- Fetched: 2026-09-05 02:35 CDT

# Viewing a Key Version

Learn how to view or retrieve information about a key version of a Master Encryption Key.

For information on retrieving key material for software-protected master encryption keys and key versions, see[Exporting Vault Keys and Key Versions](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/exportingkeys.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managing-keys-get-key-version.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managing-keys-get-key-version.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managing-keys-get-key-version.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select the name of the key you want to work with, then select Versions to see the list of key versions for the key.
- Each key version in the list can be identified by its OCID. Select Actions menu (three dots) in the row for a key version, and then select Copy to clipboard to retrieve the OCID of the key version. You can also view the following for each key version:

- State
- Auto rotation configuration
- Source of key material: internal (created within OCI Key Management) or external (created using a third-party tool and then imported into an OCI vault)
- Creation date
- 

Use the[oci kms management key-version get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key-version/get.html)command and required parameters to retrieve a key version of an OCI Master Encryption Key:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetKeyVersion](https://docs.oracle.com/iaas/api/#/en/key/latest/KeyVersion/GetKeyVersion)operation with the Management Endpoint to retrieve a key version of an OCI Master Encryption Key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
