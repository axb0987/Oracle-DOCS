# Moving a Load Balancer to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Moving_a_Load_Balancer_to_a_Different_Compartment.htm
- Fetched: 2026-09-05 01:41 CDT

# Moving a Load Balancer to a Different Compartment

Move a load balancer to a different compartment in your Oracle Cloud Infrastructure tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Moving_a_Load_Balancer_to_a_Different_Compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Moving_a_Load_Balancer_to_a_Different_Compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Moving_a_Load_Balancer_to_a_Different_Compartment.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- To view the load balancers in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the Actions menu for the load balancer, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci lb load-balancer change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/change-compartment.html)command and required parameters to move a load balancer to a different compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeLoadBalancerCompartment](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/ChangeLoadBalancerCompartment)
