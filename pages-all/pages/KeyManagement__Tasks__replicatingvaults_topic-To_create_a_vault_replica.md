# Replicating a Vault and Its Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_create_a_vault_replica.htm
- Fetched: 2026-09-05 02:36 CDT

# Replicating a Vault and Its Keys

Learn how to replicate a vault and its keys.

Virtual vaults created before the cross-region vault replication feature was introduced can't be replicated across regions. However, all private vaults support cross region replication. You can use the[GetVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/GetVault)API's`isVaultReplicable`parameter to find if a virtual vault supports cross region replication. Create a new vault and new keys if you have a vault that you need to replicate in another region and replication isn't supported for that vault. Existing keys can't be copied to a new vault.
Note  
  

- You can only replicate active vaults and active, enabled, or disabled keys.
- For information on replicating secrets, see[Replicating Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/secrets-replication.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_create_a_vault_replica.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_create_a_vault_replica.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_create_a_vault_replica.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- Select the name of the vault that you want to replicate to view its details page.
- Select Actions , then select Replicate Vault .
- In the Replicate Vault dialog box, select a destination region from the list, and then select Create Replica .
- 

Use the[oci kms management vault create-vault-replica](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/create-vault-replica.html)command and required parameters to create a replica for the vault in another region in the same realm.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateVaultReplica](https://docs.oracle.com/iaas/api/#/en/key/release/Vault/CreateVaultReplica)API with the Management Endpoint to create a replica for the vault in another region in the same OCI realm.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
