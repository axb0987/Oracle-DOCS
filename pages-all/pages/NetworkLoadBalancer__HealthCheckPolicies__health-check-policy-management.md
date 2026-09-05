# Health Check Policies for Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/health-check-policy-management.htm
- Fetched: 2026-09-05 02:48 CDT

# Health Check Policies for Network Load Balancers

Set up and use health checks to decide the availability of backend servers for a network load balancer.

A health check is a test to confirm the availability of backend servers. A health check can be a request or a connection try. Based on a time interval you specify, the network load balancer applies the health check policy to continuously monitor backend servers. If a server fails the health check, the network load balancer takes the server temporarily out of rotation. If the server later passes the health check, the network load balancer returns it to the rotation.

You configure the health check policy when you create a network load balancer. You can also configure the health check policy when you create or edit a backend set for an existing load balancer. Here is a summary of the protocols you can use with your health check policy:
- TCP-level health checks try to make a TCP connection with the backend servers and validate the response based on the connection status.

If it's not practical to create a request for the protocol you're working with, you can omit the request data. In this case, the backend is considered healthy if the TCP connection succeeds.
- HTTP-level health checks send requests to the backend servers at a specific URI and validate the response based on the status code or entity data (body) returned.
- HTTPS-level health checks send requests to the backend servers at a specific URI and validate the response based on the status code or entity data (body) returned over a secure and encrypted HTTPS protocol.
- UDP-level health checks send a single request to the backend server and match the response (if received) against the response data you specify.
- DNS-level health checks send requests to the backend servers using either UDP or TCP. The health check also uses the query name and related information that you want to provide the DNS response from the backend server.

The service provides application-specific health check capabilities to help you increase availability and reduce the application maintenance window.

You can perform the following health check policy management tasks:
- [Get a health check policy's details for a backend set](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/get-health-check-policy.htm)
- [Edit a health check policy for a backend set](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/update-health-check-policy.htm)

## Configuring the Health Check Protocol to Match the Application or Service

If you run an HTTP service, be sure to configure an HTTP-level health check. If you run a TCP-level health check against an HTTP service, you might not get a correct response. The TCP handshake can succeed and indicate that the service is up even when the HTTP service is incorrectly configured or having other issues. Although the health check appears good, customers might experience transaction failures. For example:
- The backend HTTP service has issues when talking to the health check URL and the health check URL returns 5XX messages. An HTTP health check catches the message from the health check URL and marks the service as down. In this case, a TCP health check handshake succeeds and marks the service as healthy, even though the HTTP service might not be usable.
- The backend HTTP service responds with 4XX messages because of authorization issues or no configured content. A TCP health check doesn't catch these errors.

## Heath Status Indicators

The Network Load Balancer service provides health status indicators that use the health check policies to report on the general health of the network load balancers and their components. You can see health status indicators on the Console List and Details pages for load balancers, backend sets, and backend servers. You also can use the API to retrieve this information.

Health status indicators have four levels. The following table provides the general meaning of each level:

Level Color Description
OK Green No attention required.

The resource is functioning as expected.
Warning Yellow Some reporting entities require attention.

The resource isn't functioning at peak efficiency or the resource is incomplete and requires further work.
Critical Red Some or all reporting entities require immediate attention.

The resource isn't functioning or unexpected failure is imminent.
Unknown Gray Health status can't be determined.

The resource is not responding or is in transition and might resolve to another status over time.

The precise meaning of each level differs among the following components:
- [Network load balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/../NetworkLoadBalancers/get-network-load-balancer-health.htm)
- [Backend sets](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/../BackendSets/get-backend-set-health.htm)
- [Backend servers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/../BackendServers/get-backend-server-health.htm)

### Using Health Status

At the highest level, network load balancer health reflects the health of its components. The health status indicators provide information you might need to drill down and investigate an existing issue. Some common issues that the health status indicators can help you detect and correct include:

A health check is misconfigured.

In this case, all the backend servers for one or more of the affected listeners report as unhealthy. If your investigation finds that the backend servers don't have problems, then a backend set probably includes a misconfigured health check.

A listener is misconfigured.

All the backend server health status indicators report OK , but the network load balancer doesn't pass traffic on a listener.

The listener might be configured to:
- Listen on the wrong port.
- Use the wrong protocol.
- Use the wrong policy.

If your investigation shows that the listener isn't at fault, check the security list configuration.

A security rule is misconfigured.

Health status indicators help you diagnose two cases of misconfigured security rules:
- All entity health status indicators report OK , but traffic doesn't flow (as with misconfigured listeners). If the listener isn't at fault, check the security rule configuration.
- All entity health statuses report as unhealthy. You have checked the health check configuration and the services run correctly on the backend servers.

In this case, the security rules might not include the IP range for the source of the health check requests. You can find the health check source IP on the Details page for each backend server. You can also use the API to find the IP in the`sourceIpAddress`field of the[HealthCheckResult](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/HealthCheckResult/)object.
Note  
  
The source IP for health check requests comes from a compute instance managed by the Network Load Balancer service.

One or more of the backend servers reports as unhealthy.

A backend server might be unhealthy or the health check might be misconfigured. To see the corresponding error code, check the status field on the backend server's Details page. You can also use the API to find the error code in the`healthCheckStatus`field of the[HealthCheckResult](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/HealthCheckResult/)object.

Other cases in which health status might prove helpful include:
- VCN[network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)or[network security lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)block traffic.
- Compute instances have misconfigured route tables.

Health status is updated every three minutes. No finer granularity is available.

Health status doesn't provide historical health data.

### Health Check Best Practices

Configure the health check protocol to match the application or service. If you run an HTTP service, be sure to configure an HTTP-level health check. If you run a TCP-level health check against an HTTP service, you might not get an correct response. The TCP handshake can succeed and indicate that the service is up even when the HTTP service is incorrectly configured or having other issues. Although the health check appears good, customers might experience transaction failures.

For example:
- The backend HTTP service has issues when talking to the health check URL and the health check URL returns 5XX messages. An HTTP health check catches the message from the health check URL and marks the service as down. In this case, a TCP health check handshake succeeds and marks the service as healthy, even though the HTTP service might not be usable.
- The backend HTTP service responds with 4XX messages because of authorization issues or no configured content. A TCP health check doesn't catch these errors.

### Common Side Effects of Health Check Misconfiguration

The following are common side effects of health check misconfiguration, and can be used to troubleshoot issues.
- Wrong port

In this scenario, all the backend servers report as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting the port. The port must be listening and has allowed traffic on the backend.

OCI Logging Error: errno":"EHOSTUNREACH","syscall":"connect".
- Wrong path

In this scenario, all the backend servers report as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting the path for the HTTP health check it needs to match an actual application on the backend server. In this case, you can use a curl test from a system in the same network.

For example:
```

```

You receive the configured status code in the response OCI Logging Error:
```

```

- Wrong protocol

In this scenario, all the backend servers report as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting the protocol it needs to match the protocol that's listening on the backend. For example: We only support TCP and HTTP health checks. If the backend server is using HTTPS, use TCP as the protocol.

OCI Logging Error :
```

```

- Wrong status code

In this scenario, all the backend servers report as unhealthy. If the backend servers don't have any problems, for an HTTP health check you might have made a mistake setting the status code to match the actual status code being returned from the backend. A common scenario is when a backend is returning a 302 and you're expecting a 200. This result is likely the backend sending you to a sign in page or another location on the server. In this scenario, you can either fix the backend to return the expected code or use 302 in the health check configuration.

OCI Logging Error:
```

```

where XX to be the status code that's returned.
- Wrong regex pattern

All the backend servers report as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting an incorrect regex pattern consistent with the body, or the backend isn't returning the expected body. In this scenario, you can either change the backend to match the pattern or correct the pattern to match the backend. The following are some specific pattern examples.
- Any Content - ".*"
- A page returning the value "Status:OK:" - "Status:OK:.*"
- OCI Logging Error: "response match result: failed"
- Misconfigured Network Security Groups, security lists, or local firewall

All or some backend servers report as unhealthy. If the backend servers don't have any problems, you might have made a mistake configuring either the NSGs, Security Lists, or local firewalls such as firewalld, iptables, or SELiinux. In this scenario you can use a curl or netcat test from a system that belongs to the same subnet and NSG as the balancer instance HTTP:

For example:
```

```

You can check the local firewall by using the following command:
```

```

If the firewall is missing the expected rules you can use a command set such as this to add the service: (this example is for HTTP port 80):
- 
```

```

- 
```

```

## Configuring Your Health Check Protocol to Match Your Application or Service

The service provides application-specific health check capabilities to help you increase availability and reduce your application maintenance window.

If you run an HTTP service, be sure to configure an HTTP-level health check. If you run a TCP-level health check against an HTTP service, you might not get a correct response. The TCP handshake can succeed and indicate that the service is up even when the HTTP service is incorrectly configured or having other issues. Although the health check appears good, customers might experience transaction failures. For example:
- The backend HTTP service has issues when talking to the health check URL and the health check URL returns 5XX messages. An HTTP health check catches the message from the health check URL and marks the service as down. In this case, a TCP health check handshake succeeds and marks the service as healthy, even though the HTTP service might not be usable.
- The backend HTTP service responds with 4XX messages because of authorization issues or no configured content. A TCP health check doesn't catch these errors.

## DNS Health Checking

The Network Load Balancer service support DNS health checking over TCP and UDP transport, for both IPv4 and IPv6 backend servers. DNS health checking for DNS resolver backend servers is an improvement over TCP- or UDP-based checks, because it verifies that the DNS protocol is functional for the DNS resolver backend servers. Those protocols use base64 format to specify the request and response messages, and that can be difficult when forming DNS requests and responses. Also, there can be several valid answers and RCODE in the response message, for example both NOERROR(0) and NXDOMAIN(3). Handling all these scenarios using the standard TCP or UDP health checking isn't possible.

When you create a backend set, either during the initial network load balancer creation or when you're adding a backend set to an existing network load balancer, you must specify the following protocol specific configurations if you're using DNS health checking:
- Query name : Provide a DNS domain name for the query.
- Query class : Select from the following options:
- IN : Internet (default)
- CH : Chaos
- Query type : Select from the following options:
- A : Indicates a hostname corresponding IPv4 address. (default)
- AAAA : Indicates a hostname corresponding IPv6 address.
- TXT : Indicates a text field.
- Acceptable response codes : Select one or more from the following options:
- RCODE:0 NOERROR DNS query completed successfully.
- RCODE:2 SERVFAIL Server failed to complete the DNS request.
- RCODE:3 NXDOMAIN Domain name doesn't exist.
-
