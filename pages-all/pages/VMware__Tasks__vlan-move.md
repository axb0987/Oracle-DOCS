# Moving a VMware Solution SDDC VLAN Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-move.htm
- Fetched: 2026-09-05 03:09 CDT

# Moving a VMware Solution SDDC VLAN Between Compartments

Move a VLAN associated with an SDDC in VMware Solution from one compartment to another.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-move.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the VLANs that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select the VLAN that you want to work with.
- On the details page, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[vlan change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vlan/change-compartment.html)command and required parameters to move the VLAN to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeVlanCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vlan/ChangeVlanCompartment)
