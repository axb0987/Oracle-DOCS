# Routing traffic through a central network virtual appliance
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm
- Fetched: 2026-09-05 02:47 CDT

# Routing traffic through a central network virtual appliance

There are three primary transit routing scenarios:
- Access between multiple networks through a single DRG with a firewall between networks: The scenario covered in this topic. This scenario uses the DRG as the hub, with routing configured to send packets through a firewall instance in a dedicated Virtual Cloud Network (VCN) before they can be sent to another network.
- Access to multiple VCNs in the same region: This scenario enables communication between your on-premises network and multiple VCNs in the same region over a single FastConnect private virtual circuit or Site-to-Site VPN, with a VCN as the hub. See[Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
- Private access to Oracle services: This scenario uses a service gateway in an attached hub VCN to give your on-premises network private access to Oracle services, so on-premises hosts can use their private IP addresses and traffic doesn't go over the internet. See[Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

## Highlights
- You can use FastConnect or Site-to-Site VPN to connect your on-premises network with multiple VCNs in the same region or in another region, in a hub-and-spoke topology.
- When the Dynamic Routing Gateway (DRG) acts as the hub, all VCNs can be in different regions or tenancies. For accurate routing, the CIDR blocks of the various subnets accessible to the on-premises network and other connected VCNs must not overlap.
- A[dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)can act as the hub to communicate between VCNs or with the on-premises network. This DRG has attachments for peering connections to VCNs (referred to as spoke VCNs in this topic).
- To enable the intended traffic from a spoke VCN to other attached networks through the DRG and a hub VCN (with a network virtual appliance), create route rules for the spoke VCN's subnets, spoke VCN's DRG attachment, hub VCN's DRG attachment, and the hub VCN's subnets.
- You can set up transit routing through a private IP in the hub VCN . For example, you might want to filter or inspect the traffic between the on-premises network and a spoke VCN. In that case, you route the traffic to a private IP on a network virtual appliance in the hub VCN for inspection, and the resulting traffic continues to its destination.
- By configuring route tables, you can control whether a particular subnet in a peered spoke VCN is advertised to the on-premises network.
Tip  
  
There's another scenario that lets you connect your on-premises network to multiple VCNs. Instead of using a single DRG and hub-and-spoke topology, you set up a separate DRG for each VCN and a separate private virtual circuit over a single FastConnect. However, the scenario can be used only with FastConnect through a[third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectthirdpartyprovider.htm)or through[colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectcolocate.htm). The VCNs must be in the same region and same tenancy. For more information, see[FastConnect with Multiple DRGs and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnectmultipledrgs.htm).

## Overview of Transit Routing through a Private IP

Transit routing is simply routing traffic to either a VCN or an on-premises network through a central hub VCN. Here's a basic example of why you might use transit routing: you have a large organization with different departments, each with their own VCN. Each VCN needs access to the other VCNs, but you want to ensure security by sending all traffic through a virtual network appliance running a firewall.
Note  
  
A hub is a logical concept in a hub-and-spoke topology. If you want spokes to communicate directly to each other, the hub can be just a DRG. If you want all spoke-to-spoke traffic to pass through a network virtual appliance, the hub is the combination of the DRG and a hub VCN containing the network virtual appliance.

This networking scenario optionally involves connecting your on-premises network to a VCN with either Oracle Cloud Infrastructure[FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm)or[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm). These two basic scenarios illustrate that topology:[Scenario B: Private Subnet with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm)and[Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm).

This scenario uses a hub-and-spoke topology, as illustrated in the following diagram. The term hub here means only that a VCN has a network virtual appliance that must be routed through when one spoke communicates with another spoke in this hub-and-spoke design. For details on how to enable North-South communication between your on-premises network and spoke VCNs through a network virtual appliance refer to the last section in the detailed steps that follow.
[

Use this scenario if you want to create a hub-and-spoke topology and route all traffic between spokes through a network virtual appliance in the hub . All VCNs are in the same region, and connect to a DRG in that region, but they could be in different regions or in different tenancies. The on-premises network shown is optional, and could be a VCN in another region or tenancy. In this scenario, traffic is sent from an on-premises network to the DRG and then to the network virtual appliance in VCN-Hub, then back to the DRG to be routed to VCN-B. Similarly, traffic sent from VCN-A is first routed by the DRG to VCN-Hub and then to VCN-C.

## Summary of New Concepts for Experienced Networking Service Users

If you're already familiar with the Networking service and local peering, the most important new concepts to understand are:
- For each spoke VCN subnet that needs to communicate with another network attached to the DRG, update the subnet's route table with a rule that sets the target for all traffic (the next hop) as the DRG.
- Add a new DRG route table for spoke VCN attachments, associate this route table with each spoke VCN attachment (inside the DRG). Create a static default route with the target (next hop) of the hub VCN attachment. This will route all spoke VCN traffic to the hub VCN with the network virtual appliance.
- 

Add a new DRG route table for the hub VCN attachment, associate it with the hub VCN attachment (inside the DRG). Associate an new import route distribution with this DRG route table and create policies to import attachments associated with all destinations which must be reachable from VCN-Hub.
- 

Add another VCN route table to the hub VCN, VCN-Hub, associate it with the hub VCN's attachment to the DRG, and add a route rule with a target that depends on your situation:
- Routing traffic to a spoke VCN through private IP: Set the target (the next hop) to a[private IP on the instance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route), for all traffic destined for another spoke VCN (or a specific subnet in that VCN). Be sure to[disable the source/destination check](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview)for the private IP's VNIC.
- Routing traffic to on-premises network through private IP: Set the target (the next hop) to a[private IP on the instance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route), for all traffic destined for your on-premises network. Be sure to[disable the source/destination check](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview)for the private IP's VNIC.
- Update the subnet route table in your hub VCN with rules that set the target (next hop) for all spoke VCNs and on-premises networks as the DRG.

## Before you begin

Before you attempt to implement this scenario, ensure that:
- VCN-A, VCN-B, and VCN-C (the "spoke" VCNs) are all already created, none of which are attached to a DRG.
- VCN-Hub is already created and its subnet Subnet-H has a network virtual appliance with a private IPv4 address. This VCN is not yet attached to any DRG.
- All VCNs in the scenario have non-overlapping CIDRs.
- The on-premises network is connected to the DRG with[FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm)or[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm).
- All necessary IAM policies are in already in place. See[IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm)for details.

## Process summary

Configuring transit routing involves these steps:
- Create a DRG named DRG-Hub.
- Attach spoke VCNs VCN-A, VCN-B, and VCN-C to DRG-Hub.
- Attach VCN-Hub to DRG-Hub.
- Create a route table named "RT-Spoke" in DRG-Hub with a single static rule sending all traffic to the VCN-Hub's attachment.
- Change the DRG route table used by the spoke VCN attachments to "RT-Spoke."
- Create an import DRG route distribution in DRG-Hub called "Import-Hub" with three statements, each importing routes from the VCN attachments used by VCN-A, VCN-B, and VCN-C. For more information on import route distrubtions, see[Overview of Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview)
- Create a DRG route table named "RT-Hub" in DRG-Hub and specify its import route distribution to "Import-Hub".
- Update the DRG route table of VCN-Hub's attachment to use the "RT-Hub" route table.
- Configure VCN-Hub's default route table to send all incoming traffic to the network virtual appliance instance.
- Configure Subnet-H to send all traffic destined to addresses in the VCN CIDRs of VCN-A, VCN-B, and VCN-C to the DRG attachment.

## Example: Transit routing with a DRG hub and a network virtual appliance in an attached VCN

The examples in this section show a DRG acting as a hub and an attached VCN with a firewall, you can configure as many spoke VCNs as necessary by repeating[Task 2: Attach the spoke VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g_task_2_attach_spoke_vcns).
[

Callout 1: DRG route table "RT-Spoke" (affecting traffic entering the DRG from all spoke attachments)
Destination CIDR Route Target Type
0.0.0.0/0 VCN-Hub Static

Callout 2: DRG route table "RT-Hub" (affecting traffic entering the DRG from the hub attachment)
Destination CIDR Route Target Type
172.16.0.0/16 Virtual circuit Dynamic
192.168.10.0/24 VCN-A Dynamic
192.168.20.0/24 VCN-B Dynamic
192.168.30.0/24 VCN-C Dynamic

Callout 3: Subnet-1 route table (affecting traffic leaving Subnet-1)
Destination CIDR Route Target
172.16.0.0/16 DRG
192.168.20.0/24 DRG
192.168.30.0/24 DRG

Callout 4: VCN-Hub route table "VCN-Hub-Ingress" (affecting traffic entering VCN-Hub)
Destination CIDR Route Target
172.16.0.0/16 10.0.0.10
192.168.10.0/24 10.0.0.10
192.168.20.0/24 10.0.0.10
192.168.30.0/24 10.0.0.10

Callout 5: Subnet-H route table (affecting traffic leaving Subnet-H)
Destination CIDR Route Target
172.16.0.0/16 DRG
192.168.10.0/24 DRG
192.168.20.0/24 DRG
192.168.30.0/24 DRG

Callout 6: Subnet-2 route table
Destination CIDR Route Target
172.16.0.0/16 DRG
192.168.10.0/24 DRG
192.168.30.0/24 DRG

Callout 7: Subnet-3 route table
Destination CIDR Route Target
172.16.0.0/16 DRG
192.168.10.0/24 DRG
192.168.20.0/24 DRG

[Task 1: Create DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Create the DRG (named DRG-Hub) that routes traffic between all attached VCNs.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm).
- Click Create Dynamic Routing Gateway .
- 

Enter the following items:
- Name: DRG-Hub
- Create in Compartment: The compartment where you want to create the DRG, which could be different from the compartment you're currently working in.
- Click Create Dynamic Routing Gateway .

The new DRG is created and then displayed on the Dynamic Routing Gateways page of the compartment you chose. The DRG is in the "Provisioning" state for a short period. You can connect it to other parts of your network only after provisioning is complete.

Provisioning a DRG includes creating two default route tables: one DRG route table for VCN attachments and one DRG route table for all other resources such as virtual circuits and IPSec tunnels. These route tables are used to route traffic coming into the DRG.

[Task 2: Attach the spoke VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Attach VCN-A, VCN-B, and VCN-C to DRG-Hub.
Note  
  
The VCN subnet route tables sending traffic to the DRG attachment need to account for the CIDRs of the other two VCNs. This can also be accomplished with a summary address or default route.
Note  
  
A DRG can be attached to many VCNs, but VCN can be attached to only one DRG at a time. The attachment is automatically created in the compartment that holds the VCN. A VCN does not need to be in the same compartment as the DRG.

You can eliminate local peering connections from your overall network design if you connect several VCNs in the same region to the same DRG and configure the DRG routing tables appropriately.

The following instructions have you navigate to the DRG and then choose which VCN to attach. Repeat this task for all three VCNs (VCN-A, VCN-B, and VCN-C), and create a different DRG attachment for each VCN.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you want to attach to VCN A, DRG-Hub.
- Under Resources , click Virtual Cloud Network Attachments .
- Click Create Virtual Cloud Network Attachment .
- Enter the following:
- (Optional) Enter VCN-A, or give the attachment point some other descriptive name. If you don't specify a name, one is created for you.
- Select VCN-A from the list of VCNs.
- Click Create Virtual Cloud Network Attachment .

The attachment is in the "Attaching" state for a short period. Each of the spoke VCNs get a unique attachment.

Once you have done this for all three VCNs (VCN-A, VCN-B, and VCN-C) you have direct routing between these VCNs.

[Task 3: Attach the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Attach VCN-Fire to DRG-Transit.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you want to attach to a VCN, in this case DRG-Hub.
- Under Resources , click Virtual Cloud Network Attachments .
- Click Create Virtual Cloud Network Attachment .
- Enter the following:
- (Optional) Enter VCN-Hub or give the attachment point some other descriptive name. If you don't specify a name, one is created for you.
- Select VCN-Hub from the list of VCNs.
- Click Create VCN attachment .

The attachment is in the "Attaching" state for a short period. The VCN attachment uses the default DRG route table for VCNs. Wait for the attachment to complete before moving on.

[Task 4: Create the DRG route table sending ingress traffic to the network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Create a DRG route table named "RT-Spoke" in DRG-Transit with a single static rule sending all traffic to the VCN-Hub's attachment.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click DRG Route Tables .
- Click Create DRG Route Table .
- 

Enter the following:
- Name: Enter RT-Spoke, or choose some other descriptive name.
- Destination CIDR: enter the CIDR for VCN-Fire. This example uses 0.0.0.0/0. This is a static route which sends all VCN-A, VCN-B, and VCN-C traffic to the hub VCN.
- Next Hop Attachment Type: Choose Virtual Cloud Network .
- Next hop Attachment: Choose VCN-Hub from the list.
- 

Click Create Route Table .

[Task 5: Update the route table of spoke VCN attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Change the DRG route tables used by the spoke VCN attachments (VCN-A, VCN-B, and VCN-C) to use the route table created in the previous task (RT-Spoke), which sends all incoming traffic to VCN-Hub.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click Virtual Cloud Network Attachments .
- Click the name of the DRG attachment used by one of the VCNs.
- Click Edit .
- Click Show Advanced Options .
- In the DRG route table tab, select RT-Spoke from the list of available route tables.
- Click Save Changes .

Repeat this task for all three spoke VCN attachments (VCN-A, VCN-B, and VCN-C) before proceeding to the next task.

[Task 6: Create an import route distribution](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

In this task, you create an import route distribution in DRG-Hub with three statements, each importing routes from the VCN attachments used by VCN-A, VCN-B, and VCN-C.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click Import Route Distributions .
- Click Create Import Route Distribution .
- In the screen that appears, give the import route distribution an easily recognized name like Import-Hub, then click + Another Statement twice. For each of the three statements, add the following details:
- Priority: Choose different priority numbers for each statement. For example, 10, 20, and 30.
- Match Type: Choose Attachment.
- Attachment Type Filter: Choose Virtual Cloud Network.
- DRG Attachment: Choose a VCN attachment created previously for VCN-A, VCN-B, or VCN-C.
- Click Create Import Route Distribution when finished.

[Task 7: Create a DRG route table for ingress from VCN-Hub](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Create a route table named "RT-Hub" in DRG-Hub and set its import route distribution to the distribution created previously.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click DRG Route Tables .
- Click Create DRG Route Table .
- Assign the DRG route table a name, for example RT-Hub.
- Click Show Advanced Options .
- Click Enable Import Route Distribution .
- Choose Import-Hub, the import route distribution you created in[Task 6](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g_task_6_create_import_route_distribution).
- 

Click Create Route Table .

The route table is created and then displayed on the Route Tables page in the compartment you chose.

[Task 8: Update VCN-Hub's attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Update the DRG route table of VCN-Hub's attachment to use the "RT-Hub" DRG route table.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click Virtual Cloud Network Attachments .
- Click the name of the DRG attachment used by VCN-Hub.
- Click Edit .
- Click Show Advanced Options .
- In the DRG route table tab, select RT-Hub from the list of available route tables.
- Click Save Changes .

[Task 9: Configure routing inside VCN-Hub route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Configure ingress routing in VCN-Hub to send all inbound traffic to the firewall instance.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Click the VCN you're interested in, VCN-Hub.
- Under Resources , click Route Tables .
- Click Create Route Table .
- 

Name the VCN route table VCN-Hub-Ingress, and enter the following route rules:
- Target Type Choose Private IP .
- Destination Type Choose CIDR Block .
- Destination CIDR Block Enter the CIDR block for VCN-A .
- Target Selection Enter 10.0.0.10, the private IPv4 address for the firewall instance VNIC.
- Click +Another Route Rule and repeat until you have a rule for each of the three spoke VCNs (VCN-A, VCN-B, and VCN-C)
- 

Click Create .

The VCN route table is created and then displayed on the Route Tables page for the VCN.
- Under Resources , click Dynamic Routing Gateways Attachments .
- Click the name of the DRG attachment used by VCN-Hub.
- Click Edit .
- Click Show Advanced Options .
- In the VCN route table tab, click Select Existing and select VCN-Hub-Ingress from the list of available route tables.
- Click Save Changes .

[Task 10: Configure VCN egress routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Configure VCN egress routing in VCN-Hub's subnet named Subnet-H to send all traffic destined to addresses in the VCN CIDRs of VCN-A, VCN-B, and VCN-C to the DRG attachment.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Click the VCN you're interested in, VCN-Hub.
- Under Resources , click Route Tables .
- Click the name of the route table used by Subnet-H.
- Click Add Route Rules .
- 

Enter the following:
- Target Type: Choose Dynamic Routing Gateway .
- Destination CIDR Block: Enter the CIDR block for VCN-A.
- Click + Another Route Rule and repeat until you have a rule for each of the three spoke VCNs (VCN-A, VCN-B, and VCN-C).
- Click Add Route Rules.

This completes configuration of transit routing. At this point, any packets sent from one spoke VCN to another are sent to the mutually attached DRG, redirected to a firewall in a hub VCN, and packets the firewall allows are then sent back to the DRG to be routed to their destination VCN.

## Enabling north-south traffic through a network virtual appliance

You may choose to set up a configuration where any packets sent from one spoke VCN to your on-premises network are sent to the mutually attached DRG, redirected to a network virtual appliance in a hub VCN, and packets the network virtual appliance allows are then sent back to the DRG to be routed to their on-premises destination.

[Task 1: Create the DRG route table sending ingress on-premises traffic to the network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Create a DRG route table named "RT-OnPrem" in DRG-Hub with multiple static rules forwarding all traffic to the VCN-Hub's attachment.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click DRG Route Tables .
- Click Create DRG Route Table .
- Enter the following:
- Name: Enter RT-OnPrem, or choose some other descriptive name.
- Destination CIDR: Enter the CIDR block for VCN-A.
- Next Hop Attachment Type: Choose Virtual Cloud Network .
- Next Hop Attachment: Choose VCN-Hub from the list.
- Click + Another Route Rule and repeat the process multiple times adding static routes representing the CIDR blocks for VCN-B, VCN-C, and VCN-Hub.
- Click Create Route Table .
Note  
  

All static route entries in this DRG route table will be advertised to your on-premises network via BGP on each attachment where this DRG route table is applied.

[Task 2: Update the route table of on-premises attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Change the DRG route table used by your on-premises attachments to "RT-OnPrem". This example uses FastConnect, but the same process can be applied to Site-to-Site VPN IPSec tunnels.

Change the DRG route tables used by your on-premises attachments (FastConnect virtual circuit or Site-to-Site VPN IPSec tunnels) to use the route table created in the previous task, which sends all incoming traffic to VCN-Hub.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click Virtual Circuits Attachments .
- Click the name of the DRG attachment used by one of the virtual circuits.
- Click Edit .
- Choose a DRG Route Table: Select RT-OnPrem from the list of available route tables in the dropdown.
- Click Save Changes .

Repeat this task for all on-premises attachments (VCN-A, VCN-B, and VCN-C) before proceeding to the next task.

[Task 3: Update import route distribution Import-Hub](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

In this task, you update the import route distribution used by the VCN-Hub attachment to import routes from your on-premises connections.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click the DRG you're interested in, DRG-Hub.
- Under Resources , click Import Route Distributions .
- Click the import route distribution you're interested in, Import-Hub.
- Click Manage Statements .
- Click + Another Statement .
- For each new statement, enter the following details:
- Priority: Choose different priority numbers for each statement. For example, 40.
- Match Type: Choose Attachment Type.
- Attachment Type: Choose Virtual Circuit.
- Click Create Import Route Distribution when finished.

Repeat this step for all on-premises attachments (FastConnect virtual circuit or site-to-site IPSec VPN) which must be reachable from the hub VCN.

[Task 4: Update routing inside VCN-Hub route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

Update ingress routing in VCN-Hub to send all inbound traffic to the firewall instance.
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Click the VCN you're interested in, VCN-Hub.
- Under Resources , click Route Tables .
- Select the VCN-Hub-Ingress route table.
- Click Add Route Rules and enter the following route rules:
- Target Type: Choose Private IP .
- Destination: Choose CIDR Block .
- Destination CIDR Block: Enter the CIDR block for your on-premises network.
- Target Selection: Enter the private IPv4 address for the firewall instance VNIC.
- Click Add Route Rules .

The VCN-Hub-Ingress route table will be updated with a route for your on-premises network.

[Task 5: Add route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#)

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Click the VCN you're interested in, VCN-Hub.
- Under Resources , click Route Tables .
- Click the name of the route table used by Subnet-H.
- Click Add Route Rules .
- Enter the following:
- Target Type: Choose Dynamic Routing Gateway .
- Destination CIDR Block: Enter the CIDR block for your on-premises network.
- Click Add Route Rules.

Repeat these steps for each spoke ((VCN-A, VCN-B, and VCN-C)) VCN's route table to route all traffic destined to on-premises to the attached DRG, DRG-Hub.
