# Getting a VCN Route Table's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm
- Fetched: 2026-09-05 02:44 CDT

# Getting a VCN Route Table's Details

Get details for a Virtual Cloud Network (VCN) route table.
For an overview of routing in a VCN and subnets, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the route table you want to work with. If you need help finding the list page, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Routing tab.
- Under Resources , select Route Tables . The default route table and any other route tables that have been created are displayed in the list of tables.
- Select a route table's name to view its details.
You can also find the route table in the Route Tables list, select the Actions menu (three dots) for it, and then select View details .
- 

Use the[network route-table get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/get.html)command and required parameters to get details for a VCN route table:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/GetRouteTable)
