# Editing an Existing Reserved IPv6 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-editing.htm
- Fetched: 2026-09-05 02:46 CDT

# Editing an Existing Reserved IPv6 Address

Edit the name of an existing reserved IPv6 address that's not assigned to any resource in the subnet.

When you edit a reserved IPv6 address, you can also update its tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-editing.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-editing.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-editing.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv6 Addresses .
- For the reserved IPv6 address you want to edit, select the Actions menu (three dots) , and then select Edit .
- In the Edit IPv6 resource properties panel, edit the name for the reserved IPv6 address. It doesn't have to be unique, and it can be changed in the Console. Avoid entering confidential information.
- Select Save changes .
The reserved IPv6 address is successfully updated and displayed on the page.
- 

Use the[ipv6 update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/update.html)command and required parameters to edit a reserved private IPv6 address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/UpdateIpv6)
