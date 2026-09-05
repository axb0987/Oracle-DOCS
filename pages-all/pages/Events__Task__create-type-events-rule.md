# Adding an Event Type to an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-type-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Adding an Event Type to an Events Rule

Add an event type to a rule in Events to identify the type of event included in the payload.

For more information about using event types in an events rule, see[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-type-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-type-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-type-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Conditions .
- Under Attributes , select Add attribute .
- Under Event types , select Add Event Type .
- In the Add event type panel, select a Service name and Event type .
- Select Add event type .
- 

Use the`--condition`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to add an event type of an events rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to edit an event rule. Include the`condition`
