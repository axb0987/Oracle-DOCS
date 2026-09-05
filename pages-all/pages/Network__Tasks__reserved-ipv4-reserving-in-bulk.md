# Reserving Existing IPv4 Addresses in Bulk
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-in-bulk.htm
- Fetched: 2026-09-05 02:46 CDT

# Reserving Existing IPv4 Addresses in Bulk

Update all the existing ephemeral IP addresses to a reserved IP addresses in bulk.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-in-bulk.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-in-bulk.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-reserving-in-bulk.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the subnet that you want to work with. This takes you to the VCN's details page. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the VCN details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- Perform the following actions depending on the option that you see:

- Select the IP administration tab.
- Under Resources , select IPv4 Addresses .
- To reserve all IP addresses in bulk, select the checkbox next to the Name header, and then from the Actions menu (three dots) above the list, select Reserve IP address . You can also select the checkboxes for several IP addresses individually.
- On the Add reserved IP address panel, select Reserve IP address .
All the existing ephemeral IP addresses in the Assigned state are reserved excluding the secondary and already reserved IP addresses.
- Select Close .
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
