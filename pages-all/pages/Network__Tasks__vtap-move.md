# Moving a VTAP to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm
- Fetched: 2026-09-05 02:48 CDT

# Moving a VTAP to a Different Compartment

You can move a Virtual Test Access Point (VTAP) from one compartment to another.

For more information and a feature overview, see[Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm#)
- 

- On the VTAPs list page, find the VTAP that you want to work with. If you need help finding the list page or the VTAP, see[Listing VTAPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm#top).
- From the Actions menu (three dots) for the VTAP, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[vtap change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/change-compartment.html)command and required parameters to move a VTAP to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeVtapCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/ChangeVtapCompartment)
