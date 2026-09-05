# Adding an IPv4 CIDR to a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-ipv4-cidr.htm
- Fetched: 2026-09-05 02:43 CDT

# Adding an IPv4 CIDR to a Subnet

Add an IPv4 CIDR to a subnet in a Virtual Cloud Network (VCN).

If the subnet is in a VCN with one or more assigned IPv4 CIDRs and IPv4 addressing is enabled, you can add one or more IPv4 CIDR blocks unique to the subnet. You can make this assignment when you create the subnet through API and CLI or at a later time through all the listed methods.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-ipv4-cidr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-ipv4-cidr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-ipv4-cidr.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet you want to update. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the available options:

- Select the Subnets tab, then select the name of the subnet you want to update.
- Scroll to the subnets table following the VCN details, and select the name of the subnet you want to update.
- On the subnet details page, do one of the following, depending on the available options:

- On the IP Administration tab, go to the IPv4 CIDR Blocks section and select Add IPv4 CIDR Block .
- Under Resources , select IPv4 CIDR Blocks , then select Add IPv4 CIDR Block .
- Enter an IPv4 CIDR that fits within one of your VCN IPv4 CIDR blocks.

You can have up to 16 IPv4 CIDRs per subnet.
- Select Add IPv4 CIDR Block .
- 

Use the[network subnet add-ipv4-subnet-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/add-ipv4-subnet-cidr.html)command and required parameters to edit a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddIpv4SubnetCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/AddIpv4SubnetCidr)
