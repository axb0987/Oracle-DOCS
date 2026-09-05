# Creating a Load Balancer Path Route Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrequest_topic-Creating_Path_Route_Sets.htm
- Fetched: 2026-09-05 01:41 CDT

# Creating a Load Balancer Path Route Set

Create a path route set to apply a set of path routes to a load balancer.

For prerequisite information, see[Path Route Sets for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/path-route-set_management.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrequest_topic-Creating_Path_Route_Sets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrequest_topic-Creating_Path_Route_Sets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrequest_topic-Creating_Path_Route_Sets.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select select Policies and find the Path route sets section.
- Select Create path route set .
- Enter the following information:

- Name : Enter a friendly name for the path route set. The name must be unique, and can't be changed.

The path route set name can't begin with a period and can't contain the characters ; , ? , # , % , / , \ , [ , or ] .
- Path route rules

- Order : If you have several path route rules, you can select the up or down arrows to move the corresponding rule.
Note  
  
The order of the rules within the path route set typically doesn't matter. However, if matching cascades down to prefix or suffix matching, the system chooses the first prefix or suffix rule that matches the incoming URI path.
- Match style : The type of matching to apply to incoming URIs. See[Request Routing for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm)for more information.
- URL string : The path string to match against the incoming URI path, for example`/admin/`.
- Backend set name : The name of the target backend set for requests where the incoming URI matches the specified path.
- Select + Additional rule to create another path route rule. You can have up to 20 path route rules in a set.
- Select X to delete an existing rule.
- Select Submit .
After you create a path route set, the set becomes available for use with the associated load balance. Create or update a listener to apply the path route set.
- 

Use the[oci lb path-route-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/path-route-set/create.html)command and required parameters create a path route set for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePathRouteSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/PathRouteSet/CreatePathRouteSet)
