# Backend Sets for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets.htm
- Fetched: 2026-09-05 01:41 CDT

# Backend Sets for Load Balancers

Use backend sets to create logical entities consisting of a load balancing policy, health check policy, and a list of backend servers for a load balancer.

A backend set is a logical entity defined by a load balancing policy, a health check policy, and a list of backend servers. To create a backend set, you must specify a load balancing policy and health check script, and then add a list of backend servers (compute instances). SSL (HTTPS) and session persistence configuration is optional. A backend set must be associated with one or more listeners for the load balancer to work.

For information on how many backend sets you can have with a load balancer, see[Limits on Load Balancing Resources](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Concepts/balanceoverview.htm#limits-resources).

Changing the load balancing policy of a backend set temporarily interrupts traffic and can drop active connections.

Select Backend Sets under Resources in the load balancer's Details page to display the Backend sets page. This page contains a button for creating new backend sets.
Note  
  
You can set up backend servers as compute instance pools. See[Creating Instance Pools](https://docs.oracle.com/iaas/Content/Compute/Tasks/creatinginstancepool.htm)for more information.

You can perform the following backend set management tasks:

[List the backend sets in a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-backend-set.htm)

[Create a new backend set under a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm)

[Get a backend set's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend_set.htm)

[Edit a backend set's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Editing_Backend_Sets.htm)

[Get a backend set's health details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-set-health.htm)

[Delete a backend set from a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Deleting_Backend_Sets.htm)
