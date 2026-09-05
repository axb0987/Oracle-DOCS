# Moving a local peering gateway to a different compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm
- Fetched: 2026-09-05 02:45 CDT

# Moving a local peering gateway to a different compartment

You can move a local peering gateway (LPG) from one compartment to another. When you move a local peering gateway to a new compartment, IAM policies for the new compartment apply immediately.

For more information about using compartments and policies to control access to a cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Local Peering Gateways section.
- Under Resources , select Local Peering Gateways .
- Select the the Actions menu (three dots) for the gateway, and then select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network local-peering-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/change-compartment.html)command and required parameters to get configuration details for a specific LPG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeLocalPeeringGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/ChangeLocalPeeringGatewayCompartment)
