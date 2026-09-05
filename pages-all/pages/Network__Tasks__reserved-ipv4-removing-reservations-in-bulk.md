# Removing IPv4 Address Reservations in bulk
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservations-in-bulk.htm
- Fetched: 2026-09-05 02:46 CDT

# Removing IPv4 Address Reservations in bulk

Remove all the existing reserved IP addresses in bulk.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservations-in-bulk.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservations-in-bulk.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-removing-reservations-in-bulk.htm#)
- 

- On the VCN list page, select the VCN that contains the subnet you want to work with. This takes you to the VCN's details page.
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Depending on the option that you see:

- Select the IP adminstration tab.
- Under Resources , select IPv4 Addresses .
- To remove all IP address reservations in bulk, select the Name checkbox, and select Remove IP address reservation . You can also select several IP addresses individually.
- In the Remove IP address reservation dialog box, select Remove IP address reservation .
All the existing reserved IP addresses in the Assigned state are unreserved excluding the ephemeral IP addresses.
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
