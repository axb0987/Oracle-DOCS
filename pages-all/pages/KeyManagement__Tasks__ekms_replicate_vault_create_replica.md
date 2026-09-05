# Creating a Vault Replica
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_create_replica.htm
- Fetched: 2026-09-05 02:35 CDT

# Creating a Vault Replica

Replicate a vault to a secondary region.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_create_replica.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_create_replica.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_create_replica.htm#)
- 

Before replicating a vault to a destination region, complete the following prerequisites:
- Replicate the domain to the destination region. See[Identity Domain Replication](https://docs.oracle.com/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm).
- Create a Private Endpoint (PE) in the destination region. See[Creating a PE](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms_creating_ekms_private_endpoint.htm).

- On the External Key Management Vaults page, find the vault that you want to work with. If you need help finding the list page or the vault, see[Listing External Key Management Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm).
- Select the name of the vault that you're interested in.
- In the vault details page, select Actions , then select Replicate Vault .
- In the Replicate Vault dialog box, select a destination region from the list.
- Select an identity domain from the list.
- Select private endpoint of the destination region from the list.
- Select Create Replica .
- 

Use the[oci kms management vault create-vault-replica](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/create-vault-replica.html)command and required parameters to create a replica for the vault in another region in the same realm.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateVault](https://docs.oracle.com/iaas/api/#/en/key/release/Vault/UpdateVault)API to update the details of an External KMS vault.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
