# Backend Servers for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendservers.htm
- Fetched: 2026-09-05 01:41 CDT

# Backend Servers for Load Balancers

Manage backend servers for use with a load balancer.

When you create a load balancer, you must specify the backend servers (Compute instances ) to include in each backend set . The load balancer routes incoming traffic to these backend servers based on the policies you specified for the backend set. You can use the Console to add and remove backend servers in a backend set.
Note  
  
Selection of a backend server's transport protocol (HTTP, HTTPS (using SSL), and TCP) is configured in the backend set. See[Backend Sets for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets.htm)for more information.

You can perform the following backend server management tasks:

[List of the backend servers within a backend set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-backend-server.htm).

[Add a backend server to the load balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_backend_server.htm).

[Get a backend server's details](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_server.htm).

[Edit a backend server's settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_backend_server.htm).

[Get the health details of a backend server](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-server-health.htm).

[Delete a backend server from a backend set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_backend_server.htm).

## Traffic Routing

To route traffic to a backend server, the Load Balancer service requires the IP address of the compute instance and the relevant application port. If the backend server resides within the same VCN as the load balancer, we recommend that you specify the compute instance's private IP address. If the backend server resides within a different VCN that's not peered with this VCN, you must specify the public IP address of the compute instance. If the backend server resides in a peered VCN, we recommend that you specify the private IP of the compute instance. You also must ensure that the VCN's security rules allow internet traffic.

When you add backend servers to a backend set, you specify either the instance OCID or an IP address for the server to add. An instance with multiple VNICs attached can have multiple IP addresses pointing to it. Note the following:
- If you identify a backend server by OCID, the load balancer uses the primary VNIC's primary private IP address.
- If you identify the backend servers to add to a backend set by their IP addresses, it's possible to point to the same instance more than once.

To enable backend traffic, your backend server subnets must have appropriate ingress and egress security rules. When you add backend servers to a backend set, you can specify the applicable network security groups (NSGs). If you prefer to use security lists for your VCN, the Load Balancer service Console can suggest security list rules for you. You also can configure them yourself through the Networking service. See[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm)for more information.
Note  
  
To accommodate high-volume traffic, we strongly recommends that you use stateless security rules for your load balancer subnets. See[Stateful Versus Stateless Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#stateful)for more information.

You can add and remove backend servers without disrupting traffic.

## Using Backend Servers with Public IP Addresses

If your backend servers have public IP addresses, configure a NAT gateway by adding route rules for connecting your public load balancer to its public IP address-based backend servers. See[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)for more information. Refer to the FAQ entry on adding route rules in[Flexible Load Balancing FAQ](https://www.oracle.com/cloud/networking/load-balancing/faq/)
