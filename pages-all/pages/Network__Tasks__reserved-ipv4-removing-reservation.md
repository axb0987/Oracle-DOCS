# Removing an IPv4 Address Reservation
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservation.htm
- Fetched: 2026-09-05 02:46 CDT

# Removing an IPv4 Address Reservation

Remove an existing reserved IP address from the subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservation.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform one of the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- For the reserved IPv4 address you want to remove the reservation, select the Actions menu (three dots) , and then select Remove IP address reservation .
- In the confirmation dialog box, select Remove IPv4 address reservation .
The reserved IPv4 address is successfully removed.
- 

Use the[private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html)command and required parameters to remove the private IP address reservation:

```

```

Note  
  
If the reserved IPv4 address isn't attached to any instance or Virtual Network Interface Card (VNIC), then use the[delete](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../shared/../Tasks/reserved-ipv4-deleting.htm#reserved_ipv4_deleting_using_cli)command to delete the reserved IPv4 address.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

If the reserved IPv4 address is attached to any instance or Virtual Network Interface Card (VNIC), run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)operation to remove an private IPv4 address reservation.
Note  
  
If the reserved IPv4 address isn't attached to any instance or Virtual Network Interface Card (VNIC), then run the[DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp)
