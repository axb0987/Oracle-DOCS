# Deleting a Load Balancer Routing Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_routing-policy.htm
- Fetched: 2026-09-05 01:40 CDT

# Deleting a Load Balancer Routing Policy

Remove a routing policy from a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_routing-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_routing-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_routing-policy.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Policies and find the Routing policies section.
- Select the routing policy you want.
- On the routing policy's details page, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci lb routing-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/routing-policy/delete.html)command and required parameters to remove a routing policy from a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteRoutingPolicy](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/RoutingPolicy/DeleteRoutingPolicy)
