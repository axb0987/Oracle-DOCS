# Removing an IPv4 CIDR from a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-ipv4-cidr.htm
- Fetched: 2026-09-05 02:46 CDT

# Removing an IPv4 CIDR from a Subnet

Remove an IPv4 CIDR from a subnet in a Virtual Cloud Network (VCN).

After you assign an IPv4 CIDR to a subnet, the subnet must always have at least one IPv4 CIDR block assigned. To remove an existing IPv4 CIDR block, you need to add another IPv4 CIDR block first. For more information, see[Adding an IPv4 CIDR to a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-ipv4-cidr.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-ipv4-cidr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-ipv4-cidr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-ipv4-cidr.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet you want to update. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the available options:

- Select the Subnets tab, then select the name of the subnet you want to update.
- Scroll to the subnets table following the VCN details, and select the name of the subnet you want to update.
- On the subnet details page, do one of the following, depending on the available options:

- On the IP Administration tab, go to the IPv4 CIDR Blocks section.
- Scroll to the subnets table following the VCN details, and select the name of the subnet you want to update.
- Under Resources , select IPv4 CIDR Blocks .
- Select the Actions menu (three dots) for the IPv4 CIDR and select Unassign .
- 

Use the[network subnet remove-ipv4-subnet-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/remove-ipv4-subnet-cidr.html)command and required parameters to edit a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveIpv4SubnetCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/RemoveIpv4SubnetCidr)
