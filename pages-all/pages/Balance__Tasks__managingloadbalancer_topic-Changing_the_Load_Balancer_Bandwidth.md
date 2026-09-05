# Changing a Load Balancer's Bandwidth Shape
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm
- Fetched: 2026-09-05 01:41 CDT

# Changing a Load Balancer's Bandwidth Shape

Update a load balancer to use a different bandwidth shape.

If you're not an Always Free user, you can adjust the size of the bandwidth to one of the other predefined sizes.
Note  
  

Always Free users can't change the bandwidth of a load balancer. Upgrade to a different account to increase your bandwidth size.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Update shape .
The Update shape dialog box opens. The options displayed vary on what type of existing bandwidth size option you're using.
- Changing a flexible shape: Enter the values for the Minimum bandwidth and Maximum bandwidth shape sizes you want changed.
Note  
  
Using flexible bandwidth shapes for Government accounts can result in overages if the pre-paid shape sizes are exceeded.

To specify a dynamic shape size, for example 500 Mbps, set the minimum and maximum sliders to the same value.
- Changing a dynamic shape: Select the new bandwidth of the load balancer from the Choose shape size list. The existing bandwidth size of the load balancer is unavailable to select.

You can switch from a dynamic shape size to a flexible shape by checking the Use a flexible load balancer option and specifying your shape size using the minimum and maximum sliders.
Note  
  
After you have switched to a flexible shape, you can't revert to a dynamic shape.
- Select Save changes . Changing the bandwidth size of the load balancer requires resetting all existing sessions of the load balancer.
- Select Confirm to continue.
- 

Use the[oci lb load-balancer update-load-balancer-shape](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/update-load-balancer-shape.html)command and required parameters to change a load balancer's bandwidth shape:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateLoadBalancerShape](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/UpdateLoadBalancerShape)
