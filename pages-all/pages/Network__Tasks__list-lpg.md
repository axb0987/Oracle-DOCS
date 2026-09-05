# Listing LPGs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm
- Fetched: 2026-09-05 02:45 CDT

# Listing LPGs

List the local peering gateways (LPGs) in a virtual cloud network (VCN).

A VCN can have several LPGs, and each one can be used to connect to one and only one other VCN. See[Gateway Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#gateway_limits)for more details on current LPG limits.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Local Peering Gateways section.
- Under Resources , select Local Peering Gateways .
- 

Use the[network local-peering-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/list.html)command and required parameters to list LPGs in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListLocalPeeringGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/ListLocalPeeringGateways)
