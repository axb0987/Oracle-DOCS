# Local VCN Peering Through an Upgraded DRG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm
- Fetched: 2026-09-05 02:47 CDT

# Local VCN Peering Through an Upgraded DRG

This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.

## Overview

Instead of using[local peering connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm), you can establish private network communications between two or more virtual cloud networks (VCNs) in the same region by attaching them to a common dynamic routing gateway (DRG) and making appropriate changes to VCN and DRG route tables.

This scenario is only available to an upgraded[DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).

If you're using the legacy DRG, you can peer two VCNs in the same region using Local Peering Gateways (LPG) as described in the scenario[Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm). Peering two VCNs in the same region through a DRG gives you more routing flexibility and simplified management but comes at the cost of microseconds increase in latency because the traffic routes through a virtual router, the DRG.

This sample scenario peers two VCNs. Before you implement this scenario, be sure that:
- VCN-A isn't attached to a DRG
- VCN-B isn't attached to a DRG
- The CIDRs used by VCN-A and VCN-B don't overlap

Peering VCNs in different tenancies requires more IAM policies for cross-tenancy authorization. See[IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm)for details on the permissions needed. When you attach a VCN in a different region to a DRG, use the steps in[Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm). Most of the steps in this scenario assume the DRG and both VCNs are in the same tenancy.

Steps

Here's the general process for setting up a peering between two VCNs in the same region using a DRG:
- Create the DRG : See[Task A: Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_a_dita).
- Attach VCN A to the DRG : See[Task B: Attach VCN-A to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_b_dita).
- Attach VCN B to the DRG : See[Task C: Attach VCN-B to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_c_dita).
- Configure route tables in VCN A to send traffic destined to VCN B's CIDR to the DRG : See[Task D: Configure route tables in VCN-A to send traffic destined to VCN-B's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_d_dita).
- Configure route tables in VCN B to send traffic destined to VCN A's CIDR to the DRG : See[Task E: Configure route tables in VCN-B to send traffic destined to VCN-A's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_e_dita).
- Update security rules : Update each VCN's security rules to enable traffic between the peered VCNs as intended. See[Task F: Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_f_dita).

This page summarizes some access control, security, and performance implications for peered VCNs. You can control access and traffic between two peered VCNs by using IAM policies, route tables in each VCN, route tables in the DRG, and security lists in each VCN.

## Summary of Networking components for peering through a DRG

At a high level, the Networking service components required for a local peering through a DRG include:
- Two VCNs in the same region with CIDRs that don't overlap
- A single Dynamic Routing Gateway (DRG) attached to each peer VCN
- Supporting route rules to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if wanted)
- Supporting security rules to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN

The following diagram illustrates the components.
[
Note  
  

A particular VCN can reach these resources:
- VNICs in the other VCN
- An on-premises network attached to the other VCN, if an advanced routing scenario called[transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)has been set up for the VCNs

Two VCNs interconnected with a DRG can't reach other cloud gateways (such as an internet gateway or NAT gateway) except for transit routing through an LPG. For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 couldn't use it to send traffic to endpoints on the internet. However, VCN-2 could receive traffic from the internet by way of VCN-1. For more information, see[Important Implications of VCN Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan2).

## Important Local Peering Concepts

The following concepts help you understand the basics of VCN peering using a DRG and how to establish a local peering. PEERING A peering is a relationship between two VCNs that both connect to the same DRG and can mutually route traffic. The local part of local peering indicates that the VCNs are in the same region. A particular DRG can have a maximum of 300 local DRG attachments at a time.
Caution  
  
Peer VCNs must not have overlapping CIDRs. ADMINISTRATORS In general, VCN peering can occur only if all involved VCN administrators and DRG administrators agree to it. Depending on the situation, a single administrator might be responsible for all involved DRGs, VCNs, and the related policies. For more information about the required policies and VCN configuration, see[IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm). ROUTING TO THE DRG As part of configuring the VCNs, each administrator must update the[VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)to enable traffic to flow between the VCNs. In practice, this resembles routing you set up for any gateway (such as an[internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm)or[dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)). For each subnet that needs to communicate with the other VCN, you update the subnet's route table. The route rule specifies the destination traffic's CIDR and the DRG as the target. The VCN routes traffic that matches that rule to the DRG, which in turn routes the traffic to the next hop in the other VCN. In the following diagram, VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) destined for an instance in VCN-2 (192.168.0.15) is routed to the DRG based on the rule in Subnet A's route table. From there the traffic is routed to VCN-2, and then from there, on to its destination in Subnet X. The DRG in this scenario uses a default route table.
[

Callout 1: Subnet A Route Table
Destination CIDR Route Target
172.16.0.0/12 DRG
192.168.0.0/16 DRG
0.0.0.0/0 Internet Gateway

Callout 2: Subnet X Route Table
Destination CIDR Route Target
172.16.0.0/12 DRG
10.0.0.0/16 DRG SECURITY RULES Each subnet in a VCN has one or more[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm)that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must decide which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists to match. If you use[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)(NSGs) to implement security rules, notice that you can write security rules for an NSG that specify another NSG as the source or destination of traffic. However, the two NSGs must belong to the same VCN .

## Setting up this scenario in the Console

[Task A: Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#)

A DRG created before May 2021 can't perform routing between on-premises networks and several VCNs, or provide local peering between VCNs. If you require that functionality and you see an Upgrade DRG button, select it.
Note  
  
Selecting the Upgrade DRG button also resets all existing BGP sessions and temporarily interrupt traffic from the on-premises network while the DRG upgrades. Be aware you can't roll back the upgrade.

If you reate a DRG in the same region as the VCNs you want to peer, using the steps in[Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm).

[Task B: Attach VCN-A to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#)

Note  
  
An upgraded DRG can be attached to many VCNs, but a VCN can be attached to only one DRG at a time. The attachment is automatically created in the compartment that holds the VCN. A VCN doesn't need to be in the same compartment or tenancy as the upgraded DRG.

You can eliminate local peering connections from the overall network design if you connect several VPNs in the same region to the same DRG and configure the DRG routing tables appropriately.

Peering VCNs in different tenancies requires more IAM policies for cross-tenancy authorization. See[IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm)for details on the permissions needed. When you attach a VCN in a different region to a DRG, use the steps in[Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm).

Attach VCN-A to the DRG you created in Task A. You can either[attach a DRG to a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm)or[attach a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm).

[Task C: Attach VCN-B to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#)

Note  
  
A DRG can be attached to many VCNs, but VCN can be attached to only one DRG at a time. The attachment is automatically created in the compartment that holds the VCN. A VCN doesn't need to be in the same compartment as the DRG.

You can eliminate local peering connections from the overall network design if you connect several VPNs in the same region to the same DRG and configure the DRG routing tables appropriately.

Peering VCNs in different tenancies requires more IAM policies for cross-tenancy authorization. See[IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm)for details on the permissions needed. When you attach a VCN in a different region to a DRG, use the steps in[Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm).

Attach VCN-B to the DRG you created in Task A. You can either[attach a DRG to a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm)or[attach a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm).

[Task D: Configure route tables in VCN-A to send traffic destined to VCN-B's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#)

As mentioned earlier, each administrator can do this task before or after the VCN is attached to the DRG.

Prerequisite: Each administrator must have the CIDR block for the other VCN or for specific subnets in that VCN.

For VCN-A, decide which subnets in VCN-A need to communicate with VCN-B and[update the route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)for each of those subnets to include a new rule that directs traffic destined for the other VCN's CIDR to the DRG. Use the settings:
- Target Type: Dynamic Routing Gateway.
- Destination CIDR Block: VCN-B's CIDR block. If you want, you can specify a subnet or particular subset of VCN-B's CIDR.
- Target Compartment: The compartment with the other VCN, if not the current compartment.
- Target: The DRG created in Task A.
- Description: An optional description of the rule.

Any subnet traffic with a destination that matches the rule is routed to the DRG. For more information about setting up route rules, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

If in the future you no longer need the peering and want to end the peering relationship, first delete all route rules in the VCN that specify the other VCN.
Tip  
  
Without the required routing, traffic doesn't flow between the peered VCNs. If a situation occurs where you need to temporarily stop the peering relationship, remove the route rules that enable traffic.

[Task E: Configure route tables in VCN-B to send traffic destined to VCN-A's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#)

As mentioned earlier, each administrator can do this task before or after the VCN is attached to the DRG.

Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN.

For VCN-B, decide which subnets in VCN-B need to communicate with VCN-A and[update the route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)for each of those subnets to include a new rule that directs traffic destined for the other VCN's CIDR to the DRG. Use the settings:
- Target Type: Dynamic Routing Gateway.
- Destination CIDR Block: VCN-A's CIDR block. If you want, you can specify a subnet or particular subset of VCN A's CIDR block.
- Target Compartment: The compartment with the other VCN, if not the current compartment.
- Target: The DRG created in Task A.
- Description: An optional description of the rule.

Any subnet traffic with a destination that matches the rule is routed to the DRG. For more information about setting up route rules, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

If later on you no longer need the peering and want to end the peering relationship, delete all route rules in the VCN that specify the other VCN as the target.
Tip  
  
Without the required routing, traffic doesn't flow between the peered VCNs. If you ever need to temporarily stop the peering, you can remove the route rules that enable traffic.

[Task F: Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#)

As mentioned earlier, each administrator can do this task before or after the connection is established.

Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. In general, use the same CIDR block you used in the route table rule in[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4).

Add the following rules:
- Ingress rules for the types of traffic you want to allow from the other VCN's CIDR or specific subnets.
- Egress rule to allow outgoing traffic from the local VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the other VCN.
Note  
  
The following procedure uses security lists, but you could instead implement the security rules in a[network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)and then create the subnet's resources in that NSG.

For each VCN, decide which subnets in the local VCN need to communicate with the other VCN and[update the security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/update-securitylist.htm)for each of those subnets to include rules that allow the intended egress or ingress traffic with the CIDR block or subnet of the other VCN
Example

To add a stateful rule that allows ingress HTTPS (port 443) traffic from the other VCN's CIDR use the following settings to implement that rule:
- Leave the Stateless checkbox unselected.
- Source Type: Leave as CIDR.
- Source CIDR: Enter the same CIDR block that the route rules use (see[Task D](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_d_dita)or[Task E](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_e_dita)).
- IP Protocol: Leave as TCP.
- Source Port Range: Leave as All.
- Destination Port Range : Enter 443.
- Description: An optional description of the rule.

For more information about security rules, see[Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)
