# Withdrawing an Item from a Limit Increase Request
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-item-request.htm
- Fetched: 2026-09-05 02:13 CDT

# Withdrawing an Item from a Limit Increase Request

Withdraw an item from a limit increase request in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-item-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-item-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-item-request.htm#)
- 

- On the Limit increase requests list page, select the limit increase request that you want to work with. If you need help finding the list page, see[Listing Limit Increase Requests](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm).
- Select Requested items .
- From the Actions menu (three dots) for the item, select Withdraw .
- On the Withdraw requested item dialog, select Withdraw item .
The status of the item updates to Withdrawn .
- 

Use the[oci limits-increase item cancel](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits-increase/item/cancel.html)command and required parameters to withdraw an item from a limit increase request:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CancelLimitsIncreaseItemRequest](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseItemRequest/CancelLimitsIncreaseItemRequest)
