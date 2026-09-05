# Changing a VCN's IPv4 CIDR blocks
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm
- Fetched: 2026-09-05 02:44 CDT

# Changing a VCN's IPv4 CIDR blocks

You can change or resize the IPv4 CIDR block range assigned to a Virtual Cloud Network (VCN), with some restrictions.

- The updated CIDR block range you specify must not overlap with any other CIDR block in this VCN or in a peered VCN.
- You can't change the CIDR block to a range that excludes an IP address in use in the current CIDR block range.
- While the VCN is being updated, you can't create or update the VCN's subnets, VLANs, local peering gateways (LPGs), or route tables.
Note  
  
You can't edit an IPv6 prefix that's been added to a VCN.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vcn_cidr.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the IP Administration tab, go to the CIDR Blocks/Prefixes section.
- Under Resources , select CIDR Blocks/Prefixes .
- Find the IPv4 CIDR block in the list, select the Actions menu (three dots) , and then select Edit CIDR Block .
- Make the applicable change or changes.
- Select Save Changes .
The VCN's state changes to UPDATING. The time to completion can vary depending on the size of the network. Updating a small network could take about a minute, and updating a large network could take up to an hour. You can view work requests to monitor the status of the update.
- 

Use the[network vcn modify-vcn-cidr](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/modify-vcn-cidr.html)command and required parameters to update the specified CIDR block of a VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ModifyVcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ModifyVcnCidr)
