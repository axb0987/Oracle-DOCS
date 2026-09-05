# Creating a VCN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a VCN

Create a VCN that instances, load balancers, and other resources can use to connect to each other and the internet. After you create a VCN, you must then manually create subnets, gateways, routing rules, and security settings before the VCN can connect to the internet or an on-premises network.

A virtual cloud network (VCN) is a software-defined network that you set up in the Oracle Cloud Infrastructure data centers in a particular region .

For more information about VCNs, see[Overview of VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm).

After you create a VCN, see[Creating a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm).
Note  
  

For a quick procedure that creates a VCN that you can try out immediately (one with subnets and an internet gateway), see the information about the "VCN with Internet Connectivity" wizard in[Virtual Networking Wizards](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartnetworking.htm)or see[Scenario A: Public Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm#)
- 

- On the Virtual Cloud Networks list page, select Create VCN . If you need help finding the list page, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Enter a descriptive name for the VCN (this is required). It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API or CLI). Avoid entering confidential information.
- Verify the compartment that you want to create the VCN in. Select another compartment if needed.
- In the IPv4 CIDR Blocks section, enter the following information:

- IPv4 CIDR Blocks (Required) Specify up to five but at least one nonoverlapping IPv4 CIDR blocks for the VCN. For example: 172.16.0.0/16. You can add or remove CIDR blocks later. See[Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Allowed). It might be helpful to use a[CIDR calculator](http://www.ipaddressguide.com/cidr).
- Use DNS Hostnames in this VCN This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the Internet and VCN Resolver ). If you select this option you can specify a DNS Label for the VCN, or you can let the Console to generate one for you. The page automatically displays the corresponding DNS domain name for the VCN (`<VCN_DNS_label> .oraclevcn.com`). For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).
- In the IPv6 prefixes section, assign a single Oracle-allocated IPv6 /56 prefix to this VCN, or assign a BYOIPv6 prefix or ULA prefix to the VCN. This option is available for all commercial and government regions. For more information on IPv6, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).
- (Optional) In the VN Encryption section, select whether to enable or disable encryption of all traffic between Compute instances that can use this feature. See[VN Encryption](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#govinfo_topic_LAN-encryption)for details on the consequences of enabling or disabling this feature. This feature is only available in the US Government Cloud.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- (Optional) In the Show security attributes section, add up to three security attributes to restrict access to resources. If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- Select Create VCN .
The VCN you created appears in the Virtual Cloud Networks list page.
- 

Use the[network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html)command and required parameters to create a VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn)
