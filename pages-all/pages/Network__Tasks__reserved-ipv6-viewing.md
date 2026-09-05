# Listing IPv6 Addresses of All Resources in a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-viewing.htm
- Fetched: 2026-09-05 02:46 CDT

# Listing IPv6 Addresses of All Resources in a Subnet

View IPv6 addresses of all resources in a subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-viewing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-viewing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-viewing.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv6 Addresses .
- In the IPv6 addresses section, view the list of IPv6 addresses used in the subnet along with following information:

- Name : The descriptive name for the reserved IP address.
- IP Address : The reserved IP address.
- State : The state of the IP address which either Assigned or Available .
- Lifetime : The type of IP address, either Ephemeral or Reserved . For more information, see[Types of Public IPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph).
- Created : The date and time when the IP address was reserved for the resources in the subnet.
- 

Use the[ipv6 list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/list.html)command and required parameters to list private IP addresses for an instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListIpv6s](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/ListIpv6s)
