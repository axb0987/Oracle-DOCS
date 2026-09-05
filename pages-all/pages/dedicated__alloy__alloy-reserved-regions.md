# Reserved Regions
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm
- Fetched: 2026-09-05 03:29 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#dcoc-content-body)

# Reserved Regions

Reserved Regions are multitenant regions reserved for the exclusive use of one named end customer within an existing Oracle Alloy realm. The end customer can still use the operator's other regions as disaster recovery sites.

## Deployment Model and Visibility

Reserved Regions are hidden regions in an Oracle Alloy realm. they are intended for the exclusive use of one named end customer and that customer's wholly owned subsidiaries. This deployment pattern is based on the Dedicated Region25 (DR25) model with as few as 3 base racks and can be physically located in the end-customer data center when that architecture is selected.

A Reserved Region remains multitenant within that customer boundary, but it is not visible to other customers or to the operator's other customer-facing regions. Customers in other Oracle Alloy regions cannot discover or subscribe to the Reserved Region.

## Disaster Recovery and Regional Relationships

Users in a Reserved Region can subscribe to the operator's other regions in the same realm to implement workload-level disaster recovery. This model preserves the operator's existing Oracle Alloy footprint as a recovery target while keeping the Reserved Region separate as the primary region.

If a workload requires a dedicated primary region and a dedicated secondary region, plan for a second Reserved Region or another explicitly designed failover architecture.

## Operational and Commercial Considerations

Operate a Reserved Region by using the same governance model, administration patterns, and support workflows that are used for the operator's other regions in the realm. Fusion order management controls which orders are assigned to which regions. Each Reserved Region can maintain its own regional rate card so that pricing can be tailored to that deployment.

Reserved Regions use a separate contractual commitment from the base Oracle Alloy deployment and are tied to a named end customer. The commitment is pooled with the existing Oracle Alloy usage commitment, but the Reserved Region remains a distinct deployment construct and cannot be upgraded into a full Oracle Alloy region.

## Typical Use Cases

Use Reserved Regions for regulated workloads that require stronger workload and data separation, capacity reservation for a strategic customer, smaller in-country or in-region deployments, or use of an existing customer data center as a primary or recovery site without a larger retrofit program.

## Networking

Networking follows the same architectural pattern for standard Alloy regions. This model includes mandatory internet transit for region operations, inter-region connectivity for cross-region recovery,[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm)for remote customer connectivity, an out-of-band path for emergency access, and data center operator access for onsite support.

- [Reserved Regions](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#reserved-regions)
- [Deployment Model and Visibility](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#deployment-model-and-visibility)
- [Disaster Recovery and Regional Relationships](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#disaster-recovery-and-regional-relationships)
- [Operational and Commercial Considerations](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#operational-and-commercial-considerations)
- [Typical Use Cases](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#typical-use-cases)
- [Networking](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/alloy-reserved-regions.htm#networking)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
