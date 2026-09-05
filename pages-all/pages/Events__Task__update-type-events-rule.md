# Editing an Event Type for an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-type-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Editing an Event Type for an Events Rule

Update an event type for a rule.

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)for more information on using event types in an events rule.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-type-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-type-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-type-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Conditions .
- Under Event types , select the checkbox next to the event type you want to edit.
- From the the Actions menu (three dots) , select Edit .
- Make your changes and select Save changes .
- 

Use the`--condition`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to edit an event type for an events rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to edit an event rule. Include the`condition`
