# Updating a VTAP
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm
- Fetched: 2026-09-05 02:48 CDT

# Updating a VTAP

Update the information for a Virtual Test Access Point (VTAP).

For more information and a feature overview, see[Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm#)
- 

- On the VTAPs list page, select the VTAP that you want to work with. If you need help finding the list page or the VTAP, see[Listing VTAPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm#top).
- Select Edit .

- If the VTAP is`RUNNING`, you can only update the name.
- If the VTAP is in the`STOPPED`, you can update the following options:
- Name
- VCN
- Source
- Target
- Capture filter
- Under Show Advanced Options , you can update the following options:
- VXLAN network identifier (VNI)
- Max packet size
- Priority Mode
- Tagging For information about the options, see[Creating a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-create.htm).
- Select Save Changes .
- 

Use the[vtap update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/update.html)command and required parameters to edit a VTAP:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVtap](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/UpdateVtap)
