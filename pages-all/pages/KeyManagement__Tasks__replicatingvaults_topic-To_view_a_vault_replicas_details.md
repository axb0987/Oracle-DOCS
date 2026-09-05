# Viewing a Replicated Vault's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_view_a_vault_replicas_details.htm
- Fetched: 2026-09-05 02:36 CDT

# Viewing a Replicated Vault's Details

Learn how to view the details of a replicated vault from another vault's details page using the OCI Console

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_view_a_vault_replicas_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_view_a_vault_replicas_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults_topic-To_view_a_vault_replicas_details.htm#)
- 

- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- Select the name of the source vault.
- Select View Replica Details .
- The details of the replicated vault include the following:

- Destination Region: The region in which the vault replica exists.
- Replication State: The current state of the vault in the destination region regarding replication. (A vault's replication state is unrelated to its lifecycle state. The lifecycle state of the vault in the destination region matches the lifecycle state of the vault in the source region.)
- Creation Date: The date that you started replicating data to the vault in the destination region.
- Destination Vault Name: The name of the vault in the destination region.
- OCID: The unique, Oracle-assigned ID of the vault in the destination region.
- Management Endpoint: The endpoint to use if you need to begin sending requests for management operations to the vault in the destination region.
- Cryptographic Endpoint: The endpoint to use in the event you need to begin sending requests for cryptographic operations to the vault in the destination region.
- 

Use the[oci kms management vault get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/get.html)command and required parameters to get a vault replica's details information:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/GetVault)API to get a replicated vault's details information.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
