# Troubleshooting Load Balancer Backend Server Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/troubleshooting_backend.htm
- Fetched: 2026-09-05 01:40 CDT

# Troubleshooting Load Balancer Backend Server Issues

Learn about backend server issues associated with load balancers.

## Debugging a Backend Server Timeout

When the backend server exceeds the response time when responding to a request, a 504 error occurs indicating that the backend server is either down or not responding to the request forwarded by the load balancer. The client application receives the following response code:`HTTP/1.1 504 Gateway Timeout`.

Errors can occur for the following reasons:
- The load balancer failed to establish a connection to the backend server before the connection timeout expired.
- The load balancer established a connection to the backend server but the backend didn't respond before the idle timeout period elapsed.
- The security lists or network security groups for the subnet or the VNIC didn't allow traffic from the backends to the load balancer.
- The backend server or application server failed.

Follow these steps to troubleshoot the backend server timeout errors:
- Use the`curl`utility to directly test the backend server from a host in the same network.

```

```

If this test takes longer than one second to respond, an application-level issue is causing latency. We recommend that you check any upstream dependencies that might cause latency, including:
- Network attached storage such as iSCSI or NFS
- Database latency
- An off-premise API
- An application tier
- Check the application by accessing it directly from the backend server. Check its access logs to determine if the application can be accessed and is functioning properly.
- If the load balancer and the backend server are in different subnets, then check whether the security lists contain rules to allow traffic. If no rules exist, then traffic isn't allowed.
- Enter the following commands to determine whether firewall rules exist on the backend servers that block traffic:

`iptables -L`lists all firewall rules enforced by`iptables`

`sudo firewall-cmd --list-all`lists all firewall rules enforced by`firewalld`
- Enable logging on the load balancer to determine whether the load balancer or the backend server is causing the latency.

## Testing TCP and HTTP Backend Servers

This topic describes how to troubleshoot a load balancer connection. The topology used in this procedure has a public load balancer in a public subnet and the backend servers are in the same subnet.

We recommend that you use the Oracle Cloud Infrastructure Logging service to troubleshoot issues. (See[Details for Load Balancer Logs](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_load_balancer_logs.htm).)

In addition to using Oracle Cloud Infrastructure logging, however, you can use other utilities listed in this section to troubleshoot the traffic that's processed by the load balancer and sent to a backend server. To perform these tests, We recommend that you create an instance in the same network as your load balancer and allow the traffic in the same network security groups and security lists. Use the following tools to troubleshoot:
- ping
Before using the more advanced utilities listed here, We recommend that you perform a basic`ping`test. For this test to succeed, you must allow ICMP traffic between the test instance and the backend server.
```

```

The response should look similar to:
```

```

If you receive a message that contains "64 bytes from...", then the ping succeeded.

Receiving a message that contains "Destination Host Unreachable" indicates that the system doesn't exist.

Receiving no message indicates that the system exists but the ICMP protocol isn't allowed. Check all firewalls, security lists, and network security groups to ensure ICMP is allowed.
- curl

Use the`curl`utility to send HTTP requests to a specific host, port, or URL.
- 

The following example shows using`curl`to connect to a backend server that's sending a`403 Forbidden`error:
```

```

In the preceding example, the health check fails, returning a`403`error, indicating that the backend server doesn't have local file permissions configured properly for the Health check page.
- The following example shows using`curl`to connect to a backend server that's sending a`404 Not Found`error:
```

```

In the preceding example, the health check fails, returning a`404`error, indicating that the Health check page doesn't exist in the expected location.
- The following example shows a backend server that exists and either a network security group, the security lists, or a local firewall is blocking the traffic:
```

```

- The following example shows a backend server that doesn't exist:
```

```

- Netcat

Netcat is a networking utility for reading from and writing to network connections using TCP or UDP.
- The following example shows using the`netcat`utility at the TCP level to ensure that the destination backend server can receive a connection:
```

```

In the preceding example,`port`is open for connections.
- 
```

```

In the preceding example,`port`is closed.
- Tcpdump

Use the`tcpdump`utility to capture all traffic to a backend server to ensure which traffic is coming from a load balancer and what is being returned to the load balancer.
```

```

- OpenSSL

When troubleshooting SSL issues between the load balancer instance and the backend servers, We recommend using the`openssl`utility. This utility opens an SSL connection to a specific host name and port, and prints the SSL certificate and other parameters.

Other options for troubleshooting issues are:
- `-showcerts`

This option prints all certificates in the certificate chain presented by the backend server. Use this option to identify issues, such as a missing intermediate certificate authority certificate.
- `-cipher cipher_name`

This option forces the client and server use a specific cipher suite and helps to rule out whether the backend server is allowing specific ciphers.
- Netstat

Use the`netstat -natp`command to ensure that the application running on the backend server is up and running. For TCP or HTTP traffic, the backend application, IP address, and port must all be in listen mode. If the application port on the backend server isn't in listen mode, then the TCP port of the application isn't up.
