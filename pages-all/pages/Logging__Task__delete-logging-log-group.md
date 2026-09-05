# Deleting a Log Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log-group.htm
- Fetched: 2026-09-05 02:37 CDT

# Deleting a Log Group

Delete a log group from a compartment.

Note  
  
You can't move, edit, or delete the default log group. You can't delete a log group that contains logs. Either[delete the logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log.htm)first or[move them to another log group](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-log-group-logging-log.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-log-group.htm#)
- 

- On the Log groups list page, find the log group that you want to work with. If you need help finding the list page or the log group, see[Listing Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log-group.htm).
- From the Actions menu (three dots) for the log group, select Delete .
- When prompted, confirm the deletion.
- 

Use the oci logging log-group delete command and required parameters to delete a log group:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[DeleteLogGroup](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogGroup/DeleteLogGroup)
