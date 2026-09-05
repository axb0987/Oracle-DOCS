# Disaster Recovery
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/disaster-recovery.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/disaster-recovery.htm#dcoc-content-body)

# Disaster Recovery

Disaster recovery protects Oracle Alloy workloads and data across regions and data center locations. Disaster recovery architecture should use multiple Oracle Alloy regions and multiple data center locations so that workloads, data, and operations can fail over in a controlled way.

A robust disaster recovery design uses at least two Oracle Alloy deployments in different geographies. Core building blocks can include remote peering between primary and disaster recovery sites, custom synchronization workflows for binaries and configuration, autoscaling at the recovery site, Oracle Data Guard or Oracle GoldenGate for database replication, block volume replication, object storage cross-region replication, and file storage replication.

Within one region, high availability follows the standard OCI model of one availability domain with three fault domains. Disaster recovery is a separate cross-region design concern. Disaster recovery protects applications and data from region failure rather than failure inside one region.

For more information about Oracle Cloud Infrastructure (OCI) disaster recovery, see[Disaster Recovery](https://docs.oracle.com/iaas/Content/cloud-adoption-framework/disaster-recovery.htm).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
