# Getting a Log's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm
- Fetched: 2026-09-05 02:37 CDT

# Getting a Log's Details

View the details of a log.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-log.htm#)
- 

- On the Logs list page, select the log that you want to work with. If you need help finding the list page or the log, see[Listing Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log.htm).

The log's details page opens and displays general information about the log.
- 
Note  
  
Retention Period can be set in 30-day increments, up to a maximum of 180 days. If you change the retention period from six months to one month, all the logs older than one month will no longer be accessible or searchable. For example, if changing from one month to six months, logs will not be available after one month, and six-month old logs will not be available.

The Tags tab shows associated tags for the log, and you can add or edit tags.

The Explore Log tab displays the log data Log Data on the Search page.

To view this log on the Search page directly, select Explore with Log Search . The Search page opens with the Select Logs to Search field populated with the log in the filter settings. At this point, you can perform more analysis and investigation related to this log directly on the Search page. For more information, see[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm).
- 

Select the Monitoring tab to view interactive charts for either a chosen time period or a predefined range.

The Bytes Ingested chart (total bytes of log entries ingested) and the Search Success (number of successful search queries issued by the user) are displayed.
Selecting anywhere in a chart displays a larger version of the chart. You can perform several chart actions from the Actions menu (both in the Metrics resource and in the zoomed-in view):
- View query in Metrics Explorer : Opens the chart in the Monitoring Metrics Explorer. See[Exploring a Default Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-explore.htm)for more information.
- Copy chart URL : Copies the chart URL so that you can share it.
- Copy query (MQL) : Copies the predefined service query used in the chart.
- Create an alarm on this query : Opens the Monitoring Create Alarm page. See[Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm)for more information.
- Table view : Displays a tabular summary of the chart data. Select Chart View to switch back to the chart.

For more information, see[Logging Metrics](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../metrics.htm).

- 

Use the[oci logging log get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/get.html)command and required parameters to get the details of a log:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/GetLog)
