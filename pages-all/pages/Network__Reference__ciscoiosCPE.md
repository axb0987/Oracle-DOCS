# Cisco IOS
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm
- Fetched: 2026-09-05 02:42 CDT

# Cisco IOS

This topic provides a route-based configuration for a Cisco IOS device. The configuration was validated using a Cisco 2921 running IOS version 15.4(3)M3.
Important  
  

Oracle provides configuration instructions for a tested set of[vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/CPElist.htm). Use the correct configuration for the vendor and software version.

If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes.

If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of[supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/supportedIPsecparams.htm)and consult the vendor's documentation for help.

Oracle Cloud Infrastructure offersSite-to-Site VPN, a secure IPSec connection between an on-premises network and a virtual cloud network (VCN).

The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. IP addresses used in this diagram are for example purposes only.
[

## Best Practices

This section covers general best practices and considerations for using Site-to-Site VPN.

### Configure All Tunnels for Every IPSec Connection

Oracle deploys two IPSec headends for connections to provide high availability for mission-critical workloads. On the Oracle side, these two headends are on different routers for redundancy purposes. We recommend configuring all available tunnels for maximum redundancy. This is a key part of the "Design for Failure" philosophy.

### Have Redundant CPEs in On-Premises Network Locations

We recommend that each site that connects with IPSec to Oracle Cloud Infrastructure has redundant edge devices (also known as customer-premises equipment (CPE)). You add each CPE to the Oracle Console and create a separate IPSec connection between a dynamic routing gateway (DRG) and each CPE. For each IPSec connection, Oracle provisions two tunnels on geographically redundant IPSec headends. For more information, see the[Connectivity redundancy guide (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf).

### Routing Protocol Considerations

When you create a Site-to-Site VPN IPSec connection, it has two redundant IPSec tunnels. Oracle encourages you to configure the CPE to use both tunnels (if the CPE supports it). In the past, Oracle created IPSec connections that had up to four IPSec tunnels.

The following three routing types are available, and you select the routing type separately for each tunnel in the Site-to-Site VPN:

- BGP dynamic routing: The available routes are learned dynamically through BGP. The DRG dynamically learns the routes from the on-premises network. On the Oracle side, the DRG advertises the VCN's subnets.
- Static routing: When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically.
- Policy-based routing: When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically.

For more information about routing with Site-to-Site VPN, including Oracle recommendations on how to manipulate the BGP best path selection algorithm, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/overviewIPsec.htm#ipsec_routing).

### Other Important CPE Configurations

Ensure that access lists on the CPE are configured correctly to not block necessary traffic from or to Oracle Cloud Infrastructure.

If you have several tunnels up simultaneously, you might experience asymmetric routing. To account for asymmetric routing, ensure that the CPE is configured to handle traffic coming from the VCN on any of the tunnels. For example, you need to disable ICMP inspection, configure TCP state bypass . For more details about the appropriate configuration, contact the CPE vendor's support. To configure routing to be symmetric, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/overviewIPsec.htm#ipsec_routing).

## Caveats and Limitations

This section covers general important characteristics and limitations of Site-to-Site VPN to be aware of. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

### Asymmetric Routing

Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably.

When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.

For specific Oracle routing recommendations about how to force symmetric routing, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/overviewIPsec.htm#ipsec_routing).

### Route-Based or Policy-Based Site-to-Site VPN

The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet.
Note  
  
Other vendors or industry documentation might use the term proxy ID, security parameter index (SPI) , or traffic selector when referring to SAs or encryption domains. Access Lists are also a common Cisco term for Encryption Domains.

There are two general methods for implementing IPSec tunnels:
- Route-based tunnels: Also called next-hop-based tunnels . A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel.
- Policy-based tunnels: The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.

The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections.

[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#)

If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend.

Route-based IPSec uses an encryption domain with the following values:
- Source IP address: Any (0.0.0.0/0)
- Destination IP address: Any (0.0.0.0/0)
- Protocol: IPv4

If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.

[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#)

When you use policy-based tunnels, every policy entry (a CIDR block on one side of the IPSec connection) that you define generates an IPSec security association (SA) with every eligible entry on the other end of the tunnel. This pair is referred to as an encryption domain .

In this diagram, the Oracle DRG end of the IPSec tunnel has policy entries for three IPv4 CIDR blocks and one IPv6 CIDR block. The on-premises CPE end of the tunnel has policy entries two IPv4 CIDR blocks and two IPv6 CIDR blocks. Each entry generates an encryption domain with all possible entries on the other end of the tunnel. Both sides of an SA pair must use the same version of IP. The result is a total of eight encryption domains.
[
Important  
  

If the CPE only supports policy-based tunnels, be aware of the following restrictions.
- Site-to-Site VPN supports multiple encryption domains, but has an upper limit of 50 encryption domains.
- If you had a situation similar to the prior example and only configured three of the six possible IPv4 encryption domains on the CPE side, the link would be listed in a "Partial UP" state because all possible encryption domains are always created on the DRG side.
- Depending on when a tunnel was created you might not be able to edit an existing tunnel to use policy-based routing and might need to replace the tunnel with a new IPSec tunnel.
- The CIDR blocks used on the Oracle DRG end of the tunnel can't overlap the CIDR blocks used on the on-premises CPE end of the tunnel.
- An encryption domain must always be between two CIDR blocks of the same IP version.

### If the CPE Is Behind a NAT Device

In general, the CPE IKE identifier configured on the on-premises end of the connection must match the CPE IKE identifier that Oracle is using. By default, Oracle uses the CPE's public IP address, which you provide when you create the CPE object in the Oracle Console. However, if a CPE is behind a NAT device, the CPE IKE identifier configured on the on-premises end might be the CPE's private IP address, as shown in the following diagram.
[
Note  
  
Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as cpe.example.com . For instructions, see[Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#edit_cpe_ike_id).

## Supported IPSec Parameters

For a vendor-neutral list of supported IPSec parameters for all regions, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/supportedIPsecparams.htm).

The Oracle BGP ASN for the commercial cloud realm is 31898. If you're configuring Site-to-Site VPN for the US Government Cloud, see[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params)and also[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn). For the Oracle UK Sovereign Cloud, see[Regions](https://docs.oracle.com/iaas/Content/gov-cloud/govuksouth.htm#Regions).

## CPE Configuration

Important  
  

The configuration instructions in this section are provided by Oracle Cloud Infrastructure for this CPE. If you need support or further help, contact the CPE vendor's support directly.

The following figure shows the basic layout of the IPSec connection.
[

The configuration template was validated using a Cisco 2921 running IOS version 15.4(3)M3. The template provides information for each tunnel that you must configure. We recommend setting up all configured tunnels for maximum redundancy.

The configuration template refers to these items that you must provide:
- CPE public IP address: The internet-routable IP address that's assigned to the external interface on the CPE. You or the Oracle administrator provides this value to Oracle when creating the CPE object in the Oracle Console.
- Inside tunnel interface (required if using BGP): The IP addresses for the CPE and Oracle ends of the inside tunnel interface. You provide these values when creating the IPSec connection in the Oracle Console.
- BGP ASN (required if using BGP): The on-premises BGP ASN.

In addition, you must:
- Configure internal routing that routes traffic between the CPE and the local network.
- Ensure that you allow traffic between the CPE and the Oracle VCN.
- Identify the IPSec profile used (the following configuration template references this group policy as`oracle-vpn`).
- Identify the transform set used for the crypto map (the following configuration template references this transform set as`oracle-vpn-transform`).
Important  
  

This following configuration template from Oracle Cloud Infrastructure is a starting point for what you need to apply to the CPE. Some parameters referenced in the template must be unique on the CPE, and the uniqueness can only be found by accessing the CPE. Ensure the parameters are valid on the CPE and don't overwrite any previously configured values. In particular, ensure these values are unique:
- Policy names or numbers
- Interface names
- 

Keyrings
- Access list numbers (if applicable)

Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you[configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#using_ikev2), you must configure the CPE to use only IKEv2 and related IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm).

There are separate configuration templates for IKEv1 and IKEv2.

[IKEv1 Configuration Template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#)

[View the IKEv1 configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../non-dita/vpn_cpe_ciscoios.txt)

```

```

[IKEv2 Configuration Template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#)

[View the IKEv2 configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../non-dita/vpn_cpe_ciscoios_ikev2.txt)

```

```

## Verification

The following IOS commands are included for basic troubleshooting.

Use the following command to verify that ISAKMP security associations are being built between the two peers.

```

```

Use the following command to verify the status of all BGP connections or neighbors.

```

```

Use the following command to verify the route table.

```

```

A[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/ipsecmetrics.htm).

If you have issues, see[Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Troubleshoot/ipsectroubleshoot.htm)
