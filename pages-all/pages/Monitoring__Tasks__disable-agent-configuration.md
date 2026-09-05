# Disabling an Agent Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/disable-agent-configuration.htm
- Fetched: 2026-09-05 02:39 CDT

# Disabling an Agent Configuration

Disable an agent configuration.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/disable-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/disable-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/disable-agent-configuration.htm#)
- 

- On the Agent configurations list page under Monitoring , find the agent configuration that you want to work with. If you need help finding the list page or the agent configuration, see[Listing Agent Configurations](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm).
- From the Actions menu (three dots) for the agent configuration, select Disable .
- Confirm the operation.
The agent configuration status changes to Inactive .
- 

Use the[oci logging agent-configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/update.html)command and required parameters to disable an agent configuration:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/UpdateUnifiedAgentConfiguration)operation to disable an agent configuration. Set the`isEnabled`attribute to`false`
