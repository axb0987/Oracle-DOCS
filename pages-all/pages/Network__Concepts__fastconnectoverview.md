# FastConnect Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm
- Fetched: 2026-09-05 02:41 CDT

# FastConnect Overview

Learn how FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.

Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between an on-premises data center and Oracle Cloud Infrastructure. FastConnect provides higher-bandwidth options, and a more reliable and consistent networking experience compared to internet-based connections.

## Uses for FastConnect

When you set up FastConnect virtual circuits, you can decide to use private peering or public peering . The details vary depending on whether you use a[FastConnect partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#set_up_vc), a[third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_vc), or[colocation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#task_set_up_vc).
- Private peering: To extend existing infrastructure into a virtual cloud network (VCN) in Oracle Cloud Infrastructure (for example, to implement a hybrid cloud, or a lift and shift scenario). Communication across the connection is with IPv4 private addresses (typically RFC 1918).
- Public peering: To access public services in Oracle Cloud Infrastructure without using the internet. For example, Object Storage, the Oracle Cloud Infrastructure Console and APIs, or public load balancers in a VCN. Communication across the connection is with IPv4 public IP addresses. Without FastConnect, the traffic destined for public IP addresses would be routed over the internet. With FastConnect, that traffic goes over a leased physical connection. The services available with FastConnect public peering are the same as the[Service Gateway: Supported Cloud Services](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/). For a list of the regions with address ranges (routes) that Oracle advertises by default for each of the four markets, see[FastConnect Public Peering Advertised Routes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm). You can adjust the routes advertised to an on-premises network using the[route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)settings for a connection.

In general it's assumed you use private peering, and you might also use public peering on another virtual circuit. Most of this documentation is relevant to both, with specific details called out for private compared with public.

If you decide to have several paths from an on-premises network to Oracle, see[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm).

IPv6 addressing is supported for all commercial and government regions. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm).
Note  
  
You can connect two VCNs in different regions using FastConnect colocation, with traffic between regions using that link rather than the Oracle backbone. A Layer 3 device is required to implement this, even for a layer 2 connection. Details of this use case aren't available, but are similar to[Connecting Oracle Cloud Infrastructure to Amazon VPC with Megaport Cloud Router](https://blogs.oracle.com/cloud-infrastructure/connecting-oracle-cloud-infrastructure-to-amazon-vpc-with-megaport-cloud-router)or[Connecting Oracle Cloud Infrastructure to Google Cloud Platform with Equinix Network Edge Cloud Router](https://blogs.oracle.com/cloud-infrastructure/connecting-oracle-cloud-infrastructure-to-google-cloud-platform-with-equinix-network-edge-cloud-router).

## How and Where to Connect

With FastConnect, select among the different connectivity models.

### Oracle Partners

- List of[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/).
- Port speeds in 1 Gbps, 10 Gbps, or 100 Gbps increments.
- Instructions for integrating:[FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm).

### Third-Party Provider

- Port speed of 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps per cross-connect.
- Instructions for integrating:[FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm).

### Colocation with Oracle in an Oracle Cloud Infrastructure FastConnect Location

- Colocation is available at[FastConnect Locations in North America](https://www.oracle.com/cloud/networking/fastconnect/partners/#na-locations),[FastConnect Locations in LATAM](https://www.oracle.com/cloud/networking/fastconnect/partners/#latam-locations),[FastConnect Locations in EMEA](https://www.oracle.com/cloud/networking/fastconnect/partners/#emea-locations), and[FastConnect Locations in APAC](https://www.oracle.com/cloud/networking/fastconnect/partners/#apac-locations).
- Port speed of 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps per cross-connect.
- Instructions for integrating:[FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm).

The following table summarizes several important requirements for each connectivity model.

Requirement With Oracle Partner With Third-Party Provider Colocation with Oracle
Routing requirements[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)
BGP support[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)
Layer 3 support[Recommended](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)[Recommended](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)[Recommended](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)
Obtain a Letter of Authority (LOA) from Oracle NOT APPLICABLE[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm)Yes
Network connectivity[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)NOT APPLICABLE
Cross-connect[Yes (from the partner)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm)
Redundant network connectivity[Recommended](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)[Recommended](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)[Recommended](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)
Cloud connectivity solution architecture support Recommended Recommended Recommended
FastConnect SKU Yes Yes Yes
Oracle Cloud Infrastructure Console user login (IAM policy unique setup)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)[Yes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements)
Tenancy established[Yes](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm)[Yes](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm)[Yes](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm)

## Concepts

Here are some important concepts to understand (also see the following diagrams): FastConnect The general concept of a connection between an existing network and Oracle Cloud Infrastructure over a private physical network instead of the internet. FastConnect location A specific Oracle data center where you can connect to Oracle Cloud Infrastructure. METRO AREA A geographical area (for example, Ashburn) with several FastConnect locations. All locations in a metro area connect to the same set of availability domains for resiliency in case of failure in a single location. ORACLE PARTNER A network service provider that has integrated with Oracle in a FastConnect location. See the list of[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/). If the provider is in the list, see[FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm). THIRD-PARTY PROVIDER A network service provider that isn't on the list of[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/). If you have a third-party provider and want to use FastConnect, see[FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm). COLOCATION The situation where your equipment is deployed into a FastConnect location. If your network service provider isn't on the list of[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/), you must colocate. CROSS-CONNECT In a colocation or third-party provider scenario, this is the physical cable connecting your existing network to Oracle in the FastConnect location. CROSS-CONNECT GROUP In a colocation or third-party provider scenario, this is a link aggregation group (LAG) that contains at least one cross-connect. You can add more cross-connects to a cross-connect group as your bandwidth needs increase. This is applicable only for colocation. Virtual Cloud Network (VCN) Your virtual network in Oracle Cloud Infrastructure. You can use a VCN to extend your infrastructure into the cloud. For more information, see[VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/VCNs.htm). Dynamic Routing Gateway (DRG) A virtual edge router attached to your VCN. Necessary for private peering. The DRG is a single point of entry for private traffic coming in to your VCN, whether it's over FastConnect or a[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingIPsec.htm)link. After creating the DRG, you must attach it to your VCN and add a route for the DRG in the VCN's route table to enable traffic flow. Instructions for everything are included in the sections that follow. VIRTUAL CIRCUIT An isolated network path that runs over one or more physical network connections to provide a single, logical connection between the edge of your existing network and Oracle Cloud Infrastructure. Private virtual circuits support private peering, and public virtual circuits support public peering (see[Uses for FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#uses)). Each virtual circuit is made up of information shared between you and Oracle (and also a partner if you're connecting through an Oracle partner). You could have many private virtual circuits, for example, to isolate traffic from different parts of your organization (one virtual circuit for 10.0.1.0/24; another for 172.16.0.0/16), or to provide redundancy. BGP SESSION

Border Gateway Protocol (BGP) exchanges routing and reachability information between autonomous systems (AS). A session between the two systems is established and routing information on both sides is advertised to the other side, while periodic messages are sent to verify that both sides are available to exchange traffic. If the BGP session isn't established or goes down, traffic can't pass between the two systems even if the devices and physical connections are functioning correctly. When you deactivate a virtual circuit, its associated BGP session is ended, and has to be rebuilt when you re-activate the virtual circuit. BIDIRECTIONAL FORWARDING DETECTION

Bidirectional Forwarding Detection (BFD) is a method for detection of failures in the path between adjacent networks. It provides an additional mechanism that can be used to verify connectivity between a pair of devices, but doesn't exchange route information. BFD provides faster failover than is possible with BGP timers. Short BGP timers can also lead to false positives unlike fast BFD. ORACLE EDGE The Oracle edge for a given connection consists of two distinct constructs: a physical device and a logical device. PHYSICAL DEVICE This is the FastConnect device that terminates the physical connection, also called a cross connect or cross connect group. LOGICAL DEVICE This is the FastConnect device that terminates the logical connection, also called a virtual circuit. This device might not be the same device that terminates the physical connection. LETTER OF AUTHORIZATION (LOA)

An official letter that provides written authorization to connect to another party within a data center. The letter includes specific information about where a circuit should be terminated to a telecommunications carrier or other Z-end party's interconnection environment. An LoA is required to accurately and efficiently configure[FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm)and[FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm).

## Basic Network Diagrams

The diagrams in this section introduce the basic logical and physical connections involved in FastConnect. Details specific to private peering compared with public peering are called out.

### General Concepts of FastConnect

The following diagrams illustrate the two ways to connect to Oracle with FastConnect. In both cases, the connection goes between the edge of an existing network and Oracle.

With colocation:
[

With an Oracle Partner or third-party provider:
[

### Physical Connection

The next two diagrams give more detail about the physical connections. They also show the metro area that contains the FastConnect location, and a VCN within an Oracle Cloud Infrastructure region.

The first diagram shows the colocation scenario, with a physical connection to Oracle within the FastConnect location (called a cross-connect). The physical device is the Oracle edge device that physically connects to a edge device or to partner/provider networks.

With colocation:
[

The next diagram shows a scenario with either an Oracle partner or third-party provider. It shows a physical connection to the provider, and the provider's physical connection to Oracle within the FastConnect location. In either case, this physical connection is a cross-connect.

With an Oracle Partner or third-party provider:
[

### Logical Connection: Private Virtual Circuit

The next two diagrams show a private virtual circuit, which is a single, logical connection between a edge and Oracle Cloud Infrastructure by way of a DRG. Traffic is destined for private IP addresses in a VCN.

With colocation:
[

With an Oracle Partner or third-party provider:
[

### Logical Connection: Public Virtual Circuit

A public virtual circuit gives a existing network access to Oracle services in Oracle Cloud Infrastructure. For example, Object Storage, the Oracle Cloud Infrastructure Console and APIs, and public load balancers in a VCN. All communication across a public virtual circuit uses[public IP addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingpublicIPs.htm#overview). The services available with FastConnect public peering are the same as the[Service Gateway: Supported Cloud Services](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/). For a list of the public IP address ranges (routes) that Oracle advertises, see[FastConnect Public Peering Advertised Routes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm). You can select the way this access is structured using[Route Filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering).

The first diagram shows the colocation scenario with both a private virtual circuit and a public virtual circuit. Notice that the DRG isn't involved with the public virtual circuit, only the private virtual circuit.

With colocation:
[

The next diagram shows the scenario with either an Oracle partner or third-party provider.

With an Oracle Partner or third-party provider:
[

Here are a few basics to know about public virtual circuits:
- You select which of a organization's public IP prefixes you want to use with the virtual circuit. All prefix sizes are allowed. Oracle verifies a organization's ownership of each prefix before sending any traffic for it across the connection. Oracle's verification for a specific prefix can take up to three business days. You can get the status of the verification of each prefix in the Oracle Console or API. Oracle begins advertising the Oracle Cloud Infrastructure public IP addresses across the connection only after successfully verifying at least one of a public prefixes.
- Configure a firewall rules to allow traffic coming from the[Oracle public IP addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm).
- 
An existing network can receive advertisements for Oracle's public IP addresses through several paths (for example: FastConnect and the internet service provider). Ensure that FastConnect has higher preference than the ISP. You must configure the edge appropriately so that traffic uses the preferred path to receive the benefits of FastConnect. This is important if you decide to also set up the existing network with[private access to Oracle services](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/transitroutingoracleservices.htm). For important information about path preferences, see[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/routingonprem.htm).
- You can add or remove public IP prefixes at any time by editing the virtual circuit. If you add a prefix, Oracle first verifies a company's ownership before advertising it across the connection. If you remove a prefix, Oracle stops advertising the prefix within a few minutes of a editing the virtual circuit.
- Consider FastConnect public peering as an untrusted interface, and put in place firewalls and other access controls as you would for any network interface connected to the Internet. See[Security considerations for FastConnect public peering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#security-considerations)for more information.

### Oracle Partner or Third-party Provider Scenario: BGP Session to Either Oracle or the Oracle Partner

This section is applicable if you're using FastConnect through an Oracle partner or third-party provider. A Border Gateway Protocol (BGP) session is established from a edge, but where it goes depends on which Oracle partner you use.
Tip  
  
For simplicity, the following diagrams show only a private virtual circuit. However, the location of the BGP session is the same for a public virtual circuit.

With some Oracle partners, the BGP session goes from a edge to Oracle, as shown in the following diagram. When setting up the virtual circuit with Oracle, you're asked to provide basic BGP peering information (see[General Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)).

To Oracle:
[

With other Oracle partners, a BGP session goes from a edge to the partner's, as shown in the following diagram. When setting up the virtual circuit with Oracle, you're NOT asked for any BGP session information. Instead, you share BGP information with a Oracle partner. Notice the separate BGP session that the partner establishes with Oracle.

To the Oracle Partner:
[

## To use FastConnect if you don't own a Public ASN or Public IP Address

If you use a Public ASN or Public IP Address loaned or leased from a third-party source, the third-party source must provide a Letter of Authorization (LOA) on your behalf before Oracle can comple FastConnect configuration.

The following additional steps are required to obtain approval when configuring public peering virtual connections:
- 

Obtain an LOA from the third-party source that authorizes the Customer to use the Public ASN and or Public IP address. The LOA must contain:
- Customer Name approved to the use the Public IP Address and Public ASN
- The range of the Public IP Addresses and or the Public ASN must be explicitly listed
- The third-party source who owns the Public IP Addresses and or the Public ASN
- Third-party source authorization authority signatory
- Contact email, phone number and address of third-party source
- Your enterprise's contact email and phone number
- Date of authorization and validity
- Using the Console, open a service request on the tenancy and region where you want to use the third-party provided Public ASN and Public IP Address.
- Attach the LOA to the service request.

After the service request is opened and the LOA is approved, Oracle authorizes the use of the Public ASN and or Public IP Address.

## FastConnect with Access to Multiple VCNs

You can use a single FastConnect to access multiple VCNs. Different network scenarios are available depending on your needs and which FastConnect connectivity model you use. For more information, see these topics:
- [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/transitrouting.htm): This scenario can be used with either FastConnect or Site-to-Site VPN. It involves a single DRG, and multiple VCNs in a hub-and-spoke layout.
- [FastConnect with Multiple DRGs and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectmultipledrgs.htm): This scenario can be used only with FastConnect, and only if you're using a third-party provider or colocated with Oracle. It involves multiple DRGs and private virtual circuits.

## What's Next?

See these topics to get started:
- [FastConnect Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm)
- [FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)
- [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm)
- [FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm)
- [FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm)
- [FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm)
