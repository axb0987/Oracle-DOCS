# Deleting a Load Balancer Path Route Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_path-route-set.htm
- Fetched: 2026-09-05 01:40 CDT

# Deleting a Load Balancer Path Route Set

Remove a path route set from a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_path-route-set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_path-route-set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_path-route-set.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select select Policies and find the Path route sets section.
- From the Actions menu for the path route set, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci lb path-route-set delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/path-route-set/delete.html)command and required parameters to delete a load balancer's path route set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeletePathRouteSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/PathRouteSet/DeletePathRouteSet)
