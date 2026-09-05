# Load Balancer Types
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/load_balancer_types.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Types

Learn about the different types of load balancers that you can create within your VCN.

The Load Balancer service enables you to create a public or private load balancer within your VCN. A public load balancer has a public IP address that's accessible from the internet. A private load balancer has an IP address from the hosting subnet, which is visible only within your VCN. You can configure several listeners for an IP address to load balance transport Layer 4 and Layer 7 (TCP and HTTP) traffic. Both public and private load balancers act as reverse proxies and can route data traffic to any backend server that's reachable from the VCN.

## Public Load Balancers

To accept traffic from the internet, you create a public load balancer. The service assigns it a public IP address that serves as the entry point for incoming traffic. You can associate the public IP address with a friendly DNS name through any DNS vendor.

A public load balancer is regional in scope. If your region includes several availability domains, a public load balancer requires either a regional subnet (recommended) or two availability domain-specific (AD-specific) subnets, each in a separate availability domain. With a regional subnet, the Load Balancer service creates a primary load balancer and a standby load balancer, each in a different availability domain, to ensure accessibility even during an availability domain outage. If you create a load balancer in two AD-specific subnets, one subnet hosts the primary load balancer and the other hosts a standby load balancer. If the primary load balancer fails, the public IP address switches to the secondary load balancer. The service treats the two load balancers as equal and you can't specify which one is primary.

Whether you use regional or AD-specific subnets, each load balancer requires one private IP address from its host subnet. The Load Balancer service supplies a floating public IP address to the primary load balancer. The floating public IP address does not come from your backend subnets.

If your region includes only one availability domain, the service requires just one subnet, either regional or AD-specific, to host both the primary and standby load balancers. The primary and standby load balancers each requires a private IP address from the host subnet, in addition to the assigned floating public IP address. If an availability domain outage occurs, the load balancer has no failover.
Note  
  

- You can't specify a private subnet for your public load balancer.
- To ensure reachability between the public load balancer and its public IP address based backends, configure a NAT Gateway. See[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)for more information.

## Private Load Balancers

To isolate your load balancer from the internet and simplify your security posture, you can create a private load balancer. The Load Balancer service assigns it a private IP address that serves as the entry point for incoming traffic.

When you create a private load balancer, the service requires only one subnet to host both the primary and standby load balancers. The load balancer can be regional or AD-specific, depending on the scope of the host subnet. The load balancer is accessible only from within the VCN that contains the host subnet, or as further restricted by your security rules.

The assigned floating private IP address is local to the host subnet. The primary and standby load balancers each requires an extra private IP address from the host subnet.

If an availability domain outage occurs, a private load balancer created in a regional subnet within a multi-AD region provides failover capability. A private load balancer created in an AD-specific subnet, or in a regional subnet within a single availability domain region, has no failover capability in response to an availability domain outage.

## All Load Balancers

Your load balancer has a backend set to route incoming traffic to your compute instances. The backend set is a logical entity that includes:
- A list of backend servers.
- A load balancing policy.
- A health check policy.
- Optional SSL handling.
- Optional session persistence configuration.

The backend servers (compute instances) associated with a backend set can exist anywhere, as long as the associated network security groups (NSGs), security lists, and route tables allow the intended traffic flow.

If your VCN uses network security groups (NSGs), you can associate your load balancer with an NSG. An NSG has a set of security rules that controls allowed types of inbound and outbound traffic. The rules apply only to the resources in the group. Contrast NSGs with a security list, where the rules apply to all the resources in any subnet that uses the list. For more information about NSGs, see[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).

If you prefer to use security lists for your VCN, the Load Balancer service can suggest appropriate security list rules. You also can configure them yourself through the Networking service. See[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)for more information.

See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)for detailed information comparing NSGs and security lists.

We recommend that you create your load balancer in a regional subnet.

We a recommend that you distribute your backend servers across all availability domains within the region.

To create a minimal system with a functioning load balancer, you must:
- For a public load balancer, create a VCN with an internet gateway and a public regional subnet.

Note  
  
You can't specify a private subnet for your public load balancer.
- For a private load balancer, create a VCN with at least one private subnet.
- Create at least two compute instances, each in a separate availability domain.
- Create a load balancer.
- Create a backend set with a health check policy.
- Add backend servers (compute instances) to the backend set.
- Create a listener, with optional SSL handling.
- Update the load balancer subnet security rules so they allow the intended traffic.

## Load Balancer Reachability
