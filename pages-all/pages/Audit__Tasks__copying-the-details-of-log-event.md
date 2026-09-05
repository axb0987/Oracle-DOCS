# Copying the Details of a Log Event
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/copying-the-details-of-log-event.htm
- Fetched: 2026-09-05 01:39 CDT

# Copying the Details of a Log Event

Copy the details of an Audit log event.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/copying-the-details-of-log-event.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/copying-the-details-of-log-event.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/copying-the-details-of-log-event.htm#)
- 

On the Audit list page, you can view the details of a log event.

If you need help finding the list page, see[Listing Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm).
- Select the down arrow on the right side of a log event.
- To copy an entire event :

Select the clipboard icon in the upper right of the log event, above the`eventType`parameter.
- To copy a part of an event :

Select the clipboard icon to the right of the nested parameter or value you want to copy.
Note  
  
The Audit log events copy to the clipboard in JSON format.
- 

This task can't be performed using the CLI.
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following operation to list audit log events:
- [ListEvents](https://docs.oracle.com/iaas/api/#/en/audit/latest/AuditEvent/ListEvents)

Note  
  
This API is not intended for bulk-export operations. For bulk export, see[Bulk Export of Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/../Concepts/bulkexport.htm)
