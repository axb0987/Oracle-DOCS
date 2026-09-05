# Getting Network Load Balancer Backend Server Heath Status Details
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server-health.htm
- Fetched: 2026-09-05 02:48 CDT

# Getting Network Load Balancer Backend Server Heath Status Details

View the health status details of a backend server for a network load balancer.

See[Health Status for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/../NetworkLoadBalancers/network-load-balancer-health-management.htm)for general information on getting and understanding health status details for network load balancers and their resources.

The Details page for a backend set provides the same Overall Health status indicator found in the backend set's list of backend servers. It also reports the following data for the two health checks performed against each backend server: IP ADDRESS The IP address of the health check status report provider, which is a compute instance managed by the Load Balancer service. This identifier helps you differentiate same-subnet load balancers that report health check status. The Network Load Balancer service ensures high availability by providing one primary and one standby network load balancer. To diagnose a backend server issue, you must know the source of the health check report. For example, a misconfigured security rule might cause one network load balancer instance to report that a backend server is healthy. The other network load balancer instance might return an unhealthy status. In this case, one of the two network load balancer instances cannot communicate with the backend server. Reconfigure the security rules to restore the backend server's health status. STATUS The status returned by the health check. Possible values include:
- 

OK

The backend server's response satisfied the health check policy requirements.
- 

INVALID_STATUS_CODE

The HTTP response status code did not match the expected status code specified by the health policy.
- 

TIMED_OUT

The backend server did not respond within the timeout interval specified by the health policy.
- 

REGEX_MISMATCH

The backend server response did not satisfy the regular expression specified by the health policy.
- 

CONNECT_FAILED

The health check server could not connect to the backend server.
- 

IO_ERROR

An input or output communication error occurred while reading or writing a response or request to the backend server.
- 

OFFLINE

The backend server is set to offline, so health checks are not run.
- 

UNKNOWN

Health check status is not available. LAST CHECKED The date and time of the most recent health check. Health status is updated every three minutes. No finer granularity is available.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server-health.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server-health.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server-health.htm#)
- 

This task can't be performed using the OCI Console.
- 

Use the[oci nlb backend-health get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-health/get.html)command and required parameters to get the health status details of a network load balancer's backend server:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackendHealth](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendHealth/GetBackendHealth)
