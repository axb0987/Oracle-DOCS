# Listing Service Gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing Service Gateways

List the service gateways (SGWs) available in a particular compartment.

The Console can only show the service gateway attached to a specific VCN (only one SGW is needed in a VCN), but the API and CLI can show all SGWs in a specified compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .

All service gateways in the VCN are displayed in a table.

A VCN only requires one service gateway.
- 

Use the[network service-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/list.html)command and required parameters to list all service gateways in a specified compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListServiceGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/ListServiceGateways)
