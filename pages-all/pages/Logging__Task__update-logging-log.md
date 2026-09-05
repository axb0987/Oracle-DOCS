# Editing a Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log.htm
- Fetched: 2026-09-05 02:38 CDT

# Editing a Log

Update a log's configuration.

Note  
  
The resource of a service log can't be updated.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-log.htm#)
- 

- On the Logs list page, find the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log.htm).
- From the the Actions menu (three dots) for the log, select Edit .
- For service logs , the Edit Log panel indicates the resource, and you can change the log name in the associated field under Configure Log . Avoid entering confidential information.You can also change the log retention settings
- For custom logs , you can change the custom log name in the associated field, and change the log group. Avoid entering confidential information.Select Show additional options to change log retention and tagging settings.

Note  
  

For both service and custom logs, the Retention Period can be set in 30-day increments, up to a maximum of 180 days. Logs are no longer available or searchable after the retention period has passed.

If you change the retention period from six months to one month, all the logs older than one month will no longer be accessible. For example, if changing from one month to six months, logs will not be available after one month, and six-month old logs will not be available.

Furthermore, the future time and date that a log no longer becomes available is based on the exact time and date that you created the log. For example, if you created a log on July 21 at 15:05 UTC with a retention period of three months, then on October 19 at 15:05 the log will no longer be searchable.
- Select Update .
- 

Use the[oci logging log update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/update.html)command and required parameters to edit a log:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/UpdateLog)
