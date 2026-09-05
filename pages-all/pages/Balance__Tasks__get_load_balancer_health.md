# Getting a Load Balancer's Health Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer_health.htm
- Fetched: 2026-09-05 01:40 CDT

# Getting a Load Balancer's Health Details

View the health status details for a load balancer.

The following table lists the health status indicators and their meanings.

Level

Color

Description

Critical

Red

At least one backend set associated with the load balancer returns a status of Critical .

Warning

Yellow

All the following conditions are true:
- 

At least one backend set associated with the load balancer returns a status of Warning or Pending .
- 

No backend sets return a status of Critical .
- 

The load balancer life-cycle state is Active .

Incomplete

Yellow

Any one of the following conditions is true:
- 

No backend sets are defined for the load balancer.
- 

All the following conditions are true:
- 

More than half of the backend sets associated with the load balancer return a status of Incomplete .
- 

None of the backend sets return a status of Warning or Critical .
- 

The load balancer life-cycle state is Active .

Pending

Yellow

Any one of the following conditions is true:
- 

The load balancer life-cycle state is not Active .
- 

All the following conditions are true:
- 

More than half of the backend sets associated with the load balancer return a status of Pending .
- 

None of the backend sets return a status of Warning or Critical .
- 

The load balancer life-cycle state is Active .
- The system could not retrieve metrics for any reason.

OK

Green

All backend sets associated with the load balancer return a status of OK .

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer_health.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer_health.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer_health.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, view the Overall health and Backend sets health indicators.
- 

Use the[oci lb load-balancer-health get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer-health/get.html)command and required parameters to view the health details for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetLoadBalancerHealth](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancerHealth/GetLoadBalancerHealth)
