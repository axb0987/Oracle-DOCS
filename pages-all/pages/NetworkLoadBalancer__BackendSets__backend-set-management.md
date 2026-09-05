# Backend Sets for Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/backend-set-management.htm
- Fetched: 2026-09-05 02:48 CDT

# Backend Sets for Network Load Balancers

Use backend sets to create logical entities consisting of a network load balancing policy, health check policy, and a list of backend servers for a network load balancer.

A backend set is a logical entity defined by a load balancing policy, a health check policy, and a list of backend servers. To create a backend set, you must specify a load balancing policy and health check script, and then add a list of backend servers (compute instances). A backend set must be associated with a single listener for the network load balancer to work.

You can perform the following backend set management tasks:

[List the backend sets in a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/list-backend-set.htm)

[Create a new backend set under a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/create-backend-set.htm)

[Get a backend set's details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/get-backend-set.htm)

[Edit a backend set's settings.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/update-backend-set.htm)

[Enable source preservation in a backend set.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/preserve-backend-set-source-id.htm)

[Get a backend set's health details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/get-backend-set-health.htm)

[Delete a backend set from a nework load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/BackendSets/delete-backend-set.htm)

## Types of Backend Sets

You're prompted to specify the type of mode for a backend set is when you create it. You can configure a backend set as being either Default or Non-preemption mode.

### Default Mode

A Default mode backend set contains an unlimited number of backend servers.

### Non-Preemption Mode

A Non-preemption mode backend set only has a maximum of two backend servers. You can configure one of the two backend servers as a backup. If the active backend server is unavailable because of an issue or routine maintenance, the backup takes over.

When you view details of a non-preemptive mode backend set, both the Configured State and Operational State status are displayed. The Configured State reflects how the backend server is configured (default or non-preemptive). The Operational State reflects the actual operational functionality at that moment. If a non-preemption backup backend server is active because the usual active backend server is down, then that backup backend server has an Operational Statue as Active .
