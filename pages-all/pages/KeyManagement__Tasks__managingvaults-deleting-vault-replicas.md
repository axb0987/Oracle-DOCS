# Deleting a Vault Replica
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults-deleting-vault-replicas.htm
- Fetched: 2026-09-05 02:36 CDT

# Deleting a Vault Replica

Learn how to delete a vault replica.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults-deleting-vault-replicas.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults-deleting-vault-replicas.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults-deleting-vault-replicas.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- From the list, select the name of a vault that has the replica you're deleting
- In the Replication Details field of the Vault Information tab, select View Replica Details .
- From the Actions menu (three dots) for the vault, select Delete Replica.
- 

Use the[oci kms management vault delete-vault-replica](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/delete-vault-replica.html)command and required parameters to delete a vault replica:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[DeleteVaultReplica](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/DeleteVaultReplica)API with the KMSVAULT API endpoint to delete a vault replica.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
