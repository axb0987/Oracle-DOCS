# Getting an Agent Configuration's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-agent-configuration.htm
- Fetched: 2026-09-05 02:37 CDT

# Getting an Agent Configuration's Details

View the details of an agent configuration in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-agent-configuration.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Agent Configurations .
- Select the compartment that contains the agent configuration whose details you want to get.
- Click the name of the agent configuration.

The agent configuration details page opens.

The Tags tab shows tags with this log, and you can add or edit tags.

In the Configuration tab, the Host groups - Dynamic groups , Host groups - User groups , and Log input log path configuration settings are listed. See[Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm)and[About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About)for more information.

In the Explore log tab, log data is displayed in a similar manner as the Log Data on the Search page. You can apply filters, such as sorting by newest or oldest from the Sort field, or filtering by time from the corresponding Filter by time field.
Note  
  

To view this log on the Search page directly, select Explore with Log Search . The Search page opens with the Select Logs to Search field populated with the log in the filter settings. At this point, you can perform more analysis and investigation related to this log directly on the Search page. For more information, see[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/searchinglogs.htm).
In the Monitoring tab, you can view the following interactive charts for either a chosen time period or a pre-defined ranges::
- Found Configurations : the number of agent configurations found for the dynamic user or group.
- Unauthorized Configurations : the configurations unauthorized for the dynamic user or group.
- Configuration Update Failure the failure to download configurations.
Selecting anywhere in a chart displays a larger version of the chart. You can perform several chart actions from the Actions menu (both in the Metrics resource and in the zoomed-in view):
- View query in Metrics Explorer : Opens the chart in the Monitoring Metrics Explorer. See[Exploring a Default Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-explore.htm)for more information.
- Copy chart URL : Copies the chart URL so that you can share it.
- Copy query (MQL) : Copies the predefined service query used in the chart.
- Create an alarm on this query : Opens the Monitoring Create Alarm page. See[Creating an Alarm](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm.htm)for more information.
- Table view : Displays a tabular summary of the chart data. Select Chart View to switch back to the chart.

For more information, see[Logging Metrics](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../metrics.htm).
- 

Use the[oci logging agent-configuration get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/get.html)command and required parameters to get the details of an agent configuration for logging:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/GetUnifiedAgentConfiguration)
