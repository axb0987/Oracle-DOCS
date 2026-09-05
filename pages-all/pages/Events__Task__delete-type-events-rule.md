# Removing an Event Type from an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-type-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Removing an Event Type from an Events Rule

Remove an event type from a rule.

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)for more information on using event types in an events rule.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-type-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-type-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-type-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Conditions .
- Under Event types , select the checkbox next to the attribute you want to remove.
Tip  
  
To select the entire list, select the checkbox in the header row.
- Select Remove .
- Confirm when prompted.
- 

Use the`--condition`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to remove an event type from an events rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to edit an event rule. Include the`condition`
