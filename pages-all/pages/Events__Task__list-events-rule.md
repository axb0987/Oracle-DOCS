# Listing Events Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/list-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Listing Events Rules

View the rules in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/list-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/list-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/list-events-rule.htm#)
- 

- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.
Note  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

All events rules in that compartment are listed in tabular form.

Optionally, the following tasks are available for each event rule.
- Edit a rule.
- Disable a rule.
- Delete a rule.
- Move a rule to a different compartment.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/list.html)oci events rule list`command and required parameters to list the rules in a compartment:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListRules](https://docs.oracle.com/iaas/api/#/en/events/latest/RuleSummary/ListRules)
