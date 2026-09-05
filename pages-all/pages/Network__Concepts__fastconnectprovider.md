# FastConnect: With an Oracle Partner
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm
- Fetched: 2026-09-05 02:41 CDT

# FastConnect: With an Oracle Partner

Learn about how to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.

For a summary of the different ways to connect, see[How and Where to Connect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#How).

If you instead want to use a network provider that's not on the list of[FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/), see[FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm). Or to use FastConnect by colocating with Oracle, see[FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm).

For general information about FastConnect, see[FastConnect Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm).

## Getting Started with FastConnect

Before you start, walk through the planning in[Before Getting Started: Learn and Plan](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#Before). Also see[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)and[Hardware and Routing Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#requirements).

You might also need to review information on how[to use FastConnect if you do not own a Public ASN or Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#public_asn_ip).

The following diagram shows the overall process of setting up FastConnect with an Oracle partner. The tasks that follow are represented in the diagram.
[

Also see the sequence diagram in[To get the status of a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#get_connection_status).

[Task 1: Set up connection to the Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

If you haven't already, start the process of ordering the connection from the Oracle partner, setting it up, and then testing it with the partner. It can take some time, depending on the partner.

[Task 2: Set up a DRG (private peering only)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Summary : If you plan to use a private virtual circuit (private peering), you need a DRG. If you haven't already, use the Oracle Cloud Infrastructure Console to set up a DRG, attach it to the VCN, and update routing in the VCN to include a route rule to send traffic to the DRG. Remember to update the route table. Without the route rule, no traffic can flow.

Instructions :
- [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/drg-create.htm)
- [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/attach-vcn-drg.htm)
- [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/update-rules-routetable.htm)

[Task 3: Set up virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Summary: Create one or more virtual circuits for a connection in the Oracle Console. If the network design includes more than one virtual circuit, complete the following steps for each one.

When you create a virtual circuit using an Oracle Partner, OCI metering starts when the virtual circuit is established.

Instructions :

Repeat the following steps for each virtual circuit you want to create.
- On the FastConnect connections list page, select Create FastConnect . If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).
- Select FastConnect partner and then select either Single virtual circuit (the default) or Redundant virtual circuits to configure virtual circuits that use different physical devices in the same FastConnect location.

See[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)for more about redundancy. If you select Single virtual circuit you can return later to add a redundant virtual circuit.
- Select Next .
- 

Enter the following for the virtual circuit ( Virtual circuit 1 if you selected Redundant virtual circuits ):
- Name : A descriptive name for the virtual circuits. The value doesn't need to be unique across virtual circuits, and you can change it later. Avoid entering confidential information.
- Create in Compartment : Leave as is (the compartment you're working in).
- Select Partner and select the partner from the list.
Note  
  
If you select Megaport as the partner, you can provision the partner side of the circuit using the optional steps mentioned.
- 

Select the virtual circuit type (private or public). A private virtual circuit is for private peering (where the on-premises network receives routes for the available private IP addresses). A public virtual circuit is for public peering (where the on-premises network receives routes for the Oracle Cloud Infrastructure public IP addresses). Redundant virtual circuits must both be private, or both public, so this setting is matched on the other virtual circuit. Also see[Uses for FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#uses).
- 

For a private virtual circuit, enter the following:
- Select either All traffic or IPSec over FastConnect traffic only . The virtual circuit can be used for[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec)with either choice, but you can select to only allow encrypted traffic on the virtual circuit. Redundant virtual circuits must have the same setting, so this is matched on the other virtual circuit.
- Dynamic Routing Gateway : Select the DRG to route the FastConnect traffic to. IPSec over FastConnect requires an[upgraded](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingDRGs.htm#overview__Versions)DRG. This DRG could be attached to several VCNs or to other DRGs with attached VCNs.
- Provisioned Bandwidth : Select a value. If the bandwidth needs increase later, you can update the virtual circuit to use a different value (see[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#edit_vc)).
- Partner Service Key : (Optional) Enter the service key provided by the Oracle partner. You can enter this key now or edit the circuit later. If the partner chosen is AT&amp;T Netbond, you can add a placeholder service key or leave the field blank in the virtual circuit creation phase. See[OCI FastConnect for AT&amp;T Partner - simplified procedure](https://www.ateam-oracle.com/post/oci-fastconnect-for-att-partner-simplified-procedure)for more details.

If the BGP session goes to Oracle (see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams)), the dialog box includes other fields for the BGP session:
- Customer BGP IP Address : The BGP peering IP address for the edge device (the CPE), with a subnet mask from /28 to /31.
- Oracle BGP IP Address : The BGP peering IP address you want to use for the Oracle edge (the DRG), with a subnet mask from /28 to /31.
- Enable IPv6 Address Assignment : IPv6 addressing is supported for all commercial and government regions. See[FastConnect and IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#fastconnect).
- Customer BGP ASN : The public or private ASN for the network.
- Use a BGP MD5 Authentication Key : (Optional) Select this checkbox and provide a key if the system requires MD5 authentication. Oracle supports up to 128-bit MD5 authentication.
- Enable Bidirectional Forwarding Detection : (Optional) Select this checkbox to enable[Bidirectional Forwarding Detection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#concepts).
Note  
  
When you use Bidirectional Forwarding Detection, a paired device must be configured to use a 300 ms minimum interval and a multiplier of 3.
- 

For a public virtual circuit, enter the following:
- Provisioned Bandwidth : Select a value. If the bandwidth needs increase later, you can update the virtual circuit to use a different value (see[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#edit_vc)).
- Public IP Prefixes : The public IP prefixes that you want Oracle to receive over the connection. All prefix sizes are allowed. You can enter a comma-separated list of prefixes, or one per line.
- Route Filtering : Select a[Route Filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)option. This selects the routes included in BGP advertisements to an on-premises network.
- BGP ASN : The public ASN for the network. Present only if the BGP session goes to Oracle (see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams)). Oracle specifies the BGP IP addresses for a public virtual circuit.
- Use a BGP MD5 Authentication Key : (Optional) Select this checkbox and provide a key if the system requires MD5 authentication. Oracle supports up to 128-bit MD5 authentication.
- Enable Bidirectional Forwarding Detection : (Optional) Select this checkbox to enable[Bidirectional Forwarding Detection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#concepts).
- If you're creating a redundant virtual circuit, enter the necessary information for the other virtual circuit ( Virtual circuit 2 ). If you selected Redundant virtual circuits , remember that the virtual circuit type (private or public) and All traffic or IPSec over FastConnect traffic only settings for Virtual circuit 2 are already set to match Virtual circuit 1 and if you change them the settings on the other circuit automatically change to match. If you have service agreements with more than one Oracle Partner, you can select different partners for Virtual circuit 1 and Virtual circuit 2 as long as you select the same Dynamic Routing Gateway . You can also select a different Dynamic Routing Gateway and Provisioned Bandwidth , but this requires configuring peering between the two DRGs and doesn't improve the redundancy posture.
Note  
  
Creating a redundant virtual circuit is optional if you selected Redundant virtual circuits and the partner you selected creates a Layer 3 connection to OCI, but a redundant virtual circuit is required if the partner you selected creates a Layer 2 connection. See[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)for more about Layer 2 and Layer 3 connections.
- 

Select Create .

The virtual circuit is created and displays a status page. Select Close to return to the list of virtual circuits.
- Select the name of the virtual circuit you created. While the virtual circuit is in the PENDING PARTNER state, its OCID and a link to the partner's portal are displayed in the "Connection created" confirmation box at the top of the page. The virtual circuit's OCID is also available with the other virtual circuit details. Copy and paste the OCID to another location. You give it to the Oracle partner in the next task. Also copy the OCID for the redundant circuit if you created one.

Until you complete the next task and the partner does their provisioning work, the virtual circuit's Lifecycle State is PENDING PARTNER and the BGP state is DOWN. After the partner does their work, the Lifecycle State switches to PROVISIONED. When the BGP session is established and working, the BGP state changes to UP.
Tip  
  
For a virtual circuit where the BGP session goes to the Oracle partner, the BGP state for the virtual circuit reflects the status of the separate BGP session between the Oracle partner and Oracle . For reference, see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams).

Also see the diagram in[To get the status of a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#get_connection_status).

[Task 4: Complete the partner end of the virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Contact the partner and give the OCID of each virtual circuit that you created, along with any other information the partner requests. Depending on the partner, you might do this in the partner's online portal, or over the phone. The partner then configures each virtual circuit on their end to complete the connectivity.

If your partner is either Megaport or Colt, you can also connect the OCI Console to the partner and complete the connection yourself from within the OCI Console as described in the following sections.

If your partner is AT&amp;T NetBond: To expedite virtual circuit activation, update the details for the virtual circuit with the service key after completing AT&amp;T Console setup steps. See[OCI FastConnect for AT&amp;T Partner - simplified procedure](https://www.ateam-oracle.com/post/oci-fastconnect-for-att-partner-simplified-procedure)for more details.

#### Complete virtual circuits to Megaport

The Oracle Console can add and configure a connection in the Megaport location to this virtual circuit using Megaport's API. To do this, sign in to your Megaport account with a valid username and password (the Oracle Console doesn't store the information).
Note  
  
If you're completing setup of a virtual circuit, you must have already[configured a Megaport port](https://docs.megaport.com/connections/creating-port/)in the Megaport Console to use this option. The Oracle Console can add and configure a connection to this virtual circuit for a Megaport port that already exists. It can't create a new Megaport port at the other end of the connection. This requirement doesn't apply if you're configuring a connection to another cloud provider.

The Oracle Console can optionally configure a[Megaport Cloud Router (MCR)](https://docs.megaport.com/mcr/)at the other end of the virtual circuit. An MCR can configure a connection from Oracle to AWS or other cloud service providers.

To complete a connection or create an MCR:
- At the top of the details screen for the virtual circuit you created, select Complete Connection in the Next Steps section.
- Enter the requested Megaport Username and Megaport Password for the account that created the Megaport port you want to use.
- Select Log in to Megaport .
- To complete a virtual circuit to an on-premises network, select Megaport Port for the Megaport Product and enter the following information:
- Oracle Connection Name : (Required) A friendly name that helps Megaport track the connection. The value doesn't need to be unique and you can change it later.
- Megaport Port : (Required) Select the name of the Megaport port to which you want to connect this virtual circuit.
- Oracle Connection Location (Required) Select any Megaport location close to the Oracle region for the virtual circuit.
- Connection Rate Limit (Mbps) : (Required) Enter the speed (in Mbps) for the virtual circuit. 1000 Mbps is 1 Gbps, and 10,000 Mbps is 10 Gbps. The Rate Limit must be equal to or less than the bandwidth provisioned at both ends of the virtual circuit.
- Use VLAN tagging : Enabled by default. If you decide not to use VLAN tagging, you're only able to deploy a single cross-connect on this Megaport port.
- Preferred A-End VLAN : (Optional) If you don't select a Preferred A-End VLAN, a random A-End VLAN is chosen for you.

Select Next .
- To complete a virtual circuit to another cloud provider, select Megaport Cloud Router (MCR) for the Megaport Product and enter the following information:
- Select Select an existing MCR or Create a new MCR : If you have already connected a third-party cloud service to an MCR, select Select an existing MCR select an MCR from the list. To Create a new MCR enter the following information:
- MCR Name : (Required) A friendly name that helps Megaport track the MCR. The value doesn't need to be unique and you can change it later.
- MCR Country : (Required) Select the country for the Megaport location where the MCR resides.
- MCR Location : (Required) Select the Megaport location where the MCR resides. Make this as close as possible to the Oracle region hosting the virtual circuit.
- MCR Rate Limit : (Required) The rate limit is an aggregate capacity for all connections through the MCR. The rate limit can scale from 1 Gbps to 10 Gbps and is set for the life of the MCR.
- Minimum Term : (Required) (options are no minimum, 12 month, 24 month, 36 month)
- Oracle Connection Name : (Required) A friendly name that helps Megaport track the Oracle connection. The value doesn't need to be unique and you can change it later.
- Oracle Connection Location : (Required) Select the Megaport location where the Oracle connection resides. Make this as close as possible to the Oracle region hosting the virtual circuit.
- Connection Rate Limit (Mbps) : (Required) Enter the speed (in Mbps) for the connection. 1000 Mbps is 1 Gbps, and 10,000 Mbps is 10 Gbps. The setting must be equal to or less than the bandwidth provisioned at both ends of the virtual circuit.
- Create a connection to AWS : Check this only if the third-party cloud service is AWS. Enter the following information:
- AWS Connection Name : (Required) This information is used to connect AWS to the Megaport MCR.
- AWS Account ID : (Required) Provide an AWS Account ID. Oracle doesn't retain this information.
- MCR Country : (Required) Select the country for the Megaport location where the MCR resides.
- AWS Connection Location : (Required) Select any Megaport location close to the AWS region for the connection.
- Connection Rate Limit (Mbps) : (Required) Enter the speed (in Mbps) for the connection. 1000 Mbps is 1 Gbps, and 10,000 Mbps is 10 Gbps. The setting must be equal to or less than the bandwidth provisioned at both ends of the connection.

To connect to a third-party cloud service (other than AWS), leave Create a connection to AWS unselected. For any third-party cloud service, including AWS, you also need to configure the remainder of the connection using the Megaport Console and the Console for the third-party cloud service.

Select Next .
- Confirm that the information about the circuit or MCR is correct by reviewing the displayed information.
- Confirm the quoted price of this service (paid to Megaport and not to Oracle) by selecting the Accept checkbox.
- Select Complete Connection when finished.

If for any other reason all resources can't be configured as entered, the component that can't be configured is automatically deleted. You can select Previous and enter slightly different information to resolve the issue.

After you complete these steps, expect the FastConnect virtual circuit to be in the PENDING PARTNER state while the connection provisions.

#### Complete virtual circuits to Colt

The Oracle Console can add and configure a connection to this virtual circuit using Colt's API. To do this, you log the Console into your Colt account with a valid username and password (the Oracle Console doesn't store sign-in information).
Note  
  
You must have already configured a port in the Colt Console to use this option. The Oracle Console can add and configure a connection to this virtual circuit for a port that already exists, but it can't create a new port for the connection.

To use this feature:
- At the top of the details screen for the virtual circuit you created, select Complete Connection in the Next Steps section.
- Create Connection .
- Enter the requested Colt Username and Colt Password for the account that created the Colt port you want to use.
- Select Log in to Colt .
- 

Enter the following information:
- Connection Name : (Required) A friendly name that helps Colt track the connection. The value doesn't need to be unique and you can change it later.
- Colt Ethernet Port : (Required) Select the name of the Ethernet port to which you want to connect this virtual circuit.
- Oracle Connection Location : (Required) Select any Colt location close to the Oracle region for the virtual circuit.
- Connection Bandwidth : (Required) Enter the speed (in Mbps) for the virtual circuit. 1000 Mbps is 1 Gbps, and 10,000 Mbps is 10 Gbps. The setting must be equal to or less than the bandwidth provisioned at both ends of the virtual circuit.
- Connection Commitment Period : This entry selects the length of the commitment that you make with Colt for this connection. See Colt's policies regarding extending commitments or ending them early.
- Preferred B-End VLAN : (Optional) If you don't select a Preferred B-End VLAN, a random B-End VLAN is chosen for you.
- Select Next .
- Confirm that the information about the circuit is correct by reviewing the displayed information.
- Confirm the quoted price of this circuit (paid to Colt and not to Oracle) by selecting the Accept checkbox.
- Select Create when finished.

After you complete these steps, expect the virtual circuit to be in the PENDING PARTNER state while the connection provisions.

[Task 5: Configure your edge](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

If the BGP session goes to Oracle : (see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams)), configure the edge device (your CPE) to use the BGP peering information (see[General Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#General)). Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see[Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#bgp_asn). If you need fast BGP convergence, you can use any value in these supported ranges: 6 to 60 seconds for keep-alive, and 18 to 180 seconds for hold-time. BGP timers are negotiated between the two BGP peers to the lower value used by one of the two sides. Also configure the router for redundancy according to the network design you decided on earlier (see[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)). After you successfully configure the BGP session, the virtual circuit's BGP session state changes to UP.

If the BGP session instead goes to the Oracle partner : You still need to configure the router if you haven't already. You might need to contact the partner to get the required BGP peering information. This BGP session must be up and running for FastConnect to work. Also configure the edge router for redundancy according to the network design you decided on earlier (see[FastConnect Redundancy Best Practices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm)).
Important  
  
For a public virtual circuit: An existing network can receive advertisements for Oracle's public IP addresses through several paths (for example: FastConnect and the internet service provider). Ensure that FastConnect has higher preference than the ISP. You must configure the edge appropriately so that traffic uses the preferred path to receive the benefits of FastConnect. This is important if you decide to also set up the existing network with[private access to Oracle services](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/transitroutingoracleservices.htm). For important information about path preferences, see[Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/routingonprem.htm).

[Task 6: Check light levels](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Confirm that the light levels are good for each of the physical network connections to the partner. Don't proceed until they are.

[Task 7: Confirm the interfaces are up](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Confirm your side of the interfaces for the connections to the partner are up. Don't proceed until they are.

### If the BGP Session Goes to Oracle

[Task 9a: Ping the Oracle BGP IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

For each virtual circuit, ping the Oracle BGP IP address assigned to the virtual circuit. Check the error counters and look for any dropped packets. Don't proceed until you can successfully ping this IP address without errors.

[Task 9b: Confirm that the BGP session is established](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Confirm that each virtual circuit's BGP session is in an established state and therefore ready to test (see[Task 11: Test the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#test_connection)).

### If the BGP Session Goes to the Partner

[Task 10a: Ping the partner's edge](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

For each virtual circuit, ping the partner's edge. Check the error counters and look for any dropped packets. Don't proceed until you can successfully ping the partner's edge without errors.

[Task 10b: Confirm the BGP session is established](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Confirm the BGP session you have with the partner is in an established state. Don't proceed until it is.

[Task 10c: Ping the Oracle BGP IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

For each virtual circuit, ping the Oracle BGP IP address (which you can get from the partner). Check the error counters and look for any dropped packets. When you can successfully ping this IP address without errors, the connection is ready to test.

[Task 11: Test the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

For a private virtual circuit: Tu run this test, you must create an instance in a VCN and access it (for example, with SSH) from a host in an existing private network. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). If you can, the FastConnect private virtual circuit is ready to use.

For a public virtual circuit:

- Ensure that Oracle has successfully verified at least one of the public prefixes you submitted. You can see the status of each prefix by viewing the virtual circuit's details in the Console. When one of the prefixes has been validated, Oracle starts advertising the regional Oracle Cloud Infrastructure public addresses over the connection.
- Create an instance with a public IP address.
- Ping the public IP address from a host in an existing private network. If you see the packet on the FastConnect interface on the virtual circuit, the FastConnect public virtual circuit is ready to use. However, remember that only the public prefixes that Oracle has successfully verified so far are advertised on the connection.

## Managing a Virtual Circuit

[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

- Open the navigation menu and select Networking . Under Customer connectivity , select FastConnect .

The FastConnect connections list page opens. All virtual circuits in the selected compartment are displayed in a table.
- To view the virtual circuits in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

[To get the status of a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

- On the FastConnect connections list page, select the virtual circuit that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).

The details page opens and displays information about the virtual circuit. Some items on the page are read-only, and other items enable you to edit and update the virtual circuit's configuration. Access the various resources associated with the virtual circuit by selecting their links or tabs.

The following diagram shows the different states of the virtual circuit when you're setting it up.
[

[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

You can change these items for a virtual circuit:
- The name.
- The bandwidth.
- The service key provided by an Oracle partner (for a private virtual circuit).
- Which DRG it uses (for a private virtual circuit).
- The public IP prefixes (for a public virtual circuit).
- Enable or disable Bidirectional Forwarding Detection.
- Configure the virtual circuit to only allow traffic using[IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec). By default any traffic is allowed.
- Depending on the situation, you might also have access to the BGP session information for the virtual circuit and thus can change it.
Important  
  

If a virtual circuit is working and in the PROVISIONED state before you edit it, be aware that changing any of the properties besides the name, bandwidth, and public prefixes (for a public virtual circuit) causes the virtual circuit's state to switch to PROVISIONING and might cause the related BGP session to go down. After Oracle reprovisions the virtual circuit, its state returns to PROVISIONED. Confirm that the associated BGP session is back up.

If you change the public IP prefixes for a public virtual circuit, the BGP status is unaffected. Oracle begins advertising a new IP prefix over the connection only after verifying ownership of it. The virtual circuit's state changes to PROVISIONING while Oracle implements any prefix changes.
- On the FastConnect connections list page, select the virtual circuit that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).
- Select Edit and make changes. Avoid entering confidential information.
- Select Save Changes .
- (Optional) To temporarily deactivate a virtual circuit, select the Actions button and select Deactivate . To reactivate the circuit, select the Actions button and select Activate . Deactivating the virtual circuit suspends the BGP session and traffic flow without otherwise changing the settings for the virtual circuit.

[To deactivate and activate a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Important  
  
This action is provided so you can test failover of redundant virtual circuits as described in[Maintaining Virtual Circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../shared/../Concepts/vc-maintenance.htm). The BGP session between on-premises and OCI networks is temporarily shut down (this isn't a "graceful shutdown") and resumes quickly after failover is validated.
- On the FastConnect connections list page, select the connection that you want to work with. If you need help finding the list page, see[To list the connections](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../shared/../Concepts/fastconnectcolocate.htm#fastconnectcolocate_topic_To_list_your_connections).
- Select the Actions button and then select Deactivate .
- Confirm that traffic is flowing as expected on the redundant virtual circuit.
- Select the Actions button and then select Activate .

[To manage public IP prefixes for a public virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

For general information about the prefixes, see[Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams).

You can specify public IP prefixes when you create the virtual circuit. See[Task 3: Set up virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#set_up_vc).

You can add or remove public IP prefixes later after creating the virtual circuit. See[To edit a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#edit_vc). If you add a new prefix, Oracle first verifies ownership before advertising it across the connection. If you remove a prefix, Oracle stops advertising the prefix within a few minutes of editing the virtual circuit.

You can view the state of Oracle's verification of a particular public prefix by viewing the virtual circuit's details in the Console. Here are the possible values:
- In progress : Oracle is in the process of verifying ownership of the prefix.
- Failed : Oracle couldn't verify ownership. Oracle doesn't advertise the prefix over the virtual circuit.
- Completed : Oracle successfully verified ownership. Oracle is advertising the prefix over the virtual circuit.

[To move a connection to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

You can move a connection from one compartment to another. After you move the connection to the new compartment, inherent policies apply immediately and affect access to the connection through the Console. Moving the connection to a different compartment doesn't affect the connection between a data center and Oracle Cloud Infrastructure. For more information, see[Moving a Compartment to a Different Parent Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#MoveCompartment).
- On the FastConnect connections list page, find the virtual circuit that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).
- From the Actions menu (three dots) for the virtual circuit, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- If alarms are monitoring the connection, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm)for more information.

[To terminate a virtual circuit](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#)

Important  
  
Also terminate the connection with the partner, or else the partner might continue to bill you.
- On the FastConnect connections list page, find the virtual circuit that you want to work with. If you need help finding the list page, see[To list virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#fastconnectprovider_topic_To_list_virtual_circuits).
- From the Actions menu (three dots) for the virtual circuit, select Delete .
- When prompted, confirm the deletion.

The virtual circuit's Lifecycle State changes to TERMINATING and then to TERMINATED.

## Monitoring a Connection

You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

For information about monitoring a connection, see[FastConnect Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Reference/fastconnectmetrics.htm).

## Troubleshooting

See[FastConnect Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Troubleshoot/fastconnecttroubleshoot.htm)
