# Moving a Service Gateway to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm
- Fetched: 2026-09-05 02:45 CDT

# Moving a Service Gateway to a Different Compartment

Move a service gateway into a different compartment within the same tenancy.

For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

When you move a service gateway to a new compartment, policies set for that new compartment apply immediately.

The service gateway moves to the new compartment immediately. Depending on your permissions, you can select the compartment in the left side menu to view the service gateway.

For more information about using compartments and policies to control access to this cloud network, see[Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/accesscontrol.htm). For general information about compartments, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .
- Select the the Actions menu (three dots) for the gateway, and then select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[network service-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/change-compartment.html)command and required parameters to move a service gateway into a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeServiceGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/ChangeServiceGatewayCompartment)
