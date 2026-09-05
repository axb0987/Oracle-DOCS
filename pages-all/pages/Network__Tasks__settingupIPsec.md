# Setting Up Site-to-Site VPN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm
- Fetched: 2026-09-05 02:47 CDT

# Setting Up Site-to-Site VPN

Learb how to set up Site-to-Site VPN between your on-premises network and virtual cloud network.

This topic gives instructions for constructing a Site-to-Site VPN IPSec connection from an on-premises network to a VCN. For general information about Site-to-Site VPN, see[Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm).

## Before You Get Started

To prepare, do these things first:
- Read this section:[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing)
- 

Answer these questions:

Question Answer
What is the VCN's CIDR?
What is the public IP address of the CPE device? If you have several devices for redundancy, get the IP address for each.

Note: If the CPE device is behind a NAT device, see[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/overviewIPsec.htm#components)and also[Requirements and Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/configuringCPE.htm#reqs).
Do you want to use port address translation (PAT) between each CPE device and the VCN?
What type of routing do you plan to use? If you want BGP dynamic routing, list the BGP session IP addresses to use and the ASN of the on-premises network. The IP addresses must be part of Site-to-Site VPN's encryption domain.

If you want static routing, what are the static routes for the on-premises network? See[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).

Do you plan to use policy based routing or multiple encryption domains? See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel).
Do you want to provide each tunnel's shared secret or let Oracle assign them? See[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components).
- Draw a diagram of the network layout (for examples, see the first task in[Example: Setting Up a Proof of Concept Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_poc)). Think about which parts of the on-premises network need to communicate with the VCN, and the reverse. Map out the[routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)and[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)that you need for the VCN.
Tip  
  
If you have an existing Site-to-Site VPN that uses static routing, you can[change the tunnels to instead use BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp).

The following link local IP ranges aren't valid for use with Site-to-Site VPN inside tunnel interfaces:
- 169.254.10.0 to 169.254.19.255
- 169.254.100.0 to 169.254.109.255
- 169.254.192.0 to 169.254.201.255

## Overall Process

Here's the overall process for setting up Site-to-Site VPN:
- Complete the tasks listed in[Before You Get Started](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Before).
- Set up Site-to-Site VPN components (instructions in[Example: Setting Up a Proof of Concept Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_poc)):
- Create a VCN.
- Create a DRG.
- Attach the DRG to the VCN.
- Create a route table and route rule for the DRG.
- Create a security list and required rules.
- Create a subnet in the VCN.
- Create a CPE object and provide the CPE device's public IP address.
- Create an IPSec connection to the CPE object and provide required routing information.
- Use the CPE Configuration Helper: A network engineer must configure the CPE device with information that Oracle provides during the previous steps. The CPE Configuration Helper generates the information for the network engineer. For more information, see[Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)and also[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm).
- Have a network engineer configure the CPE device.
- Validate connectivity.

If you plan to set up redundant connections, see the[Connectivity redundancy guide (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf).

## Example: Setting Up a Proof of Concept Site-to-Site VPN

Tip  
  
Oracle offers a quickstart workflow to make it easier to set up Site-to-Site VPN. For more information, see[Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm).

This example scenario shows how to set up a Site-to-Site VPN with a layout that you might use for a proof of concept (POC). It follows tasks 1 and 2 in[Overall Process](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Overall)and shows each component in the layout being created. For more complex layouts, see[Example Layout with Several Geographic Areas](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_multi_geo)or[Example Layout with PAT](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_pat).

[Task 1: Gather information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

Question Answer
What is the VCN's CIDR? 172.16.0.0/16
What is the public IP address of the CPE device? If you have several devices for redundancy, get the IP address for each.

Note: If the CPE device is behind a NAT device, see[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/overviewIPsec.htm#components)and also[Requirements and Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/configuringCPE.htm#reqs). 142.34.145.37
Will you be doing port address translation (PAT) between each CPE device and the VCN? No
What type of routing do you plan to use? There are three mutually exclusive choices:

If you plan to use BGP dynamic routing, list the BGP session IP addresses to use and the ASN of the on-premises network.

If you plan to use static routing, list the static routes for the on-premises network. See[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).

If you plan to use policy-based routing or require multiple encryption domains, list the IPv4 CIDR or IPv6 prefix blocks used on each end of the connection. See[Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel).

BGP dynamic routing example:

Tunnel 1:
- BGP Inside tunnel interface - CPE: 10.0.0.16/31
- BGP Inside tunnel interface - Oracle: 10.0.0.17/31

Tunnel 2:
- BGP Inside tunnel interface - CPE: 10.0.0.18/31
- BGP Inside tunnel interface - Oracle: 10.0.0.19/31

Network ASN: 12345

Static routing example:

Use 10.0.0.0/16 for the static route for a POC.
Do you want to provide each tunnel's shared secret or let Oracle assign them? See[Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components). Let Oracle assign.

Here's an example diagram for task 1 that uses BGP dynamic routing:
[

Callout 1: Default subnet route table
Destination CIDR Route target
10.0.0.0/16 DRG

Callout 2: security list
Destination CIDR Permission
10.0.0.0/16 Allowed

Callouts 3 to 6
Callout Function IP
3 CPE public IP address 142.34.145.37
4a Tunnel 1 BGP: Inside Tunnel Interface

CPE - 10.0.0.16/31

Oracle - 10.0.0.17/31
4b Tunnel 2 BGP: Inside Tunnel Interface

CPE - 10.0.0.18/31

Oracle - 10.0.0.19/31
5

Tunnel 1 Oracle VPN IP Address: 129.213.240.50
6

Tunnel 2 Oracle VPN IP Address: 129.213.240.53

Here's an example diagram for task 1 that uses static routing:

[

Callout 1: Default subnet route table
Destination CIDR Route target
10.0.0.0/16 DRG

Callout 2: security list
Destination CIDR Permission
10.0.0.0/16 Allowed

Callouts 3 to 6
Callout Function IP
3 CPE public IP address 142.34.145.37
4 Static route for IPSec Connection 10.0.0.0/16
5

Tunnel 1 Oracle VPN IP Address: 129.213.240.50
6

Tunnel 2 Oracle VPN IP Address: 129.213.240.53

[Task 2a: Create the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

If you already have a VCN, skip to the next task.
Tip  
  
When you use the Console to create a VCN, you can create only the VCN, or you can create the VCN with several related resources. This task creates only the VCN, and the next tasks create the other required resources.

See[Creating a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm)for detailed steps on creating a VCN in the Console.

Ensure that the VCN is done provisioning before you continue. In this example, we're using 172.16.0.0/16 as the CIDR for the VCN, but what you select doesn't matter so long as it's consistent.
[

[Task 2b: Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

[

See[Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm)for detailed steps on creating a DRG.

The DRG is created and displayed on the page. Ensure that it's done being provisioned before continuing.
Tip  
  
You could also use this DRG as the gateway for[Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/fastconnect.htm), which is another way to connect an on-premises network to a VCN.

[Task 2c: Attach the DRG to the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

[

See[Attaching a DRG to a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm)for detailed steps on attaching a DRG to a VCN.

The attachment is in the Attaching state for a short period before it's ready.

[Task 2d: Create a route table and route rule for the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

Although the VCN comes with a default route table (without any rules), in this task you create a custom VCN route table with a route rule for the DRG as target. In this example, the on-premises network is 10.0.0.0/16. You create a route rule that takes any traffic destined for 10.0.0.0/16 and routes it to the DRG. When you create a subnet in task 2f, you associate this custom route table with the subnet.
Tip  
  
If you already have an existing VCN with a subnet, you don't need to create a route table or subnet. Instead you can update the existing subnet's route table to include the route rule for the DRG.
[

Callout 1: VCN Route Table MyExampleRouteTable
Destination CIDR Route Table
10.0.0.0/16 DRG

See[Creating a VCN Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm)for detailed steps on creating VCN route tables in the Console. Use the following settings for the route rule:
- Target Type: Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself.
- Destination CIDR Block: The CIDR for the on-premises network (10.0.0.0/16 in this example).

The route table is created and displayed on the page. However, the route table doesn't do anything unless you associate it with a subnet during subnet creation (see task 2f).

[Task 2e: Create a security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

By default, incoming traffic to the instances in a VCN is set to DENY on all ports and all protocols. In this task, you set up two ingress rules and one egress rule to allow basic required network traffic. A VCN comes with a default security list with a set of default rules. However, in this task you create a separate security list with a more restrictive set of rules focused on traffic with an on-premises network. When you create a subnet in task 2f, you associate this security list with the subnet.
Tip  
  
Security lists are one way to control traffic in and out of the VCN's resources. You can also use[network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)
[

Callout 1: VCN Route Table MyExampleRouteTable
Destination CIDR Route Table
10.0.0.0/16 DRG

Callout 2: Security List MyExampleSecurityList
Ingress/Egress CIDR Protocol: Port
Ingress 10.0.0.0/16 TCP: 22
Ingress 10.0.0.0/16 ICMP: All
Egress 10.0.0.0/16 TCP: All
Important  
  
Ensure that the on-premises CIDR that you specify in the security list rules is the same (or smaller) than the CIDR that you specified in the route rule in the preceding task. Otherwise, traffic is blocked by the security lists.

See[Creating a Security List](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/creating-securitylist.htm)for detailed information on creating a security list in a VCN using the Console.
- 

Add an ingress rule with the following values, which allows incoming SSH on TCP port 22 from an on-premises network:
- Source Type: CIDR
- Source CIDR: The CIDR for an on-premises network (10.0.0.0/16 in this example)
- IP Protocol: TCP.
- Source Port Range: Leave as is (the default All).
- Destination Port Range: 22 (for SSH traffic).
- Description: An optional description of the rule.
- 

Add an egress rule with the following values, which allows outgoing TCP traffic on all ports to an on-premises network:
- Destination Type: CIDR
- Destination CIDR: The CIDR for an on-premises network (10.0.0.0/16 in this example).
- IP Protocol: TCP.
- Source Port Range: Leave as is (the default All).
- Destination Port Range: Leave as is (the default All).
- Description: An optional description of the rule.

When the security list is created it displays on the page. However, the security list doesn't do anything unless you associate it with a subnet during subnet creation (see task 2f).

[Task 2f: Create a subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

In this task, you create a subnet in the VCN. Typically a subnet has a CIDR block smaller than the VCN's CIDR. Any instances that you create in this subnet have access to an on-premises network. We recommend using[regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm). Here you create a regional private subnet.
[

Callout 1: VCN Route Table MyExampleRouteTable
Destination CIDR Route Table
10.0.0.0/16 DRG

Callout 2: Security List MyExampleSecurityList
Ingress/Egress CIDR Protocol: Port
Ingress 10.0.0.0/16 TCP: 22
Ingress 10.0.0.0/16 ICMP: All
Egress 10.0.0.0/16 TCP: All

See[Creating a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm)for detailed information on creating a subnet a VCN using the Console. Use the following values:
- Regional or AD-specific subnet: Select the radio button for Regional . We recommend using[regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm).
- CIDR Block: A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). It must be within the cloud network's CIDR block and can't overlap with any other subnets. You can't change this value later. See[Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Allowed). For reference, use a[CIDR calculator](http://www.ipaddressguide.com/cidr).
- Route Table: The route table that you created in task 2d.
- Private Subnet: Select this option. For more information, see[Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Private).
- Use DNS Hostnames in this Subnet: Leave as is (selected).
- DHCP Options: The set of DHCP options to associate with the subnet. Select the default set of DHCP options for the VCN.
- Security Lists: The security list that you created earlier.

The subnet is created and displayed on the page. The basic VCN in this example is now set up, and you're ready to create the remaining components for Site-to-Site VPN.

[Task 2g: Create a CPE object and provide the CPE device's public IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

In this task you create the CPE object, which is a virtual representation of an actual CPE device. The CPE object exists in a compartment in a tenancy. When you configure Site-to-Site VPN you need to change the configuration of the actual edge device for the on-premises network to match the configuration of the CPE object.
[

Callout 1: VCN Route Table MyExampleRouteTable
Destination CIDR Route Table
10.0.0.0/16 DRG

Callout 2: Security List MyExampleSecurityList
Ingress/Egress CIDR Protocol: Port
Ingress 10.0.0.0/16 TCP: 22
Ingress 10.0.0.0/16 ICMP: All
Egress 10.0.0.0/16 TCP: All

See[Creating a CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/cpe-create.htm)for detailed steps on creating a CPE object. In this example the most important IP address to provide is 142.34.145.37, the public or private IP address of the physical CPE device.

[Task 2h: Create an IPSec connection to the CPE object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

In this task, you create the IPSec tunnels and configure the type of routing for them (BGP dynamic routing, static routing, or policy-based routing). See[Creating an IPSec Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ip-sec-con-create.htm)for detailed steps.
Tip  
  
If you have an existing Site-to-Site VPN that uses static routing, you can[change the tunnels to instead use BGP dynamic routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp).

[Task 3: Use the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

Use the CPE Configuration Helper to generate configuration content that the network engineer can use to configure the CPE.

The content includes these items:
- For each IPSec tunnel, the Oracle VPN IP address and shared secret.
- The supported IPSec parameter values.
- Information about the VCN.
- CPE-specific configuration information.

For more information, see[Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm).

[Task 4: Have the network engineer configure the CPE](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

Provide the network engineer with the following items:
- The content generated by the[CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm).
- The[general IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/supportedIPsecparams.htm)that Oracle supports.
Important  
  
Be sure to have the network engineer configure a CPE device to support both of the tunnels in case one fails or Oracle takes one down for maintenance. If you're using BGP, see[Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).

[Task 5: Validate connectivity](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#)

After the network engineer configures the CPE device, you can confirm that the tunnel's IPSec status is Up and green. Next, you can create a Linux instance in the subnet in a VCN. Then use SSH to connect to the instance's private IP address from a host in the on-premises network. For more information, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).

## Example Layout with Several Geographic Areas

The following diagram shows a different example with the following configuration:
- Two networks in separate geographical areas that each connect to a VCN
- A single CPE device in each area
- Two IPSec VPNs (one for each CPE device)

Be aware that each Site-to-Site VPN has two routes associated with it: one for the particular geographical area's subnet, and a default 0.0.0.0/0 route. Oracle learns about the available routes for each tunnel either through BGP (if the tunnels use BGP), or because you set them as static routes for the IPSec connection (if the tunnels use static routing).
[

Callout 1: Site-to-Site VPN 1 route table
Destination CIDR Route target
10.20.0.0/16 DRG
0.0.0.0/0 DRG

Callout 2: Site-to-Site VPN 2 route table
Destination CIDR Route target
10.40.0.0/16 DRG
0.0.0.0/0 DRG

Following are some examples of situations in which the 0.0.0.0/0 route can provide flexibility:
- Assume that the CPE 1 device goes down (see the next diagram). If Subnet 1 and Subnet 2 can communicate with each other, the VCN could still reach the systems in Subnet 1 because of the 0.0.0.0/0 route that goes to CPE 2.
[
- 

If an organization adds a new geographical area with Subnet 3 and initially connects it to Subnet 2 (see the next diagram). If you added a route rule to the VCN's route table for Subnet 3, the VCN could reach systems in Subnet 3 because of the 0.0.0.0/0 route that goes to CPE 2.
[

Callout 1: VCN route table
Destination CIDR Route target
10.20.0.0/16 DRG
10.40.0.0/16 DRG
10.60.0.0/16 DRG

## Example Layout with PAT

The following diagram shows an example with this configuration:
- Two networks in separate geographical areas that each connect to a VCN
- Redundant CPE devices (two in each geographical area)
- Four IPSec VPNs (one for each CPE device)
- Port address translation (PAT) for each CPE device

For each of the four connections, the route that Oracle needs to know about is the PAT IP address for the specific CPE device. Oracle learns about the PAT IP address route for each tunnel either through BGP (if the tunnels use BGP), or because you set the relevant address as a static route for the IPSec connection (if the tunnels use static routing).

When you set up the route rules for the VCN, you specify a rule for each PAT IP address (or an aggregate CIDR that covers them all) with the DRG as the rule's target.

[

Callout 1: VCN route table
Destination CIDR Route target
PAT IP 1 DRG
PAT IP 2 DRG
PAT IP 3 DRG
PAT IP 4 DRG

## What's Next?

See these related topics and procedures:
- [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm)
- [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm)
- [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/CPElist.htm)
- [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm)
- [Changing from Static Routing to BGP Dynamic Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp)
- [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm)
- [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
- [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Reference/ipsecmetrics.htm)
- [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/ipsectroubleshoot.htm)
