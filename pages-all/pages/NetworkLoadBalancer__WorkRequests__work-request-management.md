# Work Requests for Network Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/work-request-management.htm
- Fetched: 2026-09-05 02:49 CDT

# Work Requests for Network Load Balancers

Generate information on each network load balancer operation's work requests.

Many of the network load balancer requests don't take effect immediately. In these cases, the request spawns an asynchronous workflow for fulfillment.

To provide visibility for in-progress workflows, the network load balancer creates a work request object. Because some operations depend on the completion of other operations, you must monitor each operation's work request and confirm it has succeeded before proceeding to the next operation. For example, to create a backend set and add a backend server to the new set, you first must create the backend set. After that operation completes, you can add the backend server.

If you try to add a backend server before the backend set creation completes, the system can't ensure that the request to add the server succeeds. You can monitor the request to add a backend set to decide when that workflow is complete, and then add the backend server.

You can perform the following work request management tasks:

[List the work requests for a network load balancer.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request.htm)

[Get a work request's details.](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/get-work-request.htm)

[List work request errors](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request-error.htm)

[List work request logs](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/WorkRequests/list-work-request-log.htm)

## Work Request States

The work request states are:

Work Request States
State Description
ACCEPTED The request is in the work request queue to be processed.
IN PROGRESS A work request record exists for the specified request, but no associated WORK_COMPLETED record is present.
SUCCEEDED A work request record exists for this request and an associated WORK_COMPLETED record has the state SUCCEEDED.
FAILED A work request record exists for this request and an associated WORK_COMPLETED record has the state FAILED.
Note  
  
The network load balancer doesn't use the common[Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
