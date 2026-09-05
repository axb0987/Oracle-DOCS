# Removing an IPv6 Prefix from a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm
- Fetched: 2026-09-05 02:46 CDT

# Removing an IPv6 Prefix from a Subnet

Remove an IPv6 prefix from a subnet in a Virtual Cloud Network (VCN).

After a subnet has an IPv6 prefix assigned to it, it must always have at least one IPv6 prefix assigned to it. This means that you might need to add another IPv6 prefix before you can remove an IPv6 prefix. See[Adding an IPv6 Prefix to a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add-subnet-prefix.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove-subnet-prefix.htm#)
- 

- On the VCN list page, select the VCN that contains the subnet you want to work with. This takes you to the VCN's details page.
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- On the subnet details page, perform one of the following actions depending on the option that you see:

- Select the IP administration tab, then go to the IPv6 Prefixes section.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with. Under Resources , select IPv6 Prefixes .
- Select the Actions menu (three dots) for the IPv6 prefix, and select Unassign .
- 

Use the[network subnet remove-ipv6-subnet-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/remove-ipv6-subnet-cidr.html)command and required parameters to remove an IPv6 prefix from a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveIpv6SubnetCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/RemoveIpv6SubnetCidr)
