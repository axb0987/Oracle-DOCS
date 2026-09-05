# Deleting a Reserved IPv6 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-deleting.htm
- Fetched: 2026-09-05 02:46 CDT

# Deleting a Reserved IPv6 Address

Delete a reserved IPv6 address from the subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-deleting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-deleting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-deleting.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following options depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv6 Addresses .
- For the reserved IPv6 address you want to remove the reservation, select the Actions menu (three dots) , and then select Delete .
- In the confirmation dialog box, select Delete .
The reserved IPv6 address is successfully deleted.
- 

If the reserved IPv6 address is attached to any instance or Virtual Network Interface Card (VNIC), use the[ipv6 ipv6-vnic-detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/ipv6-vnic-detach.html)command and required parameters to detach the private IPv6 address reservation, and then use the[ipv6 delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/delete.html)command and required parameters to delete the detached private IPv6 address:
```

```

Use the[ipv6 delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/delete.html)command and required parameters to delete the private IPv6 address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

If the reserved IPv6 address isn't attached to any instance or Virtual Network Interface Card (VNIC), run the[DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp)operation to delete the reserved private IPv6 address.

If the reserved IPv6 address is attached to any instance or Virtual Network Interface Card (VNIC), run the[UpdateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/UpdateIpv6)operation to detach it from the VNIC and then run the[DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp)
