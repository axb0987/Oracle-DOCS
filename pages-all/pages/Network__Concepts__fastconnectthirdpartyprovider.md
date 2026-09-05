# FastConnect: With a Third-Party Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm
- Fetched: 2026-09-05 02:41 CDT

# FastConnect: With a Third-Party Provider

This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.

For a summary of the different ways to connect, see the[connectivity models](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#How).

If you're using one of the[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/), see[FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm). Or, to use FastConnect by colocating with Oracle, see[FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm).

For general information about FastConnect, see[FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm).

## Important Points and Responsibilities

- You can use FastConnect by working with a third-party network service provider or carrier of your choice. The network provider must be capable of connecting to the Oracle routers in one of the FastConnect data center locations (see[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/)) over single-mode fiber. For more detailed technical requirements, see[Hardware and Routing Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements).
- 

An overall connection with the third-party provider includes two parts, as illustrated in the following diagram:
- Part 1 : Your physical connection to the third-party provider. The rest of this topic assumes you've already set up this part of the overall connection.
- 

Part 2 : The physical fiber connection (cross-connect) that the third-party provider sets up in the FastConnect location data center on your behalf.
[
- To obtain the[Letter of Authorization (LOA)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#concepts__LoA)for the cross-connect, you must use the Oracle Console to[set up a cross-connect or cross-connect group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_cc). The resulting LOA from Oracle covers all required details for the provider physical connection to Oracle in the preceding diagram.
- You must forward the LOA to your third-party provider, who is responsible for working with the data center to set up the physical cross-connect on your behalf.
Note  
  
When you don't provide the Oracle LOA with your order to your chosen provider, and instead give your own independent authorization just giving the building address, the details (such as the required panel and port) required for a cross connect aren't included in the price quote and the work order. You might think that placing the order first saves time, but in practice it will most often have to be redone from the beginning, taking far more time than expected.
- The third-party provider issues a cross-connect order with the data center facility to run fiber optics to complete the connection from the third-party provider's cage to Oracle's patch panel as described in the LOA. Typically the data center colocation staff are the ones who run the fiber optics to complete the connection.
- Each LOA is valid for only a limited time. If the physical cross-connect is not set up before the LOA's expiration, the LOA is revoked.
- The third-party provider is responsible for charging you for the entire connection (both parts 1 and 2) . Oracle doesn't set up this cross-connect in the data center, does not pay for it, and does not include it in your FastConnect charges.
- The LOA specifies an Oracle demarcation point. If your network provider is located at a different demarcation point in the data center cage, they must set up the cross-connect from their demarcation point to the Oracle demarcation point.

## Getting Started with FastConnect

Note  
  
In general, this topic assumes that your router supports link aggregation (LAG) and you will set up a cross-connect group (a LAG) with at least one cross-connect in it. The following procedures reflect that. However, if your router doesn't support link aggregation, you can instead set up a single non-LAG cross-connect (with no cross-connect group). The procedures in this topic are still generally applicable. Instead you work only with a single cross-connect and not one or more in a cross-connect group.

If you haven't yet, walk through the planning in[Before Getting Started: Learn and Plan](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#Before). Also see[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)and[Hardware and Routing Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements).

You might also need to review information on how[to use FastConnect if you do not own a Public ASN or Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#public_asn_ip).

The following flow chart shows the overall process of setting up FastConnect.
[

[Task 1: Set up a DRG (private peering only)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Summary : If you plan to use a private virtual circuit (private peering), you need a DRG. If you haven't already, use the Oracle Cloud Infrastructure Console to set up a DRG, attach it to the VCN, and update routing in the VCN to include a route rule to send traffic to the DRG. Remember to update the route table. Without the route rule, no traffic can flow.

Instructions :
- [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/drg-create.htm)
- [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/attach-vcn-drg.htm)
- [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/update-rules-routetable.htm)

[Task 2: Set up a cross-connect group or cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Summary : Create a connection in the Console, which consists of a cross-connect group (for link aggregation, or LAG) that contains at least one cross-connect. If you need more cross-connects in the group, you can[add them later](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#add_cc_to_ccg). You can have a maximum of eight cross-connects in a group.

You have the option to set up a single non-LAG cross-connect (with no cross-connect group) if the router doesn't support link aggregation (LAG).

When you create a cross connect with a third-party provider, OCI metering starts when a cross connect or cross connect group is activated, or 30 days after the LOA for cross connect or cross connect group was generated, which ever is the earliest. The third party provider bills the WAN service separately, beginning when they consider the connection live (independent of cross connect or cross connect group activation).

Instructions :
- On the FastConnect connections list page, select Create FastConnect . If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- 

Select FastConnect Direct .

Select this option even though a third-party provider sets up the physical connection to Oracle in the FastConnect location.
- 

Select one of the following options:
- Location redundancy : This option creates a connection with a two redundant virtual circuits in different FastConnect locations used by the same OCI region.
- Device redundancy (Recommended) : (Recommended) This option creates a connection with a two redundant virtual circuits in the same FastConnect location.
- Single FastConnect : This option creates a connection with a single virtual circuit. You can create redundancy later if you decide to.

See[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)for more about redundancy.
- Select Next .
- 

Enter the following items:
Note  
  

If you chose Location redundancy or Device redundancy (Recommended) you see these options for both Connection 1 and Connection 2 .
- Name : A descriptive name for this connection. You can't change the name later. Avoid entering confidential information. If you're creating a cross-connect group, the cross-connect group uses this name. Each cross-connect in this group also uses it, but with a hyphen and number appended (for example, MyName-1, MyName-2, and so on).
- Compartment : Leave as is (the compartment you're working in).
- 

Cross-Connect Type :
- If the on-premises edge router supports link aggregation (LAG), select Cross-Connect Group . You create a cross-connect group (a LAG) with at least one cross-connect.
- If the on-premises edge router doesn't support LAG, select Single Cross-Connect . You create a single cross-connect with no cross-connect group.
- Reference Name : The ID for the physical LAG for the cross-connect group. This makes future connection troubleshooting easier. You might need to get this value from the third-party provider. If you don't have it, you can add it later. If you're creating a single cross-connect, enter the ID for the physical fiber cable for the cross-connect.
- Number of cross-connects : Available only if you're creating a cross-connect group. This is the number of individual cross-connects to create in the cross-connect group. In the Console, you can create three. If you need more, you can[add more cross-connects later](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#add_cc_to_ccg)(total eight in a cross-connect group).
- Port speed : 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps.
- Encryption : If the connection uses[MACsec encryption](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#macsec), you must select a Port Speed of 10 Gbps or greater. You also need to provision the CAK and CKN as individual secrets in a[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm). Select the Enable MACsec Encryption box and enter the following information:
- Encryption Algorithm : The encryption cipher suite to use for the MACsec connection.
- Connectivity Association Key (CAK) : Select a Vault and a secret representing the CAK.
- Connectivity Association Key Name (CKN) : Select a Vault and a secret representing the CKN.

You can also select Show advanced options to select what happens if the MACsec session fails. The choices are:
- Fail Close : This is the default and is recommended. If the MACsec session fails and traffic encryption is no longer available, no traffic is sent over the virtual circuit until the MACsec connection can be re-established. This option prioritizes security over reachability.
- Fail Open : If the MACsec session fails and traffic encryption is no longer available, unencrypted traffic is sent over the virtual circuit until the MACsec connection can be re-established. This option prioritizes reachability over security. This option isn't recommended if MACsec is required by your organization's security standards.
- Physical location: : The FastConnect location for this connection. If you chose Device redundancy (Recommended) the physical location settings for Connection 1 and Connection 2 must match, and you can only select them from Connection 1 . If you chose Location redundancy , the physical location settings for Connection 1 and Connection 2 must be different, and their selections are independent.
- Specify Router Proximity : Optionally specify whether you want the new connection to be on the same or different router in that FastConnect location than one of the other connections.
- 

Select Create .

The new connection is created.
- Select Close to see the FastConnect page.
- Select the name of the new connection to see its details.
- 

Print the LOA for each cross-connect: Each cross-connect you created has a Letter of Authorization (LOA). Select the name to view each cross-connect's details, and then view and print the cross-connect's LOA. In the next task, you forward it to the third-party provider so they can request cabling at the FastConnect location. The cross-connect's status is PENDING CUSTOMER until you complete the next few tasks.
Note  
  
When you don't provide the Oracle LOA with the order, and instead give an independent authorization with only a building address, the details (such as the required panel and port) required for a cross connect aren't included in the price quote and the work order. You might think that placing the order first saves time, but in practice it usually has to be redone from the beginning, taking far more time than expected.

The see the LOA, select View next to Letter of Authorization in the detail screen for the connection you created.

[Task 3: Forward the LOA to the third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Forward the[LOA](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#concepts__LoA)or LOAs from the preceding task to the third-party network provider so they can request cabling at the FastConnect location. Each LOA is valid for a limited time. All required details for the connection are printed on the LOA.

[For FastConnect Providers in the Saudi Arabia West (Jeddah) Region](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Send the LOA and connection request to both the provider and also the provider's wholesale contact:
- Mobily : mobily_olo's_sales@mobily.com.sa
- Salam : carrier@salam.sa

[Task 4: Check light levels](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

After the third-party provider completes setup of the physical cross-connect in the FastConnect location, confirm from your side that the light levels for each physical connection (cross-connect) are good (&gt; -15 dBm). Don't proceed until the light levels are good.

In the Console, you can see the light levels that Oracle detects by viewing the details of the cross-connect (look for Light Level Indicator Good).

If the light levels aren't good, contact the third-party network provider.

[Task 5: Activate each cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Summary: When the physical fiber cables in the FastConnect location are set up and ready to use, return to the Oracle Console and activate each cross-connect that you set up earlier. The process of activating a cross-connect informs Oracle that the corresponding physical fiber cable is ready. Oracle then completes the router configuration for each cross-connect. Instructions:
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).
- Select the Actions button and then select Activate .
- While still viewing the cross-connect's details, select Edit and enter the ID for the physical fiber cable for this cross-connect. Adding this value can help with any connection troubleshooting in the future. If you don't have the value available now, you can add it later. If you have other cross-connects that are ready to use, wait for the first to be provisioned, and then activate the next one. Only one cross-connect in a group can be activated and then provisioned at a time. After you complete this task, each cross-connect's status changes from PENDING CUSTOMER to PROVISIONING and then to PROVISIONED (typically within three minutes).

[Task 6: Confirm that your interfaces are up](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

For each cross-connect's physical fiber cable, confirm your side of the interfaces are up. Don't proceed until they are.

In the Console, you can see the status of Oracle's side of the interfaces (up or down) by viewing the details of the cross-connect (see the preceding screenshot in task 5).
Note  
  
The Interface State is either be "Down" or "Up" until the cross-connect is activated. Even though light levels are good, the interface might still appear to be down before activation.

If the interfaces aren't up, contact the third-party network provider.

[Task 7: Set up your virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Summary : Create one or more virtual circuits for a connection in the Oracle Console. The cross-connect group (or a single non-LAG cross-connect) must first be in the PROVISIONED state.
Important  
  
To use a single FastConnect to connect an on-premises existing network to multiple DRGs and VCNs, you must set up a different private virtual circuit for each VCN. Each virtual circuit must have a different VLAN and a different set of BGP IP addresses. For more information, see[FastConnect with Multiple DRGs and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectmultipledrgs.htm). Instructions :
- In the Console, return to the details page for the connection you created earlier. Change to the Virtual Circuits tab and select Create Virtual Circuit .
- Enter the following for the new virtual circuit:
- Name : A descriptive name for the virtual circuit. The value doesn't need to be unique across all virtual circuits, and you can change it later. Avoid entering confidential information.
- Compartment : Select the compartment where you want to create the virtual circuit. If you're not sure, use the current compartment. This choice of compartment, along with a corresponding[IAM policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm), controls who has access to the virtual circuit.
- 

Select the virtual circuit type (private or public). A private virtual circuit is for private peering (where an on-premises network receives routes for a VCN's private IP addresses). A public virtual circuit is for public peering (where an on-premises network receives routes for the Oracle Cloud Infrastructure public IP addresses). Also see[Uses for FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectoverview.htm#uses).
- For a private virtual circuit, enter the following:
- Select either All traffic or IPSec over FastConnect traffic only . The virtual circuit can be used for[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectsecurity.htm#ipsec)with either choice, but you can select an option to only have encrypted traffic on the virtual circuit. For the prerequisites to use IPSec over FastConnect traffic only option, see[TransportOnly Mode: Only Allowing Encrypted Traffic on a Virtual Circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectsecurity.htm#fastconnectsecurity_topic-transport).
- Dynamic Routing Gateway : Select the DRG to route the FastConnect traffic to.
- Provisioned Bandwidth : Select the value for the bandwidth assigned to the virtual circuit. If the bandwidth needs to increase later, you can update the virtual circuit to use a different value (see[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectcolocate.htm#edit_vc)).
- VLAN : The number of the VLAN to use for this virtual circuit. It must be a VLAN not already assigned to another virtual circuit.
- Customer BGP IP Address : The BGP peering IP address for the on-premises edge (a CPE), with a subnet mask from /28 to /31.
- Oracle BGP IP Address : The BGP peering IP address you want to use for the Oracle edge (the DRG), with a subnet mask from /28 to /31.
- Enable IPv6 Address Assignment : IPv6 addressing is supported for all commercial and government regions. For more information, see[FastConnect and IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/ipv6.htm#fastconnect).
- Customer BGP ASN : The public or private ASN for an on-premises network.
- Use a BGP MD5 Authentication Key : (Optional) Select this checkbox and provide a key if your system requires MD5 authentication. Oracle supports up to 128-bit MD5 authentication.
- Enable Bidirectional Forwarding Detection : (Optional) Select this checkbox to enable[Bidirectional Forwarding Detection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectoverview.htm#concepts).
Note  
  
When you use Bidirectional Forwarding Detection, the paired device must be configured to use a 300 ms minimum interval and a multiplier of 3.
- For a public virtual circuit, enter the following:
- Provisioned Bandwidth : Select the value for the bandwidth assigned to the virtual circuit. If the bandwidth needs to increase later, you can update the virtual circuit to use a different value (see[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectcolocate.htm#edit_vc)).
- Public IP Prefixes : The public IP prefixes that you want Oracle to receive over the connection. All prefix sizes are allowed. You can enter a comma-separated list of prefixes, or one per line.
- Route Filtering : Select a[Route Filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/routingonprem.htm#route_filtering)option. This selects the routes included in BGP advertisements to an on-premises network.
- VLAN : The number of the VLAN to use for this virtual circuit. It must be a VLAN not already assigned to another virtual circuit.
- Customer BGP ASN : The public ASN for an on-premises network. Note that Oracle specifies the BGP IP addresses for a public virtual circuit.
- Use a BGP MD5 Authentication Key : (Optional) Select this checkbox and provide a key if your system requires MD5 authentication. Oracle supports up to 128-bit MD5 authentication.
- Enable Bidirectional Forwarding Detection : (Optional) Select this checkbox to enable[Bidirectional Forwarding Detection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectoverview.htm#concepts).
- (Optional) In the Redundant cross-connect panel, you can select Attach an additional cross-connect which configures the virtual circuit to span another cross-connect with another BGP session. You then select:
- Compartment : Select the compartment where you want to create the redundant virtual circuit. If you're not sure, use the current compartment. This choice of compartment, along with a corresponding[IAM policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm), controls who has access to the virtual circuit.
- Cross-connect : Select an existing cross-connect from the pull-down list.
- Customer BGP ASN : The public ASN for an on-premises network. Note that Oracle specifies the BGP IP addresses for a public virtual circuit.
- Enable IPv6 Address Assignment : IPv6 addressing is supported for all commercial and government regions. For more information, see[FastConnect and IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/ipv6.htm#fastconnect).
- Use a BGP MD5 Authentication Key (optional) : (Optional) Select this checkbox and provide a key if your system requires MD5 authentication. Oracle supports up to 128-bit MD5 authentication.
- Select Create .

The virtual circuit is created.

The virtual circuit's status is PROVISIONING briefly while Oracle's system provisions the virtual circuit. The status then switches to DOWN if the BGP session between the on-premises edge device and Oracle's edge isn't yet correctly configured, if the VLAN isn't configured correctly, or if there any other problems. Otherwise the status switches to UP.

[Task 8: Configure your edge](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Configure each of your edge routers to use the BGP information and VLAN for the virtual circuit. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn). If you need fast BGP convergence, you can use any value in these supported ranges: 6 to 60 seconds for keep-alive, and 18 to 180 seconds for hold-time. BGP timers are negotiated between the two BGP peers to the lower value used by one of the two sides.
Important  
  
For a public virtual circuit: An existing network can receive advertisements for Oracle's public IP addresses through several paths (for example: FastConnect and the internet service provider). Ensure that FastConnect has higher preference than the ISP. You must configure the edge appropriately so that traffic uses the preferred path to receive the benefits of FastConnect. This is important if you decide to also set up the existing network with[private access to Oracle services](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/transitroutingoracleservices.htm). For important information about path preferences, see[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/routingonprem.htm). If you have a cross-connect group (a LAG) with one or more cross-connects in it, here are details to know about LACP:
- LACP is required on the network interface directly plugged in to Oracle's router.
- LACP is required even if you have only a single cross-connect in the cross-connect group.
- If the third-party provider is performing any media conversion, LACP must be configured on the provider's device instead of your device. Also configure the router for redundancy according to the network design you decided on earlier. After you successfully configure BGP and the VLAN, the virtual circuit's status switches to UP.

[Task 9: Ping the Oracle BGP IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Ping the Oracle BGP IP address assigned to the virtual circuit. Check the error counters and look for any dropped packets. Don't proceed until you can successfully ping this IP address without errors.

If you set up a cross-connect group: if the ping isn't successful, and you're NOT learning MAC addresses, verify that you configured LACP as mentioned in Task 8.

[Task 10: Confirm that the BGP session is established](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

For each virtual circuit you set up, confirm the BGP session is in an established state on the on-premises side of the connection.

[Task 11: Test the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

For a private virtual circuit : To test the connection, create an instance in a VCN and access it (for example, with SSH) from a host in an existing private network. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). If the connection succeeds, the FastConnect private virtual circuit is ready to use.

For a public virtual circuit :

- Ensure that Oracle has successfully verified at least one of the public prefixes you submitted. You can see the status of each prefix by viewing the virtual circuit's details in the Console. When one of the prefixes has been validated, Oracle starts advertising the regional Oracle Cloud Infrastructure public addresses over the connection.
- Create an instance with a public IP address.
- Ping the public IP address from a host in an existing private network. If you see the packet on the FastConnect interface on the virtual circuit, the FastConnect public virtual circuit is ready to use. However, remember that only the public prefixes that Oracle has successfully verified so far are advertised on the connection.

## Managing a Connection

[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

- Open the navigation menu and select Networking . Under Customer connectivity , select FastConnect .

The FastConnect connections list page opens. All cross-connects, cross connect groups, and virtual circuits in the selected compartment are displayed in a table.
- To view the connections in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

[To get the status of a connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).

The details page opens and displays information about the connection. Some items on the page are read-only, and other items enable you to edit and update the virtual circuit's configuration. Access the various resources associated with the connection by selecting their links or tabs.

Look at the lifecycle state for the particular part of the connection that you're interested in (cross-connect group, cross-connect, or virtual circuit).

Here are reasons for particular status values:

[Cross-Connect: PENDING CUSTOMER](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

- You need to forward the LOA to the third-party provider so they can request cabling at the FastConnect location. See[Task 3: Forward the LOA to the third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_forward_loa).
- Or, you need to activate a cross-connect after confirming it's ready to use. See[Task 5: Activate each cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_activate_cc), but ensure that you performed tasks 5 and 6 first.

[Virtual circuit: DOWN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

In general this means you created a virtual circuit, but configuration is incomplete or incorrect:
- You need to configure the on-premises edge. See[Task 8: Configure your edge](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_configure_edge).
- Or, you configured BGP or the VLAN incorrectly on the on-premises edge (ensure that you configure the router to use the BGP and VLAN values assigned to the virtual circuit).

The following table summarizes the different states of each component involved in the connection at different points during setup:

Task in Setup Process CCG Icon CC Icon VC Icon
[Task 2: Set up a cross-connect group or cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_cc)PENDING PROVISIONING PENDING CUSTOMER NOT APPLICABLE
[Task 5: Activate each cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_activate_cc)PROVISIONED PROVISIONED NOT APPLICABLE
[Task 7: Set up your virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_vc)PROVISIONED PROVISIONED PROVISIONING &gt; DOWN
[Task 8: Configure your edge](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_configure_edge)PROVISIONED PROVISIONED

DOWN &gt; UP

[To add a new cross-connect to an existing cross-connect group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

When you first create a cross-connect group in the Console, you're allowed to create three cross-connects in the group. You can later add more to increase the bandwidth and resiliency of the group. The total allowed number is eight.
- 

Create the new cross-connect in the existing cross-connect group:
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- Change to the cross-connect tab, and select Add Cross-Connect .
- Enter the following items:
- Name : A descriptive name that helps you track this cross-connect. The value doesn't need to be unique across cross-connects. You can't change the name later. Avoid entering confidential information.
- Reference Name : An ID for the physical fiber cable for the cross-connect. This makes future connection troubleshooting easier. If you don't have it, you can add it later.
- 

Select Add .

The cross-connect is created. The status of the cross-connect is PENDING CUSTOMER to indicate that you have more work to do.
- Print the new cross-connect's LOA. You forward it to a third-party provider in the next step.
- Perform tasks 4 to 7 in[Getting Started with FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#getting_started). In summary, you need to have the cabling set up for the new cross-connect, validate the light levels and interfaces are good, and then activate the cross-connect.

[To deactivate and activate a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Important  
  
This action is provided so you can test failover of redundant virtual circuits as described in[Maintaining Virtual Circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../shared/../Concepts/vc-maintenance.htm). The BGP session between on-premises and OCI networks is temporarily shut down (this isn't a "graceful shutdown") and resumes quickly after failover is validated.
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list the connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../shared/../Concepts/fastconnectcolocate.htm#fastconnectcolocate_topic_To_list_your_connections).
- Select the Actions button and then select Deactivate .
- Confirm that traffic is flowing as expected on the redundant virtual circuit.
- Select the Actions button and then select Activate .

[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

You can change these items for a virtual circuit:
- The name.
- Which DRG it uses (for a private virtual circuit).
- The bandwidth.
- The BGP session information, including IPv6 addressing.
- The BGP MD5 authentication key.
- Enable or disable Bidirectional Forwarding Detection.
- The public IP prefixes (for a public virtual circuit).
- Set the virtual circuit to ACTIVE or INACTIVE.
Important  
  

Notes About Editing a Virtual Circuit

If a virtual circuit is working and in the PROVISIONED state before you edit it, be aware that changing any of the properties besides the name, bandwidth, and public prefixes (for a public virtual circuit) causes the virtual circuit's state to switch to PROVISIONING and might cause the related BGP session to go down. After Oracle reprovisions the virtual circuit, its state returns to PROVISIONED. Confirm that the associated BGP session is back up.

If you change the public IP prefixes for a public virtual circuit, the BGP status is unaffected. Oracle begins advertising a new IP prefix over the connection only after verifying ownership of it. The virtual circuit's state changes to PROVISIONING while Oracle implements any prefix changes.
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- Select the Virtual Circuits tab, and then select the virtual circuit to view its details.
- Select Edit and make changes. Avoid entering confidential information.
- Select Save Changes .
- (Optional) To temporarily deactivate a virtual circuit, select the Actions button and select Deactivate . To reactivate the circuit, select the Actions button and select Activate . Deactivating the virtual circuit suspends the BGP session and traffic flow without otherwise changing the settings for the virtual circuit.

[To edit a cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

You can change these items for a cross-connect:
- The name.
- The reference name.
- [MACsec](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectsecurity.htm#macsec)settings.
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).
- Select Edit and make changes. Avoid entering confidential information.
- Select Save Changes .

[To manage public IP prefixes for a public virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

For general information about the prefixes, see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectoverview.htm#diagrams).

You can specify public IP prefixes when you create the virtual circuit. See[Task 7: Set up your virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectcolocate.htm#task_set_up_vc).

You can add or remove public IP prefixes later after creating the virtual circuit. See[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/fastconnectcolocate.htm#edit_vc). If you add a new prefix, Oracle first verifies your company's ownership before advertising it across the connection. If you remove a prefix, Oracle stops advertising the prefix within a few minutes of editing the virtual circuit.

You can view the state of Oracle's verification of a particular public prefix by viewing the virtual circuit's details in the Console. Here are the possible values:
- In progress : Oracle is in the process of verifying your organization's ownership of the prefix.
- Failed : Oracle couldn't verify your organization's ownership. Oracle won't advertise the prefix over the virtual circuit.
- Completed : Oracle successfully verified your organization's ownership. Oracle is advertising the prefix over the virtual circuit.

[To move a connection to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

You can move a connection from one compartment to another. After you move the connection to the new compartment, inherent policies apply immediately and affect access to the connection through the Console. Moving the connection to a different compartment doesn't affect the connection between an on-premises data center and Oracle Cloud Infrastructure. For more information, see[To move a resource to a different compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To_move_a_resource_to_a_different_compartment).
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- From the Actions menu (three dots) for the connection, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- If alarms are monitoring the connection, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm)for more information.

[To terminate a connection, or part of it](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

To stop being billed for a connection, you must terminate the virtual circuit, each cross-connect, and the cross-connect group associated with the connection (in that order).
Important  
  
Also terminate the connection with the data center or third-party provider, or else they might continue to bill you.

[To terminate a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- Select the Virtual Circuits tab, and then select the virtual circuit to view its details.
- Select the Actions button, then select Delete .
- Confirm when prompted.

The virtual circuit's status changes to TERMINATING and then to TERMINATED.

[To terminate a cross-connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

If you have several cross-connects to delete in a cross-connect group, wait until the state of the first one changes to TERMINATED before deleting the next one. Also, you can't delete a cross-connect if it's the last provisioned cross-connect in a cross-connect group that's being used by a provisioned virtual circuit.
- On the FastConnect connections list page, find the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- Select the Cross-Connects tab.
- From the Actions menu (three dots) for the cross-connect, select Delete .
- When prompted, confirm the deletion.

The cross-connect's status changes to TERMINATING and then to TERMINATED.

[To terminate a cross-connect group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#)

Prerequisite: The cross-connect group must have no virtual circuits running on it and contain no cross-connects.
- On the FastConnect connections list page, find the connection that you want to work with. If you need help finding the list page, see[To list connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#fastconnectthirdpartyprovider_topic_To_list_connections).
- From the Actions menu (three dots) for the cross-connect group, select Delete .
- When prompted, confirm the deletion.

The cross-connect group's status changes to TERMINATING and then to TERMINATED.

## Monitoring the Connection

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

For information about monitoring a connection, see[FastConnect Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Reference/fastconnectmetrics.htm).

## Troubleshooting

See[FastConnect Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Troubleshoot/fastconnecttroubleshoot.htm)
