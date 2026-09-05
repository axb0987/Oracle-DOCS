# Editing an Action for an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-action-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Editing an Action for an Events Rule

Update an action for a rule.

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)for more information on using actions in an events rule.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-action-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-action-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-action-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Actions .
- Select the checkbox next to the action you want to edit
- Select the Actions menu (three dots) and then select Edit .
- Make your changes and select Save changes .
- 

Use the`--action`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to edit an action for a rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to update a rule. Update the`action`
