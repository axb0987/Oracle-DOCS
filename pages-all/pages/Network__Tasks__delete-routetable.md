# Deleting a VCN Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a VCN Route Table

Delete a Virtual Cloud Network (VCN) route table.

Prerequisite: To delete a route table, it must not be associated with a subnet or gateway. If you associate a route table with a gateway, afterwards the gateway must always have a route table associated with it. You can modify the rules in the current route table or replace it with another route table.

You can't delete the default route table in a VCN.
For an overview of routing in your VCN and subnets, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the route table you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the details page, select the Routing tab.
- Under Resources , select Route Tables .
- From the Actions menu (three dots) for the route table, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network route-table delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/delete.html)command and required parameters to delete a VCN route table:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/DeleteRouteTable)
