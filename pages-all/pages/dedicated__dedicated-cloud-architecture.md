# Oracle Dedicated Cloud Architecture
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#dcoc-content-body)

# Oracle Dedicated Cloud Architecture

This information describes the architecture for Oracle Dedicated Cloud.

## Architecture Overview

Dedicated Cloud architecture includes the compute, storage, and networking patterns that apply to Oracle Alloy and OCI Dedicated Region. Both deployment types use core Oracle Cloud Infrastructure (OCI) constructs and connectivity patterns. Service consumption follows the OCI regional networking model, fault-domain design, and compute and storage service patterns.

Architecture planning must account for resilience, capacity growth, and operational supportability. Regions use standard OCI building blocks, such as tenancies,[compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/Working_with_Compartments.htm), identity and access management[(IAM)](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)policies, virtual cloud networks[(VCNs)](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm), dynamic routing gateways[(DRGs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm), FastConnect,[private peering](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm#uses),[public endpoints](https://docs.oracle.com/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm), and[service APIs](https://docs.oracle.com/iaas/api/).

Required network circuits must remain active for service delivery and region operations. An out-of-band path is required for last-resort recovery.

Storage design follows OCI service patterns for block, file, object, and database services. Align redundancy, replication, and retention planning with workload requirements and the broader disaster recovery (DR) design across regions.

## Network Connectivity

Dedicated Cloud networking combines the logical OCI networking model that is used in public cloud with dedicated physical connectivity for region operations and customer access. Operators and customers can use public endpoints, APIs,[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm), private peering, and Site-to-Site VPN patterns. Inter-region connectivity supports DR across multiple regions in a realm.

Internet transit connectivity is mandatory because Oracle uses it to operate, monitor, and manage the region remotely.[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm)provides dedicated connectivity between customer premises and the region for workload migration or split-workload architectures. Inter-region links provide connectivity between regions for recovery and cross-region designs. Required circuit types include Internet, inter-region, FastConnect, out-of-band, and data center operator access circuits. Each circuit type has a separate operational role.

The logical paths inside a VCN remain the same as in OCI public regions. DRGs provide private connectivity between[VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm)and external destinations. Internet gateways provide bidirectional Internet access. NAT gateways provide outbound-only Internet access. Service gateways provide private access to OCI service endpoints.

At the physical network layer, Dedicated Cloud deployments use separate functional paths for Internet and OCI operations, inter-region or backbone connectivity, customer access through[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm), out-of-band management, and data center operator access for onsite personnel. OCI gateways peer directly with diverse Internet providers and provide always-on distributed denial-of-service (DDoS) protection. Inter-region connectivity runs over the Oracle backbone, and Oracle-managed Layer 2 inter-region connections use MACsec. FastConnect supports private and public peering, with a MACsec option for customer-managed Layer 2 connections and an IPsec VPN option inside partner-managed Layer 3 connections. The out-of-band path uses a hardened Internet-connected server with terminal access to edge routers and access control lists (ACLs) that limit connections.

## Circuit Requirements

Use the following circuit requirements for architecture planning.

Type Use Speed Details
Internet Region management, public subnets, and service access 2 x 10 Gbps Direct Internet access with peering to the Oracle autonomous system number (ASN), diverse paths and providers, a full routing table, and management authority to Oracle's network operations center (NOC).
Inter-region Inter-region connectivity 2 x 10 Gbps or 2 x 100 Gbps Dense wavelength-division multiplexing (DWDM) or wave circuits with diverse paths and providers.
FastConnect Remote customer connectivity 1 Gbps, 10 Gbps, or 100 Gbps One or more providers, preferably with multiple connections to different routers.
Out-of-band Break-glass console access 1 Gbps direct Internet access Access to the edge with a /29 from provider space.
Data center operator access Data center operator onsite access 100 Mbps minimum direct Internet access Uses a /30 from provider space. Wi-Fi is preferred. Use tethering only when required, and keep tethering isolated from the regional network.

## FastConnect Connectivity Models

Use the following connectivity models to plan[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm)ownership and routing.

Model How the Model Works Notes
Tenant-dedicated connection A tenant can create multiple virtual circuits that terminate on different DRGs in that tenant's tenancy. This model is the default model for tenant-dedicated connectivity.
Connection owned by one tenant and distributed across tenants The tenant that owns the connection can distribute traffic to different tenant VCNs through cross-tenancy DRG attachment. This model requires route management by the connection-owning tenant and a high-trust relationship between all tenants.
FastConnect Partner provisioned A FastConnect Partner can maintain multiple connections to Oracle and provision virtual circuits directly to different tenancy DRGs. OCI networking constructs preserve traffic isolation between tenants. Dedicated realm owners or operators can onboard as FastConnect Partners to support multitenant connectivity over partner-owned or partner-managed cross-connects.

These models clarify that[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm)is not limited to a single tenancy pattern. The connectivity model must match the operating boundary, trust model, and routing responsibilities of the deployment.

## Firewall Requirements

When a customer or operator provides the Internet transit layer for Dedicated Region or Oracle Alloy, the region connects indirectly to the Internet through customer-managed network gateways instead of peering directly with Internet service providers. This customer-managed Internet transit model can apply region-wide firewall policies, ACLs, and other traffic restrictions between the Internet and hosted resources. Oracle management traffic must always pass without restriction.

Customer-managed firewall designs must preserve resilience and avoid single points of failure. Oracle expects at least two devices and two circuits on the customer side, with physical and logical redundancy, diversity, and dual peering sessions to separate gateways. Firewall clusters can operate in active-active or active-standby mode when they meet network demand and availability requirements.

If a customer acts as the regional Internet transit provider, the customer assumes responsibility for regional Internet availability. Oracle does not prescribe a specific firewall vendor or topology. Oracle validates that the connectivity meets required resiliency, routing, physical media, and operational access requirements.

Routing must use Border Gateway Protocol (BGP) with the customer ASN to establish external BGP (eBGP) peering with the Dedicated Region gateways. The region must receive a full Internet routing table, not only a default route. Oracle provides the public IPv4 and IPv6 address space assigned to the region. These addresses must not be translated through NAT44, NAT66, or other address-translation mechanisms. Customer firewalls and ACLs must implement Oracle management allowlist policies. Any announced allowlist changes must be applied within 72 hours.

This architecture gives the customer or operator control over the Internet security frontier and preserves Oracle operational access. Oracle provides networking requirements, management allowlist policies, public IPv4 and IPv6 address space for the region, operational support, and a Letter of Authorization for peering when applicable. The customer or operator is responsible for peering, route advertisement, point-to-point addressing outside the region, firewall and ACL implementation, and maintenance coordination when network changes could affect connectivity.

- [Oracle Dedicated Cloud Architecture](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#oci-dedicated-cloud-architecture)
- [Architecture Overview](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#architecture-overview)
- [Network Connectivity](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#network-connectivity)
- [Circuit Requirements](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#circuit-requirements)
- [FastConnect Connectivity Models](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#fastconnect-connectivity-models)
- [Firewall Requirements](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-cloud-architecture.htm#firewall-requirements)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
