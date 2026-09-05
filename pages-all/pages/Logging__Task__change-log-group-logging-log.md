# Moving a Log Between Log Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-log-group-logging-log.htm
- Fetched: 2026-09-05 02:37 CDT

# Moving a Log Between Log Groups

Move a log to a different log group.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-log-group-logging-log.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-log-group-logging-log.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-log-group-logging-log.htm#)
- 

- On the Logs list page, find the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log.htm).
- To view the log groups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the the Actions menu (three dots) for the log, select Move resource .
The Move resource panel opens.
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci logging log change-log-group](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/change-log-group.html)command and required parameters to move a log between log groups:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ChangeLogLogGroup](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/ChangeLogLogGroup)
