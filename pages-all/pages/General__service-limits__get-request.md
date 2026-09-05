# Getting Details for a Limit Increase Request
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/get-request.htm
- Fetched: 2026-09-05 02:13 CDT

# Getting Details for a Limit Increase Request

Get details for an existing limit increase request.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/get-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/get-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/get-request.htm#)
- 

- On the Limit increase requests list page, select the limit increase request that you want to work with. If you need help finding the list page, see[Listing Limit Increase Requests](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm).
The details page opens and displays information about the limit increase request.
- (Optional) To view items in the limit increase request, select Requested items .

## Filtering List Results

Use filters to limit the items in the list under Requested items . From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

To perform an action on an item directly from the list table under Requested items , select an available option from the Actions menu in the row for that item:
- Copy OCID : Copy the OCID of the item to the clipboard.
- Withdraw :[Withdraw the item from the limint increase request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-item-request.htm).
- 

Use the[oci limits-increase limits-increase-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits-increase/limits-increase-request/get.html)command and required parameters to get details for a limit increase request:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetLimitsIncreaseRequest](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseRequest/GetLimitsIncreaseRequest)
