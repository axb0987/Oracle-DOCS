# Remote VCN Peering using a Legacy DRG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm
- Fetched: 2026-09-05 02:46 CDT

# Remote VCN Peering using a Legacy DRG

This topic is about remote VCN peering. In this case, remote means that the VCNs reside in different regions. If the VCNs you want to connect are in the same region, see[Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm).
Note  
  
This article assumes the DRG is a legacy DRG, and we recommend the method described in[Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)for any upgraded DRG. See[DRG versions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions)for an explanation of the DRG versions.

## Overview of Remote VCN Peering

Remote VCN peering is the process of connecting two VCNs in different regions (but the same tenancy ). Peering lets the VCNs' resources communicate using private IP addresses without routing the traffic over the internet or through an on-premises network. Without peering, a VCN would need an[internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm)and public IP addresses for the instances that need to communicate with another VCN in a different region.

### Summary of Networking Components for Remote Peering

At a high level, the Networking service components required for a remote peering include:
- 

Two VCNs with CIDRs that don't overlap, in different regions that support remote peering.
Note  
  

All VCN CIDRs Must Not Overlap

The two VCNs in the peering relationship must not have overlapping CIDRs. Also, if a particular VCN has several peering relationships, those other VCNs must not have overlapping CIDRs with each other. For example, if VCN-1 is peered with VCN-2 and also VCN-3, then VCN-2 and VCN-3 must not have overlapping CIDRs.
- A Dynamic Routing Gateway (DRG) attached to each VCN in the peering relationship. A VCN already has a DRG if you're using a[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm)IPSec tunnel or an[Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm)private virtual circuit.
- A remote peering connection (RPC) on each DRG in the peering relationship.
- A connection between those two RPCs.
- Supporting[route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if required).
- Supporting[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN.

The following diagram illustrates the components.
[
Note  
  
A VCN can only use the connected RPCs to reach VNICs in the other VCN or an on-premises network, and not destinations outside of the VCNs such as the internet. For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 couldn't use it to send traffic to endpoints on the internet. For more information, see[Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2).

### Spoke-to-Spoke: Remote Peering with Transit Routing
Note  
  
The scenario this section mentions is still supported, but is deprecated. We recommend you use the DRG Transit routing method described in[Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm).

Imagine that in each region you have several VCNs in a hub-and-spoke layout, as shown in the following diagram. This type of layout within a region is discussed in detail in[Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm). The spoke VCNs in a particular region are[locally peered](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm)with the hub VCN in the same region, using local peering gateways .

You can set up remote peering between the two hub VCNs. You can then also set up transit routing for the hub VCN's DRG and LPGs, as discussed in[Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm). This setup lets a spoke VCN in one region communicate with one or more spoke VCNs in the other region without needing a remote peering connection directly between those VCNs.

For example, you could configure routing so that resources in VCN-1-A could communicate with resources in VCN-2-A and VCN-2-B by way of the hub VCNs. That way, VCN 1-A isn't required to have a separate remote peering with each of the spoke VCNs in the other region. You could also set up routing so that VCN-1-B could communicate with the spoke VCNs in region 2, without needing its own remote peerings to them.
[

### Explicit Agreement Required from Both Sides
Peering involves two VCNs in the same tenancy that might be administered by the same party or two different ones. The two parties might both be in the same company but in different departments.

Peering between two VCNs requires explicit agreement from both parties in the form of Oracle Cloud Infrastructure Identity and Access Management policies that each party implements for their own VCN's compartment .

## Important Remote Peering Concepts

The following concepts help you understand the basics of peering and how to establish a remote peering. PEERING A peering is a single peering relationship between two VCNs. Example: If VCN-1 peers with two other VCNs, then two peerings exist. The remote part of remote peering indicates that the VCNs are in different regions. VCN ADMINISTRATORS In general, VCN peering can occur only if both of the VCN administrators agree to it. In practice, this means that the two administrators must:
- Share some basic information with each other.
- Coordinate to set up the required Oracle Cloud Infrastructure Identity and Access Management policies to enable the peering.
- Configure their VCNs for the peering. Depending on the situation, a single administrator might be responsible for both VCNs and the related policies. For more information about the required policies and VCN configuration, see[Setting Up a Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Setting). ACCEPTOR AND REQUESTOR To implement the IAM policies required for peering, the two VCN administrators must select one administrator as the requestor and the other as the acceptor . The requestor must be the one to start the request to connect the two RPCs. In turn, the acceptor must create a particular IAM policy that gives the requestor permission to connect to RPCs in the acceptor's compartment . Without that policy, the requestor's request to connect fails. REGION SUBSCRIPTION To peer with a VCN in another region, a tenancy must first be subscribed to that region. For information about subscribing, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm). REMOTE PEERING CONNECTION (RPC) A remote peering connection (RPC) is a component you create on the DRG attached to a VCN. The RPC's job is to act as a connection point for a remotely peered VCN. As part of configuring the VCNs, each administrator must create an RPC for the DRG on their VCN. A specific DRG must have a separate RPC for each remote peering it establishes for the VCN. To continue with the previous example: the DRG on VCN-1 would have two RPCs to peer with two other VCNs. In the API, a[RemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/)is an object that contains information about the peering. You can't reuse an RPC to later establish another peering with it. CONNECTION BETWEEN TWO RPCS When the requestor starts the request to peer (in the Console or API), they're effectively asking to connect the two RPCs . This means the requestor must have information to identify each RPC (such as the RPC's region and OCID ). Either VCN administrator can end a peering by deleting their RPC. In that case, the other RPC's status switches to REVOKED. The administrator could instead deactivate the connection by removing the route rules that enable traffic to flow across the connection (see the next section). ROUTING TO THE DRG As part of configuring the VCNs, each administrator must update the[VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)to enable traffic to flow between the VCNs. For each subnet that needs to communicate with the other VCN, update the subnet's route table. The route rule specifies the destination traffic's CIDR and the DRG as the target. The DRG routes traffic that matches that rule to the other DRG, which in turn routes the traffic to the next hop in the other VCN. In the following diagram, VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) destined for an instance in VCN-2 (192.168.0.15) is routed to DRG-1 based on the rule in Subnet A's route table. From there the traffic is routed through the RPCs to DRG-2, and then from there, on to the destination in Subnet X.
[

Callout 3: Subnet A Route Table
Destination CIDR Route Target
0.0.0.0/0 Internet Gateway
192.168.0.0/16 DRG-1

Callout 4: Subnet X Route Table
Destination CIDR Route Target
10.0.0.0/16 DRG-2
Note  
  

As mentioned earlier, a VCN can only use the connected RPCs to reach VNICs in the other VCN, and not destinations outside of the VCNs (such as the internet or an on-premises network). For example, in the preceding diagram, VCN-2 can't use the internet gateway attached to VCN-1. SECURITY RULES Each subnet in a VCN has one or more[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm)that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must decide which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists to allow the traffic. If you use[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)(NSGs) to implement security rules, notice that you have the option to write security rules for an NSG that specify another NSG as the source or destination of traffic. However, the two NSGs must belong to the same VCN .

## Important Implications of Peering

If you haven't yet, read[Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2)to understand important access control, security, and performance implications for peered VCNs.

## Setting Up a Remote Peering

This section covers the general process for setting up a peering between two VCNs in different regions.
Important  
  

The following procedure assumes that:
- This tenancy is subscribed to the other VCN's region. If it's not, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm).
- You already have a DRG attached to the VCN. If you don't, see[Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm).
- Create the RPCs: Each VCN administrator creates an RPC for their own VCN's DRG.
- Share information: The administrators share the basic required information.
- Set up the required IAM policies for the connection: The administrators set up IAM policies to enable the connection to be established.
- Establish the connection: The requestor connects the two RPCs (see[Important Remote Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)for the definition of the requestor and acceptor ).
- Update route tables: Each administrator updates their VCN's route tables to enable traffic between the peered VCNs or subnets.
- Update security rules: Each administrator updates their VCN's security rules to enable traffic between the peered VCNs or subnets.

The administrators can perform tasks E and F before establishing the connection. Each administrator needs to know the CIDR block or specific subnets from the other VCN and share that in task B.

[Task A: Create the RPCs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

Each[acceptor or requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)administrator creates an RPC for their own VCN's DRG.
Note  
  

Required IAM Policy to Create RPCs

If the administrators already have broad network administrator permissions (see[Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)), then they have permission to create, update, and delete RPCs. Otherwise, here's an example policy giving the necessary permissions to a group called RPCAdmins. The second statement is required because creating an RPC affects the DRG it belongs to, so the administrator must have permission to manage DRGs.

```

```

See[Creating a Remote Peering Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm)and[Remote Peering Management](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-manage-rpc.htm)for general instructions on creating and working with RPCs. If you're the acceptor, record the RPC's region and OCID and share that information with the requestor. If the two VCNs are in different tenancies, each administrator must record their tenancy OCID (found on the very bottom of the page in the Console) and give this information to the other administrator.

[Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

- 

If you're the acceptor, give this information to the requestor (for example, by email or other out-of-band method):
- The region the VCN is in (the requestor's tenancy must be subscribed to this region).
- The RPC's OCID.
- The CIDR blocks for subnets in the VCN to make available to the other VCN. The requestor needs this information when setting up routing for the requestor VCN.
- 

If you're the requestor, give this information to the acceptor:
- The region the VCN is in (the acceptor's tenancy must be subscribed to this region).
- The name of the IAM group to grant permission to create a connection in the acceptor's compartment.
- The CIDR blocks for subnets in the VCN to make available to the other VCN. The acceptor needs this information when setting up routing for the acceptor VCN.

[Task C: Set up the IAM policies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

When both VCNs are in the same tenancy but different regions, use the policies provided in[Remote Peering with DRG (in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy).

If both VCNs are in different tenancies but the same region, use the policies provided in[Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN).

[Task D: Establish the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

The requestor must perform this task.

Prerequisite: The requestor must have:
- The region the acceptor's VCN is in (the requestor's tenancy must be subscribed to the region).
- The OCID of the acceptor's RPC.

See[Creating a Remote Peering Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm)for general instructions, and use the information provided for the acceptor. See[Remote Peering Management](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-manage-rpc.htm)for general instructions on working with RPCs.

[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

As mentioned earlier, each administrator can do this task before or after the connection is established.

Prerequisite: Each administrator must have the VCN CIDR block or the CIDR block for specific subnets in the other VCN.

For each VCN, decide which subnets in the VCN need to communicate with the other VCN and update the route table (see[Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)) for each of those subnets to include a new route rule that directs traffic destined for the other VCN to the DRG:
- Target Type: Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself.
- Destination CIDR Block: The other VCN's CIDR block. If you want, you can specify a subnet or particular subset of the peered VCN's CIDR.
- Description: An optional description of the rule.

Any subnet traffic with a destination that matches the rule is routed to the DRG. For more information about VCN route tables and rules, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).
Tip  
  
Without the required routing, traffic doesn't flow between the peered DRGs. If a situation occurs where you need to temporarily stop the peering, temporarily remove the route rules that enable traffic. You don't need to delete the RPCs.

[Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

As mentioned earlier, each administrator can do this task before or after the connection is established.

Prerequisite: Each administrator must know the CIDR block or specific subnets to share with the other VCN. In general, use the same CIDR block you used in the route table rule in[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4).

Add the following rules:
- Ingress rules for the types of traffic you want to allow from the other VCN, either from the VCN's CIDR or only specific subnets.
- Egress rule to allow outgoing traffic from the local VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (such as 0.0.0.0/0), then you don't need to add a special one for the other VCN.
Note  
  
The following procedure uses security lists, but you could instead implement the security rules in a[network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)and then create the subnet's resources in that NSG.

For the local VCN, decide which subnets in the VCN need to communicate with the other VCN and[update the security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/update-securitylist.htm)for each of those subnets to include rules that allow the egress or ingress traffic with the CIDR block or subnet of the other VCN:

For more information about security rules, see[Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm).

[Example](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#)

Let's say you want to add a stateful rule that allows ingress HTTPS (port 443) traffic from the other VCN's CIDR. Here are the basic steps you take when adding a rule:
- In the Allow Rules for Ingress section, select +Add Rule .
- Leave the Stateless checkbox unselected.
- Source Type: Leave as CIDR.
- Source CIDR: Enter the same CIDR block that the route rules use (see[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4)).
- IP Protocol: Leave as TCP.
- Source Port Range: Leave as All.
- Destination Port Range : Enter 443.
-
