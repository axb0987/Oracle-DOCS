# Editing a Load Balancer's Health Check Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm
- Fetched: 2026-09-05 01:40 CDT

# Editing a Load Balancer's Health Check Policies

Update the health check policies for a load balancer and backend set.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Editing_Health_Check_Policies.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
- Select the backend set that you want to work with.
- On the backend set's details page, select Update health check .
- From the Update health check panel, edit any of the following:

- Protocol : Specify the protocol:
- HTTP
- TCP

Configure your health check protocol to match your application or service. See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)for more information.
- Port : Specify the backend server port against which to run the health check.

You can enter the value '0' to have the health check use the backend server's traffic port.
- Force plaintext health checks : (HTTP only) Optional. Check to send the health check to the backend server without SSL.

This option is only available when the backend server has its protocol is set to HTTP. It has no effect when the backend server doesn't have SSL enabled. When SSL is disabled, health checks are always plaintext.
- Interval in ms : Specify how often to run the health check, in milliseconds. The default is 10000 (10 seconds).
- Timeout in ms : Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
- Number of retries : Specify the number of retries to try before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is 3.
- Status code : (HTTP only) Specify the status code a healthy backend server must return.
- URL path (URI) : (HTTP only) Specify a URL endpoint against which to run the health check.
- Response body regex : (HTTP only) Provide a regular expression for parsing the response body from the backend server.
- Select Save changes .
- 

Use the[oci lb health-checker update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/health-checker/update.html)command and required parameters to edit a load balancer's health check policies.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`UpdateHealthChecker`](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/HealthChecker/UpdateHealthChecker)
