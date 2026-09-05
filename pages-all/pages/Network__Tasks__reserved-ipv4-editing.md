# Editing an Existing Reserved IPv4 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-editing.htm
- Fetched: 2026-09-05 02:46 CDT

# Editing an Existing Reserved IPv4 Address

Edit the name or hostname of an existing reserved IPv4 address that's not assigned to any resource in the subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-editing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-editing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-editing.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- For the reserved IPv4 address you want to edit, select the Actions menu (three dots) , and then select Edit .
- On the Edit IP resource properties page, edit the following information:

- Name : Update the name for the reserved IP address. It doesn't have to be unique. Avoid entering confidential information.
- Hostname : Update the hostname with another alphanumeric name without any spaces.
- Select Save changes .
The reserved IPv4 address is successfully updated and displayed on the page.
- 

Use the[private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html)command and required parameters to edit the private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)
