# Tagging an Agent Configuration When Updating
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-logging-agent-configuration.htm
- Fetched: 2026-09-05 02:38 CDT

# Tagging an Agent Configuration When Updating

Add metadata to an existing agent configuration. This metadata enables you to define keys and values and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-logging-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-logging-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-update-logging-agent-configuration.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Agent Configurations .
- Select the compartment that contains the agent configuration that you want to tag.
- Select the name of the agent configuration.
- On the agent configuration details page, select the Tags tab and add or edit tags as needed:
- To add one or more tags, select Add tags and enter the tag namespace (for a defined tag), key, and value.
- To edit or remove a tag, select the Actions menu (three dots) for the tag and then select the appropriate option.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci logging agent-configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/update.html)command to tag an agent configuration when you update an existing one:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/UpdateUnifiedAgentConfiguration)operation to edit the details of an agent configuration for logging. Include the`definedTags`and`freeformTags`
