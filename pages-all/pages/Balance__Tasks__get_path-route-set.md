# Getting a Load Balancer Path Route Set's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_path-route-set.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer Path Route Set's Details

View the details of a path route set for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_path-route-set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_path-route-set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_path-route-set.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select select Policies and find the Path route sets section.
- From the Actions menu for the path route set, select View Details .
The path route set's details page opens and displays information about the path route set. Some items on the page are read-only, and other items enable you to edit and update the path route set's configuration.
- 

Use the[oci lb path-route-set get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/path-route-set/get.html)command and required parameters to get the details of a load balancer's path route set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetPathRouteSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/PathRouteSet/GetPathRouteSet)
