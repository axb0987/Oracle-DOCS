# Load Balancer Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer.htm
- Fetched: 2026-09-05 01:41 CDT

# Load Balancer Management

Create and manage load balancers to provide automated traffic distribution from one entry point to several servers reachable from a virtual cloud network (VCN).

The essential components for load balancing include:
- A load balancer with pre-provisioned bandwidth.
- A backend set with a health check policy. See[Backend Sets](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets.htm)for more information.
- Backend servers for a backend set. See[Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendservers.htm)for more information.
- One or more listeners . See[Listeners](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm)for more information.
- Load balancer subnet security rules to allow the intended traffic. To learn more about these rules, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).
Note  
  
To accommodate high-volume traffic, We recommend that you use stateless security rules for any load balancer subnets. See[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)for more information.

Optionally, you can associate any listeners with SSL server certificate bundles to manage how the system handles SSL traffic. See[SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.

For information about the number of load balancers you can have, see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).

You can perform the following load balancer management tasks:

[List the load balancers in a compartment](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-load-balancer.htm).

[Create a new load balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm).

[Get a load balancer's details](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer.htm).

[Edit a load balancer's settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Editing_Load_Balancers.htm).

[Move a load balancer to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Moving_a_Load_Balancer_to_a_Different_Compartment.htm).

[Add, update, and remove load balancer security attributes](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/zpr-security-attributes.htm).

[Change a load balancer's bandwidth shape](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm).

[List a load balancer's health check summaries](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list_load_balancer_health.htm).

[Get a load balancer's health details](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer_health.htm).

[Terminate a load balancer within your tenancy](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Terminating_Load_Balancers.htm).

## Prerequisites

To implement a working load balancer, you need the following items:
- For a public load balancer in a region with several availability domains , you need a VCN with a public regional subnet or at least two public AD-specific subnets. In the latter case, each AD-specific subnet must reside in a separate availability domain. For more information on subnets, See[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)and[Public IP Address Ranges](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#oci-public-ips).
Note  
  
You can't specify a private subnet for a public load balancer.
- For a public load balancer in a region with only one availability domain, you need a VCN with at least one public subnet.
- For a private load balancer in any region, you need a VCN with at least one private subnet.
- Two or more backend servers (compute instances) running applications. For more information about compute instances, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).

## Compartments

For the purposes of access control, you must specify the compartment where you want the load balancer to reside. Consult an administrator in your organization if you're not sure which compartment to use. For information about compartments and access control, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).

## Private vs. Public IP Addresses

When you create a load balancer within a VCN, you get a public or private IP address, and provisioned total bandwidth. If you need another IP address, you can create another load balancer.
A public load balancer in a region with several availability domains requires one public regional subnet or two public AD-specific subnets to host the primary load balancer and a standby. In the latter case, each AD-specific subnet must reside in a separate availability domain. A public load balancer in a region with only one availability domain requires a single public subnet to host the primary load balancer and a standby. For more information on VCNs and subnets, see[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). You can associate the public IPv4 address with a DNS name from any vendor. You can use the public IP address as a front end for incoming traffic. The load balancer can route data traffic to any backend server that's reachable from the VCN.
Note  
  
To ensure reachability between the public load balancer and its public IP address based backends, configure a NAT Gateway. See[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)for more information.

A private load balancer requires only one subnet to host the primary load balancer and a standby. The private IP address is local to the subnet. The load balancer is accessible only from within the VCN that contains the associated subnet, or as further restricted by the security list rules. The load balancer can route data traffic to any backend server that's reachable from the VCN.

## Private IP Address Consumption

A public load balancer created in one public regional subnet consumes two private IPv4 addresses from the host subnet. The primary and secondary load balancers reside within the same subnet. Each load balancer requires a private IPv4 address from that subnet. The Load Balancer service assigns a floating public IPv4 address, which doesn't come from the host subnet. If the load balancer is enabled for IPv6, it receives an IPv6 address from the host subnet.

A public load balancer created in two public AD-specific subnets consumes two private IP addresses, one from each host subnet. The primary and secondary load balancers reside within different subnets. Each load balancer requires one private IP address from its host subnet. The Load Balancer service assigns a floating public IPv4 address, which does not come from the host subnets. If the load balancer is enabled for IPv6, it's assigned an IPv6 address from the host subnet.

A private load balancer created in a single subnet consumes three private IP addresses from the host subnet. The primary and secondary load balancers reside within the same subnet. Each load balancer requires a private IP address from that subnet. The floating private IP address also comes from the host subnet. Internet communication with a load balancer enabled for IPv6 and created in a private subnet is prohibited. You can't create a globally routable IPv6-enabled load balancer in a private subnet.
Note  
  
You can't specify the private IP addresses that are used when you create a load balancer. Instead, you're limited to the IP addresses that the load balancer is assigned. After you create the load balancer, the IP address used for client traffic doesn't change. The IP addresses used to communicate with the backend servers might change over the life of the load balancer. To use different IP addresses that are randomly generated, create a new load balancer.

## Configuration Changes and Service Disruption

For a running load balancer, some configuration changes lead to service disruptions. The following guidelines help you understand the effect of changes to your load balancer.
- Operations that add, remove, or modify a backend server create no disruptions to the Load Balancer service.
- Operations that edit an existing health check policy create no disruptions to the Load Balancer service.
- Operations that trigger a load balancer reconfiguration can produce a brief service disruption with the possibility of some terminated connections.

## Proxy Protocol

Load balancers with TCP-based listeners can use the proxy protocol feature to send source and destination IP addresses and ports to their backend servers across layers of network address translation (NAT) or TCP proxies. Use proxy protocol to support network requirements such as application security (IP ACLs) and compliance logging.

When you select the proxy protocol option when creating a load balancer (or updating an existing one), you're prompted to select one of the following options:
- 

Version 1 : Supports a human-readable header (text) format and is typically a single line of a log entry. Use this option for debugging during the early adoption stage when few implementations exist.
- 

Version 2 : Combines support for the human-readable header from Version 1 with a binary encoding of the header for greater efficiency in producing and parsing. Use this option for IPv6 addresses, which are difficult to generate and parse in ASCII form. Version 2 also better supports custom extensions.

Both versions implement the protocol as a parsable header that's placed by the connection initiator at the beginning of each connection. The protocol doesn't expect the sender to wait for the receiver before sending the header. It also doesn't wait for the receiver to send anything back.

Proxy protocol for load balancers only supports the PP2 Type Authority option for Transport Layer Security (TLS) Server Name Indication (SNI) support. This support is useful when the load balancer terminates the SSL connection rather than the backend servers. This functionality is similar to the X-Forwarded-Host option for TCP.

Ensure that your backend applications expect and can parse the Proxy Protocol version 2 header before enabling proxy protocol on your load balancer. To get more information on proxy protocol version 2, go to the[HAProxy](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt)website.

## Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
