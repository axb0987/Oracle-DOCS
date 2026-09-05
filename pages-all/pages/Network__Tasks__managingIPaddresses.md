# Private IP Addresses
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm
- Fetched: 2026-09-05 02:45 CDT

# Private IP Addresses

Learn how to manage the IP addresses assigned to an instance in a virtual cloud network.

IPv6 addressing is supported for all commercial and government regions. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).

## Overview of IP Addresses

Instances use IP addresses for communication. Each instance has at least one private IP address and optionally one or more public IP addresses. A private IP address lets the instance communicate with other instances inside the VCN, or with hosts in an on-premises network (by using Site-to-Site VPN or Oracle Cloud Infrastructure FastConnect). A public IP address lets the instance communicate with hosts on the internet. For more information, see these related topics:
- [Public vs. Private Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Public)
- [How IP Addresses Are Assigned](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#How)
- [Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm)

### About the Private IP Object

The Networking service supports private IP address assignment through private IP objects. A private IP object can be either of the following:
- IP address: A /32 bit IP address.
- IP CIDR address: An IP address range specified with a network mask (CIDR notation).

IP Address Attributes

An IP address can include the following:
- An optional hostname for DNS (for more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm)).
- An optional[public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm)assigned to it.
- Designation as a primary or secondary private IP address (with an implied /32-bit netmask).

IP CIDR Address Attributes

An IP CIDR address private object is always a secondary private IP object with a user-defined ‘/X’ netmask value.

Private IP Object Attributes

Private IP objects have the following attributes:
- Assignment by either you or Oracle.
- An Oracle-assigned OCID (see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). If you use the API, you can also assign a friendly name to each private IP object.
- Type: Either an IP address (/32-bit IP address) or an IP CIDR address (range of IP addresses in CIDR format).
- Optional association with a custom route table (see[Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing)). For IP CIDR addresses, all IPs within the range share the custom route table association.

Each instance receives a primary private IP address object during instance creation. The Networking service uses the Dynamic Host Configuration Protocol (DHCP) to pass the object's private IP address to the instance. This address doesn't change during the instance's lifetime and can't be removed from the instance. The private IP object is terminated when the instance is terminated.

If an instance has any[secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm)attached, each of those VNICs also has a primary private IP.

A private IP address can optionally have a[public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm)assigned to it.

A private IP object can be the target of a route rule in a VCN. For more information, see[Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route).

### About Secondary Private IP Objects

You can add either a secondary private IP address or secondary private IP CIDR address to a compute instance after its creation. You can add it to either the primary VNIC or a secondary VNIC on the instance. The secondary private IP address or the secondary private IP CIDR address must come from one of the CIDRs of the VNIC's subnet. You can move either a secondary private IP address or an IP CIDR address from a VNIC on one instance to a VNIC on another instance if both VNICs belong to the same subnet. A CIDR IP address cannot overlap with any other private IP objects, reserved or assigned.

Here are a few reasons why you might use secondary private IP addresses:
- Instance failover : You assign a secondary private IP to an instance. Then if the instance has problems, you can easily reassign that secondary private IP to a standby instance in the same subnet. If the secondary private IP has a public IP assigned to it, that public IP moves along with the private IP.
- Running several services or endpoints on a single instance : For example, you could have several container pods running on a single instance, and each uses an IP address from the VCN's CIDR. The containers have direct connectivity to other instances and services in the VCN. Another example: you could run several SSL websites with each one using its own IP address.

Here are a few reasons why you might use a secondary private IP CIDR address:
- Increase the number of private IP addresses on a VNIC : You assign a secondary private IP CIDR address to a VNIC if you need more than 64 private IP addresses. You can assign a CIDR block with a netmask larger than /26 or create multiple smaller CIDR blocks. However, you must not exceed the limit of 64 private IP objects per VNIC.
- Accelerate IP address allocation : Assigning a secondary private IP CIDR address to a VNIC allows you to allocate a contiguous range of IP addresses in a single API call. This method makes additional IP addresses available within seconds.

Here are more details about secondary private IP objects:
- They're supported for all Compute shapes and OS types, for both bare metal (BM) and virtual machine(VM) instances.
- A VNIC can have a maximum of 65 private IPv4 addresses: 1 primary private IP address and a combination of up to 64 secondary private IP addresses. A VNIC can also have 32 secondary IPv6 objects. A VNIC's primary address is IPv4 unless the subnet is configured for IPv6-only addressing.
- They can be assigned only after the instance is created (or the secondary VNIC is created/attached).
- A secondary private IP object assigned to a VNIC in a[regional subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/Overview_of_VCNs_and_Subnets.htm)has a null availability domain attribute. Compare this with the VNIC's primary private IP, which always has its availability domain attribute set to the instance's availability domain, regardless of whether the instance's subnet is regional or AD-specific.
- Deleting a secondary private IP object from a VNIC returns the address or range of addresses to the pool of available addresses in the subnet.
- They're automatically deleted when you terminate the instance (or detach/delete the secondary VNIC).
- The instance's bandwidth is fixed regardless of the number of private IP objects attached. You can't specify a bandwidth limit for a particular IP address on an instance.
- A secondary private IP address can have a[reserved public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Tasks/managingpublicIPs.htm)assigned to it. An IP CIDR address, including all individual IP addresses within the CIDR range, can't have a public IP assigned.
- A secondary private IP address can have an[FQDN created](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm#About)for IP resolution. A secondary private IP CIDR address cannot.
- A secondary private host IP address and each individual IP address within an IP CIDR address can query the VCN DNS resolver IP address.
- Neither a secondary private IP address nor an IP CIDR address can query the IMDS endpoint IP address.

### Private IP Object Automatic Assignment Behaviors

IPv4 Automatic Assignment
- If a subnet has only one IPv4 CIDR block, private IP addresses and IP CIDR addresses are automatically assigned from that prefix.
- When a subnet has more than one IPv4 CIDR block, assignment behaviors differ:
- If you specify a CIDR block during allocation, IPv4 private IP addresses and IP CIDR addresses are randomly assigned from that block.
- If you don't specify a CIDR block during allocation:
- IPv4 private IP addresses are assigned from the first CIDR block in the subnet. You can view this block in the IPv4 CIDR Block field in the Subnet details view in the Console or the`cidrBlock`field in the[GetSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/GetSubnet)API details.
- IPv4 private IP CIDR addresses are assigned from the other CIDR blocks in the subnet.
Note  
  
We recommend using two or more IPv4 CIDR blocks if you plan to use automatic address allocation. Using multiple CIDR blocks reduces the risk of IP fragmentation that can result from varying IP CIDR address lengths.

IPv6 Automatic Assignment

IPv6 objects have unique assignment behaviors:
- All IPv6 objects are assigned from Oracle-GUA prefixes first, if available.
- If Oracle-GUA prefixes aren't available, objects are assigned from BYOIPv6-GUA prefixes.
- If neither Oracle-GUA nor BYOIPv6-GUA prefixes are available, objects are assigned from ULA prefixes.
- IPv6 addresses are automatically assigned from the first`::/80`prefix.
- IPv6 CIDR addresses are automatically assigned from the remaining network space within the`::/64`subnet.

### Subnet Behaviors for IP CIDR Addressing

IPv4 CIDR Addressing
- A subnet with IPv4 addressing supports an IPv4 CIDR address assignment in any and all CIDR blocks associated with the subnet.
- If a CIDR address is requested from the first CIDR block of the subnet (viewable as the IPv4 CIDR Block field in the subnet's details page in the Console or the`cidrBlock`field in the[GetSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/GetSubnet)API details), the subnet transitions to an UPDATING state. The amount of time the subnet remains in UPDATING state depends on how many host IP addresses are already allocated out of the CIDR block.

During this time, you can't perform any IP address administrative tasks (assign new IP addresses, delete existing IP addresses). This is a one-time update behavior. Because of this, we recommend using two or more or more subnet CIDR blocks when IP CIDR addressing is to be used. Host IPs are automatically assigned out of the IPv4 CIDR block and IP CIDR addresses are auto-assigned out of the other subnet CIDR blocks.
- If a CIDR address is requested from any other CIDR block, no updating behavior occurs.

IPv6 CIDR Addressing
- 

A subnet with IPv6 addressing will support an IPv6 CIDR address assignment only in subnets and prefixes assigned after the CIDR addressing feature becomes Generally Available (GA) in the region and realm.
- 

If you have an existing / legacy subnet that you want to enable IP CIDR addressing support, open a[support request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm)to coordinate a manual updating task for each IPv6 prefix needing to support CIDR addressing.

### IP Address Information in the Instance Metadata

The[instance metadata](https://docs.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm)includes information about the private IP addresses at this URL:

```

```

Here's an example response:

```

```

### Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).

## Private IP Tasks

You can perform the following tasks with private IP addresses:
- [Assigning a New Secondary Private IP to a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm)
- [Configuring Linux to Use a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm)
- [Configuring Windows to Use a Secondary IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm)
- [Moving a Secondary Private IP Address to a Different VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm)
- [Listing Private IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm)
- [Getting a Private IP Address's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm)
- [Editing Private IP Address Information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm)
- [Managing Tags For a Private IP Object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm)
- [Deleting a Private IP Object](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm)
