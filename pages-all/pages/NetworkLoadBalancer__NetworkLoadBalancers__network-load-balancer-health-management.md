# Health Status for Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-health-management.htm
- Fetched: 2026-09-05 02:48 CDT

# Health Status for Network Load Balancers

Use health status indicators to report on the general health of your network load balancers and their resources.

The Network Load Balancer service provides health status indicators that use your health check policies to report on the general health of your network load balancers and their components. You can see health status indicators in the Oracle Cloud Infrastructure Console for network load balancers, backend sets, and backend servers. You also can use the CLI and API to retrieve this information.

You can perform the following health status management tasks:
- [List the health status summaries for a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer-health.htm)
- [Get a network load balancer's health status details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/get-network-load-balancer-health.htm)

## Network Load Balancer Health Summary

The Oracle Cloud Infrastructure Console list of a network load balancer's backend sets provides health status summaries that indicate the overall health of each backend set. Health status indicators have the following levels:
- OK: All backend servers in the backend set return a status of OK.
- WARNING: Both of the following conditions are true:
- Half or more of the backend set's backend servers return a status of OK.
- At least one backend server returns a status of WARNING, CRITICAL, or UNKNOWN.
- CRITICAL: Fewer than half of the backend set's backend servers return a status of OK.
- UNKNOWN: At least one of the following conditions is true:
- More than half of the backend set's backend servers return a status of UNKNOWN.
- The system could not retrieve metrics for any reason.
- The backend set does not have a listener attached.

For guidance on detecting and correcting common issues, see[Health Check Policies for Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../HealthCheckPolicies/health-check-policy-management.htm).

## Backend Set Health Details

The backend set's Details page provides the same Overall Health status indicator found in the network load balancer's list of backend sets. It also includes counters for the Backend Health status values reported by the backend set's backend servers.

The health status counter badges indicate the following:
- The number of child entities reporting the indicated health status level.
- If a counter corresponds to the overall health, the badge has a fill color.
-
