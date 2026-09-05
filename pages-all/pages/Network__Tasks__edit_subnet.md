# Editing a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm
- Fetched: 2026-09-05 02:44 CDT

# Editing a Subnet

Edit the settings for a subnet in a Virtual Cloud Network (VCN).

You can change the following characteristics of a subnet:
- Name
- Size of the assigned CIDR block
- Which set of DHCP options the subnet uses
- Which route table the subnet uses
- Which security lists the subnet uses
- The IPv4 CIDR blocks and IPv6 prefixes assigned

Be aware of the following considerations:
- The CIDR block IP range that you specify must be within one of the VCN's CIDR block ranges.
- The new range must use the same network address as the previous range. For example, the previous and new ranges could be 10.0.0.0/25 and 10.0.0.0/24.
- If you're reducing the CIDR range, ensure that no IP addresses outside of the reduced range are in use.
- The new CIDR range's broadcast address (last IP address of CIDR range) must not be an IP address in use in the previous CIDR range.
- You can't create VNICs or private IP addresses for this subnet while a CIDR block update is in progress.
- After the CIDR block update is complete, the DHCP lease for each host within the subnet must be renewed. Renewal happens automatically within 24 hours. To renew the lease immediately, see the applicable OS documentation for guidance on how to renew the lease manually.
- Ensure that you adjust the secondary VNICs and secondary IP addresses as applicable to match the updated VCN configuration.
- After you assign an IPv4 CIDR to a subnet, the subnet must always have at least one IPv4 CIDR assigned.
- After you assign an IPv6 prefix to a subnet, the subnet must always have at least one IPv6 prefix assigned.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_subnet.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN.
- Find the subnet in the Subnets list, select the Actions menu (three dots) for it, and then select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_subnet.htm).
- Select Save changes .
The changes take effect within a few seconds.
- 

Use the[network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html)command and required parameters to edit a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet)
