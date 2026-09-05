# Deleting a VMware Solution SDDC VLAN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-delete.htm
- Fetched: 2026-09-05 03:09 CDT

# Deleting a VMware Solution SDDC VLAN

Delete a VLAN associated with an SDDC in VMware Solution.

Note  
  

You can't delete a VLAN if it has any external access resources. You must first remove all external access. See[Removing External Access to a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-remove-external-access.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-delete.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the VLANs that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select the VLAN that you want to work with.
- Select Delete .
- 

Use the[vlan delete](https://docs.oracle.com/iaas/tools/oci-cli/3.23.0/oci_cli_docs/cmdref/network/vlan/delete.html)command and required parameters to delete a VLAN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteVlan](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vlan/DeleteVlan)
