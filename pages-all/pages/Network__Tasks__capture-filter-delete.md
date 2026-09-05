# Deleting a Capture Filter
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a Capture Filter

Delete a capture filter.

Important  
  
You can't delete a capture filter if it's associated with a VTAP or Flow Log.

For more information about capture filters and feature overviews, see[Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm)and[Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/vcn-flow-logs.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#)
- 

- On the Capture filters list page, find the capture filter you want to work with. If you need help finding the list page, see[Listing Capture Filters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm#top).
- From the Actions menu (three dots) for the capture filter, select Delete .
- Confirm the deletion.
- 

Use the[capture-filter delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/delete.html)command and required parameters to delete a capture filter:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteCaptureFilters](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/DeleteCaptureFilter)
