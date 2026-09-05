# Listeners for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm
- Fetched: 2026-09-05 01:41 CDT

# Listeners for Load Balancers

Use listeners to check for incoming traffic on the load balancer's IP address.

A listener is a logical entity that checks for incoming traffic on the load balancer's IP address. To handle TCP, HTTP, and HTTPS traffic, you must configure at least one listener per traffic type. When you create a listener, you must ensure that your VCN's[security rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)allow the listener to accept traffic.

Tip  
  
To accommodate high-volume traffic, we recommend that you use stateless security rules for your load balancer subnets. See[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)for more information.

You can have one SSL certificate bundle per listener. You can configure two listeners, one each for ports 443 and 8443, and associate SSL certificate bundles with each listener. For more information about SSL certificates for load balancers, see[SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm).

Select Listeners under Resources in the load balancer's Details page to display the Listeners page. This page contains a button for creating listeners.

You can perform the following listener management tasks:

[List the listeners under a load balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-listener.htm).

[Create a new listener for a load balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm).

[Get a listener's details](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_listener.htm).

[Edit a listener's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Editing_Listeners.htm)

[Enable a listener to accept traffic](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Enabling_Listeners_to_Accept_Traffic.htm).

[Delete a listener from a load balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Deleting_Listeners.htm).

## Listener Protocol Version Support

HTTP and HTTPS listeners support HTTP 1.0, HTTP 1.1 L7 protocol, and HTTP/2 listener support HTTP 2.0 L7 protocol. For HTTP L7 listeners, communication between the load balancer and its backend servers support only HTTP 1.1. Incoming HTTP 1.0 or HTTP 2.0 traffic is proxied to the backend servers as HTTP 1.1 traffic.
Note
