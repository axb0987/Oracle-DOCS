# Moving a Key to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_move_a_key_to_a_different_compartment.htm
- Fetched: 2026-09-05 02:35 CDT

# Moving a Key to a Different Compartment

Learn how to move a master encryption key to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_move_a_key_to_a_different_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_move_a_key_to_a_different_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_move_a_key_to_a_different_compartment.htm#)
- 

- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- From the Actions menu (three dots) at the end of the row entry for the key, select Move Resource .
- On the Move resource page, select the Destination compartment.
- Select Move resource .
- 

Use the[oci kms management key change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/change-compartment.html)command and required parameters to move a key to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeKeyCompartment](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ChangeKeyCompartment)operation with the Management Endpoint to change the compartment.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
