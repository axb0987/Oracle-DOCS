# Working with Site-to-Site VPN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm
- Fetched: 2026-09-05 02:48 CDT

# Working with Site-to-Site VPN

This topic contains some details about working with Site-to-Site VPN and the related components. Also see these topics:
- [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm)
- [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm)
- [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm)
- [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm)
- [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)
- [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
- [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ipsecmetrics.htm)
- [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/ipsectroubleshoot.htm)

## Changing the Static Routes

You can change the static routes for an existing IPSec connection. You can provide up to 10 static routes.

Remember that an IPSec connection can use static routing, BGP dynamic routing, or policy-based routing. When using static routing you associate the static routes with the overall IPSec connection and not the individual tunnels. If an IPSec connection has static routes associated with it, Oracle uses them for routing a tunnel's traffic only if the tunnel itself is configured to use static routing. If it's configured to use BGP dynamic routing, the IPSec connection's static routes are ignored.
Important  
  
The IPSec connection goes down while it's reprovisioned with the static route changes.

See[Updating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm)for the steps needed to change the static routes.

## Changing from Static Routing to BGP Dynamic Routing

To change an existing Site-to-Site VPN from using static routing to using BGP dynamic routing, see[Updating an IPSec Tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm#ip_sec_tunnel_update_console__static-to-bgp).
Caution  
  
When you change a tunnel's routing type, the tunnel's IPSec status doesn't change during reprovisioning. However, routing through the tunnel is affected. Traffic is temporarily disrupted until a network engineer configures the CPE device in accordance with the routing type change. If an existing Site-to-Site VPN is configured to only use a single tunnel, this process disrupts the connection to Oracle. If a Site-to-Site VPN instead uses several tunnels, we recommend reconfiguring one tunnel at a time to avoid disrupting the connection to Oracle.

## Migrating to Policy-Based VPN

Oracle Cloud Infrastructure's Site-to-Site VPN v2 service fully supports policy-based IPSec VPNs with up to 50 encryption domains per tunnel.

To prevent potential traffic disruptions, if you have been migrated from the Site-to-Site VPN v1 service to Site-to-Site VPN v2, and have configured a CPE with several encryption domains, change the tunnel configurations on the OCI side of the connection to match the CPE configuration. This article explains why this modification is so important, and the required steps to configure OCI to use policy-based IPSec VPNs.

Why migrate to the Policy-Based VPN feature

The Site-to-Site VPN v1 service is always configured as a route-based VPN and uses an any/any encryption domain for both BGP and static routing types. For policy-based VPN interoperability, Site-to-Site VPN v1 supports a CPE configured for policy-based VPNs if the CPE acts as the initiator, and only a single encryption domain is sent to OCI. Configuring multiple encryption domains in this scenario results in instability of the tunnel where you might observe the tunnel flapping or that the traffic traversing the tunnel has unsteady reachability.

The Site-to-Site VPN v2 service uses a policy-based routing type option in addition to BGP and static routing types. Site-to-Site VPN v2's BGP and static routing types remain route-based and support a single any/any encryption domain. These options work with a single encryption domain policy-based CPE configuration, however this isn't recommended and sending more than one encryption domain results in tunnel instability.

The policy-based routing type available for Site-to-Site VPN v2 is a fully featured policy-based VPN that lets you configure the OCI side to fully match a CPE's policy-based configuration and accept all the individual security associations (SAs) required for a stable IPSec VPN tunnel.

For more information on encryption domains and the different IPSec VPN tunnel types, see[Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm).

After the tunnels have been migrated from Site-to-Site VPN v1 to v2, they continue to use the same routing type (BGP or static) as configured before migration. See for the step-by-step process to change existing route-based tunnels to use policy-based routing.

See[Updating an IPSec Tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm#ip_sec_tunnel_update_console__pbr)for specific steps for migrating to policy-based VPN.

## Changing the CPE IKE Identifier That Oracle Uses

If the[CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to give Oracle the CPE IKE identifier. You can either specify it when you create the IPSec connection, or later edit the IPSec connection and change the value. Oracle expects the value to be an IP address or fully qualified domain name (FQDN). When you specify the value, you also specify which type it is.
Important  
  
The IPSec connection goes down while it's reprovisioned to use the CPE IKE identifier.

See[Updating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm)for the steps needed to change the CPE IKE identifier that Oracle uses.

## Using IKEv2

Oracle supports Internet Key Exchange (IKE) version 1 and[version 2](https://tools.ietf.org/doc/html/rfc7296)(IKEv2).

To use IKEv2 with a CPE that supports it, you must:
- Configure each IPSec tunnel to use IKEv2 in the Oracle Console. See[Creating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm).
- Configure the CPE to use IKEv2 encryption parameters that the CPE supports. For a list of parameters that Oracle supports, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).

### New IPSec Connection using IKEv2

Note  
  

If you[create a new IPSec connection manually](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm), you can specify IKEv2 when you create the IPSec connection in the Oracle Console.

If you instead use the[VPN quickstart workflow](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm), the IPSec connection is configured to use IKEv1 only. However, after the workflow is complete, you can[edit the resulting IPSec tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm)in the Oracle Console and change them to use IKEv2.

### Upgrading an Existing IPSec connection to IKEv2

Important  
  
We recommend performing the following process for one tunnel at a time to avoid disruption in an IPSec connection. If the connection isn't redundant (for example, doesn't have redundant tunnels), expect downtime while you upgrade to IKEv2.
- [Change the tunnel's IKE version](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-update.htm)in the Oracle Console to use IKEv2 and the related encryption parameters that the CPE supports. For a list of parameters that Oracle supports, see[Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm).
- If the security associations don't rekey immediately, force a rekey for that tunnel on the CPE. To do this, clear the phase 1 and phase 2 security associations and don't wait for them to expire. Some CPE devices wait for the SAs to expire before rekeying. Forcing the rekey lets you confirm immediately that the IKE version configuration is correct.
- To verify, ensure that the security associations for the tunnel rekey correctly. If they don't, confirm that the correct IKE version is set in the Oracle Console and on the CPE, and that the CPE is using the appropriate parameters.

After you confirm the first tunnel is up and running again, repeat the preceding steps for the second tunnel.

## Changing the Shared Secret That an IPSec Tunnel Uses

When you set up Site-to-Site VPN, by default Oracle provides each tunnel's shared secret (also called the pre-shared key). You might have a particular shared secret that you want to use instead. You can specify each tunnel's shared secret when you create the IPSec connection, or you can edit the tunnels and provide each new shared secret then. For the shared secret, only numbers, letters, and spaces are allowed. We recommend using a different shared secret for each tunnel.
Important  
  
When you change a tunnel's shared secret, both the overall IPSec connection and the tunnel go into the Provisioning state while the tunnel is reprovisioned with the new shared secret. The other tunnel in the IPSec connection remains in the Available state. However, while the first tunnel is being reprovisioned, you can't change the second tunnel's configuration.

See[Getting an IPSec Tunnel's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_get.htm#ip_sec_tunnel_get_console__change-shared-secret)for steps needed to change the shared secret that an IPSec tunnel uses.

## Monitoring Site-to-Site VPN

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

For information about monitoring a connection, see[Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ipsecmetrics.htm).

## Site-to-Site VPN Log Messages

You can enable logging and view the log messages generated for various operational aspects of Site-to-Site VPN such as the negotations that occur in bringing an IPSec tunnel UP. Enabling and accessing the Site-to-Site VPN log messages can be done by using Site-to-Site VPN or the Logging Service.
- For an overview of the Logging service in general, see[Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).
- For details on enabling and accessing the Site-to-Site VPN log messages by using the Logging service, see[Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm).
- 

For details on the Site-to-Site VPN log message schema, see[Details for Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_vpn_connect.htm).

To enable message logging, see[Getting IPSec Connection Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm#ip_sec_con_get_console__log-enable).

To view log messages, see[Getting IPSec Connection Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-get.htm#ip_sec_con_get_console__log-view).

## Moving an IPSec Connection or CPE Object to a Different Compartment

You can move resources from one compartment to another. After you move the resource to the new compartment, inherent policies apply immediately and affect access to the resource through the Console. Moving the CPE object to a different compartment doesn't affect the connection between an on-premises data center and Oracle Cloud Infrastructure. For more information, see[Working with Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#Working).

See[Moving an IPSec Connection Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-change_compartment.htm)and[Moving a CPE to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-change_compartment.htm)for more details.

## Managing DRGs

For tasks related to DRGs, see[Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm).

## Maintaining IPSec Tunnels

To ensure the security, stability, and performance of our system, Oracle regularly updates software across the OCI platform. These updates include critical fixes such as vulnerability patches, new features, and bug fixes, which improves the overall functionality and reliability. During the update process, an IPSec tunnel is moved from one VPN headend to another headend, which leads to the IPSec connection getting reset when only one tunnel is used. Only one IPSec tunnel in an IPSec connection is moved. While we can't prevent this brief interruption to the tunnel, we have optimized the update mechanism to minimize the downtime. When the Customer Premise Equipment (CPE) continuously tries to reestablish the connection, normal IPSec tunnel downtime is under a minute. This design lets Oracle maintain a balance between keeping the system secure and reliable while minimizing the disruption to connectivity. Sometimes restoring the IPSec tunnel can take up to 10 minutes:
- When the tunnel is set as a responder only on the OCI side and the CPE isn't trying to bring the tunnel up immediately
- When the CPE fails to respond to the IKE negotiation started by the OCI side

While the IPSec tunnel flap during software updates is unavoidable, OCI provides redundant tunnels. These redundant tunnels are designed to maintain continuous traffic flow, even during the brief period when one tunnel experiences downtime. If redundancy has been set up correctly, all traffic routed through the primary tunnel seamlessly switches to the redundant tunnel during a tunnel flap. This failover mechanism ensures that services remain uninterrupted, and the traffic flow is preserved without significant delays. OCI ensures that the redundant tunnels land on two distinct VPN headends. During our software updates only one tunnel is impacted at a time.

We recommend and expect that you test redundancy by taking down the primary VPN tunnel, both during the initial setup and on a regular cadence thereafter. Confirm that VCN instances remain reachable while the primary tunnel is offline, and the traffic is shifting to the redundant tunnel. The VPN Redundancy section in this[Redundancy Guide](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf)provides more insight into setting up the redundancy for VPN tunnels in different use cases.

You can use the following steps to temporarily disable a tunnel yourself to test redundancy failover from a primary IPSec tunnel to a secondary IPSec tunnel:

- Go to the tunnel details page as described in[Updating an IPSec Tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm)and edit the Shared Secret .
- To temporarily disable a tunnel:
- Cut the text in the shared secret field, and replace it with a few random letters or numbers. This causes the BGP session to go down and traffic can failover to the other tunnel. This field can't be empty.
Paste the original string in the shared secret field into a text file. You need this to reestablish the BGP session after confirming redundancy is working as expected.
- Select Save changes .
- Confirm that traffic is still flowing on the secondary IPSec tunnel in the connection.
- To restore a temporarily disabled tunnel:
- Go to the tunnel details page as described in[Updating an IPSec Tunnel](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-tunnel_update.htm)and edit the Shared Secret .
- Paste in the original text in the shared secret field.
- Select Save changes .
-
