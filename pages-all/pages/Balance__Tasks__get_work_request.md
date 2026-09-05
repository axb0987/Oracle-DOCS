# Getting a Load Balancer Work Request's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_work_request.htm
- Fetched: 2026-09-05 01:41 CDT

# Getting a Load Balancer Work Request's Details

View the details of a work request for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_work_request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_work_request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_work_request.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Work requests .
The Work requests list opens. All work requests are displayed in a table.
- Find the work request whose details you want to get.
The following details for each work request are displayed:
- Status : For a list of statuses and their descriptions, see[Work Request Status Descriptions](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/viewingworkrequest.htm#WorkRequestStatus).
- Type : API method used for the work request.
- OCID : Oracle Cloud identifier of the work request.
- Error details : Details of any errors associated with the work.
- Started : UTC-based date-time group when the work request was started.
- Finished : UTC-based date-time group when the work request was finished.
- 

Use the[oci lb work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/work-request/get.html)command and required parameters to get the details of a load balancer work request:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/WorkRequest/GetWorkRequest)
