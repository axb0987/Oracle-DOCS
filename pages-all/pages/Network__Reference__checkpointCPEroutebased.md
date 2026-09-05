# Check Point: Route-Based
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm
- Fetched: 2026-09-05 02:42 CDT

# Check Point: Route-Based

This topic provides a route-based configuration for Check Point CloudGuard. The instructions were validated with Check Point CloudGuard version R80.20.
Important  
  

Oracle provides configuration instructions for a tested set of[vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/CPElist.htm). Use the correct configuration for the vendor and software version.

If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes.

If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of[supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/supportedIPsecparams.htm)and consult the vendor's documentation for help.

This topic is for route-based (VTI-based) configuration. If you instead want policy-based configuration, see[Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEpolicybased.htm). Policy-based routing is mentioned in passing in this article, we advise that you understand both methods.

Check Point experience is required. This topic doesn't include how to add Check Point CloudGuard Security Gateway to Check Point CloudGuard Security Manager. For more information about using Check Point products, see the Check Point documentation.
Important  
  

Oracle provides configuration instructions for a tested set of[vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/CPElist.htm). Use the correct configuration for the vendor and software version.

If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes.

If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of[supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/supportedIPsecparams.htm)and consult the vendor's documentation for help.

Oracle Cloud Infrastructure offers Site-to-Site VPN, a secure IPSec connection between an on-premises network and a virtual cloud network (VCN).

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

This section covers general important characteristics and limitations of Site-to-Site VPN to be aware of.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

### Asymmetric Routing

Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably.

When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.

For specific Oracle routing recommendations about how to force symmetric routing, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/overviewIPsec.htm#ipsec_routing).

### Route-Based or Policy-Based IPSec Connection

The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet.
Note  
  
Other vendors or industry documentation might use the term proxy ID, security parameter index (SPI) , or traffic selector when referring to SAs or encryption domains. Access Lists are also a common Cisco term for Encryption Domains.

There are two general methods for implementing IPSec tunnels:
- Route-based tunnels: Also called next-hop-based tunnels . A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel.
- Policy-based tunnels: The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.

The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections.

[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend.

Route-based IPSec uses an encryption domain with the following values:
- Source IP address: Any (0.0.0.0/0)
- Destination IP address: Any (0.0.0.0/0)
- Protocol: IPv4

If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.

[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

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

## CPE Configuration (Route-Based)

Important  
  

The configuration instructions in this section are provided by Oracle Cloud Infrastructure for this CPE. If you need support or further help, contact the CPE vendor's support directly.

The following figure shows the basic layout of the IPSec connection.
[

### About Using IKEv2

Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you[configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#using_ikev2), you must configure the CPE to use only IKEv2 and related IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm).

To use IKEv2, a variation on one of the tasks is presented in the next section. In[task 4](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#task4), when configuring encryption, select IKEv2 only for the encryption method.

### Redundancy with BGP Over IPSec

For redundancy, we recommend using BGP over IPSec. By default, if you have two connections of the same type (for example, two IPSec VPNs that both use BGP), and you advertise the same routes across both connections, Oracle prefers the oldest established route when responding to requests or starting connections. To force routing to be symmetric, We recommend using BGP and AS path prepending with routes to influence which path Oracle uses when responding to and starting connections. For more information, see[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Concepts/routingonprem.htm).

The Oracle DRG uses /30 or /31 as subnets for configuring IP addresses on the interface tunnels. Remember that the IP address must be part of Site-to-Site VPN's encryption domain and must be allowed in the firewall policy to reach the peer VPN through the interface tunnel. You might need to implement a static route through the tunnel interface for the peer IP address.

Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. If you're configuring Site-to-Site VPN for the Government Cloud, see[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params)and also[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn).

For the on-premises side, you can use a private ASN. Private ASNs are in the range 64512–65534.

[Task 1: InstallSite-to-Site VPN on Check Point CloudGuard Security Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

Prerequisite: Before starting, add Check Point CloudGuard Security Gateway to Check Point CloudGuard Security Manager. Also establish the Secure Internal Communication (SIC) so you can configure the IPSec tunnel by using the Check Point Smart Console. For instructions to add the Security Gateway to CloudGuard or to establish the SIC, see the Check Point documentation.
[
- 

Install the IPSec VPN module. We recommend that you also install the Monitoring module for traffic analysis.

[
- Select OK to save the changes.

[Task 2: Create the VTI interface from GAIA](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

In this task, you configure a VTI interface that passes traffic by using routing rules from the VTI interface to the newly created IPSec tunnel.
- Sign in to the GAIA portal using the Check Point CloudGuard Security Gateway public or private IP address.
- On the GAIA portal, select the Advanced view.
- Under Network Management , go to Network Interfaces .
- 

Select Add , and then select VPN Tunnel .
[
- 

Specify the following items:
- VPN Tunnel ID: A number that gets added to the VTI interface called vpnt*, where the asterisk is the VPN tunnel ID number specified . For VPN tunnel ID = 1, the interface is labeled vpnt1.
- 

Peer: The name of the interoperable device that you created earlier for the IPSec tunnel. In this case, the name is OCI-VPN_BGP1.
Important  
  
If the name you specify here doesn't match the name of the interoperable device, traffic doesn't flow through the IPSec tunnel.
- Numbered: Select Numbered to create a numbered interface.
- Local Address: The local IP address that was specified in the Oracle Console as the Inside Tunnel Interface - CPE .
- Remote Address: The remote IP address that was specified in the Oracle Console as the Inside Tunnel Interface - Oracle .
[
- 

Select OK .
- Under Network Management , go to IPv4 Static Routes .
- 

Specify the following items:
- Static route for the Oracle IP address: Add an IP address with /32 mask for the remote IP address that was specified in the Oracle Console as the Inside Tunnel Interface - Oracle .
- Static routes to the VCN subnets: If you're using static routing for this IPSec connection to Oracle, add at least one subnet for the Oracle VCN to be reached through the IPSec tunnel. The following screenshot shows a static route to 172.31.2.0/26. If you're using BGP for this IPSec connection to Oracle, skip this item because thoe routes are learned through BGP (see the next section).
[

Now all traffic with a specific destination learned from a static route passes through the newly created IPSec tunnel.
- 

Get the interfaces and verify that the VPN tunnel is in the list:
- In the Smart Console, go to Gateways &amp; Servers .
- Select the Check Point Security Gateways , and double-select.
- 

Under General Properties , on the Network Management page, select Get Interfaces .

The VPN tunnel interface should appear in the list.
- To force a route-based VPN to take priority, create an empty group and assign it to the VPN domain:
- On the VPN Domain page, select Manually defined , and then select Create empty group .
- Select New , select Group , and then select Simple Group .
- 

Enter an Object Name , and then select OK . Don't assign any objects to this empty group.
[

[Task 3: Create an interoperable device](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

Later, you create a VPN Community. Before you can, you must create an Interoperable Device that gets used in Check Point CloudGuard Security Gateway to define the Oracle DRG.
- 

Create the new interoperable device.
[
- 

On the General Properties page of the new interoperable device, add a name to identify the IPSec tunnel. Enter the IP address that Oracle assigned for the Oracle end of the tunnel when creating the IPSec connection.
[
- 

To force the route-based VPN to take priority, you must create an empty group and assign it to the VPN domain. To do that, on the Topology page, in the VPN Domain section, select Manually defined , and select the empty group.
- 

On the IPSec VPN page, you can optionally add the new interoperable device to an existing VPN Community. You can skip this step if you don't yet have any VPN Communities created.

Notice that you skip the Traditional mode configuration , because you define all the Phase 1 and Phase 2 parameters in the VPN Community in a later step. The VPN Community applies those parameters to all interoperable devices that belong to the VPN Community.
[
- 

On the Link Selection page, under Always use this IP address , select Main address , which was the address you specified when creating the interoperable device. You can use a specific IP address as the IKE ID.
[
- 

On the VPN Advanced page, select Use the community settings , which applies all the options and values in the VPN Community, including the Phase 1 and Phase 2 parameters.
[
- Select OK to save the changes.

[Task 4: Create a VPN community](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

- Go to Security Policies , and then from Access Tools , select VPN Communities .
- 

Create a Star Community .
[
- 

For the star community, add a name.
- 

On the Gateways page, select the values for Center Gateways and Satellite Gateways . This star community acts as a settings template for the interoperable devices you specify in Center Gateways and Satellite Gateways .
- Center Gateways : For the Check Point CloudGuard Security Gateway.
- Satellite Gateways : For the CPE that connects to the Oracle DRG for each IPSec tunnel.
[
- 

To allow traffic, go to Global Properties , and then VPN , and then Advanced .
[
[
- 

Select Enable VPN Directional Match in VPN Column . Later you create a security policy that uses a directional match condition to allow traffic to pass based on routing rules.
- Select OK .
- 

On the Encryption page, configure the Phase 1 and Phase 2 parameters that Oracle supports. For a list of those values, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm).

If you're configuring Site-to-Site VPN for the Government Cloud, see[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params).

Notice that to use IKEv2, for the Encryption Method , instead select IKEv2 only .
[
- 

On the Tunnel Management page, select Set Permanent Tunnels . We recommend that you:
- Select On all tunnels in the community to keep all the Oracle IPSec tunnels up all the time.
- In the VPN Tunnel Sharing section, select One VPN tunnel per Gateway pair .

The latter option generates only one pair of IPSec security associations (SAs), and each SA with only one security parameter index (SPI) (unidirectional).

When you use policy-based tunnels, every policy entry generates a pair of IPSec SAs, (also referred to as an encryption domain ).
Important  
  
The Oracle VPN headend can support multiple encryption domains, within limitations. See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for full details.

Oracle creates a route-based IPSec connection, which means that everything is routed through an encryption domain that has 0.0.0.0/0 (any) for local traffic and 0.0.0.0/0 (any) for remote traffic. For more information, see[Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/ipsecencryptiondomains.htm).
[
- 

On the Shared Secret page, select Use only Shared Secret for all external members , and add the shared secret that Oracle generated for the tunnel when creating the IPSec connection.

Oracle supports only shared secret keys. Note that you can[change the shared secret](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#edit_shared_secret)in the Oracle Console.
[
- Select OK to save the changes.

[Task 5: Create a security policy](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

- 

Go to Access Control , and then the Policy tab. Create specific security policies by using Directional Match Condition , which allows traffic to pass based on route tables. Set up the condition with these settings:
- Internal_Clear &gt; VPN Community created
- VPN Community created &gt; VPN Community created
- VPN Community created &gt; Internal_Clear

In this case, the VPN Community is OCI-DRG-BGP and the Internal_Clear is predefined by Check Point.
[
- Select OK to save the changes.
- 

Select Install Policy to apply the configuration.
[

[Task 6: Enable BGP](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

Perform the following steps for each tunnel.
- Go to Advanced Routing, and then BGP .
- 

Under BGP Global Settings , select Change Global Settings , and then add a router ID and local ASN.
[
- Select Save .

[Task 7: Redistribute routes into BGP](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#)

- Go to Advanced Routing, and then Route Distribution .
- 

Select Add Redistribution From , and then select Interface , which is for adding all connected subnets.
[
- 

In the Add Redistribution from Interface dialog, configure the following items:
- To Protocol: Select BGP AS 31898 . Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. If you're configuring Site-to-Site VPN for the Government Cloud, see[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn).
- Interface: Select all to advertise all connected subnets.
[
- Select Save .

Now the BGP session should be up and advertising and receiving subnets.

## Verification

The following CLI command verifies BGP peers and routing.

```

```

The following command verifies that you're receiving BGP routes.

```

```

The following command verifies the routes that are being advertised. In this example, replace &lt;remote_IP_address&gt; with the remote IP address that was specified in the Oracle Console as the Inside Tunnel Interface - Oracle

```

```

The following command verifies the routes that are being received.

```

```

Use options 2 and 4 in the following command to verify security associations (SAs).

```

```

A[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/ipsecmetrics.htm).

If you have issues, see[Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Troubleshoot/ipsectroubleshoot.htm)
