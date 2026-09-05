# Tagging an Agent Configuration at Creation
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-logging-agent-configuration.htm
- Fetched: 2026-09-05 02:38 CDT

# Tagging an Agent Configuration at Creation

Add metadata to an agent configuration when you first create it. This metadata enables you to define keys and values and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-logging-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-logging-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/tag-create-logging-agent-configuration.htm#)
- 

See[Creating an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-logging-agent-configuration.htm)for more information on adding tags during agent configuration creation.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci logging agent-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/create.html)command to tag an agent configuration when you create it:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/CreateUnifiedAgentConfiguration)operation to create an agent configuration for logging. Include the`definedTags`and`freeformTags`
