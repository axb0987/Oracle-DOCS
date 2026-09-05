# Editing a VMware Solution SDDC VLAN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-update.htm
- Fetched: 2026-09-05 03:09 CDT

# Editing a VMware Solution SDDC VLAN

Update the properties of a VLAN associated with an SDDC in VMware Solution, such as its name, tags, route tables, and NSGs.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-update.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the VLANs that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select the VLAN that you want to work with.
- Select Edit .
- Make any necessary changes.
- Select Save changes .
- 

Use the[vlan update](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/network/vlan/update.html)command and required parameters to edit a VLAN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVlan](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vlan/UpdateVlan)
