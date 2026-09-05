# Adding a Reserved IPv4 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-adding.htm
- Fetched: 2026-09-05 02:46 CDT

# Adding a Reserved IPv4 Address

Reserve an IPv4 address in a subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-adding.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-adding.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-adding.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- Select Add reserved IPv4 address .
- On the Add reserved IP address page, enter the following information:

- Name : Provide a descriptive name for the reserved IP address. It doesn't have to be unique, and it can be changed later in the Console. Avoid entering confidential information.
- IPv4 IP address : Provide the IPv4 IP address to be reserved.
Note  
  
Ensure that the provided IP address isn't in use and is in the range from 10.0.0.2 to 10.0.0.254.
- Hostname : Provide a alphanumeric hostname without any spaces.
- Tags : Provide tags for the IPv4 address to be reserved. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Add reserved IP address .

The new reserved IPv4 address is successfully created and displayed on the page.
- 

Use the[network private-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/create.html)command and required parameters to create a reserved private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/CreatePrivateIp)
