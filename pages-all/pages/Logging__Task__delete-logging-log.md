# Deleting a Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm
- Fetched: 2026-09-05 02:37 CDT

# Deleting a Log

Delete a log from a log group.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm#)
- 

- On the Logs list page, find the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log.htm).
- From the Actions menu (three dots) for the log group, select Delete .
- When prompted, confirm the deletion.

Note  
  
If you're notified that an agent configuration is associated with the log, you can still delete the log.
- 

Use the[oci logging log delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/delete.html)command and required parameters to delete a log object from a log group:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[DeleteLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/DeleteLog)
