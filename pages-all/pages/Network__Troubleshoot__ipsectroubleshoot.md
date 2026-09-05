# Site-to-Site VPN Troubleshooting
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm
- Fetched: 2026-09-05 02:48 CDT

# Site-to-Site VPN Troubleshooting

Create a service request at[My Oracle Support](http://support.oracle.com/)

This topic covers the most common troubleshooting issues for Site-to-Site VPN. Some suggestions assume that you're a network engineer with access to the CPE device's configuration.

## Log Messages

Viewing log messages generated for various operational aspects of Site-to-Site VPN can be a valuable aid in troubleshooting many of the issues presented during operation. Enabling and accessing the Site-to-Site VPN log messages can be done through Site-to-Site VPN or the Logging service.
- For an overview of the Logging service in general, see the[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)
- For details on enabling and accessing the Site-to-Site VPN log messages by using the logging service, see[Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm)
- For details on enabling and accessing the Site-to-Site VPN log messages through the Networking service, see[Site-to-Site VPN Log Messages](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/workingwithIPsec.htm#viewing_your_vpn_connect_log_messages).
- 

For details on the Site-to-Site VPN log message schema, see[Details for Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_vpn_connect.htm).

See the following table for a better interpretation of Site-to-Site VPN log messages, which lists of the different tunnel-down scenarios and the possible logs seen on the OCI Console.

Interpreting Console Logs
Tunnel down reason Logs populated in OCI logging section
Mismatched IKE version

`STATE_V2_PARENT_I1: 60 second timeout exceeded after 7 retransmits. No response (or no acceptable response) to our first IKEv2 message`

`dropping unexpected IKE_SA_INIT message containing NO_PROPOSAL_CHOSEN notification; message payloads: N; missing payloads: SA,KE,Ni`

`received and ignored notification payload: NO_PROPOSAL_CHOSEN_date_time ep_85 pluto[68971]: "xxxxxxx" #xxx: set ikev1 error <14>`
Mismatched subnets

`No IKEv2 connection found with compatible Traffic Selectors`

`responding to CREATE_CHILD_SA message (ID 30) from CPE_PUBLIC_IP:4500 with encrypted notification TS_UNACCEPTABLE`

`cannot respond to IPsec SA request because no connection is known for MISMATCHED_SOURCE_SUBNET===VPN_PUBLIC_IP[+S?C]...VPN_PUBLIC_IP[+S?C]===MISMATCHED_DESTINATION_SUBNET`
Mismatched Pre-shared key

`STATE_MAIN_I3: 60 second timeout exceeded after 7 retransmits. Possible authentication failure: no acceptable response to our first encrypted messag`

`IKE SA authentication request rejected by peer: AUTHENTICATION_FAILED`

`authentication failed: computed hash does not match hash received from peer ID_IPV4_ADDR 'VPN_PUBLIC_IP'`

`responding to IKE_AUTH message (ID 1) from VPN_PUBLIC_IP:4500 with encrypted notification AUTHENTICATION_FAILED`
Proposal mismatched

`OAKLEY proposal refused: missing encryption`

`Oakley Transform [AES_CBC (128), HMAC_SHA2_256, DH19] refused`

`no acceptable Oakley Transform`

`sending notification NO_PROPOSAL_CHOSEN to VPN_PUBLIC_IP:500`

`failed to add connection: ESP DH algorithm 'modp1024' is not supported`

`received unauthenticated v2N_NO_PROPOSAL_CHOSEN - ignored`
Mismatched PFS

`ignoring informational payload NO_PROPOSAL_CHOSEN, msgid=xxxxxx, length=12`

`received and ignored notification payload: NO_PROPOSAL_CHOSEN`

`dropping unexpected ISAKMP_v2_CREATE_CHILD_SA message containing v2N_INVALID_SYNTAX notification; message payloads: SK; encrypted payloads: N; missing payloads: SA,Ni,TSi,TSr`

`"xxxxxxxx"[1] VPN_PUBLIC_IP #580: encountered fatal error in state STATE_V2_REKEY_CHILD_I`
Mismatched IKE ID

`Peer ID 'MISMATCHED_IKE_ID_IP_ADDRESS' mismatched on first found connection and no better connection found`

`sending encrypted notification INVALID_ID_INFORMATION to VPN_PUBLIC_IP:4500`

## Tunnel Flapping

Interesting traffic at all times: We recommend always having interesting traffic running through the IPSec tunnels if the CPE supports it. Cisco ASA requires that you configure SLA monitoring, which keeps interesting traffic running through the IPSec tunnels. For more information, see the section for "IP SLA Configuration" in the[Cisco ASA policy-based configuration template](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm#CPE).

Multiple IPSEC Connections: You can use two IPSec connections for redundancy. If both IPSec connections have only a default route (0.0.0.0/0) configured, traffic routes to either of those connections because Oracle uses asymmetric routing. If you want one IPSec connection as primary and another one as backup, configure more-specific routes for the primary connection and less-specific routes (or the default route of 0.0.0.0/0) on the backup connection.

Local IKE identifier: Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as cpe.example.com . For instructions, see[Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/workingwithIPsec.htm#edit_cpe_ike_id).

Maximum Transmission Unit (MTU): The standard internet MTU size is 1500 bytes. For more information on how to find the MTU, see[Overview of MTU](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Overview).

## CPE Configuration

Local IKE identifier: Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as cpe.example.com . For instructions, see[Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/workingwithIPsec.htm#edit_cpe_ike_id).

Cisco ASA: Policy Based: We recommend using a[route-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEroutebased.htm)to avoid interoperability issues and to achieve tunnel redundancy with a single Cisco ASA device.

The Cisco ASA doesn't support route-based configuration for software versions older than 9.7.1. For the best results, if the device supports it, we recommend that you upgrade to a software version that supports route-based configuration.

With policy-based configuration, you can configure only a single tunnel between a Cisco ASA and a Dynamic Routing Gateway (DRG).

Multiple Tunnels If you have multiple tunnels up simultaneously, ensure that the CPE is configured to handle traffic coming from the VCN on any of the tunnels. For example, you need to disable ICMP inspection, configure TCP state bypass, and so on. For more details about the appropriate configuration, contact the CPE vendor's support.

## Encryption Domain Issues

The Oracle VPN headends use route-based tunnels, but can work with policy-based tunnels with some caveats. See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel)for full details.

Stateful security list rules: If you're using[stateful security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securityrules.htm#stateful)(for TCP, UDP, or ICMP traffic), you don't need to ensure that a security list has an explicit rule to allow ICMP type 3 code 4 messages because the Networking service tracks the connections and automatically allows those messages. Stateless rules require an explicit ingress security list rule for ICMP type 3 code 4 messages. Confirm that the instance firewalls are set up correctly.

## General Site-to-Site VPN Issues

### IPSec tunnel is DOWN

Check these items:
- 

Basic configuration : The IPSec tunnel consists of both phase-1 and phase-2 parameters. Confirm that both are configured correctly. You can configure the CPE phase 1 and phase 2 parameters in the OCI end using custom configurations. To use custom configurations on the tunnel, go to advanced options and enable set custom configurations . This lets you manually define phase 1 and phase 2 parameters on the OCI end.

Oracle has also recommended certain parameters for phase 1 and phase 2. See the parameters for[phase-1 (ISAKMP) and phase-2 (IPSec) configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/supportedIPsecparams.htm)and use those parameters if the previous step doesn't bring up the tunnel. For more information on configuring CPE device, see the configuration appropriate for the CPE device:

- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/CPElist.htm)
- [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/CPEconfigurationhelper.htm)
- 

Checkpoint:
- [Check Point: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/checkpointCPEroutebased.htm)
- [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/checkpointCPEpolicybased.htm)
- Cisco ASA:
- [Cisco ASA: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEroutebased.htm)
- [Cisco ASA: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm)
- [Cisco IOS](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoiosCPE.htm)
- [FortiGate](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/fortigateCPE.htm)
- [Furukawa Electric](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/furukawaCPE.htm)
- [Juniper MX](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/junipermxCPE.htm)
- [Juniper SRX](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/junipersrxCPE.htm)
- [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/libreswanCPE.htm)
- [NEC IX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/necixCPE.htm)
- [Openswan](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/openswanCPE.htm)
- [Palo Alto](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/paloaltoCPE.htm)
- [WatchGuard](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/watchguardCPE.htm)
- [Yamaha RTX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/yamahartx.htm)
- 
Local and remote proxy IDs: If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and select one of the following two options:

Option Local Proxy ID Remote Proxy ID
1 ANY (or 0.0.0.0/0) ANY (or 0.0.0.0/0)
2 On-premises CIDR (an aggregate that covers all the subnets of interest) VCN's CIDR
- NAT device: If the CPE is behind a NAT device, the CPE IKE identifier configured on the CPE might not match the CPE IKE identifier Oracle is using (the public IP address of the CPE). If the CPE doesn't support setting the CPE IKE identifier on the on-premises end, you can provide Oracle with the CPE IKE identifier in the Oracle Console. For more information, see[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/overviewIPsec.htm#components).

### IPSec tunnel is UP, but no traffic is passing through

Check these items:
- 

Phase 2 (IPSec) configuration: Confirm that the[phase 2 (IPSec) parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/supportedIPsecparams.htm)are configured correctly on the CPE device. See the configuration appropriate for the CPE device:

List of configurations

- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/CPElist.htm)
- [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/CPEconfigurationhelper.htm)
- 

Checkpoint:
- [Check Point: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/checkpointCPEroutebased.htm)
- [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/checkpointCPEpolicybased.htm)
- Cisco ASA:
- [Cisco ASA: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEroutebased.htm)
- [Cisco ASA: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm)
- [Cisco IOS](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoiosCPE.htm)
- [FortiGate](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/fortigateCPE.htm)
- [Furukawa Electric](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/furukawaCPE.htm)
- [Juniper MX](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/junipermxCPE.htm)
- [Juniper SRX](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/junipersrxCPE.htm)
- [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/libreswanCPE.htm)
- [NEC IX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/necixCPE.htm)
- [Openswan](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/openswanCPE.htm)
- [Palo Alto](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/paloaltoCPE.htm)
- [WatchGuard](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/watchguardCPE.htm)
- [Yamaha RTX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/yamahartx.htm)
- VCN security lists: Ensure the[VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securitylists.htm)allow the appropriate traffic (both ingress and egress rules). Note that the VCN's[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securitylists.htm#Default)doesn't allow ping traffic (ICMP type 8 and ICMP type 0). You must add the appropriate ingress and egress rules to allow ping traffic.
- Firewall rules: Ensure that the firewall rules allow both ingress and egress traffic with the Oracle VPN headend IPs and the VCN CIDR block.
- Asymmetric routing: Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from a VCN to an on-premises network can use any tunnel that's "up" on a device. Configure firewalls as appropriate. Otherwise, ping tests or application traffic across the connection don't work reliably.
- Cisco ASA: Don't use the originate-only option with an Oracle Site-to-Site VPN IPSec tunnel. It causes the tunnel's traffic to be inconsistently blackholed. The command is only for tunnels between two Cisco devices. Here's an example of the command NOT to use for the IPSec tunnels:`crypto map <map name> <sequence number> set connection-type originate-only`

### IPSec tunnel is UP, but traffic is passing in only one direction

Check these items:
- Asymmetric routing: Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from a VCN to an on-premises network can use any tunnel that's "up" on a device. Configure firewalls as appropriate. Otherwise, ping tests or application traffic across the connection don't work reliably.
- Single tunnel preferred: To use only one of the tunnels, ensure that you have the proper policy or routing in place on the CPE to prefer that tunnel.
- Multiple IPSec connections: If you have multiple IPSec connections with Oracle, ensure that you specify more specific static routes for the preferred IPSec connection.
- VCN security lists: Ensure that the[VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securitylists.htm)allow traffic in both directions (ingress and egress).
- Firewall rules: Ensure that the firewall rules allow traffic in both directions with the Oracle VPN headend IPs and the VCN CIDR block.

## Troubleshooting Site-to-Site VPN with a Policy-Based Configuration

### IPSec tunnel is DOWN

Check these items:
- 

Basic configuration: The IPSec tunnel consists of both[phase-1 (ISAKMP) and phase-2 (IPSec) configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/supportedIPsecparams.htm). Confirm that both are configured correctly on the CPE device. See the configuration appropriate for the CPE device:

List of configurations

- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/CPElist.htm)
- [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/CPEconfigurationhelper.htm)
- 

Checkpoint:
- [Check Point: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/checkpointCPEroutebased.htm)
- [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/checkpointCPEpolicybased.htm)
- Cisco ASA:
- [Cisco ASA: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEroutebased.htm)
- [Cisco ASA: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm)
- [Cisco IOS](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoiosCPE.htm)
- [FortiGate](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/fortigateCPE.htm)
- [Furukawa Electric](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/furukawaCPE.htm)
- [Juniper MX](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/junipermxCPE.htm)
- [Juniper SRX](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/junipersrxCPE.htm)
- [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/libreswanCPE.htm)
- [NEC IX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/necixCPE.htm)
- [Openswan](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/openswanCPE.htm)
- [Palo Alto](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/paloaltoCPE.htm)
- [WatchGuard](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/watchguardCPE.htm)
- [Yamaha RTX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/yamahartx.htm)
- 
Local and remote proxy IDs: If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and select one of the following two options:

Option Local Proxy ID Remote Proxy ID
1 ANY (or 0.0.0.0/0) ANY (or 0.0.0.0/0)
2 On-premises CIDR (an aggregate that covers all the subnets of interest) VCN's CIDR
- NAT device: If the CPE is behind a NAT device, the CPE IKE identifier configured on the CPE might not match the CPE IKE identifier Oracle is using (the public IP address of the CPE). If the CPE doesn't support setting the CPE IKE identifier on the on-premises end, you can provide Oracle with the CPE IKE identifier in the Oracle Console. For more information, see[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/overviewIPsec.htm#components).
- Cisco ASA: Don't use the originate-only option with an Oracle Site-to-Site VPN IPSec tunnel. It causes the tunnel's traffic to be inconsistently blackholed. The command is only for tunnels between two Cisco devices. Here's an example of the command NOT to use for the IPSec tunnels:`crypto map <map name> <sequence number> set connection-type originate-only`

### IPSec tunnel is UP but keeps flapping

Check these items:
- Initiation of connection: Ensure that the CPE device is starting the connection.
- 
Local and remote proxy IDs: If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and select one of the following two options:

Option Local Proxy ID Remote Proxy ID
1 ANY (or 0.0.0.0/0) ANY (or 0.0.0.0/0)
2 On-premises CIDR (an aggregate that covers all the subnets of interest) VCN's CIDR
- 
Interesting traffic at all times: We recommend always having interesting traffic running through the IPSec tunnels if the CPE supports it. Cisco ASA requires that you configure SLA monitoring, which keeps interesting traffic running through the IPSec tunnels. For more information, see the section for "IP SLA Configuration" in the[Cisco ASA policy-based configuration template](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm#CPE).

### IPSec tunnel is UP but traffic is unsteady

Check these items:
- 
Local and remote proxy IDs: If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and select one of the following two options:

Option Local Proxy ID Remote Proxy ID
1 ANY (or 0.0.0.0/0) ANY (or 0.0.0.0/0)
2 On-premises CIDR (an aggregate that covers all the subnets of interest) VCN's CIDR
- 
Interesting traffic at all times: We recommend always having interesting traffic running through the IPSec tunnels if the CPE supports it. Cisco ASA requires that you configure SLA monitoring, which keeps interesting traffic running through the IPSec tunnels. For more information, see the section for "IP SLA Configuration" in the[Cisco ASA policy-based configuration template](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm#CPE).

### IPSec tunnel is only partially UP
[

If you had a configuration similar to the example preceding and only configured three of the six possible IPv4 encryption domains on the CPE side, the link would be listed in a "Partial UP" state because all possible encryption domains are always created on the DRG side.

Partial up SA: We recommend always having interesting traffic running through the IPSec tunnels. Certain CPE vendors require you to always have interesting traffic through the tunnel to keep phase 2 up. Vendors such as Cisco ASA require the[SLA monitor](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Reference/ciscoasaCPEpolicybased.htm)monitor to be configured. Similarly, Palo Alto features such as path monitoring can be used. Such features keep interesting traffic running through the IPSec tunnels. Scenarios have been seen with vendors such as Cisco ASA acting as the "initiator" doesn't bring phase 2 up until there is no interesting traffic. This causes the SA to be down either when the tunnel is brought up or after security association rekey.

## BGP Session Troubleshooting for Site-to-Site VPN

### BGP status is DOWN

Check these items:
- IPSec status: For the BGP session to be up, the IPSec tunnel itself must be up.
- BGP address: Verify that both ends of the tunnel are configured with the correct BGP peering IP address.
- ASN: Verify that both ends of the tunnel are configured with the correct BGP local ASN and Oracle BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn).
- MD5: Verify that MD5 authentication is disabled or not configured on the CPE device. Site-to-Site VPN doesn't support MD5 authentication.
- 

Firewalls: Verify that an on-premises firewall or access control lists aren't blocking the following ports:
- TCP port 179 (BGP)
- UDP port 500 (IKE)
- IP protocol port 50 (ESP)

If a CPE device's firewall is blocking TCP port 179 (BGP), the BGP neighborship state is always down. Traffic can't flow through the tunnel because the CPE device and Oracle router don't have any routes.

### BGP status is flapping

Check these items:
- IPSec status: For the BGP session to be up and not flapping, the IPSec tunnel itself must be up and not flapping.
- Maximum prefixes: Verify that you're advertising no more than 2000 prefixes. If you're advertising more, BGP isn't established.

### BGP status is UP, but no traffic is passing through

Check these items:
- VCN security lists: Ensure the[VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securitylists.htm)allow the appropriate traffic (both ingress and egress rules). Note that the VCN's[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securitylists.htm#Default)doesn't allow ping traffic (ICMP type 8 and ICMP type 0). You must add the appropriate ingress and egress rules to allow ping traffic.
- Correct routes on both ends: Verify that you have received the correct VCN routes from Oracle and the CPE device is using those routes. Likewise, verify that you're advertising the correct on-premises network routes over the Site-to-Site VPN, and the VCN route tables use those routes.

### BGP status is UP, but traffic is passing in only one direction

Check these items:
- VCN security lists: Ensure that the[VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Concepts/securitylists.htm)allow traffic in both directions (ingress and egress).
- Firewalls: Verify that on-premises firewalls or access control lists aren't blocking traffic to or from the Oracle end.
- Asymmetric routing: Oracle uses asymmetric routing. If you have several IPSec connections, ensure that the CPE device is configured for asymmetric route processing.
- Redundant connections: If you have redundant IPSec connections, ensure that they're both advertising the same routes.

## Troubleshooting Redundant IPSec connections

Remember these important notes:
- FastConnect uses BGP dynamic routing. Site-to-Site VPN IPSec connections can use either static routing or BGP, or a combination.
- For important details about routing and preferred routes when using redundant connections, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/overviewIPsec.htm#ipsec_routing).
- You can use two IPSec connections for redundancy. If both IPSec connections have only a default route (0.0.0.0/0) configured, traffic routes to either of those connections because Oracle uses asymmetric routing. If you want one IPSec connection as primary and another one as backup, configure more-specific routes for the primary connection and less-specific routes (or the default route of 0.0.0.0/0) on the backup connection.

### IPSec and FastConnect are both set up, but traffic is only passing through IPSec

Ensure that you use more specific routes for the connection you want as primary. If you're using the same routes for both IPSec and FastConnect, see the discussion of routing preferences in[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/overviewIPsec.htm#ipsec_routing).

### Two on-premises data centers each have an IPSec connection to Oracle, but only one is passing traffic

Verify that both IPSec connections are up and ensure that you have asymmetric route processing enabled on the CPE.

If both IPSec connections have only a default route (0.0.0.0/0) configured, traffic routes to either of those connections because Oracle uses asymmetric routing. If you want one IPSec connection as primary and another one as backup, configure more-specific routes for the primary connection and less-specific routes (or the default route of 0.0.0.0/0) on the backup connection.

For more information about this type of setup, see[Example Layout with Several Geographic Areas](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/settingupIPsec.htm#example_multi_geo)
