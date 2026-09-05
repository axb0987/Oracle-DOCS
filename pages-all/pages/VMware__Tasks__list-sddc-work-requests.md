# Listing a VMware Solution SDDC's Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-sddc-work-requests.htm
- Fetched: 2026-09-05 03:08 CDT

# Listing a VMware Solution SDDC's Work Requests

View all work requests for an SDDC in VMware Solution.

Work requests are spawned by starting operations such as Create SDDC .

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-sddc-work-requests.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-sddc-work-requests.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-sddc-work-requests.htm#)
- 

- On the Software-Defined Data Centers list page, select the SDDC that contains the work requests that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select Work requests.
- 

Use the[work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/work-request/list.html)command and required parameters to list all work requests in a compartment. To view the work requests for a specific resource, specify the resource's OCID :

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/vmware/latest/WorkRequest/ListWorkRequests)operation to get a list of work requests in a compartment. To view the work requests for a specific SDDC, specify its OCID in the`resourceId`
