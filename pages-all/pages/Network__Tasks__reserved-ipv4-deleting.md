# Deleting a Reserved IPv4 Address
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-deleting.htm
- Fetched: 2026-09-05 02:46 CDT

# Deleting a Reserved IPv4 Address

Delete a reserved IPv4 address from the subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-deleting.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-deleting.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-deleting.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- For the reserved IPv4 address you want to delete, select the Actions menu (three dots) , and then select Delete .
- In the confirmation dialog box, select Delete .
The reserved IPv4 address is successfully deleted.
- 

If the reserved IPv4 address is attached to any instance or Virtual Network Interface Card (VNIC), use the`private-ip private-ip-vnic-detach`command and required parameters to detach a private IPv4 address reservation, and then use the[private-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/delete.html)command and required parameters to delete the detached private IP address:
```

```

Use the[private-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/delete.html)command and required parameters to delete the private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

If the reserved IPv4 address isn't attached to any instance or Virtual Network Interface Card (VNIC), then run the[DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp)operation to delete the reserved private IPv4 address.

If the reserved IPv4 address is attached to any instance or Virtual Network Interface Card (VNIC), run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)operation to detach it from the VNIC and then run the[DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp)
