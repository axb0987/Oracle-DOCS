# Comparing Load Balancer and Network Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Reference/lb-vs-nlb.htm
- Fetched: 2026-09-05 01:40 CDT

# Comparing Load Balancer and Network Load Balancer

Compare the features and capabilities of the Load Balancer and Network Load Balancer services.

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
