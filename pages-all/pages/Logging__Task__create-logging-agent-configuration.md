# Creating an Agent Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm
- Fetched: 2026-09-05 02:37 CDT

# Creating an Agent Configuration

Create an agent configuration in Logging to ingest events from your applications into a custom log.

To create an agent configuration, you must first install the Oracle fluentd-based agent. For details, see[Installing the Agent](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/installing_the_agent.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Agent Configurations .
- Select a compartment that you have permission to work in.
- Select Create agent config .
- In the Create agent configuration panel, enter a name and description for the configuration. Avoid entering confidential information.
- Select the compartment that you want to create the configuration in.
- (Optional) Add one or more tags to the agent configuration: Expand Tags and then select Add Tag .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Under Host Groups , where you define which VMs apply to this configuration, select one of the following options from the Group type list:

- Dynamic group : Dynamic Group refers to a group of instances that you can create in the IAM feature of the Console. For more information, see[About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About). Select a dynamic group from the Group list.
- User group : User group refers,to the IAM Groups feature of the Console. For more information, see[Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm). Select a user group from the Group list.
- To add more groups, select Another host group .

You can add a combination of group types for the agent configuration.
Note  
  
A maximum of five groups per configuration is allowed, and a host can be in a maximum of five different groups.
- Under Agent configuration , define the format of the logs (what logs you want to watch for) in Configure log inputs . Select one of these options from the Input type list, and then enter an input name and a file path:

- For Windows event log , enter an input name and select one or more event channels.
- For Log path , enter an input name and one or more file paths. For example, / &lt;log_path&gt; / &lt;log_name&gt; .

You can specify multiple log file paths, separated by a comma (,). For more information, see[https://docs.fluentd.org/input/tail#path](https://docs.fluentd.org/input/tail#path).
```

```

Example configuration:
```

```

- Expand Advanced parser options , and in the Parser list, select a parser and message key to specify how to parse the log. Some parsers require further input and have more options, depending on the type chosen.
For example for JSON , you must select a Time type value from the list, while optionally, you can specify event time and null field settings. For REGEXP, you can specify the regular expression for matching logs, along with the time format. For more information, see[Log Inputs and Parsers](https://docs.oracle.com/iaas/Content/Logging/Concepts/log_inputs_and_parsers.htm).
Important  
  
The NONE parser type is required, even if you don't want to specify a particular parser type.
- Under Select log destination , the user group or dynamic group in the configuration that you select in Compartment needs to have permission to work in the compartment.

Select the Log Group , and the Log name from the corresponding lists.

The Log name can only point to a custom log, and the custom log must exist in the chosen log group for the configuration to work. If a custom log doesn't exist, you must first create one before you can create this agent configuration.
- (Optional) Select Show additional options . Under Logging agent operational metrics , select Enable to help monitor and identify potential problems with the agent.

Under Emit destination , select the compartment and specify a namespace, and optionally specify the resource group from the corresponding fields.
Note  
  
Though Resource group is optional, it defaults to "defaultGroup" if nothing is selected.
Under Operational metrics , select the operational metrics that you want to enable for the agent configuration.
- Heartbeat : Unified Monitoring Agent state. A value of 1 denotes the agent is available, and 0 denotes the agent isn't responding. This metric is always enabled and can't be turned off.

Dimensions : The instance's Unified Monitoring Agent version, operation system, architecture, region, AD, and instance ID.
- RestartMetric : Unlike the Heartbeat metric, which is periodic, RestartMetric is sent only one time during the lifetime of the agent, that is, when the agent is being restarted. Monitoring restarts are essential for understanding agent stability. Frequent restarts can indicate system malfunctions, and being aware of unexpected restarts can help operators to address configuration problems or resource constraints.

Dimensions : Instance ID.
- EmitRecords : The total number of emitted log records. A record corresponds to the log lines sent to the backend. This metric provides insight on the increase and decrease in the number of log lines ingested, and the volume of logs being processed. A sudden drop or increase in this number can signal problems in the logging pipeline. For example, some log lines could be rejected and not included during log ingestion.

Dimensions : Instance ID, and tag.
- BufferSpaceAvailable : The available buffer space expressed as a percentage. The value starts at 100 and decreases as the buffer amount gets used. The agent uses buffers to handle bursts of incoming data and potential backpressure from outputs. Monitoring this metric helps ensure you don't run out of buffer space, which could lead to data loss or backpressure. If buffer space is consistently running low, you might need to optimize the agent configuration and allocate more resources.

Dimensions : Instance ID, and tag.
- ShowFlushCount : The total number of slow flushes. Flushing refers to the act of sending buffered data to its intended destination. A slow flush means that the flushing of data from the buffer to its destination is taking longer than the set threshold. This number is incremented when the buffer flush is longer than 20 seconds. Monitoring slow flushes helps identify performance problems. If flushes are consistently slow, the buffer can fill up faster than data can be cleared out, leading to data loss or backpressure issues.

Dimensions : Instance ID, and tag.
- RollbackCount : The total number of times the agent rolls back a transaction because it couldn't successfully flush the buffer to the emit destination. Rollbacks typically occur when a write or try_write fails, or issues with the OCI Logging service, network issues, or configuration problems are present. High rollback counts are a clear indicator of reliability issues in the logging pipeline that need investigation.

Dimensions : Instance ID, and tag.
- RetryCount : Tracks the number of times the agent tries to retry a data send operation after a failure. Retries indicate transient issues with delivering data, and high retry counts can indicate network instability. While rollbacks might deal with larger transactional issues, retries often indicate smaller, possibly more frequent disruptions.

Dimensions : Instance ID, and tag.

After the agent configuration is created, you can view which operational metrics are enabled[when getting an agent configuration's details](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-agent-configuration.htm).
- (Optional) Select Save as stack to save the resource configuration as a stack.
For more information, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- Select Create .
The agent configuration is created and appears in the Agent Configurations page.
- 

Use the[oci logging agent-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/create.html)command and required parameters to create an agent configuration for logging:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/CreateUnifiedAgentConfiguration)
