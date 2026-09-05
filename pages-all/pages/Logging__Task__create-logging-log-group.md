# Creating a Log Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log-group.htm
- Fetched: 2026-09-05 02:37 CDT

# Creating a Log Group

Create a log group that functions as a logical container for organizing logs. You must create a log group before you can create a log.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log-group.htm#)
- 

- On the Log groups list page, select Create log group . If you need help finding the list page, see[Listing Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log-group.htm).

The Create log group panel opens.
- Enter the following information:
- Compartment : The compartment in which you want to create the log group. This field is already filled in based on your compartment choice in step 2.
- 

Name : A name for this log group. The first character of a log group name must be a letter. For more information, see[Log and Log Group Names](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#log_and_log_group_names). Avoid entering confidential information.
- Description : A friendly description.
- Tags : Optionally, enter tagging information.
- 

Select Create .

The log group is created and the details page for it opens. On this page, you can perform the following actions:
- Edit the group
- Move the group to a different compartment
- Add tags
- Delete the log group
- View log group information and tags
- View log group resources (explore the log group, view the logs included in the log group, create custom or service logs, and view metrics)

The Monitoring tab in a log group details in a log group detail page functions the same as in a log detail page. See[Getting a Log's Details](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm)for more information.
- 

Use the[oci logging log-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-group/create.html)command and required parameters to create a log group:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateLogGroup](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogGroup/CreateLogGroup)
