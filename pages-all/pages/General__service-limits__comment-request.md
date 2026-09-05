# Adding a Comment to a Limit Increase Request
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/comment-request.htm
- Fetched: 2026-09-05 02:13 CDT

# Adding a Comment to a Limit Increase Request

Add a comment to a limit increase request in Oracle Cloud Infrastructure. The request must be in progress with a comment from Oracle Support.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/comment-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/comment-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/comment-request.htm#)
- 

- On the Limit increase requests list page, select the limit increase request that you want to work with. If you need help finding the list page, see[Listing Limit Increase Requests](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm).
The details page opens and displays information about the limit increase request.
- Select Support .

If this tab isn't visible, then Oracle Support hasn't commented on the request, or the request isn't in progress.

All comments for the limit increase request are displayed in a table.

To view details about a comment, expand it.

To limit the comments in the list, use filters. From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table.

To change the order of the comments in the list table, use the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).
- Select Add comment .
- In the Add comment panel, enter your comment, and then select Add .
Your comment is sent to Oracle Support.
- 

Use the[oci limits-increase limits-increase-request patch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits-increase/limits-increase-request/patch.html)command and required parameters to add a comment to a limit increase request:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[PatchLimitsIncreaseRequest](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseRequest/PatchLimitsIncreaseRequest)
