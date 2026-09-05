# Listing Agent Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm
- Fetched: 2026-09-05 02:39 CDT

# Listing Agent Configurations

List agent configurations in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Agent Configurations .
- To view the agent configurations in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the alarms in the list. Perform one of the following actions depending on the options that you see:
- To filter the list by agent configuration status, select a status value from the Status list.
- To filter the list by tag, select add under Tag filters .

## Actions

In the list table, select the name of an agent configuration to open its details page, where you can view its status and perform other tasks.

To perform an action on an agent configuration directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that agent configuration:
- Edit :[Update the agent configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm).
- Disable :[Disable the agent configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/disable-agent-configuration.htm).
- Enable :[Enable the agent configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/enable-agent-configuration.htm).
- Copy OCID : Copy the OCID of the agent configuration to the clipboard.
- Add tags : Add one or more tags to the agent configuration. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Move Resource :[Move the agent configuration to another compartment](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/change-compartment-agent-configuration.htm).
- Delete :[Delete the agent configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/delete-agent-configuration.htm).

To create an agent configuration, select Create agent config .
- 

Use the[oci logging agent-configuration list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/list.html)command and required parameters to list agent configurations:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListUnifiedAgentConfigurations](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/ListUnifiedAgentConfigurations)operation to list agent configurations.

Example API request:

This example sorts by time created, in descending order.
```

```
