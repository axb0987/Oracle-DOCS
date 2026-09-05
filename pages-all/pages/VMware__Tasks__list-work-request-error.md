# Listing a VMware Solution SDDC's Work Request Errors
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-work-request-error.htm
- Fetched: 2026-09-05 03:08 CDT

# Listing a VMware Solution SDDC's Work Request Errors

Learn how to get a list of all errors for a specific work request.

Work requests are spawned by starting operations such as Create SDDC . If a work request fails, you can retrieve a list of all errors for the work request for troubleshooting purposes.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-work-request-error.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-work-request-error.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-work-request-error.htm#)
- 

- On the Software-Defined Data Centers list page, select the SDDC that contains the work requests that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select Work requests.
- Select the work request that you want to work with.
- Select Error messages .
- 

Use the[work-request-error list-errors](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/work-request-error/list-errors.html)command and required parameters to get a list of errors for a specific work request:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequestErrors](https://docs.oracle.com/iaas/api/#/en/vmware/latest/WorkRequestError/ListWorkRequestErrors)
