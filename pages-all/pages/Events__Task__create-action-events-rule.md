# Adding an Action to an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-action-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Adding an Action to an Events Rule

Add an action to a rule in Events to perform a specific task.

For more information on using actions in a rule, see[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-action-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-action-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-action-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Actions .
- Under Actions , select Add .
- In the Add action panel, select the type of action to add and then provide the information specific to that resource:
- To add a stream, select Streaming , select the compartment where the stream that you want to use is located, and then select the stream.
- To add a topic, select Notifications , select the compartment where the topic that you want to use is located, and then select the topic.
- To add a function, select Functions , select the compartment where the function that you want to use is located, select the function application, and then select the function.
- Select Add action .
Note  
  
Next, you can[enable](https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-action-events-rule.htm#top)the action.
- 

Use the`--action`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to add an action to a rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to create a rule. Include the`action`
