# Listing VCN Route Tables
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing VCN Route Tables

List VCN route tables in a particular VCN and compartment.
For an overview of routing in VCNs and subnets, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the route table you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Routing tab.
- Under Resources , select Route Tables .

The default VCN route table and any other route tables are displayed in a table.
- 

Use the[network route-table list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/list.html)command and required parameters to list the route tables in the specified VCN and compartment.:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListRouteTables](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/ListRouteTables)
