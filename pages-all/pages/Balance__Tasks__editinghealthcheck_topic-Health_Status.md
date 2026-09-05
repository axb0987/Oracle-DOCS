# Health Status Indicators for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/editinghealthcheck_topic-Health_Status.htm
- Fetched: 2026-09-05 01:40 CDT

# Health Status Indicators for Load Balancers

Learn about the health status indicators for a load balancer.

The Load Balancer service provides health status indicators that use your health check policies to report on the general health of your load balancers and their components.

The following table provides the general meaning of each level:

Level Color Description
Critical Red Some or all reporting entities require immediate attention.

The resource isn't functioning or unexpected failure is imminent.
Warning Yellow Some reporting entities require attention.

The resource isn't functioning at peak efficiency or the resource is incomplete and requires further work.
Incomplete Yellow The load balancer doesn't have any backend sets configured or backend sets exist that contain no attached backend servers.
Pending Yellow The health status can't be determined.

The resource isn't responding or is in transition and might resolve to another status over time.

OK

Green

No attention required.

The resource is functioning as expected.

The precise meaning of each level differs among the following components:
- [Load balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_load_balancer_health.htm)
- [Backend sets](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-set-health.htm)
- [Backend servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_backend-server-health.htm)
