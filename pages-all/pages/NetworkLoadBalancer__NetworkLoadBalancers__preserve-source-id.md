# Enabling Network Load Balancer Source/Destination Preservation
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm
- Fetched: 2026-09-05 02:49 CDT

# Enabling Network Load Balancer Source/Destination Preservation

Configure your private IP address network load balancer so that the original source and destination header (IP addresses and ports) of each incoming packet is preserved all the way to the backend server.

You can configure the network load balancer so that the original source and destination IP addresses and ports contained in the header of each incoming packet are preserved all the way to the backend server. The network load balancer doesn't change packet characteristics. The source and destination IP header information is identical when viewed at the network load balancer or a backend server. No network address translation (NAT) occurs.
Note  
  
Source/destination is only available for network load balancers using private IP addresses. If source/destination preservation is enabled, the Network Load Balancer service doesn't support users selecting the backend servers using their IP address.

Use network load balancer source/destination IP header preservation to operate in a bump-in-the-wire kind of mode to scale your network virtual appliances (NVAs) such as firewalls and software-defined wide area networks (SD-WANs).

Configure the network load balancer as a route target (private IP next hop following the route rule on the internet gateway (IGW)/dynamic route gateway (DRG) route table). Incoming traffic isn't directed to the network load balancer virtual IP but instead is directed to the actual server.

The following illustration shows how the East to West traffic flows between application subnets works:  
  

The following illustration shows how the North to South traffic flows between application subnets works:
  
  

Note  
  

- The source/destination preservation feature is only available on the private network load balancers.
- Enabling this feature doesn't change the source and destination addresses of connections between the network load balancer and the backend sets. Update the VCN route tables applied to relevant subnets to ensure traffic is routed correctly for the preserved source and destination addresses. See[VCN Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm)for more information.

These instructions are for enabling the source/destination preservation feature in an existing network load balancer. You can enable this feature when you first create the network load balancer. See[Creating a Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm)for more information.

## Symmetric Hashing

When you enable source/destination preservation in a network load balancer, either when creating a new network load balancer or updating an existing one, you also have the option to enable symmetric hashing. The network load balancer uses symmetric hashing to calculate the same hash for packets belonging to the same flow in both forward and return directions.

The hash doesn't change when the source IP address:port value is exchanged with the destination IP address:port value. Enable symmetric hashing when you want to inspect both forward and return traffic with the same firewall appliance that's hosted as a backend on the network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Edit preservation .
- Select Preserve source/destination header (IP, Port) to enable this feature.
- Select Save changes .
- 

Use the`--is-preserve-source true`option when running the[oci nlb network-load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/create.html)or[oci network-load-balancer update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/update.html)commands to create or update a network load balancer's preservation:

```

```

or

```

```

When enabled,`skipSourceDestinationCheck`is automatically turned on the network load balancer VNIC, and packets are sent to the backend with the entire IP header intact.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Include the`isPreserveSourceDestination=true`option when creating or updating the network load balancer. When enabled,`skipSourceDestinationCheck`parameter is automatically turned on the load balancer VNIC, and packets are sent to the backend server with the entire IP header intact.

For more information, see[CreateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/CreateNetworkLoadBalancer)or[UpdateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/UpdateNetworkLoadBalancer)
