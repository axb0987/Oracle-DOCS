# Scenario B: Private Subnet with a VPN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm
- Fetched: 2026-09-05 02:47 CDT

# Scenario B: Private Subnet with a VPN

This topic explains how to set up Scenario B, which consists of a virtual cloud network (VCN) with a regional private subnet . Other servers are in separate availability domains for redundancy. The VCN has a dynamic routing gateway (DRG) and Site-to-Site VPN for connectivity to your on-premises network. The VCN has no direct connection to the internet. Any connection to the internet would need to come indirectly by way of the on-premises network.

The subnet uses the[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default), which has default rules that are designed to make it easy to get started with Oracle Cloud Infrastructure. The rules enable typical required access (for example, inbound SSH connections and any type of outbound connections). Remember that security list rules only allow traffic. Any traffic not explicitly covered by a security list rule is denied.

This scenario can use a legacy or upgraded[DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).

In this scenario, you add rules to the default security list. You could instead create a custom security list for those rules. You would then set up the subnet to use both the default security list and the custom security list.
Tip  
  
Security lists are one way to control traffic in and out of the VCN's resources. You can also use[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)

The subnet uses the default route table, which starts out with no rules when the VCN is created. In this scenario, the table has only a single rule for the DRG. No route rule is required to route traffic within the VCN itself. The subnet uses the default security list. See the following figure.
[

Callout 1: Regional private subnet route table
Destination CIDR Route target
0.0.0.0/0 DRG
Tip  
  
The scenario uses Site-to-Site VPN for connectivity. However, you could instead use[Oracle Cloud Infrastructure FastConnect.](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm)

## Prerequisites

To set up the VPN in this scenario, you need to get the following information from a network administrator:
- Public IP address of the customer-premises equipment (CPE) at your end of the VPN
- Static routes for your on-premises network (this scenario uses static routing for the VPN tunnels, but you could instead use[BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing))

You provide Oracle this information and in return receive the information your network administrator must have to configure the CPE at your end of the VPN.

### Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're a member of the Administrators group, you already have the required access to implement Scenario B. Otherwise, you need access to Networking, and you need the ability to launch instances. See[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).

## Setting Up Scenario B

Setup is easy in the Console. Alternatively, you can use the Oracle Cloud Infrastructure API, which lets you perform the individual operations yourself.
Important  
  
Most of this process involves working with the Console or API (whichever you choose) for a short period to set up the necessary Networking components. But there's also a critical step that requires a network administrator in your organization to take information you receive from setting up the components and use it to configure the CPE at your end of the VPN. Therefore you can't complete this process in one short session. Plan to take a break while the network administrator completes the configuration and return afterward to confirm communication with your instances over the VPN.

### Using the Console

[Task 1: Set up the VCN and subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#)

- 

Create the VCN:
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Under List Scope , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm).
- Click Create Virtual Cloud Network .
- 

Enter the following:
- Name: A descriptive name for the VCN. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- Create in Compartment: Leave as is.
- CIDR Block: One or more non-overlapping CIDR blocks for the VCN. For example: 172.16.0.0/16. You can add or remove CIDR blocks later. See[Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Allowed). For reference, here's a[CIDR calculator](http://www.ipaddressguide.com/cidr).
- Enable IPv6 Address Assignment: IPv6 addressing is supported for all commercial and government regions. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).
- Use DNS Hostnames in this VCN: This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the Internet and VCN Resolver ). If you select this option you can specify a DNS Label for the VCN, or you can let the Console to generate one for you. The page automatically displays the corresponding DNS domain name for the VCN (`<VCN_DNS_label> .oraclevcn.com`). For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).
- Tags: Leave as is. You can add tags later if you want. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Click Create Virtual Cloud Network .

The VCN is then created and displayed on the Virtual Cloud Networks page in the compartment you chose.
- 

Create the regional private subnet:
- While still viewing the VCN, click Create Subnet .
- 

Enter the following:
- Name: A friendly name for the subnet (for example, Regional Private Subnet ). It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- Regional or Availability Domain-Specific: Select Regional (recommended), which means the subnet spans all availability domains in the region. Later when you launch an instance, you can create it any availability domain in the region. For more information, see[Overview of VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm).
- CIDR Block: A single, contiguous CIDR block within the VCN's CIDR block. For example: 172.16.0.0/24. You cannot change this value later. For reference, here's a[CIDR calculator](http://www.ipaddressguide.com/cidr).
- Enable IPv6 Address Assignment: This option is available only if the VCN is in the US Government Cloud. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).
- Route Table: Select the default route table.
- Private or public subnet : Select Private Subnet , which means instances in the subnet cannot have public IP addresses. For more information, see[Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Private).
- Use DNS Hostnames in this Subnet: This option is available only if a DNS label was provided for the VCN when it was created. The option is required for assignment of DNS hostnames to hosts in the subnet, and also when you plan to use the VCN's default DNS feature (called the Internet and VCN Resolver ). If you select the checkbox, you can specify a DNS label for the subnet, or let the Console generate one for you. The page automatically displays the corresponding DNS domain name for the subnet as an FQDN. For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).
- DHCP Options: Select the default set of DHCP options.
- Security Lists: Select the default security list.
- Tags: Leave as is. You can add tags later if you want. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Click Create Subnet .

The subnet is then created and displayed on the Subnets page.
- 

Update the[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default)to include rules to allow the types of connections that your instances in the VCN need:
- While still on the page displaying your VCN's subnets, click Security Lists , and then click the default security list.
- Under Resources , click either Ingress Rules or Egress Rules depending on the type of rule you want to work with. You can add one rule at a time by clicking either Add Ingress Rule or Add Egress Rule .
- 

Add your wanted rules. Here are suggested ones to add to the default ones already in the default security list:

Example: Ingress HTTP access
- Type: Ingress
- Stateless : Unselected (this is a[stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm#stateful))
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range : 80
- Description: An optional description of the rule.

Example: Ingress HTTPS access
- Type: Ingress
- Stateless : Unselected (this is a[stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm#stateful))
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range : 443
- Description: An optional description of the rule.

Example: Ingress SQL*Net access for Oracle databases
- Type: Ingress
- Stateless : Unselected (this is a[stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm#stateful))
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range : 1521
- Description: An optional description of the rule.

Example: Ingress RDP access required for Windows instances
- Type: Ingress
- Stateless : Unselected (this is a[stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm#stateful))
- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range : 3389
- Description: An optional description of the rule.
Tip  
  
For extra security, you could modify all the stateful ingress rules to allow traffic only from within your VCN and your on-premises network. Create separate rules for each, one with the VCN's CIDR as the source, and one with the on-premises network's CIDR as the source.

For a production VCN, you typically set up one or more custom security lists for each subnet. You can edit the subnet to[use different security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/change-use-securitylist.htm)if you like. If you choose not to use the default security list, do so only after carefully assessing which of its default rules you want to duplicate in your custom security list. For example: the[default ICMP rules in the default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default)are important for receiving connectivity messages.

[Task 2: Create instances in separate availability domains](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#)

You can now create one or more instances in the subnet (see[Launching an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)). The scenario's diagram shows instances in two different availability domains. When you create the instance, you choose the AD, which VCN and subnet to use, and several other characteristics.

However, you can't yet communicate with the instances because there's no gateway connecting the VCN to your on-premises network. The next procedure walks you through setting up Site-to-Site VPN to enable that communication.

[Task 3: Add Site-to-Site VPN to your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#)

- 

Create a customer-premises equipment (CPE) object:
- Open the navigation menu and select Networking . Under Customer connectivity , select Customer-premises equipment .
- Click Create Customer-Premises Equipment .
- Enter the following:
- Create in Compartment: Leave the default value (the compartment you're currently working in).
- Name: A friendly name for the customer-premises equipment object. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- IP Address: The public IP address of the CPE at your end of the VPN (see[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Prerequi)).
- Click Create .

The CPE object is in the "Provisioning" state for a short period.
- 

Create a Dynamic Routing Gateway (DRG):
- Open the navigation menu and select Networking . Under Customer connectivity , select Dynamic routing gateway .
- Click Create Dynamic Routing Gateway .
- For Create in Compartment: Leave the default value (the compartment you're currently working in).
- Enter a friendly name for the DRG. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- Click Create .

The DRG is in the "Provisioning" state for a short period. Wait until the DRG is fully provisioned before continuing.
- 

Attach the DRG to your VCN:
- Click the DRG that you created.
- Under Resources , click Virtual Cloud Networks .
- Click Attach to Virtual Cloud Network .
- Select the VCN. Ignore the section for advanced options, which is only for an advanced routing scenario called transit routing , which is not relevant here.
- Click Attach .

The attachment is in the "Attaching" state for a short period. Wait for this process to finish.
- 

Update the default route table (which has no rules yet):
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Click your VCN.
- Under Resources , click Route Tables , and then click the default route table.
- Click Add Route Rule .
- 

Enter the following:
- Target Type: Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself.
- Destination CIDR Block: 0.0.0.0/0 (which means that all non-intra-VCN traffic that is not already covered by other rules in the route table go to the target specified in this rule).
- Description: An optional description of the rule.
- 

Click Add Route Rule .

The VCN's default route table now directs outbound traffic to the DRG and ultimately to your on-premises network.
- 

Create an IPSec Connection:
- Open the navigation menu and select Networking . Under Customer connectivity , select Site-to-Site VPN .
- Click Create IPSec Connection .
- 

Enter the following:
- Create in Compartment: Leave the default value (the compartment you're currently working in).
- Name: Enter a friendly name for the IPSec connection. It doesn't have to be unique. Avoid entering confidential information.
- Customer-Premises Equipment Compartment: Leave as is (the VCN's compartment).
- Customer-Premises Equipment: Select the CPE object you created earlier.
- Dynamic Routing Gateway Compartment: Leave as is (the VCN's compartment).
- Dynamic Routing Gateway: Select the DRG that you created earlier.
- Static Route CIDR: Enter at least one static route CIDR (see[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Prerequi)). If you need to add another, click Add Static Route . You can enter up to 10 static routes, and you can[change the static routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route)later.
- Click Show Advanced Options and optionally provide the following items:
- CPE IKE Identifier: Oracle defaults to using the public IP address of the CPE. But if your[CPE is behind a NAT device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components), you might need to enter a different value. You can either enter the new value here, or[change the value](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id)later.
- Tunnel 1 and Tunnel 2 : Leave as is. Later if you want to use BGP dynamic routing instead of static routing for the VPN tunnels, see[Changing from Static Routing to BGP Dynamic Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp).
- Tags: Leave as is. You can add tags later. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- 

Click Create IPSec Connection .

The IPSec connection is created and displayed on the page. The connection is in the Provisioning state for a short period.

The displayed tunnel information includes the IP address of the VPN headend and the tunnel's IPSec status (possible values are Up, Down, and Down for Maintenance). At this point, the status is Down. To view the tunnel's shared secret, click the Actions menu (three dots) , and then click View Shared Secret .
- 

Copy the Oracle VPN IP address and shared secret for each of the tunnels and share them with the network engineer who configures the on-premises router.

For more information, see[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm). You can view this tunnel information here in the Console at any time.

You have now created all the components required for Site-to-Site VPN. Next,your network administrator must configure the CPE device before network traffic can flow between your on-premises network and VCN.

[Task 4: Configure your CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#)

These instructions are for the network administrator.
- Ensure you have the tunnel configuration information Oracle provided during VPN Connect setup. See[Task 3: Add Site-to-Site VPN to your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#To_add_a_VPN_to_your_cloud_network).
- Configure your CPE according to the information in[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm).

If instances are already in the subnet, you can confirm the IPSec connection is up and running by connecting to the instances from your on-premises network.

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following operations:
- [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn): Always include a DNS label for the VCN if you want the instances to have hostnames (see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm)).
- [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet): Create one regional private subnet. Include a DNS label for the subnet if you want the instances to have hostnames. Use the default route table, default security list, and default set of DHCP options.
- [CreateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/CreateDrg): Creates a dynamic routing gateway (DRG)
- [CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment): Attaches the DRG to the VCN.
- [CreateCpe](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Cpe/CreateCpe): Provide the public IP address of the CPE at your end of the VPN (see[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Prerequi)).
- [CreateIPSecConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnection/CreateIPSecConnection): Provide the static routes for your on-premises network (see[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Prerequi)). The command returns the configuration information that your network administrator needs to configure your CPE. If you need that information later, you can get it with[GetIPSecConnectionDeviceConfig](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionDeviceConfig/GetIPSecConnectionDeviceConfig). For more information about the configuration, see[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm).
- [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable): To enable communication through the VPN, update the default route table to include this route: a route rule with destination = 0.0.0.0/0, and destination target = the DRG you created earlier.
- 

First call[GetSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/GetSecurityList)to get the default security list, and then call[UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)to add rules for the types of connections that your instances in the VCN need. Be aware that`UpdateSecurityList`overwrites the entire set of rules. Here are some suggested rules to add:
- Stateful ingress: Source type=CIDR, source CIDR=0.0.0.0/0, protocol=TCP, source port = all, destination port=80 (for HTTP).
- Stateful ingress: Source type=CIDR, source CIDR=0.0.0.0/0, protocol=TCP, source port = all, destination port=443 (for HTTPS).
- Stateful ingress: Source type=CIDR, source CIDR=0.0.0.0/0, protocol=TCP, source port = all, destination port=1521 (for SQL*Net access to Oracle databases).
- Stateful ingress: Source type=CIDR, source CIDR=0.0.0.0/0, protocol=TCP, source port=all, destination port=3389 (for RDP; required only if using Windows instances).
- [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance): Create one or more instances in the subnet. The scenario's diagram shows instances in two different availability domains. When you create the instance, you choose the AD, which VCN and subnet to use, and several other characteristics. For more information, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
Tip  
  
For more security, you could modify all the stateful ingress rules to allow traffic only from within your VCN and your on-premises network. Create separate rules for each, one with the VCN's CIDR as the source, and one with the on-premises network's CIDR as the source.
Important  
  
Although you can create instances in the subnet, you can't communicate with them from your on-premises network until your network administrator configures your CPE (see[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm)). After that, Site-to-Site VPN should be up and running. You can confirm its status by using[GetIPSecConnectionDeviceStatus](https://docs.oracle.com/iaas/api/#/en/iaas/latest/IPSecConnectionDeviceConfig/GetIPSecConnectionDeviceConfig)
