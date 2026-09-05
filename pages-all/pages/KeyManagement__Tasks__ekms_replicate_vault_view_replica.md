# Viewing a Vault Replica
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_view_replica.htm
- Fetched: 2026-09-05 02:35 CDT

# Viewing a Vault Replica

Learn how to view the details of a replicated External Key Management vault using the OCI Console.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_view_replica.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_view_replica.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_view_replica.htm#)
- 

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault to view its details.
- Select View Replica Details .
-   

The details of the replicated vault include the following:
- Destination Region: The region in which the vault replica exists.
- Replication State: The current state of the vault in the destination region regarding replication. (A vault's replication state is unrelated to its lifecycle state. The lifecycle state of the vault in the destination region matches the lifecycle state of the vault in the source region.)
- Creation Date: The date that you started replicating data to the vault in the destination region.
- Destination Vault Name: The name of the vault in the destination region.
- OCID: The unique, Oracle-assigned ID of the vault in the destination region.
- Management Endpoint: The endpoint to use if you need to begin sending requests for management operations to the vault in the destination region.
- Cryptographic Endpoint: The endpoint to use in the event you need to begin sending requests for cryptographic operations to the vault in the destination region.
- 

Use the[list-vault-replicas](https://docs.oracle.com/iaas/tools/oci-cli/3.52.1/oci_cli_docs/cmdref/kms/management/vault/list-vault-replicas.html)command and required parameters to list the replicas of a vault.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ListVaultReplicas](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/ListVaultReplicas)API with the Management Endpoint to view the replicas for a vault.

Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
