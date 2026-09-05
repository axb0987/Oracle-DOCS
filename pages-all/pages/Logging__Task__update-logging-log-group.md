# Editing a Log Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log-group.htm
- Fetched: 2026-09-05 02:38 CDT

# Editing a Log Group

Update a log group's configuration.

Note  
  
You can't move, edit, or delete the default log group.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log-group.htm#)
- 

- On the Log groups list page, find the log group that you want to work with. If you need help finding the list page or the log group, see[Listing Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log-group.htm).
- From the Actions menu (three dots) for the log group, select Edit .
The Edit log group panel opens. You can change the log group name and its description in the associated fields. Avoid entering confidential information. For more information about naming, see[Log and Log Group Names](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#log_and_log_group_names).
- Select Update .
- 

Use the[oci logging log-group update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-group/update.html)command and required parameters to edit a log group:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateLogGroup](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogGroup/UpdateLogGroup)
