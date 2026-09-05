# Editing a Load Balancer Routing Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_routing-policy.htm
- Fetched: 2026-09-05 01:42 CDT

# Editing a Load Balancer Routing Policy

Update a routing policy for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_routing-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_routing-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_routing-policy.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Policies and find the Routing policies section.
- Select the routing policy you want.
- On the routing policy's details page, select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Routing Policy](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_routing-policy.htm).
- Select Save changes .
- 

Use the[oci lb routing-policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/routing-policy/update.html)command and required parameters to update a routing policy for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateRoutingPolicy](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/RoutingPolicy/UpdateRoutingPolicy)
