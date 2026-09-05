# Adding IP Address Ranges to a VCN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add_cidr_to_vcn.htm
- Fetched: 2026-09-05 02:43 CDT

# Adding IP Address Ranges to a VCN

You can add an IPv4 CIDR block or IPv6 prefix to a Virtual Cloud Network (VCN), with some limitations.

- The IPv4 CIDR block or IPv6 prefix you add must not overlap with any other address range in the VCN or in a peered VCN.
- The new IPv4 CIDR block or IPv6 prefix must not include an IP address used in an existing route rule.
- While the VCN is being updated, you can't create or update the VCN's subnets, VLANs, local peering gateways (LPGs), or route tables.
- After you add an IPv6 prefix to a VCN, you can't edit the IPv6 prefix.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add_cidr_to_vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add_cidr_to_vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/add_cidr_to_vcn.htm#)
- 

To add IP address ranges, follow these steps:

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the IP Administration tab, go to the CIDR Blocks/Prefixes section.
- Under Resources , select CIDR Blocks/Prefixes .
- Select Add CIDR Block/IPv6 Prefix .
- Enter the value of the CIDR block or IPv6 prefix that you want to add to the VCN.
With IPv6, you can select an Oracle-allocated IPv6 prefix, select a BYOIPv6 prefix that you already imported, or specify a ULA prefix. For BYOIPv6, you can also subdivide the prefix here, if you're only assigning part of the imported IPv6 prefix to this VCN.
- Select Add CIDR Blocks/Prefixes .
The VCN's state changes to Updating. Completing this operation can take a few minutes. You can view work requests to monitor the status of the update.
- 

Use the[network vcn add-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/add-vcn-cidr.html)command and required parameters to add an IPv4 CIDR block to a VCN:

```

```

Use the[network vcn add-ipv6-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/add-ipv6-vcn-cidr.html)command and required parameters to add an IPv6 prefix to a VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddVcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/AddVcnCidr)operation to add an IPv4 CIDR block to a VCN.

Run the[AddIpv6VcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/AddIpv6VcnCidr)
