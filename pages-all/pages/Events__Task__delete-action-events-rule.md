# Removing an Action from an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-action-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Removing an Action from an Events Rule

Remove an action from a rule.

Important  
  
You can remove an action only if the rule will still contain at least one action. Alternatively, you can disable the action instead of removing it.

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)for more information on using actions in an events rule.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-action-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-action-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-action-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Actions .
- Select the checkbox next to the action you want to remove.
Tip  
  
To select the entire list, select the checkbox in the header row.
- Select the Actions menu (three dots) and then select Remove .
- Confirm when prompted.
- 

Use the`--action`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to remove an action from an events rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to update an events rule. Update the`action`
