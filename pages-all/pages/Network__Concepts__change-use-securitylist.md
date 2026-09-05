# Changing Which Security Lists a Subnet Uses
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm
- Fetched: 2026-09-05 02:41 CDT

# Changing Which Security Lists a Subnet Uses

Change which security lists are used in a particular subnet in a virtual cloud network (VCN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the security list you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with. Security Lists is the first section on the page.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Depending on the option that you see:

- Select the Security tab.
- Under Resources , select Security Lists .
- To add a security list, select Add Security List , and select the new security list you want the subnet to use.
- From the Actions menu (three dots) for the security list, select Remove . Remember that a subnet must always have at least one security list associated with it.

The changes take effect within a few seconds.
- 

Use the[network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html)command and described parameters to change which security list a subnet uses:

```

```

The security-list-ids are OCIDs of the security list or lists the subnet will use. This replaces the entire current set of security lists. Remember that security lists are associated with the subnet , but the rules are applied to the individual VNICs in the subnet. This is a complex type whose value must be valid JSON.

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet)
