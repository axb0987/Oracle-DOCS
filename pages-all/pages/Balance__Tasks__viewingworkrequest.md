# Work Requests for Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/viewingworkrequest.htm
- Fetched: 2026-09-05 01:42 CDT

# Work Requests for Load Balancer

Generate information on each load balancer operation's work requests.
Note  
  
The Load Balancer service doesn't use the common[Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)to support work request operations. Instead, the Load Balancer API supports Load Balancer work requests. See[Using the Console to View Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr)for information on viewing work requests for other services.

You can perform the following work request management tasks:

[List the work requests for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-work-request.htm)

[Get a work request's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_work_request.htm)

## Work Request Status Descriptions

Learn about the various statuses applicable for a load balancer's work requests.

Many of the Oracle Cloud Infrastructure Load Balancer service requests do not take effect immediately. In these cases, the request spawns an asynchronous workflow for fulfillment. To provide visibility for in-progress workflows, the Load Balancer service creates a work request object.

Because some operations depend on the completion of other operations, you must monitor each operation's work request and confirm it has succeeded before proceeding to the next operation. For example, to create a backend set and add a backend server to the new set, you first must create the backend set. After that operation completes, you can add the backend server. If you try to add a backend server before the backend set creation completes, the system can't ensure that the request to add the server succeeds.

You can monitor the request to add a backend set to determine when that workflow is complete, and then add the backend server.

The following table lists the work request states:

Work Request States
Status Description
Accepted The request is in the work request queue to be processed.
In Progress A work request record exists for the specified request, but no associated WORK_COMPLETED record exists.
Succeeded A work request record exists for this request and an associated WORK_COMPLETED record has the state Succeeded .
Failed A work request record exists for this request and an associated WORK_COMPLETED record has the state Failed .

Check the Error Details column for more information on the reason for the fail. For example:

`All five non-reserved IP addresses of the subnet_CIDR for ocid have already been allocated.`
