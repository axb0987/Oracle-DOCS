# Configuring VCN Security Rules for File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm
- Fetched: 2026-09-05 02:04 CDT

# Configuring VCN Security Rules for File Storage

Before you can mount a file system, you must configure security rules to allow traffic to the mount target's VNIC using specific protocols and ports. Security rules enable traffic for the following:
- Open Network Computing Remote Procedure Call (ONC RPC) rpcbind utility protocol
- Network File System (NFS) protocol
- Network File System (MOUNT) protocol
- Network Lock Manager (NLM) protocol
- LDAPS protocol (if using NFS v.3[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm)or[LDAP for authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm))
- DNS protocol (if using customer-managed DNS)

## File Storage Security Rule Scenarios

There are several basic scenarios that require different security rules for File Storage:

[Scenario A: Mount target and instance in different subnets (recommended)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

Tip  
  

Use separate subnets for mount targets and instances to control exactly which IP addresses are assigned to instances and avoid interference or availability outages because of mount target IP requirements.

For more information, see the[instance creation failure due to IP address allocation for mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/instance-creation-ip-allocated.htm)and[insufficient unallocated IP addresses during failover](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/mounttargetfails.htm)troubleshooting topics.

In this scenario, the mount target that exports the file system is in a different subnet than the instance you want to mount the file system to. Security rules must be configured for both the mount target and the instance either in a security list for each subnet, or a network security group (NSG) for each resource.

Set up the following the following security rules for the mount target . Specify the instance IP address or CIDR block as the source for ingress rules:
- Stateful ingress from source instance CIDR ALL source ports to destination ports 111, 2048, 2049, and 2050, TCP protocol.
- Stateful ingress from source instance CIDR ALL source ports to destination ports 111 and 2048, UDP protocol.
Important  
  
We recommend that NFS clients be limited to reserved ports. To do this, set the Source Port range to 1-1023 . You can also set export options for a file system to require clients to connect from a privileged source port. For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).

Next, set up the following security rules for the instance . Specify the mount target IP address or CIDR block as the destination for egress rules:
- Stateful egress from ALL source ports to destination mount target CIDR ports 111, 2048, 2049, and 2050, TCP protocol.
- Stateful egress from ALL source ports to destination mount target CIDR ports 111 and 2048, UDP protocol.

Here's an example of the rules for this scenario set up in security list rules for the instance and mount target. This example shows rules for specific source and destination CIDR blocks.

Ingress rules for the mount target's NSG or subnet security list. The instance CIDR block`10.0.0.0/24`is the source:

[

Egress rules for the instance's NSG or subnet security list. The mount target CIDR block`10.0.1.0/24`is the destination:

[

#### Using a Security List

Security lists are associated with subnets. If you use security lists to set up your security rules, you need to set up the mount target rules in the mount target subnet, and the instance rules in the instance subnet. You can add the rules to the default security list for each subnet, or create new security lists.

#### Using a network security group (NSG)

Another method for applying security rules is to set them up in a network security group (NSG), and then add the mount target and instance to the NSG. Unlike security list rules that apply to all VNICs in the subnet, NSGs apply only to resource VNICs you add to the NSG.

See[Ways to Enable Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Ways)for an overview of these methods and instructions about how to use them to set up security rules.

[Scenario B: Mount target and instance in the same subnet](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

Caution  
  

We recommend that mount targets and instances use separate subnets to control exactly which IP addresses are assigned to instances and avoid interference or availability outages because of mount target IP requirements.

For more information, see the[instance creation failure due to IP address allocation for mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/instance-creation-ip-allocated.htm)and[insufficient unallocated IP addresses during failover](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Troubleshooting/mounttargetfails.htm)troubleshooting topics.

In this scenario, the mount target that exports the file system is in the same subnet as the instance you want to mount the file system to.
- Stateful ingress from source instance CIDR ALL source ports to destination ports 111, 2048, 2049, and 2050, TCP protocol.
- Stateful ingress from source instance CIDR ALL source ports to destination ports 111 and 2048, UDP protocol.
- Stateful egress from ALL source ports to destination mount target CIDR ports 111, 2048, 2049, and 2050, TCP protocol.
- Stateful egress from ALL source ports to destination mount target CIDR ports 111 and 2048, UDP protocol.
Important  
  
We recommend that NFS clients be limited to reserved ports. To do this, set the Source Port range to 1-1023 . You can also set export options for a file system to require clients to connect from a privileged source port. For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).

Here's an example of the rules for this scenario set up for a single subnet that contains both the mount target and the instance. In this example, both the mount target and the instance are in CIDR block`10.0.0.0/24`:

[

[

#### Using a security list

Security lists are associated with subnets. You can set up the required security rules in the default security list for the mount target subnet, or create a new security list. Security list rules apply to all resources in the subnet.

#### Using a network security group (NSG)

Another method for applying security rules is to set them up in a network security group (NSG), and then add the mount target to the NSG. Unlike security list rules that apply to all VNICs in the subnet, NSGs apply only to the resource VNICs you add to the NSG.

See[Ways to Enable Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Ways)for an overview of these methods and instructions about how to use them to set up security rules.

[Scenario C: Mount target and instance use TLS in-transit encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

In this scenario, in-transit encryption secures data between instances and mounted file systems using TLS v.1.2 (Transport Layer Security) encryption. See[Using In-transit TLS Encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm)for more information.

You can limit the source to the IP address or CIDR block of your choice.

Set up the following security rules for the mount target :
- Stateful ingress from source CIDR ALL source ports to destination port 2051, TCP protocol.

Here's an example of the rule for this scenario set up in security list for the mount target's NSG or subnet. This example shows rules for specific source CIDR block`10.0.0.0/24`as the source:

[

#### Using a security list

Security lists are associated with subnets. You can set up the required security rules in the default security list for the mount target subnet, or create a new security list. Security list rules apply to all resources in the subnet.

#### Using a network security group (NSG)

Another method for applying security rules is to set them up in a network security group (NSG), and then add the mount target to the NSG. Unlike security list rules that apply to all VNICs in the subnet, NSGs apply only to resource VNICs you add to the NSG.

See[Ways to Enable Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Ways)for an overview of these methods and instructions about how to use them to set up security rules.

[Scenario D: Mount target uses LDAP for authorization](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

In this scenario, traffic between a mount target and the LDAPS port of an LDAP server is allowed.

You can limit the source to the IP address of the mount target and the destination IP address to your LDAP server's subnet.

Set up the following security rules for the mount target :
- Stateful egress from TCP ALL ports to LDAP server IP (or corresponding CIDR) port 636 .
Note  
  
This rule assumes LDAPS uses the default port of 636. Change this value if your LDAP server is using a different port.

If using a customer-managed DNS server, the mount target also needs the following security rules:
- Stateful egress from TCP ALL ports to DNS server IP (or corresponding CIDR) port 53 .
- Stateful egress from UDP ALL ports to DNS server IP (or corresponding CIDR) port 53 .

#### Using a security list

Security lists are associated with subnets. You can set up the required security rules in the default security list for the mount target subnet, or create a new security list. Security list rules apply to all resources in the subnet.

#### Using a network security group (NSG)

Another method for applying security rules is to set them up in a network security group (NSG), and then add the mount target to the NSG. Unlike security list rules that apply to all VNICs in the subnet, NSGs apply only to resource VNICs you add to the NSG.

See[Ways to Enable Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Ways)for an overview of these methods and instructions about how to use them to set up security rules.

## Ways to Enable Security Rules for File Storage

The Networking service offers two virtual firewall features that both use security rules to control traffic at the packet level. The two features are:
- Security lists: The original virtual firewall feature from the Networking service. When you create a VCN, a default security list is also created. Add the required rules to the security list for the subnet that contains the mount target. (If you're setting up[Scenario A: Mount target and instance in different subnets (recommended)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-a), you have to add rules for both subnets.) See[Setting Up Required Rules in a Security List](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Setting)for instructions.
- Network security groups (NSGs): A subsequent feature designed for application components that have different security postures. Create an NSG that contains the required rules, and then add the mount target to the NSG. Alternatively, you can add the required rules to a previously existing NSG, and add the mount target to the NSG. Each mount target can belong to up to five (5) NSGs. (If you're setting up[Scenario A: Mount target and instance in different subnets (recommended)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-a), you have to add both the mount target and instance to an NSG that contains the required security rules.) See[Setting Up Required Rules in a Network Security Group (NSG)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#Setting2)for instructions.
Important  
  

You can use security lists alone, network security groups alone, or both together. It depends on your particular security needs.

If you choose to use both security lists and network security groups, the set of rules that applies to a given mount target VNIC is the combination of these items:
- The security rules in the security lists associated with the VNIC's subnet
- The security rules in all NSGs that the VNIC is in

It doesn't matter which method you use to apply security rules to the mount target VNIC, as long as the ports for protocols necessary for File Storage are correctly configured in the rules applied.

See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm),[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm), and[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for more information, examples, and scenarios about how these features interact in your network.[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm)provides general information about networking. See[About File Storage Security](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm)for information about how security rules work with other types of security in File Storage.

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)covers management of all networking components, including security lists and NSGs. See the[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm)for more information.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Using the Console

### Setting Up Required Rules in a Security List

You can add the required rules to a pre-existing security list associated with a subnet, such as the default security list that is created along with the VCN. See[Creating a Security List](https://docs.oracle.com/iaas/Content/Network/Concepts/creating-securitylist.htm)for more information.

[To add required rules to a security list](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- 

In the Scope section, select the compartment that contains the VCN the subnet is in.
- Click the name of the VCN.
- On the details page for the cloud network, in Resources , and then click Security Lists .
- Click the name of the security list used by the subnet.
- In Resources , click Ingress Rules .
- 

Click Add Ingress Rules .
- Specify that it's a stateful rule by leaving the check box clear. (For more information about stateful and stateless rules, see[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)). By default, rules are stateful unless you specify otherwise.
- To allow traffic from the subnet of the cloud network, click Source Type , choose CIDR , and then enter the CIDR block for the subnet. For example,`10.0.0.0/24`.
- Click IP Protocol , and then choose the protocol. For example, TCP .
- 

In Source Port Range , specify the range of ports that you want to allow traffic from. Alternatively, accept the default of All to allow traffic from any source port.
- Click Destination Port Range , and then enter individual ports or a port range. For example, 2048-2050 .
- Click + Additional Ingress Rule to create more ingress rules.
- When you're done, click Add Ingress Rules .
- Next, create the egress rules. In Resources , click Egress Rules .
- 

Click Add Egress Rules.
- Specify that it's a stateful rule by leaving the check box clear.
- Click Destination Type , choose CIDR , and then enter the CIDR block for the subnet. For example,`10.0.0.0/24`.
- Click IP Protocol , and then choose the protocol. For example, TCP .
- 

In Source Port Range , and then enter individual ports or a port range. For example, 2048-2050 .
- In Destination Port Range , accept the default of All to allow traffic to any destination port.
- Click + Additional Egress Rule to create more egress rules.
- When you're done, click Add Egress Rules .

### Setting Up Required Rules in a Network Security Group (NSG)

The general process for setting up NSGs that work with File Storage is:
- Create an NSG with the required security rules. (Alternatively, you can add them to a previously existing NSG.)
- Add the mount target (or more specifically, the mount target's VNIC) to the NSG. You can do this when you create the mount target, or you can update the mount target and add it to one or more NSGs that contain the required security rules.
- If you're setting up[Scenario A: Mount target and instance in different subnets (recommended)](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-a), you'll have to add both the mount target and instance to an NSG that contains the required security rules.

[To create an NSG with the required security rules](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

Prerequisite: Become familiar with the[parts of security rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).
- Open the navigation menu , select Networking , and then select Virtual cloud networks .
- Click the VCN you're interested in.
- Under Resources , click Network Security Groups .
- Click Create Network Security Group .
- 

Enter the following:
- Name: A descriptive name for the network security group. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Create in Compartment: The compartment where you want to create the network security group, if different from the compartment you're currently working in.
- Show Tagging Options: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Click Next .
- 

Enter ingress rules.
- Specify that it's a stateful rule by leaving the check box clear. (For more information about stateful and stateless rules, see[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)). By default, rules are stateful unless you specify otherwise.
- In Direction , choose Ingress .
- To allow traffic from the subnet of the cloud network, click Source Type , choose CIDR , and then enter the CIDR block for the subnet. For example,`10.0.0.0/24`.
- Click IP Protocol , and then choose the protocol. For example, TCP .
- 

In Source Port Range , specify the range of ports that you want to allow traffic from. Alternatively, accept the default of All to allow traffic from any source port.
- Click Destination Port Range , and then enter individual ports or a port range. For example, 2048-2050 .
- Click + Another Rule to create more ingress rules.
- 

Enter egress rules.
- Specify that it's a stateful rule by leaving the check box clear.
- In Direction , choose Egress .
- Click Destination Type , choose CIDR , and then enter the CIDR block for the subnet. For example,`10.0.0.0/24`.
- Click IP Protocol , and then choose the protocol. For example, TCP .
- 

In Source Port Range , and then enter individual ports or a port range. For example, 2048-2050 .
- In Destination Port Range , accept the default of All to allow traffic to any destination port.
- Click + Another Rule to create more egress rules.
- When you're done, click Create .

[To add a mount target to an NSG](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

- When creating a mount target along with a file system: See[Creating a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm).
- When creating only the mount target: See[Creating a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm).
- 

For an existing mount target:

- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- 

In the List Scope section, select a compartment.
- 

Find the mount target you're interested in, click the Actions menu (three dots) , and then click View Mount Target Details .
- 

In the Mount Target Information tab, click the Edit link next to Network Security Groups .
- Select a Compartment and NSG from the list.
- Click Save .

[To add an instance to an NSG](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#)

See[Adding or Removing a Resource from an NSG](https://docs.oracle.com/iaas/Content/Network/Concepts/nsg-add_remove_resource.htm)
