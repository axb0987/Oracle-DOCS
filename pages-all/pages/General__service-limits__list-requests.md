# Listing Limit Increase Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm
- Fetched: 2026-09-05 02:13 CDT

# Listing Limit Increase Requests

List existing limit increase requests for the tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm#)
- 

Open the navigation menu and select Governance &amp; Administration . Under Support , select Limit increase requests .

The Limit increase requests list page opens. All limit increase requests for the tenancy are displayed in a table.

## Filtering List Results

Use filters to limit the limit increase requests in the list. Perform one of the following actions depending on the options that you see:
- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table.
- Above the table, enter an SR number.
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a limit increase request to open its details page, where you can view its status and perform other tasks.

To perform an action on a limit increase request directly from the list table, select an available option from the Actions menu in the row for that limit increase request:
- View details : Open the details page for the limit increase request.
- Copy OCID : Copy the OCID of the limit increase request to the clipboard.
- Withdraw :[Withdraw the limit increase request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-request.htm).
- Manage tags : Add one or more tags to the limit increase request. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

To create a limit increase request, select Create .
- 

Use the[oci limits-increase limits-increase-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits-increase/limits-increase-request/list.html)command and required parameters to list limit increase requests:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListLimitsIncreaseRequests](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseRequest/ListLimitsIncreaseRequests)
