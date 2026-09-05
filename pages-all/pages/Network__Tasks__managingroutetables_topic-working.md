# Working with VCN Route Tables and Route Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm
- Fetched: 2026-09-05 02:45 CDT

# Working with VCN Route Tables and Route Rules

Learn about VCN route tables and route rules.

Each VCN has a default route table. You can also create custom route tables. You can add, remove and edit route rules in any route table. By default, each VCN automatically routes traffic between sources and destinations within the VCN. You don't need to define explicit route rules for this routing behavior inside a VCN, but you can change it by defining custom route rules for traffic between subnets in a VCN. For example, you can redirect traffic between two subnets in a VCN to flow through a firewall by defining an[intra-VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__intra_vcn)route rule defining the firewall private IP address as the next-hop for each other's IP prefixes.

Each subnet in a VCN uses a single route table. When you create a subnet, you can specify which route table to use. If you don't specify any, the default route table for the VCN is used. You can[change which route table the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm)at any time. When you have a public subnet and a private subnet in a VCN (for an example of this usage, see[Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm)), use different route tables for the subnets because the route rules for the subnets need to be different.

You can optionally assign a descriptive name to a custom route table during creation. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the route table a unique identifier called an Oracle Cloud ID (OCID). For more information on OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

A route rule specifies a destination CIDR block and the target (the next hop) for any traffic that matches that CIDR. Here are the allowed types of targets for a route rule:
- [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm): For subnets that need private access to networks connected to a VCN (for example, an on-premises network connected with a[Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm)or[FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm), a[peered VCN in the same region](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm), or a[peered VCN in another region](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)).
- [Internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm): For public subnets that need direct access to the internet.
- [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm): For subnets with instances that don't have public IP addresses but need outbound access to the internet.
- [Service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm): For subnets that need private access to Oracle services such as Object Storage.
- [Local peering gateway (LPG):](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm)For subnets that need private access to a peered VCN in the same region.
- [Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm): For subnets that need to route traffic to an instance in the VCN. For more information, see[Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). Also see[Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN).
Note  
  
You can't delete a particular resource when it's the target for a route rule. For example, you can't delete an internet gateway that has traffic routed to it. Delete all rules (in all route tables) with that internet gateway as the target before you try to delete the gateway or other resource.

When adding a route rule to a route table, you provide the destination CIDR block and target (plus the compartment where the target resides). Exception: if the target is a service gateway , instead of a destination CIDR block, you specify an Oracle-provided string that represents the public endpoints for the service of interest. That way you don't need to know all the service's CIDR blocks, which might change over time.

If you misconfigure a rule (for example, enter the wrong destination CIDR block), the network traffic you intended to route might be dropped (blackholed) or sent to an unintended target.

You can[move route tables from one compartment to another](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm). Moving a route table doesn't affect its attachment to VCNs or subnets. When you move a route table to a new compartment, inherent policies apply immediately and affect access to the route table. For more information, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm).

You can't delete a VCN's default route table. To delete a custom route table, it must not be associated with a subnet or a gateway, such as DRG, LPG, IGW, NGW or SGW. See the[Learn routing in OCI Networking with examples (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/learn-routing-in-oci-networking-with-examples.pdf)technical brief to learn more about VCN routing.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

The following management tasks can be performed with route tables:
- [Creating a VCN Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm)
- [Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)
- [Getting a VCN Route Table's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm)
- [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)
- [Changing Which VCN Route Table a Subnet Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm)
- [Moving a VCN Route Table to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm)
- [Deleting a VCN Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm)

[To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#)

For each VCN subnet that must send traffic to a connected[DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm), you must add a route rule to the VCN route table associated with that subnet. If all the subnets in the VCN use the default route table, you must add a rule to only that one table.

If all non-intra-VCN traffic that's not covered by another rule in the table must be routed to the DRG, add this new rule:
- Target Type: Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself.
- Destination CIDR Block = 0.0.0.0/0. To limit the rule to a specific network (for example, an on-premises network), then use that network's CIDR instead of 0.0.0.0/0.

For step-by-step instructions, see[Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm).

[To associate a VCN route table with an existing DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#)

Important  
  
Perform this task only if you're setting up an advanced scenario for transit routing. See[Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)and[Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm).

A DRG attachment always has a route table associated with it, but you can associate a different route table, edit the table's rules, or delete some or all rules.

Prerequisites: the VCN that the DRG is already attached to must have a route table.
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Select the DRG attached to the VCN that has the route table you want to use with the attachment.
- 

Select the Actions menu (three dots) , and then select either:
- Associate Route Table: If the DRG attachment has no route table associated with it yet.
- Associate Different Route Table: If you're changing which route table is associated with the DRG attachment.
- Select the route table.
- Select Associate Route Table .
