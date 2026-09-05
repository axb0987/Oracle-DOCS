# Getting a Cost Analysis Scheduled Report's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-get.htm
- Fetched: 2026-09-05 01:44 CDT

# Getting a Cost Analysis Scheduled Report's Details

Get the details of a Cost Analysis scheduled report in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/schedule-get.htm#)
- 

- 

On the Scheduled reports list page, select the scheduled report that you want to work with. (Select the link under Job name .) If you need help finding the list page or the scheduled report, see[Listing Cost Analysis Scheduled Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/../Tasks/schedule-list.htm).

The details page opens and displays information about the scheduled report.
- To view the history of report runs, select the History tab.

This tab displays information about report runs, including names of scheduled report files in the bucket and bucket links.
- To open the bucket page in Object Storage, select the bucket link.

The bucket link is available in the Destination (Object storage bucket) field (under Details ) or in the Message field (in the History tab).
- 

Use the[oci usage-api schedule get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/usage-api/schedule/get.html)command and required parameters to get a Cost Analysis scheduled report's details:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetSchedule](https://docs.oracle.com/iaas/api/#/en/usage/latest/Schedule/GetSchedule)
