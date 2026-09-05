# Updating Network Load Balancer Network Security Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer-security.htm
- Fetched: 2026-09-05 02:49 CDT

# Updating Network Load Balancer Network Security Groups

Update the network security groups' configuration for a network load balancer.

See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for information on this feature.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer-security.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer-security.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/update-network-load-balancer-security.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Edit next to Network security groups .
- Select an NSG from the list to use with your network load balancer. Select Change compartment to select an NSG from a different compartment than the one indicated.
- Select +Add another security group to add another NSG to the list.
- Select Submit .
- 

Use the[oci nlb network-load-balancer update-network-security-groups](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/update-network-security-groups.html)command and required parameters to update a network load balancer's security groups:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateNetworkSecurityGroups](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/UpdateNetworkSecurityGroups)operation to update the network security groups for a network load balancer. See[UpdateNetworkSecurityGroups](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/UpdateNetworkSecurityGroups)
