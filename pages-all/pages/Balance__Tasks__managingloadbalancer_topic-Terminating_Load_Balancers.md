# Terminating a Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Terminating_Load_Balancers.htm
- Fetched: 2026-09-05 01:41 CDT

# Terminating a Load Balancer

Remove a load balancer from your Oracle Cloud Infrastructure tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Terminating_Load_Balancers.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Terminating_Load_Balancers.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Terminating_Load_Balancers.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- From the Actions menu for the load balancer, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[oci lb load-balancer delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/delete.html)command and required parameters to remove a load balancer from your tenancy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[`DeleteLoadBalancer`](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/DeleteLoadBalancer)
