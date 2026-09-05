# Understanding Load Balancer Health Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/understanding_health_issues.htm
- Fetched: 2026-09-05 01:42 CDT

# Understanding Load Balancer Health Issues

Understand the health issues related to load balancers and how to interpret them.

At the highest level, load balancer health reflects the health of its components. The health status indicators provide information you might need to drill down and investigate an existing issue. Some common issues that the health status indicators can help you detect and correct include:

A health check is misconfigured.

In this case, all the backend servers for one or more of the affected listeners report as unhealthy. If your investigation finds that the backend servers do not have problems, then a backend set probably includes a misconfigured health check.

A listener is misconfigured.

All the backend server health status indicators report OK , but the load balancer does not pass traffic on a listener.

The listener might be configured to:
- 

Listen on the wrong port.
- 

Use the wrong protocol.
- 

Use the wrong policy.

If your investigation shows that the listener is not at fault, check the security list configuration.

A security rule is misconfigured.

Health status indicators help you diagnose two cases of misconfigured security rules:
- 

All entity health status indicators report OK , but traffic does not flow (as with misconfigured listeners). If the listener is not at fault, check the security rule configuration.
- 

All entity health statuses report as unhealthy. You have checked your health check configuration and your services run properly on your backend servers.

In this case, your security rules might not include the IP range for the source of the health check requests. You can find the health check source IP on the Details page for each backend server. You can also use the API to find the IP in the`sourceIpAddress`field of the[HealthCheckResult](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/HealthCheckResult/)object.
Note  
  

Source IP

The source IP for health check requests comes from a compute instance managed by the Load Balancer service.

One or more of the backend servers reports as unhealthy.

A backend server might be unhealthy or the health check might be misconfigured. To see the corresponding error code, check the status field on the backend server's Details page. You can also use the API to find the error code in the`healthCheckStatus`field of the[HealthCheckResult](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/HealthCheckResult/)object.

Other cases in which health status might prove helpful include:
- 

VCN network security groups or security lists block traffic.
- 

Compute instances have misconfigured route tables.

Health status is updated every three minutes. No finer granularity is available.
