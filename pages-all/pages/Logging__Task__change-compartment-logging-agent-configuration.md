# Moving an Agent Configuration Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-agent-configuration.htm
- Fetched: 2026-09-05 02:37 CDT

# Moving an Agent Configuration Between Compartments

Move an agent configuration in Logging to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-agent-configuration.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Agent Configurations .
- Select the compartment that contains the agent configuration that you want to move.
- Select the name of the agent configuration.
- From the Actions menu for the agent configuration, select Actions and then Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci logging agent-configuration change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/change-compartment.html)command and required parameters to move an agent configuration for logging between compartments:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeUnifiedAgentConfigurationCompartment](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/ChangeUnifiedAgentConfigurationCompartment)
