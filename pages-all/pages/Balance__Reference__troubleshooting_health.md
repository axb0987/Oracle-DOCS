# Troubleshooting Load Balancer Health Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_health.htm
- Fetched: 2026-09-05 01:40 CDT

# Troubleshooting Load Balancer Health Issues

Learn about heath issues associated with load balancers.

## Backend Servers Health Checks

Receiving a 502 Bad Gateway error can indicate one of the following causes:
- No backend servers are assigned to the backend set.
- No backend servers are responding to the health check.

If you receive this error, determine why the backend servers aren't responding to health check. Check and adjust any health check settings, including status code, regular expressions, interval timeout, port, and protocol.

See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Tasks/load_balancer_health_management.htm)for more information.

## Health Status

Any of the following load balancer behaviors are indicative of health status issues:
- The client behaves as expected but fails periodically.
- The backend server switches between passing and failing the health check.
- The entries`Unhealthy to Healthy`or`Healthy to Unhealthy`appears in error logs.

These are possible causes of health status issues:
- An unhealthy backend server becomes healthy.
- The health status of the backend server changes often, indicating a chronic problem.

Possible solutions include:
- Ensuring that the instance is not changing health status abnormally.
- Checking application logs on the backend server for any application-specific issues.

See[Common Load Balancer Errors](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/../Troubleshooting/common_load_balancer_errors.htm)for more information.

## Unreachable Host Health Checks

Any of the following load balancer behaviors are indicative of unreachable host health checks:
- The backend server fails the health check.
- The client fails with a 502 Bad Gateway error.
- The entry`EHOSTUNREACH`appears in error logs.

These are possible causes of unreachable host health checks:
- The backend server health check fails because of an unreachable host.
- The backend server health check fails because of a connection reset.
- An application or firewall is actively refusing the connection.

Possible solutions include:
- Checking the local instance firewall to confirm that traffic is being allowed.
- Checking the local instance to confirm that the application is running.
- Checking the network security group and security lists to confirm that traffic is allowed.

See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm)for more information.

## Health Check Connection

Any of the following load balancer behaviors are indicative of health connection issues:
- The client fails with a 502 Bad Gateway error.
- The backend server is periodically or chronically failing health checks.
- The entry`connect timed out`appears in the error logs.

These are possible causes of health connection issues:
- The backend server isn't responding to health checks in the expected time period.
- Slow upstream dependency including, database, application service or API, or slow storage services, such as Oracle Cloud Infrastructure File Storage service, Elastic Block Store, or Object Storage.

Possible solutions include:
- Performing a local test to the backend server to eliminate the load balancer as a cause.
- Checking the performance of all upstream dependencies.
- Checking application logs on the backend server for any dependencies reporting any sort of timeout.

See[Testing TCP and HTTP Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_backend.htm#TestTCPHTTPBackendServers)
