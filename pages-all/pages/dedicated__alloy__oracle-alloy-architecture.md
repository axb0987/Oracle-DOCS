# Oracle Alloy Architecture
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/oracle-alloy-architecture.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/oracle-alloy-architecture.htm#dcoc-content-body)

# Oracle Alloy Architecture

Oracle Alloy uses the same core OCI architecture constructs that are used in public OCI. These constructs include tenancies,[compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/Working_with_Compartments.htm), Identity and Access Management[(IAM)](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)policies, virtual cloud networks[(VCNs)](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm), dynamic routing gateways[(DRGs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm),[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm),[private peering](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm#uses), and[service APIs](https://docs.oracle.com/iaas/api/).

The operator can scale from an initial region to multiple regions within the same realm. The operator can also add deployment patterns, such as Reserved Regions, for specified end-customer deployments.

Resilience should be treated as a first-class architecture requirement. Qualified Oracle Alloy opportunities require operators to own and operate multiple data centers to support disaster recovery and backup strategies. Capacity planning is continuous and uses built-in tooling to forecast demand, monitor usage, and plan expansions.

The Dedicated Cloud Architecture section describes shared compute, storage, and networking architecture because the same underlying patterns apply to Oracle Alloy and OCI Dedicated Region.

## Implementation View

Oracle manages Oracle hardware, OCI platform services, software updates, service health monitoring, security operations for the cloud platform, and the tools that forecast and manage region capacity.

The operator provides the qualified data center environment. This environment includes space, power, cooling, facility access controls, and environmental readiness. The operator works with Oracle on deployment, growth planning, and operational readiness.

The operator owns the commercial and customer layer. This layer includes customer onboarding, contracts, branding, pricing, subscriptions, billing, service access governance, announcements, and Tier 1 support.

- [Oracle Alloy Architecture](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/oracle-alloy-architecture.htm#oracle-alloy-architecture)
- [Implementation View](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/oracle-alloy-architecture.htm#implementation-view)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
