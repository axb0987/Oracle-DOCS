# Moving a Subnet Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm
- Fetched: 2026-09-05 02:45 CDT

# Moving a Subnet Between Compartments

Move a subnet in a Virtual Cloud Network (VCN) to a different compartment.

For more information, see[Working with Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#Working).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_subnet_compartment.htm#)
- 

- On the Virtual Cloud Networks list page, find the VCN with the subnet that you want to move. If you need help finding the list page, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Subnets tab.
- Scroll down to the table following the VCN details, which lists the subnets in the VCN.
- From the Actions menu (three dots) for the subnet, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network subnet change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/change-compartment.html)command and required parameters to move a subnet from one compartment to another:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeSubnetCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/ChangeSubnetCompartment)
