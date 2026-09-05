# Creating an Agent Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm
- Fetched: 2026-09-05 02:38 CDT

# Creating an Agent Configuration

Create an agent configuration in Logging to ingest metric data into a custom metric.

Agent configuration updates are detected and automatically loaded.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm#)
- 

- On the Agent configurations list page under Monitoring , select Create agent config . If you need help finding the list page, see[Listing Agent Configurations](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-agent-configuration.htm).
- In the Create agent configuration panel, enter a name and description for the configuration. Avoid entering confidential information.
- Select the compartment that you want to create the configuration in.
- Under Choose host groups , for Group type , select an option, and then select the group that you want.
For example, select Dynamic group , then select the dynamic group that matches the resources with the agent configurations.
- Under Agent configuration , enter the base URL to the metric input.

For example, expose metrics from a virtual machine (VM) using an HTTP endpoint in Prometheus format:
```

```

- Optionally select Another endpoint to add another endpoint.
All endpoints go to the same compartment and namespace.
- Under Select metric destination , select the compartment and metric namespace that you want to publish custom metrics to.
- (Optional) Add one or more tags to the agent configuration: Expand Tags and then select Add Tag .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
The newly created agent configuration is listed on the Agent Configurations page.
- 

Use the[oci logging agent-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/agent-configuration/create.html)command and required parameters to create an agent configuration:

```

```

[Example command and JSON files](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm#)

```

```

`group-association.json`:
```

```

`create-service-configuration.json`:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateUnifiedAgentConfiguration](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/UnifiedAgentConfiguration/CreateUnifiedAgentConfiguration)operation to create an agent configuration.

[Example API request](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-agent-configuration.htm#)

```

```
