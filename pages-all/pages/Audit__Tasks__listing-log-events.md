# Listing Audit Log Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm
- Fetched: 2026-09-05 01:39 CDT

# Listing Audit Log Events

Get a list of the Audit events in a Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm#)
- 

- 

Open the navigation menu , select Observability &amp; Management , and then from Logging select Audit .

The Audit list page opens. All existing events that occurred in the selected compartment are displayed in a list table.
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.
Note  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
Optionally, you can do the following with an event from the Audit list.
- [Searching Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/searching-log-events.htm)
- [Copying the Details of a Log Event](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/copying-the-details-of-log-event.htm)
- [Viewing the Details of a Log Event](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewing-details-of-log-event.htm)
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
Note  
  
This API isn't intended for bulk-export operations. For bulk export, see[Bulk Export of Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/../Concepts/bulkexport.htm).

Use the following operation to list audit log events:[ListEvents](https://docs.oracle.com/iaas/api/#/en/audit/latest/AuditEvent/ListEvents)
