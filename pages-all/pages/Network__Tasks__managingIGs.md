# Internet Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm
- Fetched: 2026-09-05 02:45 CDT

# Internet Gateway

This topic describes how to set up and manage an internet gateway to give a VCN internet access.
Tip  
  
Oracle also offers a[NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm), which is recommended for subnets in the VCN that don't require external connections from the internet.

## Highlights

- An internet gateway is an optional gateway you can add to a VCN to enable direct connectivity to the internet.
- The gateway supports connections from within the VCN (egress) and connections from the internet (ingress).
- Resources that need to use the gateway for internet access must be in a[public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Public)and have[public IP addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm). Resources that have private IP addresses can instead use a[NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm)to start connections to the internet.
- Each public subnet that needs to use the internet gateway must have a[route table rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)that specifies the gateway as the target.
- You use[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)to control the types of traffic allowed in and out of resources in that subnet. Ensure that the rules allow only the appropriate types of internet traffic.
- The internet gateway can be used only by resources in the gateway's VCN. Hosts in the connected on-premises network or in a[peered VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm)can't use that internet gateway.
- You can't add or move an internet gateway to a VCN within a[security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zones.htm). Security zones don't use[public subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Public).
- Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway, provided security rules and route table rules allow that access.

## Overview of Internet Gateways

Before continuing, read[Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Private)and also understand how to set up[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)for the resources in a subnet.

An internet gateway as an optional virtual router that connects the edge of the VCN with the internet. To use the gateway, the hosts on both ends of the connection must have public IP addresses for routing. Connections that originate in a VCN and are destined for a public IP address (either inside or outside the VCN) go through the internet gateway. Connections that originate outside the VCN and are destined for a public IP address inside the VCN go through the internet gateway.

A specific VCN can have only one internet gateway. You control which public subnets in the VCN can use the gateway by configuring the subnet's associated route table. You use security rules to control the types of traffic allowed in and out of resources in those public subnets.

The following diagram illustrates a VCN setup with a single public subnet. The VCN has an internet gateway, and the public subnet is configured to use the VCN's default route table. The table has a route rule that sends all egress traffic from the subnets to the internet gateway. The gateway allows any ingress connections from the internet with a destination IP address equal to the public IP address of a resource in the VCN. However, the public subnet's security list rules decide the specific types of traffic that are allowed in and out of the resources in the subnet. Those specific security rules aren't shown.
[

Callout 1: VCN Default Route Table
Destination CIDR Route Target
0.0.0.0/0 Internet Gateway
Tip  
  
Traffic between a VCN and a public IP address within Oracle Cloud Infrastructure (such as Object Storage) should be routed through a service gateway instead of an internet gateway.

## Working with Internet Gateways

You create an internet gateway in the context of a specific VCN and the internet gateway is always attached to that VCN. However, you can disable and reenable the internet gateway at any time. Compare this with a[dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)(DRG), which you create as a standalone object that you then attach to a particular VCN. DRGs use a different model because they're intended to be modular building blocks for privately connecting VCNs to an on-premises network or other VCNs.

For traffic to flow from a public subnet to the Internet, you must create a corresponding route rule in the subnet's route table. For example, if destination CIDR = 0.0.0.0/0 and target = internet gateway, to route the traffic through a firewall the target can be the private IP address of the firewall. The firewall subnet then needs a route (for example 0.0.0.0/0) to reach the Internet with the internet gateway as the target.

For traffic flowing from the internet to a destination in a public subnet, the internet gateway routes the traffic directly to the destination by default. You can associate a route table with the internet gateway and define route rules that route ingress public traffic to destinations in the VCN. For example, if you want the internet gateway to route the traffic to a firewall in the VCN first, you can create a route rule for the destination subnet CIDR with the firewall private IP address as the target. Route rules to destinations outside the VCN in an internet gateway route table aren't supported.

Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway provided security rules and route table rules allow that access.

For the purposes of access control, you must specify the compartment where you want the internet gateway to reside. If you're not sure which compartment to use, put the internet gateway in the same compartment as the cloud network. For more information, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm).

You can assign a friendly name to the internet gateway. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the internet gateway a unique identifier called an Oracle Cloud ID (OCID). For more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

To delete an internet gateway, it doesn't have to be disabled, but there must not be a route table that lists it as a target.

See[Gateway Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#gateway_limits)and[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)for limits-related information.

## Internet Gateway Setup

Prerequisites:
- Decide which subnets in the VCN need access to the internet, and create those public subnets.

Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway provided security rules and route table rules allow that access.
- Decide the types of ingress and egress internet traffic that you want to enable for the resources in each public subnet (examples: ingress HTTPS connections, ingress ICMP ping connections).
- The required IAM policy is in place to allow you to work with Networking service resources. For administrators: see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).
Important  
  

If the public subnet is configured to use the[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default), remember that the list includes several helpful default rules that enable basic required access (examples: ingress SSH, egress access to all destinations). We recommend that you become familiar with the basic access that these default rules provide. If you select not to use the default security list, ensure this basic access by implementing these security rules either in[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)(NSGs) or custom[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm).

The following procedure uses security lists, but you could instead implement the security rules in a network security group and then create all the subnet's resources in that NSG.
- 

For each public subnet that needs to use the internet gateway,[set up the subnet's security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/update-securitylist.htm)to allow internet traffic. See the following example settings:

Imagine you have web servers in the public subnet. This example shows how to add an ingress rule for HTTPS connections (TCP port 443) coming from the internet to the web server. Without this rule, inbound HTTPS connections aren't allowed.
- Leave the Stateless checkbox unselected.
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: Leave as TCP.
- Source Port Range: Leave as All.
- Destination Port Range : Enter 443.
- Description: An optional description of the rule.
- 

[Create the VCN's internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm).

After the internet gateway is created and displayed on the Internet Gateways page of the VCN you chose, it's already enabled but you still need to add a route rule that allows traffic to flow to the gateway.
- 

For each public subnet that needs to use the internet gateway,[update the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)using the following example settings:
- Target Type: Internet Gateway
- Destination CIDR block: 0.0.0.0/0 (which means that all non-intra-VCN traffic not already covered by other rules in the route table goes to the target specified in this rule)
- Compartment: The compartment containing the internet gateway.
- Target: The internet gateway you created.
- Description: An optional description of the rule.
