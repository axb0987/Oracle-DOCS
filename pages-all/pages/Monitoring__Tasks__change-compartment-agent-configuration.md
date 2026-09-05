# Moving an Agent Configuration to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-agent-configuration.htm
- Fetched: 2026-09-05 02:38 CDT

# Moving an Agent Configuration to a Different Compartment

Move an agent configuration to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-agent-configuration.htm#)
- 

- On the Agent configurations list page under Monitoring , find the agent configuration that you want to work with. If you need help finding the list page or the agent configuration, see[Listing Agent Configurations](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm).
- From the Actions menu (three dots) for the agent configuration, select Move Resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci logging agent-configuration change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/change-compartment.html)command and required parameters to move an agent configuration to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeUnifiedAgentConfigurationCompartment](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/ChangeUnifiedAgentConfigurationCompartment)operation to move an agent configuration to another compartment.

Example API request:
```

```
