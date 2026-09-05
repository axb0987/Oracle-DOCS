# Reserving an Existing IPv6 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-reserving.htm
- Fetched: 2026-09-05 02:46 CDT

# Reserving an Existing IPv6 Address

Update an existing ephemeral IPv6 address to a reserved IPv6 address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-reserving.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-reserving.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-reserving.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv6 Addresses .
- For the ephemeral IPv6 address you want to change to reserved IPv6 address, select the Actions menu (three dots) , and then select Reserve IP address .
- In the confirmation dialog box, select Reserve IPv6 address .
The IPv6 address is successfully reserved and displayed on the page.
- 

Use the[ipv6 update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/update.html)command and required parameters to reserve private IPv6 address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/UpdateIpv6)
