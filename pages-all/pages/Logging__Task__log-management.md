# Log Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/log-management.htm
- Fetched: 2026-09-05 02:38 CDT

# Log Management

Learn about how to create and manage logs.
You can perform the following log management tasks:
- 

[Creating a Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log.htm)
- 

[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm)
- 

[Getting a Log's Details](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm)
- 

[Editing a Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log.htm)
- 

[Moving a Log Between Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-log-group-logging-log.htm)
- 

[Deleting a Log](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm)

The Console Logs page lists both[custom logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/custom_logs.htm)and[service logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/service_logs.htm)(indicated by the Log type field). The page is organized in terms of the following fields:
- Log name
- Log type
- Status
- Details
- Created

From this page you can click the Log name entry to go to the log details page, or click the linked resource in Details to go directly to the resource. For example, if the log is for the Load Balancer service, clicking the link opens the load balancer details page. From the Actions menu (three dots) , you can edit the log, disable logging, change the log group, view tags, or delete the log.

[To enable or disable an existing log](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/log-management.htm#)

- On the Logs list page, select the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log.htm).

The log's details page opens
- Select Disable Log / Enable Log . A confirmation dialog is displayed regarding the disabling or enabling of the log.
- Confirm by selecting Disable Log / Enable Log . The log detail page changes its status and displays Inactive (for a disabled log) or Active (for an enabled log) in the status field, both on the log detail page and the Logs page.
