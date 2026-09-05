# Moving a Network Load Balancer to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/change-compartment-network-load-balancer.htm
- Fetched: 2026-09-05 02:48 CDT

# Moving a Network Load Balancer to a Different Compartment

Move a network load balancer to a different compartment in your Oracle Cloud Infrastructure tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/change-compartment-network-load-balancer.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/change-compartment-network-load-balancer.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/change-compartment-network-load-balancer.htm#)
- 

- On the Network load balancers list page, find the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- To view the network load balancers in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the Actions menu (three dots) for the network load balancer, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci network-load-balancer nlb change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/change-compartment.html)command and required parameters to move a network load balancer between compartments:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeNetworkLoadBalancerCompartment](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/ChangeNetworkLoadBalancerCompartment)
