# Withdrawing a Limit Increase Request
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-request.htm
- Fetched: 2026-09-05 02:13 CDT

# Withdrawing a Limit Increase Request

Withdraw a limit increase request in Oracle Cloud Infrastructure. All items in the request are withdrawn.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-request.htm#)
- 

- On the Limit increase requests list page, find the limit increase request that you want to work with. If you need help finding the list page, see[Listing Limit Increase Requests](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm).
- From the Actions menu (three dots) for the limit increase request, select Withdraw .
- On the Withdraw limit request dialog, select Withdraw .
The status of the limit increase request and all of its items update to Withdrawn .
- 

Use the[oci limits-increase limits-increase-request cancel](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits-increase/limits-increase-request/cancel.html)command and required parameters to withdraw a limit increase request:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CancelLimitsIncreaseRequest](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseRequest/CancelLimitsIncreaseRequest)
