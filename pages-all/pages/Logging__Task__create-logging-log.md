# Creating a Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log.htm
- Fetched: 2026-09-05 02:37 CDT

# Creating a Log

Create a log that contains critical diagnostic information that tells you how your Oracle Cloud Infrastructure (OCI) services are performing and being accessed.

Log groups are logical containers for organizing logs. Logs must always be inside log groups. You must[create a log group](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log-group.htm)before you create a log.

For more information about logs and required permissions for working with them, see[Log Group Management](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/log-group-management.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-log.htm#)
- 

- On the Logs list page, select Create custom log . If you need help finding the list page, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-log.htm).

The Create custom log panel opens.
- Enter a name for the custom log. Avoid entering confidential information.
- Select the compartment that you want to create the log in.
- Under Log group , select an existing log group to place the custom log into, or create one.
- (Optional) In the Tags section, add one or more tags to the log.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Show additional options and then select how long to retain the log, in 30-day increments, up to a maximum of 180 days:
Note  
  

If you change the retention period from six months to one month, all the logs older than one month will no longer be accessible. For example, if changing from one month to six months, logs will not be available after one month, and six-month old logs will not be available.

Furthermore, the future time and date that a log no longer becomes available is based on the exact time and date that you created the log. For example, if you created a log on July 21 at 15:05 UTC with a retention period of three months, then on October 19 at 15:05 the log will no longer be searchable.
- Select Next .
- On the Create agent configuration page, create a new configuration to define the parameters for the associated log data (the default), or add it later. The agent configuration defines what instances the configuration applies to ( Host groups ), which log files are obtained, and what parser (if any) is used ( Configure log inputs ).
- If you select Add new configuration , go to the next step.
- If you select Add configuration later , skip to the last step in this task.
- Enter a name and description for the configuration. Avoid entering confidential information.
- Select the compartment that you want to create the configuration in.
- Under Host Groups , where you define which VMs apply to this configuration, select one of the following options from the Group type list:
- Dynamic group : Dynamic Group refers to a group of instances that you can create in the IAM feature of the Console. For more information, see[About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About). Select a dynamic group from the Group list.
- User group : User group refers to the IAM Groups feature of the Console. For more information, see[Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm). Select a user group from the Group list.
- To add more groups, select Add host group .

You can add a combination of group types for the agent configuration.
Note  
  
A maximum of five groups per configuration is allowed, and a host can be in a maximum of five different groups.
- Under Agent configuration , define the format of the logs (what logs you want to watch for) in Configure log inputs . Select one of the options from the Input type list, and then enter the relevant values:
- For Windows event log , enter an input name and select one or more event channels.
- For Log path , enter an input name and one or more file paths. For example, / &lt;log_path&gt; / &lt;log_name&gt; .

You can specify multiple log file paths, separated by a comma (,). For more information, see[https://docs.fluentd.org/input/tail#path](https://docs.fluentd.org/input/tail#path).
```

```

Example configuration:
```

```

Select Add log input to add more custom log inputs.
- 

Select Show advanced parser options , then select a parser to specify how to parse the log. Some parsers require further input and have more options, depending on the type chosen.

For example for JSON , you must select a Time type value from the list, while optionally, you can specify event time and null field settings. For REGEXP , you can specify the regular expression for matching logs, along with the time format. For more information, see[Log Inputs and Parsers](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/log_inputs_and_parsers.htm).
Important  
  
The NONE parser type is required, even if you don't want to specify a particular parser type.
- Select Create .

The custom log object is created, along with the its associated agent configuration (if specified), which pulls data from instances, and pushes into the custom log object.
- 

Use the[oci logging log create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/create.html)command and required parameters to create a log in a log group:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/CreateLog)
