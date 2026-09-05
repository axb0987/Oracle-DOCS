# Moving a NAT Gateway to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm
- Fetched: 2026-09-05 02:45 CDT

# Moving a NAT Gateway to a Different Compartment

Move a NAT gateway into a different compartment within the same tenancy.

You can move a NAT gateway from one compartment to another. When you move a NAT gateway to a new compartment, inherent policies apply immediately.

For more information about using compartments and policies to control access to a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-change-compartment.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the NAT Gateways section.
- Under Resources , select NAT Gateways .
- Select the the Actions menu (three dots) for the gateway, and then select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network nat-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/change-compartment.html)command and required parameters to move a NAT gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeNatGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/ChangeNatGatewayCompartment)
