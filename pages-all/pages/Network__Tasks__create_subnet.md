# Creating a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a Subnet

Create a subnet in a VCN. A subnet is a logical subdivision of a Virtual Cloud Network (VCN). Each subnet consists of a contiguous range of IP addresses that don't overlap with other subnets in the VCN.

To create a subnet, you must have already created a VCN for this subnet to be part of.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select Create subnet .
- Select Create Subnet .
- Enter a friendly name for the subnet. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- Verify the compartment that you want to create the subnet in. Select another compartment if needed.
- Select the subnet type, either Regional or Availability Domain-specific . We recommend creating only[regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm), which means that the subnet can contain resources in any of the region's availability domains. If you instead select Availability Domain-specific (the only type of subnet that Oracle originally offered), you must also specify an availability domain. This choice means that any instances or other resources later created in this subnet must also be in that availability domain.
- In the IPv4 CIDR block section, enter a single, contiguous IPv4 CIDR block for the subnet (for example, 172.16.0.0/24) from within one of the VCN's CIDR blocks. This CIDR that can't overlap with any other subnets. You can change the size of this CIDR block later. See[Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Allowed). For reference, use the[CIDR calculator](http://www.ipaddressguide.com/cidr).
- In the IPv6 Prefixes section, request an Oracle-allocated IPv6 /64 prefix, or enter BYOIPv6 or ULA prefixes. You can have a maximum of 16 IPv6 prefixes in a subnet. After you assign an IPv6 prefix to a subnet, it must always have at least one IPv6 prefix assigned to it. This option is available for subnets if the VCN is already enabled for IPv6. For more information, see[IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/ipv6.htm).
- In the Subnet Access section, select either Private subnet or Public subnet If you want resources such as Compute instances or Load Balancers in the subnet to have public IP addresses, select Public subnet . For more information, see[Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Private).
- In the DNS Resolution section, decide whether to select Use DNS hostnames in this Subnet . This option is available only if a DNS label was provided for the VCN when it was created. The option is required for assignment of DNS hostnames to hosts in the subnet, and also when you plan to use the VCN's default DNS feature (called the Internet and VCN Resolver ). If you select the checkbox, you can specify a DNS label for the subnet, or let the Console generate one for you. The page automatically displays the corresponding DNS domain name for the subnet as an FQDN. For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm).
You can also select the set of DHCP options to associate with the subnet. If you enabled compartment selection, first specify the compartment that contains the set of DHCP options.
- In the Security Lists section you can associate up to five security lists with the subnet. If you enabled compartment selection, first specify the compartment that contains the security list.
- (Optional) In the Resource Logging section, decide whether to enable Resource Logging, and if so set the required options. For details about enabling logging, see[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm). Resource logging is turned off by default.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create Subnet .
The subnet is created and is displayed on the Subnets list or tab on the details page of the VCN that you created it in.
- 

Use the[network subnet create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/create.html)command and required parameters to create a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet)
