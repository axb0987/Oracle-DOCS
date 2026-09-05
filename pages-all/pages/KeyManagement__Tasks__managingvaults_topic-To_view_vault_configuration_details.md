# Listing Vault Replicas
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_view_vault_configuration_details.htm
- Fetched: 2026-09-05 02:36 CDT

# Listing Vault Replicas

Learn how to list replicas of a specified vault.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_view_vault_configuration_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_view_vault_configuration_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_view_vault_configuration_details.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- From the list, select the name of a vault that has been replicated.
- The Replication Details field is displayed on the Vault Information tab for vaults that have been replicated. Select View Replica Details for information on the replica of the source vault. This button only displays for vaults that have replicas.

In the Replica Details list, view the replicas of the vault you are working with. To see details for a particular replica, use the arrow beside the name of the destination region to expand the row. The following details are available:
- Destination Vault Name: The name of the replicated vault.
- OCID: The unique, Oracle-assigned ID of the vault replica.
- Management Endpoint: The service endpoint to perform management operations against. For destination vaults, management operations only include`List`and`Get`operations.
- Cryptographic Endpoint: The service endpoint to perform cryptographic operations against. Cryptographic operations include[Encrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/EncryptedData/Encrypt),[Decrypt](https://docs.oracle.com/iaas/api/#/en/key/latest/DecryptedData/Decrypt), and[GenerateDataEncryptionKey](https://docs.oracle.com/iaas/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey),[Sign](https://docs.oracle.com/iaas/api/#/en/key/release/SignedData/Sign), and[Verify](https://docs.oracle.com/iaas/api/#/en/key/latest/VerifiedData/Verify)operations.
- 

Use the[oci kms management vault list-vault-replicas](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/list-vault-replicas.html)command and required parameters to list vault replicas:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ListVaultReplicas](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/ListVaultReplicas)API with the KMSVAULT API endpoint to retrieve a list of replicas of a vault in OCI.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
