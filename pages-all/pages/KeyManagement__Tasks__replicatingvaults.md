# Replicating Vaults and Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/replicatingvaults.htm
- Fetched: 2026-09-05 02:36 CDT

# Replicating Vaults and Keys

Replicate vaults and keys for disaster recovery scenarios. Replication helps in reading keys in a vault from a different region within the same realm.

You can replicate vaults from one region to a second region to make them and the keys that they contain available in the remote region. Replicating vaults provides the following benefits:
- Improved Disaster Recovery: Replicating keys to across regions ensures data accessibility and faster recovery in the event of regional disruptions.
- Data Protection: Maintaining redundant key copies safeguards against accidental loss or unauthorized access.
- Compliance and Data Residency: For regulated industries and organizations with specific data residency requirements, replication ensures compliance with relevant laws.
Note  
  
See[Replicating Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/secrets-replication.htm)for information on replicating secrets across regions.

## How Replication Works

When you configure cross-region replication for a vault, the service automatically synchronizes the creation, deletion, update, or move of any keys or key versions between a specified vault and a replica of that vault in another region. The vault from which the service replicates data is known as the source vault. The vault in the destination region to which the service replicates data from the source vault is known as the vault replica.

The vault maintains FIPS 140-2 Level 3 security during regional replication, and keys are exported as encrypted binary objects and restored only within Oracle-provided FIPS 140-2 Level 3 hardware security modules (HSMs) within your tenancy. Keys never leave the HSM in plain text. The start and delete replication operations are logged in OCI Audit logs.

## Source and Replica Vault Management

The service supports using the vault replica for cryptographic operations. You can't perform management operations directly on the vault replica and its keys. For example, you can't create keys directly in the vault replica, nor can you back up the vault replica. You can find the cryptographic endpoint of the vault replica by viewing the vault replica's details, and you can use that endpoint when needed.

To stop the replication of a source vault, delete the vault replica in the destination region. Because only one vault replica can exist for a source vault at any time, you must delete an existing vault replica to replicate the source vault in a different destination region.

## Recovery Time and Recovery Point During Fail Over

Recovery time objective (RTO) is the maximum time applications might be unavailable during a fail over to the destination region. RTO is near zero in a steady state, because every key created in the source region is immediately replicated to the destination region. The delay is primarily from the network latency between regions, and measured in milliseconds. Therefore, applications can fail over to the destination region and access keys almost instantly.

Recovery point objective (RPO) is the maximum amount of data that might be lost in the source region during a fail over. RPO for replicated vault keys is zero, because KMS doesn't confirm a replication operation is successful until a key is committed to persistent HSM storage, helping to ensure no data loss.
Note  
  

OCI KMS supports two types of vault offerings:
- Virtual vault: A cost-effective, multi tenant service for managing keys.
- Private vault: A single-tenant service providing enhanced isolation and security.

Note the following limitations and considerations:
- 

Virtual vaults created before the cross-region vault replication feature was introduced can't be replicated across regions. However, all private vaults support cross region replication. You can use the[GetVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/GetVault)API's`isVaultReplicable`parameter to find if a virtual vault supports cross region replication. Create a new vault and new keys if you have a vault that you need to replicate in another region and replication isn't supported for that vault. Existing keys can't be copied to a new vault.

If you have a vault that doesn't support cross-region replication, the Replicate Vault button on the vault details page is disabled.
- By default, private vaults have a limit of zero, so, you must request a service limit increase in the destination region where you want to replicate a private vault before creating a vault replica.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: for a typical policy that gives access to vaults, keys, and secrets, see[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#sec-admins-manage-vaults-keys). Besides policies for users and groups, you must also write a policy that gives the Vault service the ability to do everything with vaults so it can create and manage vaults on your behalf during replication. For example, the following policy gives permission to the service in all regions realm-wide:

```

```

To restrict permissions to specific compartments, specify the compartment instead. For more information about permissions or if you need to write more restrictive policies, see[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)
