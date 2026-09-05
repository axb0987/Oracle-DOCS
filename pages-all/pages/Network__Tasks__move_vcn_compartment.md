# Moving a VCN Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm
- Fetched: 2026-09-05 02:45 CDT

# Moving a VCN Between Compartments

You can move a VCN from one compartment to another.

When you move a VCN, its associated VNICs, private IPs, and ephemeral IPs move with it to the new compartment. This changes the management of the resources with no changes to the routing of the traffic.

The VCN is moved immediately. Resources attached to the VCN are moved asynchronously and don't appear in the new compartment until the move is complete.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm#)
- 

- On the Virtual Cloud Networks list page, find the VCN that you want to move. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- From the Actions menu (three dots) for the VCN, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- If alarms monitor the VCN, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm).
- 

Use the[network vcn change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/change-compartment.html)command and required parameters to move a VCN from one compartment to another.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeVcnCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ChangeVcnCompartment)
