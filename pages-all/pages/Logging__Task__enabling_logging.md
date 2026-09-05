# Enabling Logging for a Resource
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/enabling_logging.htm
- Fetched: 2026-09-05 02:37 CDT

# Enabling Logging for a Resource

Service logs can be enabled directly on the resource itself, on the Logs page, or on a log group details page.

When you enable a service log on a specific resource, you specify the category. Different resources can have different categories. For example, rules in the Events Service have the Logs resource available for logging management. The rule can issue a log according to the category listed in the corresponding Category field. On this page, the logs are listed that the resource can create.
Note  
  
When a log object is in an invalid state after failing (CREATING, DELETING, UPDATING), the only action available will be to delete the object. You can use the CLI to retrieve the logs of the work flow, to identify the nature of the failure (for example, a resource not found, an operation wasn't allowed on the resource, an internal failure, and so on). See[CLI Examples](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/using_the_cli_loggroups.htm)for more information on logging CLI commands.

For more information on enabling a log on the Logs page, see[Enabling Logging on the Logs page](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/enabling_logging.htm#enabling_logging__enableloglogspage).

## Enabling Logging from a Service's Resource page
For Oracle Cloud Infrastructure services that are compatible with Logging, the Logs resource allows you to manage the logs issued by the resource. You can view the following information:
- Category
- Status
- Log name
- Log group In addition, you can enable or disable logging, edit the log, or delete it (the last two options are available in the action menu). When enabling logging, you also create the log object itself.

For a newly created resource, logging is automatically enabled. For a resource you want to enable logging on, under Resources select Logs , and then turn on Enable Logging . The Create Log panel is displayed, and the entry fields are already filled:
- Compartment (the same as your resource)
- Log Group : The first log group in your compartment. You can select another log group, or create a new group by selecting Create New Group .
- Log Name : Already filled as the name of your resource and the category, which are combined with an underscore ( &lt;resource&gt; _ &lt;category&gt; ). For example, if the resource is named "resource" and the category is "ruleexecutionlog", the log name is "resource_ruleexecutionlog".
- Log Retention : The default retention period for the log in 30-day increments, up to a maximum of 180 days. You can select a different retention period.
Note  
  

If you change the retention period from six months to one month, all the logs older than one month will no longer be accessible. For example, if changing from one month to six months, logs will not be available after one month, and six-month old logs will not be available.

Furthermore, the future time and date that a log no longer becomes available is based on the exact time and date that you created the log. For example, if you created a log on July 21 at 15:05 UTC with a retention period of three months, then on October 19 at 15:05 the log will no longer be searchable.

After logging is enabled, you can select the link under Log name or Log group to view the log details or log group details pages.

To disable logging, toggle the Enable log control, which displays a disable logging confirmation dialog. Select Disable Log to confirm. The Status field is set to INACTIVE to indicate the inactive status.

When creating a log, a log object is established. To delete the log, select Delete from the action menu. A confirmation is displayed confirming whether you want to delete the log. After selecting Delete , this removes the log object, instead of disabling it (which means the log object still exists but doesn't record new data into it).

## Enabling Logging on the Logs page

- On the Logs list page, find the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log.htm).
- From the the Actions menu (three dots) for the log, select, select Enable service log .

The Enable Resource Log panel opens.
- Enter the following information:
- Resource Compartment : Enter a compartment you have permission to work in.
- Service : Select the service that you want to enable resource logging from the list.
- Resource : Select the specific resource you want to enable logging from the list.
Tip  
  
You can type in these fields to perform a filtered search of all compartments, services, and resources.
- Under Configure Log , define the:
- 

Log Category : The type of log to create. For example, Object Storage buckets have categories for read and write. Select Read Access Events to enable a log with only read events. Select Write Access Events for a log with only write events. Or select All categories for both.

You can only have one log for any combination of service, resource, and log category. For example, Object Storage buckets have two categories: read and write. Therefore:
- You can enable a single read log and a single write log for every bucket in your tenancy.
- You can't enable more than two logs (one read and one write) for any one bucket.
- 

(Optional) Log Name : The name of the log. See[Log and Log Group Names](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/managinglogs.htm#log_and_log_group_names)for more information. Avoid entering confidential information. Select Enable auto archiving to object storage (legacy) to automatically create a bucket in your compartment, and place a copy of your log there. See[Legacy Archival](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/legacy_archival.htm)for more information.
- 
In Compartment , select the compartment for the log.
Tip  
  
You can type in the list box to perform a filtered search of all compartments in the tenancy.
- 
In Log Group , select a log group for the log.
Tip  
  
To create a new log group, select Create New Group .
- Expand Advanced Options to define the log's location, retention period, and tagging. configure the log:
- Under Log Location , define these values:
- Compartment : the compartment for the log.
- Log group : a log group for the log.
- In Log Retention , select a value from the list:
Note  
  

If you change the retention period from six months to one month, all the logs older than one month will no longer be accessible. For example, if changing from one month to six months, logs will not be available after one month, and six-month old logs will not be available.

Furthermore, the future time and date that a log no longer becomes available is based on the exact time and date that you created the log. For example, if you created a log on July 21 at 15:05 UTC with a retention period of three months, then on October 19 at 15:05 the log will no longer be searchable.
- 1 month (the default) (30 days)
- 2 months (60 days)
- 3 months (90 days)
- 4 months (120 days)
- 5 months (150 days)
- 6 months (180 days)
- Under Add Tags , click Add tag to add one or more tags to the log. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create . The log details page is displayed, and shows the log is in the process of being created (a "Creating log" message is displayed). See[Getting a Log's Details](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm)for more information.

## Enabling Logging in Log Group Details
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Log Groups .
- Select a compartment you have permission to work in.
- Select the name of the log group you want to enable service logs for.

The log group details page opens.
- Select the Logs tab, then select Actions and Enable service log .
- Follow the steps in[Enabling Logging on the Logs page](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/enabling_logging.htm#enabling_logging__enableloglogspage)
