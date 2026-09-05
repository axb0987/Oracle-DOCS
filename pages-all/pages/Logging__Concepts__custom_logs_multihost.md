# Selecting Target Hosts with Dynamic Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/custom_logs_multihost.htm
- Fetched: 2026-09-05 02:36 CDT

# Selecting Target Hosts with Dynamic Groups

To set up a configuration for multiple hosts, you can use the Dynamic Group feature from IAM.

The overall process first involves creating a compartment, then placing all the instances in the compartment you want to collect logs from. Next, you can create the Dynamic Group. The Dynamic Group policy statement would then point to the compartment that contains the instances. Lastly, create a log group, custom log, and its associated agent configuration.
Set the following policy statement:
```

```

This policy statement allows the agent configuration to push logs to the Logging service backend, which you can later see in the Logging Service's Search page.

In the Dynamic Groups configuration, set up your Dynamic Group to have a rule that includes all the agents that you want to use to send logs to the Logging service. For example, in a Rule inside the Dynamic Group it can state:
```

```

If you remove`instance.id = 'ocid1.instance. <region> . <location> . <unique_ID> '`and just have:
```

```
this means use all the instances under this compartment to send logs. For more information on Dynamic Groups, see[About Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#About).

Next, create the log group (see[Creating a Log Group](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/create-logging-log-group.htm)). After the log group is created, you can then create the custom log and the agent configuration (see[Using the Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/create-logging-log.htm#console)for steps to create the custom log and agent configuration). During the agent configuration, you can use the Dynamic Group you created earlier and select it in the Choose Host Groups section of the Agent Configurations panel. This links the log configuration with the instance you want to send logs to. Once the agent configuration is active, the logs you see are sent by the instance, inside the Dynamic Group you earlier set up. You can later click Explore with Log Search in the agent configuration to view the logs through the Search page (see[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm)
