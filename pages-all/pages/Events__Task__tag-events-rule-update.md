# Tagging an Events Rule when Updating
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-update.htm
- Fetched: 2026-09-05 02:02 CDT

# Tagging an Events Rule when Updating

Add metadata to a rule when you update it. This metadata enables you to define keys and values and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-update.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule, then select Tags .
- Select Add .
- 

Enter or select values for these items:
- Namespace
- Key
- Value
Note  
  
See[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)for descriptions of these fields.
- 

Select Add tag to add another tag. Select X to remove a tag.
- 

Select Add tags .

You see the tags you added.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci events rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/update.html)command to tag a rule when you update it:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/UpdateRule)operation to update a rule. Include the`definedTags`and`freeformTags`
