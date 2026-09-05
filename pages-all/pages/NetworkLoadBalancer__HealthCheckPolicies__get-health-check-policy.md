# Getting Network Load Balancer Health Check Policy Details
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/get-health-check-policy.htm
- Fetched: 2026-09-05 02:48 CDT

# Getting Network Load Balancer Health Check Policy Details

View the health check policy details for a network load balancer and backend set.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/get-health-check-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/get-health-check-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/get-health-check-policy.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- From the Actions menu for the backend set you want, select Update health check .
The Update health check dialog box opens. Here you can view health check details and change its settings.
- 

Use the[oci nlb health-checker get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/health-checker/get.html)command and required parameters to get the health check policy details of a network load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetHealthChecker](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/HealthChecker/GetHealthChecker)
