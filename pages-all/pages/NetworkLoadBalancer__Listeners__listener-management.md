# Listeners for Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/listener-management.htm
- Fetched: 2026-09-05 02:48 CDT

# Listeners for Network Load Balancers

Set up listeners that check for incoming traffic on the IP address of the network load balancer.

A listener is a logical entity that checks for incoming traffic on the network load balancer's IP address. To handle TCP, HTTP, and HTTPS traffic, you must configure at least one listener per traffic type. When you create a listener, you must ensure that your VCN's security rules allow the listener to accept traffic. For more information, ee[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).
Tip  
  
To accommodate high-volume traffic, we recommend that you use stateless rules for your network load balancer subnets. For more information, see[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful).

You can select from the following protocols when creating a listener:
- TCP : Allows only TCP traffic on a specific or all ports.
- UDP : Allows only UDP traffic on a specific or all ports.
- TCP/UDP : Allows both TCP and UDP traffic on a specific or all ports.
- TCP/UDP/ICMP : Allows both TCP and UDP traffic on any port and also allows ICMP traffic. This option is only for SRC/DST header preserved mode (transparent mode).
- L3IP : Allows Layer 3 IP traffic. You can only select and configure this protocol from the CLI and API. Note the following regarding Layer 3 IP traffic:

- Only 2-tuple and 3-tuple network load balancing policies are allowed in the L3IP listeners.
- Only source preserved backend servers are allowed for the L3IP listeners.
- Only a single L3IP listener is allowed for each network load balancer.
- The listener port must be Any(0) for the L3IP listener and for the backend set attached to it.

You can perform the following listener management tasks:

[List the listeners under a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/list-listener.htm)

[Create a new listener for a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/create-listener.htm)

[Get a listener's details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/get-listener.htm)

[Edit a listener's settings.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/update-listener.htm)

[Change a listener's idle timeout.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/../NetworkLoadBalancers/configure-idle-timeout.htm)

[Delete a listener from a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/Listeners/delete-listener.htm)
