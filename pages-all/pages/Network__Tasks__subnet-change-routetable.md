# Changing Which VCN Route Table a Subnet Uses
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm
- Fetched: 2026-09-05 02:47 CDT

# Changing Which VCN Route Table a Subnet Uses

Change which virtial cloud network (VCN) route table a subnet uses.
For an overview of routing in your VCN and subnets, see[VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the route table you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab, then select the name of the subnet you want to work with.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN. Select the name of the subnet you want to work with.
- On the subnet details page, perform one of the following actions depending on the option that you see:

- On the subnet details page, select Actions then select Edit .
- On the subnet details page, select Edit .
- In the Route Table section, select the new route table you want the subnet to use.
- Select Save changes .
The changes takes effect within a few seconds.
- 

Use the[network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html)command and described parameters to change which route table a subnet uses:

```

```

The route-table-id is the OCID of the route table the subnet will use.

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable)
