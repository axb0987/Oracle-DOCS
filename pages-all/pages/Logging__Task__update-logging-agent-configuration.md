# Editing an Agent Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-agent-configuration.htm
- Fetched: 2026-09-05 02:38 CDT

# Editing an Agent Configuration

Update an agent configuration in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-agent-configuration.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Agent Configurations .
- Select the compartment that contains the agent configuration that you want to edit.
- Select the name of the agent configuration.
- On the agent configuration details page, select Actions and then Edit .
- In the Edit Agent configuration panel, change the configuration name, description, host groups, log inputs, log destination, agent operational metrics, and tags, as needed. For descriptions of these fields, see[Creating an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm).
- Select Update .
- 

Use the[oci logging agent-configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/update.html)command and required parameters to edit the details of an agent configuration for logging:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/UpdateUnifiedAgentConfiguration)
