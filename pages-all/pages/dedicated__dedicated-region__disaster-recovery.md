# Disaster Recovery
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/disaster-recovery.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/disaster-recovery.htm#dcoc-content-body)

# Disaster Recovery

Use this section to learn how to design resiliency across Dedicated Regions and how to distinguish high availability within a region from DR across regions.

High availability protects workloads inside a Dedicated Region through fault domains and service-level resiliency patterns. DR protects applications and data from region-level failure by replicating the application stack between a primary Dedicated Region and a second Dedicated Region in a different geography.

DR Design Area Guidance
Region pair Use at least two Dedicated Regions for a robust DR strategy. Separate regions by sufficient distance, commonly described as 50 miles to 100 miles or more, based on disaster scenarios and local regulations.
Connectivity Inter-region connectivity is required when two or more Dedicated Regions exist in the same realm. It supports replication, failover coordination, and recovery operations.
Application stack Replicate application binaries, configuration, identity dependencies, storage, and databases. Use continuous integration and continuous delivery (CI/CD) or custom automation to keep deployments synchronized.
Data replication Use appropriate OCI mechanisms, such as Data Guard, GoldenGate, block volume replication, object storage cross-region replication, and file storage replication.
Capacity The DR site must have enough capacity for mission-critical workloads. For example, if 50% of primary capacity supports mission-critical systems, size the DR site to carry that protected workload during failover.
Recovery time objective and recovery point objective Oracle provides tooling and best practices, but customers are responsible for DR architecture, testing, and achieved recovery time objective (RTO) and recovery point objective (RPO) outcomes.

We recommend planning DR between a pair of Dedicated Regions. For mission-critical workloads, DR from a Dedicated Region to an OCI commercial public region or to a non-OCI on-premises environment is not recommended because identity, storage, and database synchronization across those boundaries is limited.

For more information about Oracle Cloud Infrastructure (OCI) disaster recovery, see[Disaster Recovery](https://docs.oracle.com/iaas/Content/cloud-adoption-framework/disaster-recovery.htm).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
