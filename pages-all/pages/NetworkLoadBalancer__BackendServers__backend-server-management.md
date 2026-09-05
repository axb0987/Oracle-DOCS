# Backend Servers for Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/backend-server-management.htm
- Fetched: 2026-09-05 02:48 CDT

# Backend Servers for Network Load Balancers

Manage the backend servers that receive incoming traffic based on the policies you specified for the backend set that contains it for the network load balancer.

When you create a network load balancer, you must specify the backend servers (compute instances ) to include in each backend set . The network load balancer routes incoming traffic to these backend servers based on the policies you specified for the backend set. You can use the Console to add and remove backend servers in a backend set.

You can perform the following backend server management tasks:

[List of the backend servers within a backend set.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/list-backend-server.htm)

[Add a backend server to the backend set.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/create-backend-server.htm)

[Get a backend server's details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server.htm)

[Edit a backend server's settings.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/update-backend-server.htm)

[Get the health details of a backend server.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/get-backend-server-health.htm)

[Delete a backend server from a backend set.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/delete-backend-server.htm)

## Traffic Routing

To route traffic to a backend server, the Load Balancer service requires the IP address of the compute instance and the relevant application port. If the backend server resides within the same VCN as the load balancer, Oracle recommends that you specify the compute instance's private IP address. You also must ensure that the VCN's security rules allow Internet traffic.
Note  
  

- You can't add backend servers using public IPs.
- You can't place backend servers behind an internet gateway.

When you add backend servers to a backend set, you specify either the instance OCID or an IP address for the server to add. An instance with several VNICs attached can have several IP addresses pointing to it.
- If you identify a backend server by OCID, the Load Balancer service uses the primary VNIC's primary private IP address.
- If you identify the backend servers to add to a backend set by their IP addresses, you can point to the same instance more than one time.

To enable backend traffic, your backend server subnets must have appropriate ingress and egress security rules. When you add backend servers to a backend set, you can specify the applicable network security groups (NSGs). If you prefer to use security lists for your VCN, the Load Balancer service Console can suggest security list rules for you. You also can configure them yourself through the Networking service. See[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)for more information.
Tip  
  
To accommodate high-volume traffic, we recommend that you use stateless security rules for your load balancer subnets. For more information, see[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful).

You can add and remove backend servers without disrupting traffic.

## Backend Servers in Non-Preemptive Backend Sets

You can only assign two backend servers to a non-preemptive backend set. You have the option of specifying one of those backend servers as a backup. If the active backend server is down because of an issue or routine maintenance, the backup backend server takes over.

When you add the first backend server to a non-preemptive backend set, by default it's configured as the active backend set. If you add a second backend server, you can specify either backend server as a backup. You can't have more than one backend server configured as a backup.

You can't edit a backend server that's part of a non-preemptive mode backend server.

For more information on backend sets, see[Backend Sets](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendServers/../BackendSets/backend-set-management.htm)
