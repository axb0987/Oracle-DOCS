# DNS in a Virtual Cloud Network
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm
- Fetched: 2026-09-05 02:41 CDT

# DNS in a Virtual Cloud Network

Learn about the choices for DNS in your virtual cloud network.

The Domain Name System (DNS) lets computers use hostnames instead of IP addresses to communicate with each other. This feature is limited to traffic within a Virtual Cloud Network (VCN), for use of DNS with internet traffic, see[DNS and Traffic Management](https://docs.oracle.com/iaas/Content/DNS/home.htm).

## Choices for DNS in a VCN

Following are the choices for DNS name resolution for the instances in a VCN. You make this choice for each subnet in the VCN, using the subnet's set of DHCP options. This is similar to how you configure which route table and security lists are associated with each subnet. For more information, see[DHCP Options](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingDHCP.htm).
Note  
  
You use the Domain Name Server DHCP option to specify the DNS Type for the associated subnet. If you change the option's value, either restart the DHCP client on the instance or reboot the instance. Otherwise, the change doesn't get picked up until the DHCP client refreshes the lease (within 24 hours).
DEFAULT CHOICE: INTERNET AND VCN RESOLVER This is an Oracle-provided option that includes two parts:
- Internet Resolver: Lets instances resolve hostnames that are publicly published on the internet. The instances don't need to have internet access by way of either an internet gateway or a connection to an on-premises network (such as a Site-to-Site VPN IPSec connection through a DRG ).
- VCN Resolver: Lets instances resolve hostnames (which you can assign) of other instances in the same VCN. For more information, see[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/dns.htm#About). By default, new VCNs you create use the Internet and VCN Resolver. If you're using the Networking API, this choice refers to the`VcnLocalPlusInternet`enum in the[DhcpDnsOption object](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpDnsOption/).
Note  
  

By default. the Internet and VCN Resolver doesn't let instances resolve the hostnames of hosts in an on-premises network connected to a VCN by Site-to-Site VPN or FastConnect. That functionality can be achieved either by using a custom resolver or by configuring the VCN's[private DNS resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Concepts/dns-topic-Private-resolver.htm). CUSTOM RESOLVER Use DNS servers for resolution (maximum three). They could be DNS servers that are:
- Available through the internet. For example, 216.146.35.35 for Dyn's Internet Guide.
- In the VCN.
- In an on-premises network, which is connected to the VCN by way of a Site-to-Site VPN or FastConnect (through a DRG ).

## About the DNS Domains and Hostnames

When you initially create a VCN and subnets, you can specify DNS labels for each. Subnet DNS labels can only be set if the VCN itself is created with a DNS label. The labels, along with the parent domain of`oraclevcn.com`form the VCN domain name and subnet domain name:
- VCN domain name :`<VCN_DNS_label> .oraclevcn.com`.
- Subnet domain name :`<subnet_DNS_label> . <VCN_DNS_label> .oraclevcn.com`.

When you then create a Compute instance, you can assign a hostname to the VNIC that's automatically created during instance creation (the primary VNIC ). Along with the subnet domain name, the hostname forms the instance's fully qualified domain name (FQDN):
- Instance FQDN :`<hostname> . <subnet_DNS_label> . <VCN_DNS_label> .oraclevcn.com`

For example:`database1.privatesubnet1.abccorpvcn1.oraclevcn.com`.

The FQDN resolves to the instance's private IP address. The Internet and VCN Resolver also performs reverse DNS lookup, which lets you find the hostname corresponding to the private IP address.

If you add a[secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingVNICs.htm)to an instance, you can specify a hostname. The resulting FQDN resolves to the VNIC's private IP address (the primary private IP ).

If you add a[secondary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingIPaddresses.htm)to a VNIC, you can specify a hostname. The resulting FQDN resolves to that private IP address.
Important  
  
We recommend that you always use the instance FQDN when sending messages to a host, or alternately specify only the hostname for messages sent within a VCN.

### Requirements for DNS Labels and Hostnames

- VCN and subnet labels : Max 15 alphanumeric characters and must start with a letter. Hyphens and underscores aren't allowed. The value can't be changed later.
- Hostnames : Max 63 characters, letters and numbers are allowed. Hyphens are allowed. Periods aren't allowed, hyphens aren't allowed at the beginning or end of the hostname, and the hostname can't be all numbers. Hostnames must be compliant with RFCs[952](https://tools.ietf.org/html/rfc952)and[1123](https://tools.ietf.org/html/rfc1123). The value can be changed later.
Important  
  
The Networking service supports hostnames up to 63 characters. However, some older OSs enforce shorter hostnames. In Linux, here's how to find the maximum allowed hostname length:

```

```

If an instance has a hostname longer than the OS-specific maximum, the instance's FQDN isn't resolvable within the VCN. You can use the Networking service to[update the VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingVNICs.htm#console)and change the hostname to a shorter value.

Uniqueness:
- VCN DNS label must be unique across VCNs in a tenancy (not required, but a best practice).
- Subnet DNS labels must be unique within the VCN.
- Hostnames must be unique within the subnet.
Tip  
  
Don't confuse the DNS label or hostname with the friendly name you can assign to the object (the display name ), which doesn't have to be unique.

### Validation and Generation of the Hostname

If you set DNS labels for the VCN and subnets, Oracle validates the hostname for DNS compliance and uniqueness during Compute instance creation. If either of these requirements isn't met, the creation request fails.

If you don't specify a hostname during instance creation, Oracle tries to use the instance's display name as the hostname. If the display name doesn't pass the validation, Oracle automatically generates a DNS-compliant hostname that's unique across the subnet. You can see the generated hostname on the instance's page in the Console. In the API, the hostname is part of the[VNIC object](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/).

If you don't provide a hostname or display name during instance creation using the SDK or CLI, Oracle doesn't generate a display name or hostname. This means the instance isn't resolvable using the Internet and VCN Resolver.

If you don't provide a hostname or display name during instance creation using the Console, Oracle autogenerates a display name and a corresponding DNS record, provided the subnet has a valid DNS label associated with it.
Note  
  
The Linux OS hostname on the instance is automatically set to the hostname you set during instance creation (or the one generated by Oracle). If you change the hostname directly on the instance, the FQDN of the instance doesn't get updated.

If you add a[secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingVNICs.htm)to an instance, or add a[secondary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingIPaddresses.htm)to a VNIC, Oracle never tries to generate a hostname. Provide a valid hostname if you want the private IP address to be resolvable using the Internet and VCN Resolver.

### DHCP Options for DNS

Two[DHCP options](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingDHCP.htm)are related to DNS in the VCN:
- Domain Name Server : To specify the choice for DNS type (either Internet and VCN Resolver, or Custom Resolver).
- Default value in the default set of DHCP options : Internet and VCN Resolver
- Search Domain : To specify a single search domain. When resolving a DNS query, the OS appends this search domain to the value being queried. You can specify only one search domain for the set of DHCP options.
- Default value in the default set of DHCP options : The VCN domain name (`<VCN_DNS_label> .oraclevcn.com`), if you specified a DNS label for the VCN during creation but didn't specify a search domain value. If you specified a search domain value, then that value is used for the Search Domain option. If you didn't specify a DNS label, the default set of DHCP options doesn't include a Search Domain option.
Caution  
  
We recommend that you always use the instance FQDN when sending messages to a host in another subnet/VCN and don't rely on the DNS search domain.
Important  
  

In general, when any set of DHCP options is initially created (the default set or a custom set you create), the Networking service automatically adds the Search Domain option and sets it to the VCN domain name (`<VCN_DNS_label> .oraclevcn .com`) if all conditions are met :
- The VCN has a DNS label.
- DNS Type = Internet and VCN Resolver.
- You didn't specify a search domain during creation of the set of DHCP options.

After the set of DHCP options is created, you can always remove the Search Domain option or set it to a different value.

### Enabling DNS Hostnames in a VCN

Only new VCNs created after the release of the Internet and VCN Resolver feature have automatic access to it. How to enable DNS hostnames for a new VCN depends on which interface you're using.

[If you create a VCN and subnets with the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#)

- When creating the VCN:
- Select Use DNS Hostnames in this VCN .
- Specify a DNS label for the VCN. If you select this option but don't specify a DNS label, the Console assumes that you want to use the Internet and VCN Resolver in the VCN and automatically generates a DNS label for the VCN.

The Console takes the VCN name you provided, removes nonalphanumeric characters, ensures that the first character is a letter, and truncates the label to 15 characters. The Console displays the result, and if you dislike it, you can instead enter another value in the DNS Label field. See[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About).
- When creating the subnets:
- Select Use DNS Hostnames in this Subnet .
- Specify a DNS label for each subnet. If you check the checkbox but don't specify the DNS label for a specific subnet, the Console assumes you want to use the Internet and VCN Resolver for the subnet and automatically generates a DNS label for the subnet.

The Console takes the subnet name you provided, removes nonalphanumeric characters, ensures that the first character is a letter, and truncates the label to 15 characters. The Console displays the result, and if you dislike it, you can instead enter a custom value in the DNS Label field. See[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About).
Note  
  
Subnet DNS labels can only be set if the VCN itself is created with a DNS label.
- Associate any set of DHCP options that has DNS type = Internet and VCN Resolver. The default set of DHCP options in the VCN uses the Internet and VCN Resolver by default.
- When creating Compute instances:
- Select the option to assign a private DNS record.
- Specify a hostname (or at least a display name) for each instance. For more information, see[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About).

If you don't select Use DNS Hostnames in this VCN when creating the VCN, you can't set the DNS label for the VCN or subnets, and you can't specify a hostname during Compute instance creation.
Note  
  
The previous procedure assumes you create the VCN and subnets one at a time in the Console. The Console has a feature that automatically creates a VCN with subnets and an internet gateway all at the same time. If you use that feature to create the VCN and subnets, the Console automatically generates DNS labels for them.

[If you create a VCN and subnets with the API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#)

- 

When creating the VCN:
- Specify a DNS label for the VCN. See[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About). If you don't set a value (if it's null), Oracle assumes that you don't want to use the Internet and VCN Resolver, even if the DHCP options have[DhcpDnsOption](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpDnsOption/)`serverType`=`VcnLocalPlusInternet`.
- 

When creating the subnets:
- Specify a DNS label for each subnet. See[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About). If you specified a DNS label for the VCN, but you don't specify a DNS label for the subnet, Oracle assumes that you don't want the instances in the subnet to use the Internet and VCN Resolver and the ability to use hostnames to communicate with instances in the VCN is no longer available.
Note  
  
Subnet DNS labels can only be set if the VCN itself was created with a DNS label.
- Associate any set of DHCP options that has[DhcpDnsOption](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpDnsOption/)`serverType`=`VcnLocalPlusInternet`, which is the default DHCP option in the VCN.
- 

When creating instances:
- Select the option to assign a private DNS record.
- Specify a hostname (or at least a display name) for each instance. For more information, see[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About).

If you don't specify a DNS label when creating the VCN, you can't do the following things:
- Set the DNS label for the subnets (causing the`CreateSubnet`call to fail).
- Specify a hostname during the Compute instance creation (causing the`LaunchInstance`call to fail).
- Assign a hostname to a[secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingVNICs.htm)or a[secondary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingIPaddresses.htm).

### Scenario 1: Use Internet and VCN Resolver with DNS Hostnames Across the VCN

The typical scenario is to enable the Internet and VCN Resolver across an entire VCN , so that all instances in the VCN can communicate with each other without knowing their IP addresses. To do that, follow the instructions in[About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About), and assign a DNS label to the VCN and every subnet. Then assign every instance a hostname (or at least a display name) at creation. If you add a[secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingVNICs.htm)or[secondary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingIPaddresses.htm), also assign it a hostname. The instances can then communicate with each other using FQDNs instead of IP addresses.

### Scenario 2: Use a Private DNS Resolver to Resolve DNS Hostnames

You can use a private DNS resolver to answer DNS queries for a VCN using a configuration you create. The resolver listens on 169.254.169.254 by default, but you can also define endpoints for listening for queries and forwarding them to other resolvers in other VCNs, a customer's on-premises network, or other private network. For more information, see[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm).

### Scenario 3: Use Different DHCP Options Per Subnet

[Scenario 1](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#Typical)assumes you want to use the Internet and VCN Resolver the same way across all subnets, and thus all instances in the VCN. You could, however, configure different DNS settings for each subnet , because the DHCP options are configured at the subnet level . The important thing to understand is: the subnet where you want to generate the DNS query is where you need to configure the corresponding Internet and VCN Resolver settings.

For example, if you want instance A in subnet A to resolve the hostname of instance B in subnet B, you must configure subnet A to use the Internet and VCN Resolver. Conversely, if you want instance B to resolve the hostname of instance A, you must configure subnet B to use the Internet and VCN Resolver.

You can configure a different set of DHCP options for each subnet. For example, you could set subnet A's Search Domain to`subneta.vcn1.oraclevcn.com`, which means all instances in subnet A could only use hostnames to communicate with each other. You could similarly set subnet B's Search domain to`subnetb.vcn1.oraclevcn.com`
