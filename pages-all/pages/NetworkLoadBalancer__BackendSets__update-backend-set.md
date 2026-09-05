# Editing a Network Load Balancer Backend Set
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/update-backend-set.htm
- Fetched: 2026-09-05 02:48 CDT

# Editing a Network Load Balancer Backend Set

Update the configuration of a backend set for a network load balancer.
Note  
  
Changing the load balancing policy of a backend set temporarily interrupts traffic and can drop active connections.
Note  
  
If you selected L3 IP for your listener traffic type, the Preserve Source IP option is automatically enabled. You can't disable it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/update-backend-set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/update-backend-set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/update-backend-set.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- From the Actions menu for the backend set you want, select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Backend Set](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/create-backend-set.htm).

Note  
  
If you selected L3 IP as your listener traffic type for your network load balancer, you can't disable the preserve source ID feature.
- Select Save changes .
- 

Use the[oci nlb backend-set update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/update.html)command and required parameters to edit a network load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateBackendSet](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendSet/UpdateBackendSet)
