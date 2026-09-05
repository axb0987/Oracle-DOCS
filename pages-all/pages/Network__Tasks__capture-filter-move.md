# Moving a Capture Filter to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm
- Fetched: 2026-09-05 02:43 CDT

# Moving a Capture Filter to a Different Compartment

Move a capture filter from one compartment to another.

For more information about capture filters and a feature overview, see[Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm). For information about compartments and access control, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#)
- 

- On the Capture filters list page, find the capture filter you want to work with. If you need help finding the list page, see[Listing Capture Filters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm#top).
- From the Actions menu (three dots) for the capture filter, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[capture-filter change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/change-compartment.html)command and required parameters to move a capture filter to a different compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeCaptureFilterCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/ChangeCaptureFilterCompartment)
