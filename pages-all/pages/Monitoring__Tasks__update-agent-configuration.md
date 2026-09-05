# Updating an Agent Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm
- Fetched: 2026-09-05 02:40 CDT

# Updating an Agent Configuration

Update an agent configuration.

When you update an agent configuration, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

Agent configuration updates are detected and automatically loaded.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm#)
- 

- On the Agent configurations list page under Monitoring , find the agent configuration that you want to work with. If you need help finding the list page or the agent configuration, see[Listing Agent Configurations](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm).
- From the Actions menu (three dots) for the agent configuration, select Edit .
- In the Edit agent configuration panel, update the values as needed.
For more information about the fields, see[Creating an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm).
- Select Save changes .
- 

Use the[oci logging agent-configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/update.html)command and required parameters to update an agent configuration:

```

```

[Example command and JSON files](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm#)

```

```

`update-service-configuration.json`:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/UpdateUnifiedAgentConfiguration)operation to update an agent configuration.

[Example API request](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/update-agent-configuration.htm#)

```

```
