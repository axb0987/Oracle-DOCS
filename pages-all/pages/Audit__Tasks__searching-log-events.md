# Searching Log Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/searching-log-events.htm
- Fetched: 2026-09-05 01:39 CDT

# Searching Log Events

Use the Console, CLI or API to search for log events.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/searching-log-events.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/searching-log-events.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/searching-log-events.htm#)
- 

Use the following instructions to search log events.

- On the Audit list page, use the Start date box to set the start date and time for the range of results you want to see. Select the arrows on either side of the month to go backward or forward.

If you need help finding the list page, see[Listing Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/listing-log-events.htm).
- (Optional) Specify a time by doing one of the following:

- Select Time and specify an exact start time in thirty-minute increments.
- Type an exact time in the Start date box.

The service uses a 24-hour clock, so you must provide a number between`0`and`23`for the hour. Remember to calculate the offset between Greenwich Mean Time (UTC) and the local time.
- Repeat step 3 and 4 to set an end date and time.

- (Optional) In the Keywords box, type the text you want to find and select Search .

Note  
  
To search for more than one keyword at a time, you can use the[Logging advanced search](https://docs.oracle.com/iaas/Content/Logging/Concepts/searchinglogs.htm#advanced_search_queries)instead.

Tip: To find log events with a specific status code, include quotes (") around the code to avoid results that have those numbers embedded in a longer string.
- (Optional) Under Request action types , specify one or more operations with which to filter results.

- GET
- POST
- PUT
- PATCH
- DELETE

The results are updated to include only log events that were processed within the time range and filters you specified. If an event occurred in the recent past, you must wait to see it in the list. The service typically requires up to 15 minutes for processing.

If the specified time range has more than 100 results for the specified time range, you can select the upper right arrow next to the page number at the bottom of the page to advance to the next page of log events.
Tip  
  
If you get fewer than 100 results on the last page of a results list, you might still have more results, which you can access by select the upper right arrow. If there are more results, Audit prompts you to move forward.

To view all the key-value pairs in a log event, see[Viewing the Details of a Log Event](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/viewing-details-of-log-event.htm).
- 

Use the command and required parameters to list audit event logs:
```

```

`[OPTIONS]`represents the required parameters:
- The OCID of the compartment.
- The start and end time you want to search.

Also, many optional parameters are available. For a complete list of flags and variable options for the Audit service CLI commands, see the[command line reference for Audit](https://docs.oracle.com/iaas/tools/oci-cli/3.54.0/oci_cli_docs/cmdref/audit.html).
- 

Use the API and required parameters to list audit event logs.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following operation to list audit log events:
- [ListEvents](https://docs.oracle.com/iaas/api/#/en/audit/latest/AuditEvent/ListEvents)

Note  
  
This API is not intended for bulk-export operations. For bulk export, see[Bulk Export of Audit Log Events](https://docs.oracle.com/en-us/iaas/Content/Audit/Tasks/../Concepts/bulkexport.htm)
