# Removing an IPv4 CIDR Block or IPv6 Prefix from a VCN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm
- Fetched: 2026-09-05 02:46 CDT

# Removing an IPv4 CIDR Block or IPv6 Prefix from a VCN

You can remove an IPv4 CIDR block or IPv6 prefix from a Virtual Cloud Network (VCN), with some restrictions.

- You can't remove an IPv4 CIDR block if an IP address in that range is in use.
- While the VCN is being updated, you can't create or update the VCN's subnets, VLANs, local peering gateways (LPGs), or route tables.
- After you assign an IPv6 prefix to a VCN, the VCN must always have at least one IPv6 prefix assigned to it. A VCN must always have at least one IPv4 CIDR block assigned to it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remove_cidr_block_vcn.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the IP Administration tab, go to the CIDR Blocks/Prefixes section.
- Under Resources , select CIDR Blocks/Prefixes .
- Find the IPv4 CIDR block or IPv6 prefix in the list, select the Actions menu (three dots) , and then select Remove CIDR Block .
- Select Remove CIDR Block .
The VCN's state changes to Updating. The time to completion can vary depending on the size of the network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can view work requests to monitor the status of the update.
- 

Use the[network vcn remove-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/remove-vcn-cidr.html)command and required parameters to remove an IPv4 CIDR block from a VCN:

```

```

Use the[network vcn remove-ipv6-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/remove-ipv6-vcn-cidr.html)command and required parameters to remove an IPv6 prefix from a VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveVcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/RemoveVcnCidr)operation to remove an IPv4 CIDR block from a VCN.

Run the[RemoveIpv6Cidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/RemoveIpv6Cidr)
