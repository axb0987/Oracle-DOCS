# Strongswan
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm
- Fetched: 2026-09-05 02:43 CDT

# Strongswan

[Strongswan](https://www.strongswan.org/)is an open source IPSec-based VPN solution. Most Linux distributions include Strongswan or make it easy to install. You can install it on hosts in either an on-premises network or a a cloud provider network.

This topic provides configuration for CPE running Strongswan. The Strongswan 5.x branch supports both the IKEv1 and IKEv2 key exchange protocols with the native NETKEY IPSec stack of the Linux kernel.
Important  
  

Oracle provides configuration instructions for a tested set of[vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm). Use the correct configuration for the vendor and software version.

If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes.

If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of[supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm)and consult the vendor's documentation for help.

Oracle Cloud Infrastructure offers Site-to-Site VPN, a secure IPSec connection between an on-premises network and a virtual cloud network (VCN).

The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. IP addresses used in this diagram are an example only.

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

For more information about routing with Site-to-Site VPN, including Oracle recommendations on how to manipulate the BGP best path selection algorithm, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/overviewIPsec.htm#ipsec_routing).

### Other Important CPE Configurations

Ensure that access lists on the CPE are configured correctly to not block necessary traffic from or to Oracle Cloud Infrastructure.

If you have several tunnels up simultaneously, you might experience asymmetric routing. To account for asymmetric routing, ensure that the CPE is configured to handle traffic coming from the VCN on any of the tunnels. For example, you need to disable ICMP inspection, configure TCP state bypass . For more details about the appropriate configuration, contact the CPE vendor's support. To configure routing to be symmetric, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/overviewIPsec.htm#ipsec_routing).

## Caveats and Limitations

This section covers general important characteristics and limitations of Site-to-Site VPN to be aware of. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

### Asymmetric Routing

Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably.

When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.

For specific Oracle routing recommendations about how to force symmetric routing, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/overviewIPsec.htm#ipsec_routing).

### Route-Based or Policy-Based Site-to-Site VPN

The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet.
Note  
  
Other vendors or industry documentation might use the term proxy ID, security parameter index (SPI) , or traffic selector when referring to SAs or encryption domains. Access Lists are also a common Cisco term for Encryption Domains.

There are two general methods for implementing IPSec tunnels:
- Route-based tunnels: Also called next-hop-based tunnels . A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel.
- Policy-based tunnels: The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.

The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections.

### If the CPE Is Behind a NAT Device

In general, the CPE IKE identifier configured on the on-premises end of the connection must match the CPE IKE identifier that Oracle is using. By default, Oracle uses the CPE's public IP address, which you provide when you create the CPE object in the Oracle Console. However, if a CPE is behind a NAT device, the CPE IKE identifier configured on the on-premises end might be the CPE's private IP address, as shown in the following diagram.
[
Note  
  
Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as cpe.example.com . For instructions, see[Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/workingwithIPsec.htm#edit_cpe_ike_id).

## Supported IPSec Parameters

For a vendor-neutral list of supported IPSec parameters for all regions, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

The Oracle BGP ASN for the commercial cloud realm is 31898. If you're configuring Site-to-Site VPN for the US Government Cloud, see[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params)and also[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn). For the Oracle UK Sovereign Cloud, see[Regions](https://docs.oracle.com/iaas/Content/gov-cloud/govuksouth.htm#Regions).

## CPE Configuration

Important  
  

The configuration instructions in this section are provided by Oracle Cloud Infrastructure for this CPE. If you need support or further help, contact the CPE vendor's support directly.

The following figure shows the basic layout of the IPSec connection.

[

### Default Strongswan Configuration Files

The default Strongswan installation creates the following files:
- `etc/strongswan/ipsec.conf`: The root of the Strongswan configuration.
- `/etc/strongswan/ipsec.secrets`: The root of the location where Strongswan looks for secrets (the tunnel pre-shared keys).

The default`etc/strongswan/ipsec.conf`file includes this line:

```

```

The default`etc/strongswan/ipsec.secrets`file includes this line:

```

```

The preceding lines automatically merge all the`.conf`and`.secrets`files in the`/etc/strongswan`directory into the main configuration and secrets files that Strongswan uses.

### About Using IKEv2

Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you[configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2), you must configure the CPE to use only IKEv2 and related IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

You specify the IKE version when setting up the IPSec configuration file in[task 3](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#StrongswanCPE_topic-task_3)in the next section. In that example file, a comment shows how to configure IKEv1 or IKEv2.

### Configuration Process

The following configuration process discusses how a route-based tunnel is configured on Strongswan. The Oracle VPN headends use route-based tunnels. We recommend that you configure Strongswan with the[Virtual Tunnel Interface (VTI) configuration syntax](https://libreswan.org/wiki/Route-based_VPN_using_VTI).

For details about the specific parameters used in this document, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

[Task 1: Prepare the Strongswan instance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Depending on the Linux distribution you're using, you might need to enable IP forwarding on the interface to allow clients to send and receive traffic through Strongswan. In the`/etc/sysctl.conf`file, set the following values and apply the updates with`sudo sysctl -p`.

If you're using an interface other than eth0, change`eth0`in the following example to the interface (lines 5 and 7).

If you're using several interfaces, configure lines 5 and 7 for that interface as well.

```

```

[Task 2: Decide the required configuration values](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

The Strongswan configuration uses the following variables. Decide the values before proceeding with the configuration.
- `${cpeLocalIP}`: The IP address of the Strongswan device.
- `${cpePublicIpAddress}`: The public IP address for Strongswan, also the IP address of the outside interface. Depending on the network topology, the value might be different from`${cpeLocalIP}`.
- `${oracleHeadend1}`: For the first tunnel, the Oracle public IP endpoint obtained from the Oracle Console.
- `${oracleHeadend2}`: For the second tunnel, the Oracle public IP endpoint obtained from the Oracle Console.
- `${sharedSecret1}`: The pre-shared key for the first tunnel. You can use the default Oracle-provided pre-shared key, or provide one when you set up the IPSec connection in the Oracle Console.
- `${sharedSecret2}`: The pre-shared key for the second tunnel. You can use the default Oracle-provided pre-shared key, or provide one when you set up the IPSec connection in the Oracle Console.
- `${vcnCidrNetwork}`: The VCN IP range.

[Task 3: Set up the configuration file: /etc/strongswan/ipsec.conf](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Strongswan configuration uses the concept of left and right to define the configuration parameters for the local CPE device and the remote gateway. Either side of the connection (the conn in the Strongswan configuration) can be left or right, but the configuration for that connection must be consistent. In this example:
- left: The local Strongswan CPE
- right: The Oracle VPN headend

Use the following template for the`/etc/strongswan/ipsec.conf`file. The file defines the two tunnels that Oracle creates when you set up the IPSec connection.
Important  
  

If the CPE is behind a one-to-one NAT device, uncomment the`leftid`parameter and set it equal to the`${cpePublicIpAddress}`.

```

```

Note  
  

Statements such as`ike=`and`esp=`can be changed for specific parameters based on the[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

[Task 4: Set up the secrets file: /etc/strongswan/ipsec.secrets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Use the following template for the`/etc/strongswan/ipsec.secrets`file. It contains two lines per IPSec connection (one line per tunnel).

```

```

[Task 5: VTI Creation](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

The following command creates a VTI interface with the defined name and binds it to the tunnel using local and remote IPs.

```

```

- `<name>`can be any valid device name (ipsec0, vti0, and so on). The ip command treats names starting with`vti`as special in some instances (such as when retrieving device statistics). The IP addresses are the endpoints of the IPSec tunnel. A private IP can be used when the CPE is behind a NAT device.
- `<mark>`must match the mark configured for the connection.

After creating the VTI, it must be enabled (use`ip link set <name> up`) and then you can install routes and use routing protocols as shown in the following example.

```

```

[Task 6: Modify Routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

The route installation by the IKE daemon must be disabled. To do this, change`charon.conf`as shown.

```

```

[Task 7: Restart Strongswan](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

After setting up the configuration and secrets files, you must restart the Strongswan service. Use the following command:

```

```

Note  
  
Restarting the Strongswan service might impact existing tunnels.

[Task 8: Configure IP routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Use the following`ip`command to create static routes that send traffic to a VCN through the IPSec tunnels. If you're signed in with an unprivileged user account, you might need to use`sudo`before the command.
Note  
  
Static routes created with the ip route command don't persist through a reboot. To find how to make the routes persist, see the documentation of the Linux distribution of choice.

```

```

## Verification

A[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ipsecmetrics.htm).

If you have issues, see[Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/ipsectroubleshoot.htm).

You can also enable OCI logging to get access to VPN logs.

### Verifying the Tunnel Interface Status

Verify the current state of the Strongswan tunnels by using the following command.

```

```

If the returned output is similar to the following example, the tunnel is established.
```

```

In the future, if you need to open a support ticket with Oracle about the Strongswan tunnel, include the complete output of the`strongswan status`command.

### Verifying the Tunnel Interface Status

Verify that the virtual tunnel interfaces are up or down by using the`ifconfig`command or the`ip link show`command. You can also use applications such as[tcpdump](https://www.tcpdump.org/)with the interfaces.

Here's an example of the`ifconfig`output with a working Strongswan implementation that shows the available VTIs.
```

```

Here's an example of the`ip link show`output:
```

```

## Configure Dynamic Routing with Strongswan

[Task 1: Install quagga to prepare the instance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

We recommend using quagga to configure BGP. To install quagga, use the following Oracle Linux command (if you're using a different Linux distribution the commands might vary slightly):
```

```

[Task 2: Configure zebra](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Change the zebra configuration (`/etc/quagga/zebra.conf`) to define the VTI IP address, which is required because BGP uses peering. Define the following variables for zebra:
- `${vti_name1}`: The name of the first VTI used. For example, vti1.
- `${vti_name2}`: The name of the second VTI used. For example, vti2.
- `${vti_ipaddress1}`: The IP address allocated to the first VTI used.
- `${vti_ipaddress2}`: The IP address allocated to the second VTI used.
- `${local_subnet}`: The local CPE subnet.

These variables are used in the following configuration file excerpt:

```

```

[Task 3: Configure bgpd](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

The bgpd config file is also required for BGP configuration. Define the following variables for bgpd:
- `${LOCAL_ASN}`: The BGP ASN of the on-premises network.
- `${router-id_ipaddress}`: The BGP ID of the local network.
- `${local_subnet}`: The local subnet that needs to be advertised.
- `${bgp_peer-ip _network}`: The /30 CIDR for the peer IP network in OCI.
- `${neighbor_peer_ip_address}`: The OCI BGP peer IP address.

These variables are used in the following configuration file excerpt from`/etc/quagga/bgpd.conf`:

```

```

[Task 4: Configure instances to use IP addresses with VTIs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Enabling strongswan to use routes and virtual IPs requires changes to`/etc/strongswan/strongswan.d/Charon.conf`.

Uncomment the lines that read`#install_routes = yes`and`#install_virtual_ip = yes`and change the values to "no" as shown:

```

```

[Task 5: Enable and start](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/StrongswanCPE.htm#)

Use the following commands to enable and start service for zebra and BGPD:

```

```
