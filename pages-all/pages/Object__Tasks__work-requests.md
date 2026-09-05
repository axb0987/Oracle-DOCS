# Object Storage Work Requests
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/work-requests.htm
- Fetched: 2026-09-05 02:52 CDT

# Object Storage Work Requests

View the state of work requests associated with Object Storage.

The Object Storage service handles work requests asynchronously. The service creates a queue for work requests and then processes the requests when system resources become available. To provide visibility for in-progress operations, Object Storage creates a[work request](https://docs.oracle.com/iaas/Content/API/Concepts/workrequests.htm). You can track the progress of the operation by monitoring the status of the work request.

You can perform the following Object Storage work request management tasks:

[List the work requests for a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm).

[Get the details of a work request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm).

[List the errors for a work request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-error.htm).

[List the logs for a work request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-log-entry.htm).

[Cancel a work request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/cancel-work-request.htm).

## Work Request Status Descriptions

You can view the status of a work request in the following locations:
- The Work request list. See[Listing Work Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm)for more information.
- The work request's Details page. See[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm)for more information.

Monitor these locations to get the updated status of a work request.

The following table lists and describes the work request status levels:

Work Request Status Indicators
Status Description
Accepted The request is in the work request queue to be processed.
In Progress A work request record exists for the specified request, but no associated WORK_COMPLETED record exists.
Completed A work request record exists for this request and an associated WORK_COMPLETED record has the state Completed .
Canceling The work request is in the process of being canceled.
Canceled The work request has been canceled.
Failed A work request record exists for this request and an associated WORK_COMPLETED record has the state Failed .

Check the Error Details column for more information on the reason for the fail. For example:

`All five non-reserved IP addresses of the subnet_CIDR for ocid have already been allocated.`

To learn more about why a work request failed, see[Lising a Work Request's Errors](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-error.htm)
