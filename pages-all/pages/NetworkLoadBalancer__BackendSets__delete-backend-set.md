# Deleting a Network Load Balancer Backend Set
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/delete-backend-set.htm
- Fetched: 2026-09-05 02:48 CDT

# Deleting a Network Load Balancer Backend Set

Remove a backend set from a network load balancer.
Note  
  

You cannot delete a backend set used by an active listener.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/delete-backend-set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/delete-backend-set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/delete-backend-set.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- From the Actions menu for the backend set you want, select Delete .
- When prompted, confirm the deletion.
The backend set you removed no longer appears in the backend set list.
- 

Use the[oci nlb backend-set delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/delete.html)command and required parameters to delete a network load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteBackendSet](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendSet/DeleteBackendSet)
