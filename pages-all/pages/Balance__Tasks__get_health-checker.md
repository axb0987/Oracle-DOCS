# Getting a Load Balancer's Health Check Policy Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_health-checker.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer's Health Check Policy Details

View the details of a health check policy for a load balancer and backend set.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_health-checker.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_health-checker.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_health-checker.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select the backend set that you want to work with.
- On the backend set's details page, select Update health check .
The Update health check dialog box appears. Here you can view details on the backend set's health check details.
- 

Use the[oci lb health-checker get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/health-checker/get.html)command and required parameters to view the details of a health check policy for a load balancer and backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`GetHealthChecker`](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/HealthChecker/GetHealthChecker)
