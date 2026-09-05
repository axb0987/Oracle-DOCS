# Viewing Audit Log Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewinglogevents.htm
- Fetched: 2026-09-05 01:39 CDT

# Viewing Audit Log Events

Describes how to view Audit log events.

Audit provides records of API operations performed against supported services as a list of log events. The service logs events at both the tenant and compartment level.

When viewing events logged by Audit, you might be interested in specific activities that happened in the tenancy or compartment and who was responsible for the activity. You will need to know the approximate time and date something happened and the compartment in which it happened to display a list of log events that includes the activity in question. List log events by specifying a time range on the 24-hour clock in Greenwich Mean Time (GMT), calculating the offset for your local time zone, as appropriate. New activity is appended to the existing list, usually within 15 minutes of the API call, though processing time can vary.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The following policy statement gives the specified group (Auditors) the ability to view all the Audit event logs in the tenancy:
```

```

To give the group access to the Audit event logs in a specific compartment only (ProjectA), write a policy like the following:
```

```

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for the Audit, see[Details for the Audit Service](https://docs.oracle.com/iaas/Content/Identity/Reference/auditpolicyreference.htm).

## Searching and Filtering in the Console

When you navigate to Audit in the Console, a list of results is generated for the current compartment. Audit logs are organized by compartment, so if you're looking for a particular event, you must know which compartment the event occurred in. You can filter the list in all the following ways:
- Date and time
- Request Action Types (operations)
- Keywords

For example, users begin to report that their try to sign in are failing. You want to use Audit to research the problem. Adjust the date and time to search for corresponding failures during a window of time that starts a little before the events were reported. Look for corresponding failures and similar operations preceding the failures to correlate a reason for the failures.
Note  
  
The service logs events at the time they're processed. There can be a delay between the time an operation occurs and when it's processed.

You can filter results by request actions to zero in on only the events with operations that interest you. For example, say that you only want to know about instances that were deleted during a specific time frame. Select a delete request action filter to see only the events with delete operations.

You can also filter by keywords. Keyword filters are powerful when combined with the values from audit event fields. For example, say that you know the username of an account and want a list of all activity by that account in a particular time frame. Do a search using the username as a keyword filter.

Every audit event contains the same fields, so search for values from those fields. To get a better understanding of what values are available, see[Contents of an Audit Log Event](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/../Reference/logeventreference.htm)
