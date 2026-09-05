# Deleting a Subnet
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a Subnet

Delete a subnet from a Virtual Cloud Network (VCN).

Before you can delete a subnet, it must have no instances,[load balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)s, OCI database systems, or orphaned mount targets in it. For more information, see[Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion).

If the subnet is empty, its state changes to TERMINATING briefly and then TERMINATED. If the subnet is not empty, you get an error indicating that there are still instances or other resources in it that you must delete first.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_subnet.htm#)
- 

- On the VCN list page, select the VCN that contains the subnet you want to work with. This takes you to the VCN's details page.
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN.
- From the Actions menu (three dots) for the subnet you want to delete, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network subnet delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/delete.html)command and required parameters to delete a subnet:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/DeleteSubnet)
