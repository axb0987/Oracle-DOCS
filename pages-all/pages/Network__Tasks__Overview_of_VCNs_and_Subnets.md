# Overview of VCNs and Subnets
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm
- Fetched: 2026-09-05 02:42 CDT

# Overview of VCNs and Subnets

Learn about virtual cloud networks (VCNs) and subnets in OCI.

This topic describes virtual cloud networks (VCNs) and the subnets in them. This topic uses the terms virtual cloud network , VCN , and cloud network interchangeably. The Console uses the term Virtual Cloud Network , whereas for brevity the API uses VCN .

A VCN is a software-defined network that you set up in the Oracle Cloud Infrastructure data centers in a particular region . A subnet is a subdivision of a VCN. For an overview of VCNs, allowed size, default VCN components, and scenarios for using a VCN, see[Networking Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm).

A VCN can have several non-overlapping IPv4 CIDR blocks that you can change after you create the VCN. Regardless of the number of CIDR blocks, the max number of private IP objects you can create within the VCN is 64,000. A VCN can optionally be enabled for IPv6 and Oracle allocates a /56 prefix. You can also import a BYOIP IPv6 prefix and assign it to an existing VCN or create a new VCN with a BYOIP or ULA IPv6 prefix.

You can privately connect a VCN to another VCN so that the traffic doesn't traverse the internet. The CIDRs for the two VCNs must not overlap. For more information, see[Access to Other VCNs: Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm). For an example of an advanced routing scenario that involves the peering of several VCNs, see[Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm).

Each subnet in a VCN consists of one or more contiguous range of IPv4 addresses and optionally IPv6 addresses that don't overlap with other subnets in the VCN. Example: 172.16.1.0/24. With IPv4 addresses and IPv6 addresses, the first two addresses and the last in the subnet's CIDR are reserved by the Networking service. You can change the size of a subnet’s IPv4 prefix after creation. IPv6-enabled subnets are always /64.

Subnets act as a unit of configuration comprised of: a route table, security lists, and DHCP options. For more information, see[Default Components that Come With a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Default).

Subnets can be either public or private (see[Public vs. Private Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Public)). The choice of public or private happens during subnet creation, and you can't change it later.

You can think of each Compute instance as residing in a subnet. But to be precise, each instance is attached to a[virtual network interface card (VNIC)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm), which in turn resides in the subnet and enables a network connection for that instance.

IPv6 addressing is supported for all commercial and government regions. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).

## About Regional Subnets

Originally subnets were designed to cover only one availability domain (AD) in a region. They were all AD-specific , which means the subnet's resources were required to reside in a particular availability domain. Now subnets can be either AD-specific or regional . You select the type when you create the subnet. Both types of subnets can coexist in the same VCN. In the following diagram, subnets 1 to 3 are AD-specific, and subnet 4 is regional.
[

Aside from the removal of the AD constraint, regional subnets behave the same as AD-specific subnets. We recommend using regional subnets because they're more flexible. They make it easier to efficiently divide a VCN into subnets while also designing for availability domain failure.

When you create a resource such as a Compute instance, you decide which availability domain the resource is in. From a virtual networking standpoint, you must also decide which VCN and subnet the instance is in. You can select either a regional subnet, or an AD-specific subnet that matches the AD you chose for the instance.
Caution  
  
If anyone in your organization implements a regional subnet, be aware that you might need to update any client code that works with Networking service subnets and private IPs . Regional subnets involve possible breaking API changes. For more information, see the[regional subnets](https://docs.oracle.com/iaas/releasenotes/changes/08c01d20-c829-47f2-8d54-9e9958f50ba8/)release note.

## VCN and Subnet Limits

Resource

Scope

Oracle Universal Credits

Pay As You Go or Trial
VCN Region 50 10
Subnets VCN 300 300
IPv4 CIDRs VCN 16 16
IPv6 Prefixes VCN 16 16
IPv4 CIDRs Subnet 16 16
IPv6 Prefixes Subnet 16 16
Oracle allocated IPv6 prefix VCN 1 1
Private Service Access (PSA) Endpoints VCN 50 50
Private Service Access (PSA) Endpoints Region 200 200
* Limit for this resource can be increased to a maximum of five.

## Working with VCNs and Subnets

One of the first things you do when working with Oracle Cloud Infrastructure resources is create a VCN with one or more subnets. You can easily get started in the Console with a simple VCN and some related resources that enable you to create and connect to an instance. See[Tutorial - Launching Your First Linux Instance](https://docs.oracle.com/iaas/Content/GSG/Reference/overviewworkflow.htm)or[Tutorial - Launching Your First Windows Instance](https://docs.oracle.com/iaas/Content/GSG/Reference/overviewworkflowforWindows.htm).

For the purposes of access control, when you create a VCN or subnet, you must specify the compartment where you want the resource to reside. Consult the tenancy administrator if you're not sure which compartment to use.

You can optionally assign descriptive names to the VCN and its subnets. The names don't have to be unique, and you can change them later. Oracle automatically assigns each resource a unique identifier called an Oracle Cloud ID (OCID). For more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You can also add a DNS label for the VCN and each subnet, which are required if you want the instances to use the Internet and VCN Resolver feature for DNS in the VCN. For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).

When you create a subnet, you can optionally specify a[route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)for the subnet to use. If you don't, the subnet uses the cloud network's default route table. You can[change which route table the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm)at any time.

Also, you can optionally specify one or more[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm)for the subnet to use (up to five). If you don't specify any, the subnet uses the cloud network's[default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm#Default). You can[change which security list the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm)at any time. Remember that the[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securityrules.htm)are enforced at the instance level, even though the list is associated at the subnet level.[Network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm)are an alternative to security lists and let you apply a set of security rules to a set of resources that all have the same security posture , instead of all the resources in a particular subnet.

You can optionally specify a[set of DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDHCP.htm)for the subnet to use. All instances in the subnet receive the configuration specified in that set of DHCP options. If you don't specify a set, the subnet uses the cloud network's default set of DHCP options. You can[change which set of DHCP options the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm)at any time.

To delete a subnet, it must contain no resources (no instances, load balancers, OCI database systems, and orphaned mount targets). For more details, see[Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion).

To delete a VCN, its subnets must contain no resources. Also, the VCN must have no attached gateways. If you're using the Console, the "Delete All" process you can use after first ensuring the subnets are empty. See[Deleting a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm).

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

### Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).

### Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect the ability to manage VCNs and subnets:
- Subnets in a security zone can't be public. All subnets must be private.
-
