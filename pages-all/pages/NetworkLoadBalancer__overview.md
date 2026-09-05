# Overview of Flexible Network Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/overview.htm
- Fetched: 2026-09-05 02:49 CDT

# Overview of Flexible Network Load Balancer

Understand what network load balancers are, and how to get access to links that provide details on specific network load balancer topics.

The Oracle Cloud Infrastructure Flexible Network Load Balancer service (Network Load Balancer) provides automated traffic distribution from one entry point to multiple backend servers in your virtual cloud network (VCN). It operates at the connection level and load balances incoming client connections to healthy backend servers based on Layer 3/Layer 4 (IP protocol) data. The service offers a load balancer with your choice of a regional public or private IP address that's elastically scalable and scales up or down based on client traffic with no bandwidth configuration requirement.

Network Load Balancer provides the benefits of flow high availability, source and destination IP addresses, and port preservation. It is designed to handle volatile traffic patterns and millions of flows, offering high throughput while maintaining ultra low latency. Network load balancers have a default concurrent connection limit of 330,000 connections per Availability Domain (AD). In three AD regions, by default, network load balancers have a concurrent connection limit of one million. Network Load Balancer is the ideal load balancing solution for latency sensitive workloads.

Network Load Balancer is also optimized for long-running connections in the order of days or months. A given flow is always forwarded to the same backend server for the lifetime of the connection, making it best suited for your database type applications. You can configure application-specific health checks to ensure that the network load balancer directs traffic only to healthy backend servers.

You can see a comparison of the Network Load Balancer and Load Balancer services features and functionality here:[Comparing Load Balancer and Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/overview.htm#lb-vs-nlb).

The Network Load Balancer documentation contains the following major sections:

[Introduction to Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/introduction.htm)

[Network Load Balancer Management](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm)

[Health Status for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-health-management.htm)

[Backend Sets for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/backend-set-management.htm)

[Backend Servers for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/backend-server-management.htm)

[Listeners for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/listener-management.htm)

[Health Check Policies for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/HealthCheckPolicies/health-check-policy-management.htm)

[Work Requests for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/work-request-management.htm)

[Network Load Balancer Metrics](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Metrics/metrics.htm)

## Comparing Load Balancer and Network Load Balancer

Oracle Cloud Infrastructure load balancers provide automated traffic distribution from one entry point to many servers reachable from your VCN. They improve resource usage, ease scaling, and help ensure high availability. To meet your organization's needs, we make the following types of load balancers available:
- Load balancers : The Load Balancer service provides a reverse proxy solution that hides the IP of the client from backend application server and in reverse. It can perform advanced layer 7 (HTTP/HTTPS), layer 4 (TCP) load balancing and SSL offloading. Load balancers work best for websites, mobile apps, SSL termination, and advanced HTTP handling. Features of the Load Balancer service include:
- Can load balance applications and processes.
- Acts as a reverse proxy.
- Can achieve up to 8 Gbps per load balancer.
- Supports backend autoscaling.
- Can terminate SSL connections.
- Can have a web application firewall.
- One load balancer instance for free (limited to 10 Mbps).
- Network load balancers : The Network Load Balancer service provides a pass-through (non-proxy solution) that can preserve the client header (source and destination IP). Network load balancers are built for speed, optimized for long running connections, high throughput and low latency. Network load balancers work best for scaling network virtual appliances such as firewalls, real-time streaming, long running connections, Voice over IP (VoIP), Internet of Things (IoT), and trading platforms. Features of the Network Load Balancer service include:
- Can load balance packet forwarding, network traffic, and applications.
- Can preserve the client header information.
- Capable of scaling beyond 8 Gbps.
- Supports backend autoscaling.
- Low-latency network integrated load balancer.
- Network load balancers are Always Free tier.

The following table contains a comparison chart between the Load Balancer and Network Load Balancer services.

Load Balancer Comparison
Purpose Load Balancer Network Load Balancer
What is the throughput per load balancer? Up to 8 Gbps Can exceed 8 Gbps
Can it support backend autoscaling? Yes Yes
What do you need to load balance? Applications, processes Packet forwarding, network traffic and applications
What protocol do you need to work with? HTTP/HTTPS/TCP/gRPC TCP/UDP/ICMP/IP
Do you need high availability? Yes Yes
Do you need to set up health checks? Yes Yes
Do you need TCP load balancing? Yes Yes
Do you need UDP load balancing? No Yes
Do you need to interact with HTTP/HTTPS? Yes No
Do you need SSL termination? Yes No
Do you need IPv6 support? Yes Yes
Do you need IP-based session stickiness? Yes Yes
Do you need HTTP session stickiness? Yes No
Do you need web application firewall protection? Yes No
