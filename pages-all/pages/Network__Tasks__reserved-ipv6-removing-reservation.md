# Removing an IPv6 Address Reservation
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-removing-reservation.htm
- Fetched: 2026-09-05 02:46 CDT

# Removing an IPv6 Address Reservation

Remove an existing reserved IP address from the subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-removing-reservation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-removing-reservation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv6-removing-reservation.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP adminstration tab.
- Under Resources , select IPv6 Addresses .
- For the reserved IPv6 address you want to remove the reservation, select the Actions menu (three dots) , and then select Remove IP address reservation .
- In the confirmation dialog box, select Remove IPv6 address reservation .
The reserved IPv6 address is successfully removed.
- 

Use the[ipv6 update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/ipv6/update.html)command and required parameters to remove private IPv6 address reservation:

```

```

Note  
  
If the reserved IPv6 address isn't attached to any instance or Virtual Network Interface Card (VNIC), then use the[delete](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../shared/../Tasks/reserved-ipv6-deleting.htm#reserved_ipv6_delete_using_cli)command to delete the reserved IPv6 address.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

If the reserved IPv6 address is attached to any instance or Virtual Network Interface Card (VNIC), run the[UpdateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/UpdateIpv6)operation to remove a private IPv6 address reservation.
Note  
  
If the reserved IPv6 address isn't attached to any instance or Virtual Network Interface Card (VNIC), then run the[DeleteIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/DeleteIpv6)
