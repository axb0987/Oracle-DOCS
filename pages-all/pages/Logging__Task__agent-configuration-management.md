# Agent Configuration Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/agent-configuration-management.htm
- Fetched: 2026-09-05 02:37 CDT

# Agent Configuration Management

Learn about how to create and manage agent configurations.
You can perform the following agent configuration tasks:
- 

[Creating an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm)
- 

[Listing Agent Configurations](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/list-logging-agent-configuration.htm)
- 

[Getting an Agent Configuration's Details](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/get-logging-agent-configuration.htm)
- 

[Editing an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-logging-agent-configuration.htm)
- 

[Moving an Agent Configuration Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-agent-configuration.htm)
- 

[Creating a Log Configuration for an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-logging-agent-configuration.htm)
- 

[Editing a Log Configuration for an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-logging-agent-configuration.htm)
- 

[Tagging an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-logging-agent-configuration.htm)
- 

[Deleting an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/delete-logging-agent-configuration.htm)
To use agent configurations, you must be running an Oracle Cloud Infrastructure instance with the supported operating system (see[Agent Management Overview](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Concepts/agent_management.htm)). Agent configurations give you a central experience to easily configure what custom logs you want to ingest across your fleet of hosts. A configuration allows you to select:
- Which hosts you want to collect logs from.
- Exactly which logs you want to ingest from those hosts.
- A log group/log destination. You can manage agent configurations using the Console and Logging API. In addition, since you can choose to create an agent configuration later after creating a custom log, you can use the Agent Configurations page to set up the agent configuration and point it to your custom log.

[To enable or disable an existing agent configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/agent-configuration-management.htm#)

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Agent Configurations . The Agent Configurations page is displayed.
- Under List Scope , Compartment , choose a compartment you have permission to work in.
- Click the linked agent configuration name under Name in the table. The agent configuration detail page is displayed.
- Click Disable / Enable . A confirmation dialog is displayed regarding the disabling or enabling of the agent configuration.
- Confirm by clicking Disable / Enable . The agent configuration detail page changes its status and displays Inactive (for a disabled configuration), or Active (for an enabled configuration) in the status field, both on the agent configuration detail page and the Agent Configurations page.
