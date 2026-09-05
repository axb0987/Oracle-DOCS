# Viewing the Details of a Log Event
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewing-details-of-log-event.htm
- Fetched: 2026-09-05 01:39 CDT

# Viewing the Details of a Log Event

View the details of an Audit log event.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewing-details-of-log-event.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewing-details-of-log-event.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewing-details-of-log-event.htm#)
- 

- On the Audit list page, you can view the details of a log event.

If you need help finding the list page, see[Listing Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm).
- To see only the top-level details :

Select the down arrow on the right side of an event
- To see lower-level details :

Select the plus sign ( + ) on the left side of the collapsed parameter
- 

Use the command and required parameters to list audit event logs:
```

```

`[OPTIONS]`represents the required parameters:
- The OCID of the compartment.
- The start and end time you want to search.

Also, many optional parameters are available. For a complete list of flags and variable options for the Audit service CLI commands, see the[command line reference for Audit](https://docs.oracle.com/iaas/tools/oci-cli/3.54.0/oci_cli_docs/cmdref/audit.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following operation to list audit log events:
- [ListEvents](https://docs.oracle.com/iaas/api/#/en/audit/latest/AuditEvent/ListEvents)

Note  
  
This API is not intended for bulk-export operations. For bulk export, see[Bulk Export of Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/../Concepts/bulkexport.htm)
