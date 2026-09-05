# Moving a VCN Route Table to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm
- Fetched: 2026-09-05 02:45 CDT

# Moving a VCN Route Table to a Different Compartment

Move a Virtual Cloud Network (VCN) route table to a different compartment.
For an overview of routing in a VCN and subnets, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the route table you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Routing tab.
- Under Resources , select Route Tables .
- From the Actions menu (three dots) for the route table, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network route-table change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/change-compartment.html)command and required parameters to move a VCN route table to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeRouteTableCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/ChangeRouteTableCompartment)
