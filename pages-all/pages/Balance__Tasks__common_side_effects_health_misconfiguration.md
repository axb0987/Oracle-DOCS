# Common Side Effects of Load Balancer Health Check Misconfigurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/common_side_effects_health_misconfiguration.htm
- Fetched: 2026-09-05 01:40 CDT

# Common Side Effects of Load Balancer Health Check Misconfigurations

Learn about common side effects associated with misconfiguring load balancer health checks.

The following are common side effects of health check misconfiguration, and can be used to troubleshoot issues.
- 

Wrong Port

In this scenario, all backend servers are reported as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting the port. The port must be a port that's listening and has allowed traffic on the backend.

OCI Logging Error:`errno:EHOSTUNREACH, syscall:connect`
- 

Wrong Path

In this scenario, all the backend servers are reported as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting the path for the HTTP health check it needs to match an actual application on the backend. In this scenario, you can use the`curl`utility to test from a system in the same network. For example:`$ curl -i http:// backend_ip_address /health`

You receive the configured status code in the response OCI Logging Error:`"msg":"invalid statusCode","statusCode":404,"expected":"200".`
- 

Wrong Protocol

In this scenario, all the backend servers are reported as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting the protocol it needs to match the protocol that's listening on the backend. For example: We only support TCP and HTTP health checks. If your backend is using HTTPS, then you would need to use TCP as the protocol.

OCI Logging Error:`code:EPROTO, errno:EPROTO`
- 

Wrong Status Code

In this scenario, all the backend servers are reported as unhealthy. If the backend servers don't have any problems, for an HTTP health check you might have made a mistake setting the status code to match the actual status code being returned from the backend. A common scenario is when a backend returns a`302`status code but you're expecting a`200`status code. This result is likely the backend sending you to a sign-in page or another location on the server. In this scenario, you can either fix the backend to return the expected code or use`302`in your health check configuration.

OCI Logging Error:`msg:invalid statusCode, statusCode: nnn ,expected:200`where`nnn`to be the status code that's returned.
- 

Wrong Regex Pattern
All the backend servers report as unhealthy. If the backend servers don't have any problems, you might have made a mistake setting an incorrect regex pattern consistent with the body, or the backend isn't returning the expected body. In this scenario, you can either change the backend to match the pattern or correct the pattern to match the backend. The following are some specific pattern examples.
- 

Any Content -`.*`
- 

A page returning the value`Status:OK:`-`Status:OK:.*`
- 

OCI Logging Error:`response match result: failed`
- 

Misconfigured Network Security Groups, Security Lists. or Local Firewall

All or some backend servers report as unhealthy. If the backend servers don't have any problems, then you might have improperly configured either the network security groups, security lists, or local firewalls (such as`firewalld`,`iptables`, or`SELinux`. In this scenario, you can use either the`curl`or`netcat`utilities to test from a system that belongs to the same subnet and network security group as your load balancer instance HTTP. For example:`$ curl -i http:// backend_ip_address /health TCP`and`nc -zvw3 backend_ip_address 443`.

You can check your local firewall by using the following command:`firewall-cmd --list-all --zone=public.`. If your firewall is missing the expected rules, then you can use a command set such as this to add the service (this example is for HTTP port 80):
- 

`firewall-cmd --zone=public --add-service=http`
- 

`firewall-cmd --zone=public --permanent --add-service=http`
