# Replicating an External Key Management Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault.htm
- Fetched: 2026-09-05 02:35 CDT

# Replicating an External Key Management Vault

Replicate OCI external vaults and key references to a secondary region within the same realm that supports cross-region vault replication for EKMS.
Replicating vaults for EKMS provides the following benefits:
- Improved Disaster Recovery: Replicating vaults and keys ensures a robust disaster recovery solution in the event of regional disruptions,
- Data Protection: Maintaining redundant key copies safeguards against accidental loss or unauthorized access.
- Compliance and Data Residency: For regulated industries and organizations with specific data residency requirements, replication ensures compliance with relevant laws.

## How Cross-Region Replication Works

When enabling cross-region replication for an external vault, OCI's Key Management service synchronizes any creation, deletion, modification, or relocation of any external key or key versions references between the primary external vault and its replica in a secondary region. The originating vault, termed the source vault, starts the replication process. The destination vault, termed as the vault replica, receives the replicated data.

During this regional replication process, the external vault maintains FIPS 140-2 Level 3 security standards and the external key references are exported as encrypted binary objects.
Note  
  

OCI's cross-region replication for external vaults includes replicating the vault and its associated key references. However, it's important to understand that replicating externally managed keys is your responsibility and isn't part of OCI's replication process.

## Source and Replica Vault Management

The Key Management service supports using the vault replica for cryptographic operations. However, you can't perform management operations directly on the external vault replica and its key references. For example, creating key references directly in the replica vault or performing backup operations on it aren't supported. To use the replica vault for cryptographic tasks, you can access its cryptographic endpoint, which is available in the vault replica's details.

To stop the replication of a source vault, delete the vault replica in the destination region. As only one replica can be associated with a source vault at a particular time, deleting the existing replica is necessary if replication to a different destination region is required.

## Recovery Time and Recovery Point During Fail Over

The Recovery Time Objective (RTO) in a fail over scenario is the maximum potential downtime for applications when switching to the destination region. In a steady state, RTO is near zero because every external key created in the source region is immediately replicated to the destination. The minimal delay is primarily from the network latency between regions, and measured in milliseconds. This ensures that applications can swiftly fail over to the destination region and access external keys almost instantly.
