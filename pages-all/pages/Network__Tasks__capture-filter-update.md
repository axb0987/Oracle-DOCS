# Updating a Capture Filter
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm
- Fetched: 2026-09-05 02:43 CDT

# Updating a Capture Filter

Update the information for a capture filter.

For more information about capture filters and a feature overview, see[Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm#)
- 

- On the Capture filters list page, select the capture filter you want to work with. If you need help finding the list page, see[Listing Capture Filters](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-list.htm#top).
- To change the display name or sampling rate for the capture filter, select Edit , make the change, and then save them.
- To change the rules used in the capture filter, select Manage rules and perform the following actions as needed:

- Change one or more of the existing rules, or add or delete a rule. There must always be at least one rule in a capture filter.
- To change the order of the rules, select Reorder for a rule. You can move the rule up one level in the list order, move it down one level, move it to the top of the list, or move it to the bottom of the list.
- Select Save Changes .
- 

Use the[capture-filter update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/update.html)command and required parameters to edit a capture filter:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCaptureFilter](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/UpdateCaptureFilter)
