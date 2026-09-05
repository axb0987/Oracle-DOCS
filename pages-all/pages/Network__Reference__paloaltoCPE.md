# Palo Alto
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm
- Fetched: 2026-09-05 02:42 CDT

# Palo Alto

This topic provides configuration for a Palo Alto device. The configuration was validated using PAN-OS version 8.0.0.

Palo Alto experience is required.
Important  
  

Oracle provides configuration instructions for a tested set of[vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/CPElist.htm). Use the correct configuration for the vendor and software version.

If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes.

If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of[supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/supportedIPsecparams.htm)and consult the vendor's documentation for help.

Oracle Cloud Infrastructure offersSite-to-Site VPN, a secure IPSec connection between an on-premises network and a virtual cloud network (VCN).

The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. IP addresses used in this diagram are only examples.
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

[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend.

Route-based IPSec uses an encryption domain with the following values:
- Source IP address: Any (0.0.0.0/0)
- Destination IP address: Any (0.0.0.0/0)
- Protocol: IPv4

If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.

[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

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

### Important Details About the Configuration Instructions
- Commits: For PAN to activate the configuration, you must perform the commit action after any configuration change.
- Example IP addresses: The example configuration uses IP addresses from class A 10.0.0.0/8 (RFC1918) and 198.51.100.0/24 (RFC5735). When you perform the configuration on the CPE, use the correct IP addressing plan for the networking topology.

The example configuration uses the following variables and values:
- Inside tunnel1 interface - CPE: 198.51.100.1/30
- Inside tunnel2 interface - CPE: 198.51.100.5/30
- Inside tunnel1 interface - Oracle: 198.51.100.2/30
- Inside tunnel2 interface - Oracle: 198.51.100.6/30
- CPE ASN: 64511
- On-premises network: 10.200.1.0/24
- VCN CIDR block: 10.200.0.0/24
- CPE public IP address: 10.100.0.100/24
- Oracle VPN headend (DRG) IP address 1: 10.150.128.1/32
- Oracle VPN headend (DRG) IP address 2: 10.150.127.1/32
- Tunnel number 1: tunnel.1
- Tunnel number 2: tunnel.2
- Exit interface: ethernet1/1

### About Using IKEv2

Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you[configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#using_ikev2), you must configure the CPE to use only IKEv2 and related IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm).

To use IKEv2, special variations of some steps are presented in the next section. Here is a summary of the special steps:
- For[task 2 (defining the ISAKMP peers)](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#task2), when you add the IKE gateway:
- On the General tab, for the Version , select IKEv2 only mode .
- On the Advanced Options tab, select the IKE crypto profile associated with the IKEv2 tunnel.
- For[task 5 (configuring the IPSec sessions)](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#task5), configure the proxy ID.

### Configuration Process

The following process includes BGP configuration for the IPSec connection. If you instead want to use static routing, perform tasks 1–5, and then skip to[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#config).

[Task 1: Configure the ISAKMP Phase 1 policy](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

In this example, the same ISAKMP policy is used for both tunnels.
- Go to Network , to IKE Crypto , and then select Add .
- 

Configure the parameters as shown in the next screenshot. For a list of the values, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm). If you're configuring Site-to-Site VPN for the Government Cloud, see[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params).
[

The next screenshot shows the final result for this task:
[

[Task 2: Define the ISAKMP peers](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

- Go to Network , to IKE Gateways , and then select Add .
- 

For peer 1, configure the parameters as shown in the next screenshots.
- 

On the General tab:
- Version: For IKEv1, select IKEv1 only mode . To use IKEv2, select IKEv2 only mode. Notice that if you're using IKEv2, later in[task 5](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#task5)you also add proxy IDs.
- Interface: The interface that owns the public IP address on the CPE. Change ethernet1/1 to the particular value for the networking topology.
- Peer IP addresses: The public IP address that Oracle assigned to the Oracle headend of the tunnel. Change the value to the correct IP address for the first tunnel.
- Pre-shared Key: The shared secret that Oracle automatically assigned during IPSec tunnel creation. If you want, you can[specify a different value](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#edit_shared_secret). Enter the same value here and in the Oracle Console.
- Local Identification and Peer Identification : The IKE IDs. The Local Identification is the CPE's public IP address. The Remote Identification is the Oracle VPN headend IP address for the first tunnel.
[
- 

On the Advanced Options tab, ensure that the values are set for the first peer according to the following screenshot.
[

If you're using IKEv2 instead, select the IKE crypto profile associated with the IKEv2 tunnel.
[
- 

For peer 2, configure the parameters as shown in the next screenshots.
- 

On the General tab:
- Version: For IKEv1, select IKEv1 only mode . To use IKEv2, select IKEv2 only mode . For IKEv2, notice that you also need to provide a proxy ID later in[task 5](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#task5).
- Interface: The interface that owns the public IP address on the CPE. Change ethernet1/1 to the particular value for the networking topology.
- Peer IP addresses: The public IP address that Oracle assigned to the Oracle headend of the tunnel. Change the value to the correct IP address for the second tunnel.
- Pre-shared Key: The shared secret that Oracle automatically assigned during IPSec tunnel creation. If you want, you can[specify a different value](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/workingwithIPsec.htm#edit_shared_secret). Enter the same value here and in the Oracle Console.
- Local Identification and Peer Identification : The IKE IDs. The Local Identification is the CPE's public IP address. The Remote Identification is the Oracle VPN headend IP address for the second tunnel.
[
- 

On the Advanced Options tab, ensure that the values are set for the second peer according to this screenshot:
[

If you're using IKEv2 instead, select the IKE crypto profile associated with the IKEv2 tunnel.
[

The next screenshot shows the final result for this task:
[

[Task 3: Define the IPSec Phase 2 policy](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

In this example, the same IPSec crypto profile is used for both tunnels.
- Go to Network , to IPSec Crypto , and then select Add .
- 

Configure the parameters as shown in the next screenshot.
[

The next screenshot shows the final result for this task:
[

[Task 4: Configure the virtual tunnel interfaces](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

- Go to Network , to Interfaces , to Tunnel , and then select Add .
- 

For peer 1, configure the parameters as shown in the next screenshots.
- 

On the Config tab, assign the interface according to the virtual router and security zone configuration. In this example, the default virtual router and ipsec_tunnel security zone are used.
[
- 

On the IPv4 tab, ensure that the values are set for the first peer according to the following screenshot. In this example, the IP address for the tunnel interface is ipsec_address_static1 = 198.51.100.1/30. Configure the tunnel IP address according to the networking IP addressing plan.
[
- 

For peer 2, configure the parameters as shown in the next screenshots.
- 

On the Config tab, assign the interface according to the virtual router and security zone configuration. In this example, the default virtual router and ipsec_tunnel security zone are used.
[
- 

On the IPv4 tab, ensure that the values are set for the second peer according to the following screenshot. In this example, the IP address for the tunnel interface is ipsec_address_static2 = 198.51.100.5/30. Configure the tunnel IP address according to the networking IP addressing plan.
[

The next screenshot shows the final result for this task:
[

[Task 5: Configure the IPSec sessions](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

- Go to Network , to IPSec Tunnels , and then select Add .
- 

For peer 1, configure the parameters on the General tab as shown in the next screenshot.

Notice that if you're using IKEv1, you don't need to add specific proxy IDs to the Proxy IDs tab. They're not needed for an IKEv1 route-based VPN configuration.

However, for IKEv2, do add proxy IDs to the Proxy IDs tab for better interoperability. Ensure that you also configured the IKE gateway to use IKEv2 earlier in[task 2](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#task2).
[
- 

For peer 2, configure the parameters on the General tab as shown in the next screenshot.

If you're using IKEv2, also add proxy IDs on the Proxy IDs tab.
[

[Task 6: Configure BGP over IPSec](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

Note  
  
To use static routing instead of BGP, skip task 6 and go to[Configuring Static Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#static_routing).

BGP over IPSec requires IP addresses on the tunnel interfaces on both ends.

The screenshots in this example use these subnets for the tunnel interfaces:
- 198.51.100.0/30
- CPE: 198.51.100.1/30
- DRG: 198.51.100.2/30
- 198.51.100.4/30
- CPE: 198.51.100.5/30
- DRG: 198.51.100.6/30

Replace the example values with the BGP IP addresses you specified in the Oracle Console for the inside tunnel interfaces.

This task consists of three subtasks, each with several steps.

[Subtask 6-a: Configure the BGP parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

- 

Go to Network , to Virtual Routers , to default , and then to BGP . This example uses the default virtual router. Also, the example uses 10.200.1.10 for the router ID and 64511 for the ASN. Use the correct virtual router based on your networking configuration, and use the correct router ID and ASN for your environment.
[
- 

On the General tab, configure the parameters as shown in the next screenshot.
[
- 

On the Advanced tab, configure the parameters as shown in the next screenshot.
[
- 

On the Peer Group tab:
- Add the first Peer Group, and under the Peer Group Name , add the first session. Add the BGP session with the DRG.
[
- 

For the first tunnel, on the Addressing tab, configure the parameters as shown in the next screenshot.Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. If you're configuring Site-to-Site VPN for the Government Cloud, see[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn).
[
- 

On the Connection Options tab, configure the parameters as shown in the next screenshot.
[
- 

On the Advanced tab, configure the parameters as shown in the next screenshot.
[
- 

On the Peer Group tab, add the second Peer Group, and under the Peer Group Name , add the second session. Add the BGP session with the DRG.
[
- 

For the second tunnel, on the Addressing tab, configure the parameters as shown in the next screenshot.
[
- 

On the Connection Options tab, configure the parameters as shown in the next screenshot.
[
- 

On the Advanced tab, configure the parameters as shown in the next screenshot.
[

The next screenshot shows the final Peer Group configuration:
[
- 

On the Import tab, configure the parameters as shown in the next screenshots. Here you configure tunnel.1 as the primary and tunnel.2 as the backup for the VCN route received from the DRG by way of BGP (10.200.0.0/24). From the BGP perspective, both tunnels are in the Established state.
- 

For the first rule, on the General tab, configure the parameters as shown in the next screenshot.
[
- 

On the Match tab, configure the parameters as shown in the next screenshot.
[
- 

On the Action tab, configure the parameters as shown in the next screenshot.
[
- 

For the second rule, on the General tab, configure the parameters as shown in the next screenshot.
[
- 

On the Match tab, configure the parameters as shown in the next screenshot.
[
- 

On the Action tab, configure the parameters as shown in the next screenshot.
[
- 

On the Export tab, configure the parameters as shown in the next screenshots. Here you configure a policy to force the DRG to prefer tunnel.1 for the returning path to the on-premises network CIDR (10.200.1.0/24).
- 

On the General tab, configure the parameters as shown in the next screenshot.
[
- 

On the Match tab, configure the parameters as shown in the next screenshot.
[
- 

On the Action tab, configure the parameters as shown in the next screenshot.
[

The next screenshot shows the final Export configuration:
[

Notice that no configuration is required for the Conditional Adv or Aggregate tabs.
- 

On the Redist Rules tab, configure the parameters as shown in the next screenshot. Here you announce the on-premises network CIDR in BGP.
[

[Subtask 6-b: Wait for the BGP sessions to establish and then check the BGP status](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

- 

Go to Network , to IPSec Tunnels , to the Virtual Router column, and then click Show Routes .
[
- 

Go to BGP , and then to the Peer tab to verify that the BGP session is established. Any other value means that the BGP session has not been established successfully and route exchange will not occur.
[
- 

On the Local RIB tab: The prefixes are received from the DRG, with tunnel.1 being preferred.
[
- 

On the RIB Out tab: The on-premises network CIDR is sent by way of BGP to DRG1 with as_path of 64511, and for DRG2, with an as_path of 64511, 64511. In this way, based on the BGP Best Path Algorithm, the route preferred by the DRG to reach the on-premises network CIDR uses the connection over tunnel.1.
[

[Subtask 6-c: Confirm that the BGP routes have been inserted in the route table](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#)

To view the routes, go to Routing , and then to the Route Table tab.
[

### Configuring Static Routing

Use the instructions here if the CPE doesn't support BGP over IPSec, or you don't want to use BGP over IPSec.

In this task, you configure static routes to direct traffic through the tunnel interfaces to reach the DRG and finally the VCN hosts.
- Follow tasks 1–5 in the preceding section.
- Configure static routes:
- Go to Network , to Virtual Routers , to default , to Static Routes , and then select Add .
- 

For Route 1, configure the parameters as shown in the next image.
[
- 

For Route 2, configure the parameters as shown in the next image.
[
- 

(Recommended) Enable ECMP for traffic sent through the two tunnels. The metric for both routes is set to 10. Here are some important notes about enabling ECMP:
- First check to see if the networking design supports ECMP.
- Enabling or disabling ECMP on an existing virtual router causes the system to restart the virtual router. The restart might cause existing sessions to be terminated.
- 

This example uses the default virtual router. Use the correct virtual router for this network environment.

To enable ECMP, go to Network , to Virtual Routers , to default , to Router Settings , to ECMP , and then select Enable .
[

Here are screenshots that show the final configuration after this task is complete:
[
[

### Changing the IKE Identifier

If the CPE is behind a NAT device with a private IP address on the exit interface that the tunnel interfaces use as the source, you must specify the public IP address of the NAT device as the local IKE ID. You can do this by setting the Local Identification value in the IKE Gateway configuration:
[

## Verification

To verify the IPSec tunnel status:
[

Use this command to verify the IKE SA:

```

```

Use this command to verify the IPSec tunnel configuration:

```

```

To verify the BGP status, look for Established :
[

To verify the BGP status from the command line:

```

```

To verify that the routes are installed in the route table:

```

```

A[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/ipsecmetrics.htm).

If you have issues, see[Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Troubleshoot/ipsectroubleshoot.htm)
