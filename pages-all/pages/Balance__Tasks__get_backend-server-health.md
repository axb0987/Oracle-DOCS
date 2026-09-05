# Getting a Load Balancer Backend Server's Health Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-server-health.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer Backend Server's Health Details

View the health status details of a backend server for a load balancer.

The primary and standby load balancers both provide health check results that contribute to the health status.

See[Health Status Indicators for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Health_Status.htm)for descriptions of the load balancer health indicators.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-server-health.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-server-health.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-server-health.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select Backends .
The Backends tab opens. All backend servers in the selected backend set are displayed in a table.
- View the health status of the backend server under Health .
- 

Use the[oci lb backend-health get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-health/get.html)command and required parameters to view the health status details of a backend server for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackendHealth](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendHealth/GetBackendHealth)operation to view the health status details of a backend server for a load balancer.

## Health Details

Here are the health levels and their descriptions:
- 

Critical (red): Neither health check has returned a status of OK .
- 

Warning (yellow): One health check returned a status of OK and one did not.
- 

Pending (yellow): One or both health checks returned a status of Pending or the system was unable to retrieve metrics.
- 

OK (green): The primary and standby load balancer health checks both return a status of OK .

See[Health Status Indicators for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Health_Status.htm)
