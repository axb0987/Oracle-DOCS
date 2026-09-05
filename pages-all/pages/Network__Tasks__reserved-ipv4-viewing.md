# Listing the IPv4 Addresses of All Resources in a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-viewing.htm
- Fetched: 2026-09-05 02:46 CDT

# Listing the IPv4 Addresses of All Resources in a Subnet

View IPv4 addresses of all resources in a subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-viewing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-viewing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-viewing.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- In the IPv4 addresses section, view the list of IP addresses used in the subnet along with following information:

- Name : The descriptive name of the reserved IP address. It doesn't have to be unique, and it can be changed later in the Console. Avoid entering confidential information.
- IP address : The the reserved IP address.
- State : The state of the IP address, either Assigned or Available .
- Lifetime : The type of IP address, either Ephemeral or Reserved . For more information, see[Types of Public IPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph).
- Fully qualified domain name : The FDQN of the reserved IP address.
- Created : The date and time when the IP address was reserved for the resources in the subnet.
- 

Use the[private-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/list.html)command and required parameters to list private IP addresses for an instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListPrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps)
