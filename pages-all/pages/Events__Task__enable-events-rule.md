# Enabling and Disabling an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Enabling and Disabling an Events Rule

Enable and disable a rule.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- 

Select the events rule you want to enable or disable.

The Rules dialog box appears
- 

From Actions , select Enable or Disable .
- Confirm when prompted.
- 

Use the`--is-enabled`option when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to enable (`true`) or disable (`false`) a rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to enable a rule. Include the`isEnabled`attribute and the values`true`and`false`
