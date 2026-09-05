# Viewing Application Logs on Managed Nodes and Self-Managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm
- Fetched: 2026-09-05 01:57 CDT

# Viewing Application Logs on Managed Nodes and Self-Managed Nodes

Find out how to view the logs of applications running on managed nodes and self-managed nodes in a Kubernetes cluster you've created using Kubernetes Engine (OKE).

Having created a cluster using Kubernetes Engine, you can use Oracle Cloud Infrastructure Logging to view and search the logs of applications running on compute instances hosting managed nodes and self-managed nodes in the cluster.

Before you can collect and parse the application logs using Oracle Cloud Infrastructure Logging:
- You must have already:
- Enabled monitoring for compute instances hosting managed nodes and self-managed nodes (see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm)).
- Installed the Oracle Cloud Agent software on compute instances hosting managed nodes and self-managed nodes. The agent enables you to specify which logs to collect and how to parse them. The agent is installed by default on managed node compute instances. To confirm that the agent is already installed, see[Verify Agent Installation](https://docs.oracle.com/iaas/Content/Logging/Task/verify_agent_installation.htm).
- You must have already:
- Created a dynamic group with a rule that includes the compute instances hosting managed nodes and self-managed nodes as target hosts (see[About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About)and[Selecting Target Hosts with Dynamic Groups](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs_multihost.htm)). For example:

```

```

- Created a policy for the dynamic group with a policy statement to allow the target hosts in the dynamic group to push logs to Oracle Cloud Infrastructure Logging (see[Selecting Target Hosts with Dynamic Groups](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs_multihost.htm)). For example:

```

```

Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format`dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format`dynamic-group id <dynamic-group-ocid>`.

Having completed the above prerequisites, you can then define custom logs and associated agent configurations to view application logs on compute instances hosting managed nodes and self-managed nodes. Note that application logs must be output to the file path that you specify when you create an agent configuration (typically, but not necessarily,`/var/logs/containers`). For more information about custom logs and agent configurations, see[Custom Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs.htm).

Note that in addition to viewing application logs on compute instances hosting managed nodes and self-managed nodes, you can also:
- Monitor the overall status of the cluster itself, node pools, and nodes. See[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).
- View and search the logs of Kubernetes processes (such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver running in the cluster's control plane. See[Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm).
- Monitor the health, capacity, and performance of clusters, node pools, and nodes at a more granular level using metrics , alarms , and[notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). See[Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengmetrics.htm).

## Using the Console

To define a new custom log object and an associated agent configuration to enable you to view and search the logs of applications running on compute instances hosting managed nodes and self-managed nodes in a cluster:
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
- Choose a Compartment you have permission to work in.
- Select Create custom log to create a new custom log.
- 

On the Create custom log page, specify:
- Custom log name: A name of your choosing for the new custom log. Avoid entering confidential information.
- Compartment: The compartment in which to create the new custom log.
- Log Group: The log group in which to place the custom log. Optionally, select Create New to create a new log group (see[Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm)).
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Optionally, select Show additional options and specify:
- Retention time (in months): The length of time (in months) to retain the custom log. Select one of the predefined options, or select Custom time and specify a number of months of your choosing (up to 60).
- Select Next .

For convenience, these instructions now describe how to create a new agent configuration associated with the new custom log (although you can create a new agent configuration later if you prefer).
- 

On the Create agent configuration page, select Add new configuration and specify:
- Configuration Name: A name of your choosing for the new agent configuration. Avoid entering confidential information.
- Description: A description for the new agent configuration.
- Compartment: The compartment in which to create the new agent configuration.
- In the Host Groups section, specify:
- Group type: Select Dynamic group .
- Group: An existing dynamic group that includes managed nodes in the cluster's managed node pools as target hosts. The dynamic group you select must have permission to access the compartment you specified for the agent configuration, and must also allow target hosts to push logs to Oracle Cloud Infrastructure Logging.
- For Configuration type , select Logging .
- 

In the Agent configuration section, specify:
- Configure log inputs: One or more locations from which to obtain application logs as inputs to the custom log, as follows:
- Input type: Select Log path .
- Input name: A name of your choosing for the new log input.
- File paths: Specify the path to application logs on the compute instances hosting managed nodes and self-managed nodes, and select Add to list . For example, typically (but not necessarily)`/var/logs/containers/*`
- Advanced parser options: (optional) Select a parser to parse the log. Some parsers require further input and have more options.
- Select log destination: The options are pre-populated with the custom log details you specified previously.
- Optionally, select Show additional options and specify:
- Logging agent operational metrics: Select this option to capture metrics for one or more operations of the logging agent. You enable the operational metrics individually.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the custom log and the associated agent configuration.

To view and search the contents of a custom log created for an application running on compute instances hosting managed nodes and self-managed nodes in a cluster:
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Logs .
- Select the name of the custom log that you want to view.
- (Optional) Select the Explore log tab to see log entries. You can sort log entries by age, and filter by time.
- (Optional) Select Explore with log search to open the central logging Search page. You can apply filters, and explore and visualize the log data in different ways (see[Viewing Custom Logs in a Compute Instance](https://docs.oracle.com/iaas/Content/Logging/Concepts/viewing_custom_logs_in_a_compute_instance.htm)
