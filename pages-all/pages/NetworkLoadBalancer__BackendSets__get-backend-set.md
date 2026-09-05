# Getting a Network Load Balancer Backend Set's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/get-backend-set.htm
- Fetched: 2026-09-05 02:48 CDT

# Getting a Network Load Balancer Backend Set's Details

View the details of a backend set for a network load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/get-backend-set.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/get-backend-set.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/get-backend-set.htm#)
- 

- On the Network load balancers list page, select the network load balancer that you want to work with. If you need help finding the list page or the network load balancer, see[Listing Network Load Balancers](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).
- On the details page, select Backend sets .
All backend sets in the selected network load balancer are displayed in a table.
- Select the backend set.
The details page for the backend set opens and displays information about the backend set. Some items on the page are read-only, and other items enable you to edit and update the backend set's configuration. Access the various resources associated with the backend set by selecting their links or tabs.
- 

Use the[oci nlb backend-set get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/get.html)command and required parameters to get the details of a network load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBackendSet](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/BackendSet/GetBackendSet)
