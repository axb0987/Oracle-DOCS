# Canceling a VMware Solution SDDC's HCX License Downgrade
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-cancel-downgrade-hcx.htm
- Fetched: 2026-09-05 03:09 CDT

# Canceling a VMware Solution SDDC's HCX License Downgrade

Learn how to cancel a pending HCX license downgrade.

After an HCX license downgrade is started, the request remains in a`PENDING`state until the HCX Monthly Billing Cycle End Date. A notification appears on the SDDC Details page that shows the date that Enterprise features end.

You can cancel an HCX license downgrade as long as it's still in a PENDING state.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-cancel-downgrade-hcx.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-cancel-downgrade-hcx.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-cancel-downgrade-hcx.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
A notification appears on the SDDC details page that shows the date that Enterprise features end.
- Select Cancel downgrade .
This option could be in the banner at the top of the page or on the right side of the notification.
- 

Use the[cancel-downgrade-hcx](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/cancel-downgrade-hcx.html)command and required parameters to cancel an HCX license downgrade:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CancelDowngradeHcx](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/CancelDowngradeHcx)
