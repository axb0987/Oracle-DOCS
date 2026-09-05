# CPE Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm
- Fetched: 2026-09-05 02:43 CDT

# CPE Configuration

This topic is for network engineers. It explains how to configure the on-premises device (the customer-premises equipment, or CPE) at the on-premises end of Site-to-Site VPN so traffic can flow between an on-premises network and Virtual Cloud Network (VCN). See these related topics:
- [Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/landing.htm): For general information about the parts of a VCN
- [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm): For various topics about IPSec VPNs
- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm): For a list of CPE devices Oracle has verified

The following figure shows the basic layout of Site-to-Site VPN's IPSec connection using the internet.[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)is similar, but the traffic only traverses a private virtual circuit.
[

## Requirements and Prerequisites

Here are the requirements and prerequisites to be aware of before moving forward.

### Routing Considerations

For important details about routing for Site-to-Site VPN see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from a VCN to an on-premises network can use any tunnel that's "up" on a device. Configure firewalls as appropriate. Otherwise, ping tests or application traffic across the connection don't work reliably.

If you use BGP dynamic routing with Site-to-Site VPN, you can configure routing so that Oracle prefers one tunnel over the other.

To use[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectsecurity.htm#ipsec)you can't update a CPE object to add that functionality. Instead, support must be established at the CPE's initial setup. You also can't have the IPSec tunnels and virtual circuits for this connection use the same DRG route tables.

Note that the[Cisco ASA policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ciscoasaCPE.htm)uses a single tunnel.

### Creation of Cloud Network Components

You or someone in your organization must have already used the Oracle Console to create a VCN and an IPSec connection, which consists of two or more IPSec tunnels for redundancy. You must gather the following information about those components:
- VCN OCID: The VCN[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)is a unique Oracle Cloud Infrastructure identifier that has a UUID at the end. You can use this UUID or any other string that helps you identify this VCN in the device configuration and doesn't conflict with other object-group or access-list names.
- VCN CIDR
- VCN CIDR subnet mask
- 

For each IPSec tunnel:
- The IP address of the Oracle IPSec tunnel endpoint (the VPN headend)
- The shared secret

### Information About the On-premises CPE Device

You also need some basic information about the inside and outside interfaces of the on-premises device (CPE). For a list of the required information for a particular CPE, see the links in this list:[Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm).

By default, NAT-T is enabled on all Site-to-Site VPN IPSec tunnels. We recommend leaving NAT-T enabled when configuring Site-to-Site VPN to OCI.

If the CPE is behind a NAT device, you can provide Oracle with the CPE's IKE identifier. For more information, see[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components).

A single CPE object public IP can have up to 8 IPSec connections.

### Route-Based Compared to Policy-Based IPSec

The Oracle VPN headends use route-based tunnels, but can work with policy-based tunnels with some caveats. See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for full details.

## Site-to-Site VPN Best Practices

- Configure all tunnels for every IPSec connection: Oracle deploys several IPSec headends for connections to provide high availability for mission-critical workloads. Configuring all the available tunnels is a key part of the "Design for Failure" philosophy. (Exception:[Cisco ASA policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ciscoasaCPE.htm), which uses a single tunnel.)
- Have redundant CPEs in on-premises locations: We recommend that each site that connects with IPSec to Oracle Cloud Infrastructure have redundant CPE devices. You add each CPE to the Oracle Cloud Infrastructure Console and create a separate IPSec connection between a Dynamic Routing Gateway (DRG) and each CPE. For each IPSec connection, Oracle provisions two tunnels on geographically redundant IPSec headends. Oracle might use any tunnel that's "up" to send traffic back to an on-premises network. For more information, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
- 

Consider backup aggregate routes: If you have several sites connected by means of Site-to-Site VPN to Oracle Cloud Infrastructure, and those sites are connected to on-premises backbone routers, consider configuring the IPSec connection routes with both the local site aggregate route and a default route.

Note that the DRG routes learned from the IPSec connections are only used by traffic you route from a VCN to the DRG. The default route is only used by traffic sent to the DRG whose destination IP address doesn't match the more specific routes of any of the tunnels.

## Confirming the Status of the Connection

After you configure the IPSec connection, you can test the connection by creating a Compute instance into the VCN and then pinging it from an on-premises network. For information about creating a Compute instance, see[Launching an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). To ping the instance, the VCN's security rules must[allow ping traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm#ping).

You can get the status of the IPSec tunnels in the API or Console. For instructions, see[Getting an IPSec Tunnel's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm).

## Device Configurations

For links to the specific configuration information for each verified CPE device, see[Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm)
