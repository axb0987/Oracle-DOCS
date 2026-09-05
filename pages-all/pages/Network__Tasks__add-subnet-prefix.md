# Adding an IPv6 Prefix to a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm
- Fetched: 2026-09-05 02:43 CDT

# Adding an IPv6 Prefix to a Subnet

Add an IPv6 prefix to a subnet in a Virtual Cloud Network (VCN).

If the subnet is in a VCN that has one or more assigned IPv6 prefixes and the subnet is enabled for IPv6 addressing, you can add an IPv6 prefix unique to the subnet. This assignment can be done when you create the subnet or later.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm#)
- 

- On the VCN list page, select the VCN that contains the subnet you want to work with. This takes you to the VCN's details page.
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- On the subnet details page, perform one of the following actions depending on the option that you see:

- On the IP administration tab, go to the IPv6 prefixes section and select Add IPv6 Prefix .
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with. Under Resources , select IPv6 Prefixes then select Add IPv6 Prefix .
- Choose a /64 IPv6 prefix. This can be from an Oracle-assigned IPv6 prefix assigned to the VCN, from BYOIP IPv6 prefix, or a ULA prefix.

You can have up to 16 IPv6 prefixes per subnet, including one allocated by Oracle.
- Select Add IPv6 Prefix .
- 

Use the[network subnet add-ipv6-subnet-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/add-ipv6-subnet-cidr.html)command and required parameters to add an IPv6 prefix to a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddIpv6SubnetCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/AddIpv6SubnetCidr)
