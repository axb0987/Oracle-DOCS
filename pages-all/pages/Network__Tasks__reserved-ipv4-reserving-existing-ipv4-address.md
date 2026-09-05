# Reserving an Existing IPv4 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-existing-ipv4-address.htm
- Fetched: 2026-09-05 02:46 CDT

# Reserving an Existing IPv4 Address

Update an existing ephemeral IP address to a reserved IP address.

Note  
  
Secondary IP addresses and already assigned private IP addresses can't be reserved.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-existing-ipv4-address.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-existing-ipv4-address.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-existing-ipv4-address.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- For the ephemeral IPv4 address you want to change to reserved IPv4 address, select the Actions menu (three dots) , and then select Reserve IP address .
- In the confirmation dialog box, select Reserve IPv4 address .
The IPv4 address is successfully reserved and displayed on the page.
- 

Use the[private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html)command and required parameters to reserve the private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)
