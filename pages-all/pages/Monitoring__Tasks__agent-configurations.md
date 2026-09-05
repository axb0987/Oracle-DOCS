# Managing Agent Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/agent-configurations.htm
- Fetched: 2026-09-05 02:38 CDT

# Managing Agent Configurations

Use agent configurations to ingest metric data into custom metrics. For example, expose metrics from a virtual machine (VM) using an HTTP endpoint in Prometheus format. An agent configuration uses the agent, or Unified Monitoring Agent, also known as the Oracle Cloud Agent plugin that's called "Custom Logs Monitoring".
Note  
  
The[Monitoring API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)is another way to publish custom metrics.
[

Agent configuration updates are detected and automatically loaded.

## Before You Begin

To publish custom metrics using an agent configuration, an instance must be in a dynamic group, and that dynamic group must be allowed to manage agent configurations and to use metrics.
- 

[Install the agent.](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/install-agent.htm)
- 

[Verify that the agent is installed.](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/verify-agent-installation.htm)
- 

Define a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/To_create_a_dynamic_group.htm)for the resource or resources.

Example[matching rules](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm):

To specify an instance by ID:
```

```

To specify all instances in a compartment:
```

```

- 

Grant permissions to the dynamic group to manage agent configurations, and to use agent configurations to publish custom metrics to a metric namespace.

Example[policy](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm):
```

```

- 

Set up an input for the agent configuration.

For example, expose metrics from a virtual machine (VM) using an HTTP endpoint in Prometheus format:
```

```

## Tasks

The following pages describe agent installation and verification:
- [Installing the Agent](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/install-agent.htm)
- [Verifying Agent Installation](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/verify-agent-installation.htm)

The following pages describe how you can manage agent configurations:
- [Listing Agent Configurations](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-agent-configuration.htm)
- [Creating an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/create-agent-configuration.htm)
- [Getting an Agent Configuration's Details](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/get-agent-configuration.htm)
- [Updating an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/update-agent-configuration.htm)
- [Moving an Agent Configuration to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/change-compartment-agent-configuration.htm)
- [Disabling an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/disable-agent-configuration.htm)
- [Enabling an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/enable-agent-configuration.htm)
- [Deleting an Agent Configuration](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/delete-agent-configuration.htm)

## Supported Operating Systems

Following are the operating systems (OSs) supported by agent configurations:

OS non-FIPS FIPS ARM
Oracle Linux 7 Yes Yes Yes
Oracle Linux 8 Yes Yes Yes
Oracle Linux 9 Yes Yes Yes
Oracle Linux 10 Yes No Yes
CentOS 7 Yes Yes No
Red Hat Enterprise Linux 8 Yes Yes Yes
Red Hat Enterprise Linux 9 Yes Yes Yes
Red Hat Enterprise Linux 10 Yes No Yes
Windows Server 2016 Yes Yes No
Windows Server 2019 Yes Yes No
Windows Server 2022 Yes Yes No
Windows Server 2025 Yes Yes No
Ubuntu 18.04 Yes No No
Ubuntu 20.04 Yes No No
Ubuntu 22.04 Yes No Yes
Ubuntu 24.04 Yes No Yes
Note  
  

The Oracle Unified Monitoring Agent is designed to function on standard Linux distributions, including Rocky Linux. If you use a Linux distribution that's not listed in the support matrix, contact your distribution provider for details on Unified Monitoring Agent installation and support.

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
