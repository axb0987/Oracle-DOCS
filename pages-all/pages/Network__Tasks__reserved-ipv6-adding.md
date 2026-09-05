# Adding a Reserved IPv6 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-adding.htm
- Fetched: 2026-09-05 02:46 CDT

# Adding a Reserved IPv6 Address

Reserve an IPv6 address in a subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-adding.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-adding.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-adding.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv6 Addresses .
- Select Add reserved IPv6 address .
- In the Add reserved IPv6 address dialog box, enter the following information:

- Name : Provide a descriptive name for the reserved IP address. It doesn't have to be unique, and it can be changed later in the Console. Avoid entering confidential information.
- Subnet IPv6 prefix : Provide the IPv6 prefix to be reserved.
- IPv6 address : Provide the IPv6 to be reserved.
- Tags : Provide tags for the IPv6 address to be reserved. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Add reserved IPv6 address .

The new reserved IPv6 address is successfully created and displayed on the page.
- 

Use the[ipv6 create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/create.html)command and required parameters to create a reserved private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/CreateIpv6)
