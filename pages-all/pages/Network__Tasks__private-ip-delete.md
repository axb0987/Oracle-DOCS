# Deleting a Private IP Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm
- Fetched: 2026-09-05 02:46 CDT

# Deleting a Private IP Object

Unassign and delete a private IP object from a VNIC.

Note  
  
Using the CLI or API, you can also delete more than one private IP object from a single VNIC with a single command.

Prerequisite: We recommend removing the IP address from the OS configuration before deleting it from the VNIC. See[Configuring Linux to Use a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm)or[Configuring Windows to Use a Secondary IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm).

Caution  
  
If the private IP is the[target of a route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route), deleting it from the VNIC causes the route rule to drop the traffic.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab.
The IP addresses associated with the VNIC are listed in tabular form.
- Find the IP object you want to update, select its Actions menu (three dots), and then select Unassign Private IP .
- Confirm when prompted.
- 

Use the[private-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/delete.html)command and required parameters to delete a private IP address:

```

```

Optionally, use the[network private-ip bulk-delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/bulk-delete.html)command and required parameters to multiple private IP addresses:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp)operation to delete a private IP address.

Optionally, run the[BulkDeletePrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/BulkDeletePrivateIps)
