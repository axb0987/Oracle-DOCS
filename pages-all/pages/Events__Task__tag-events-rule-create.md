# Tagging an Events Rule at Creation
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-create.htm
- Fetched: 2026-09-05 02:02 CDT

# Tagging an Events Rule at Creation

Add metadata to a rule when you first create it. This metadata enables you to define keys and values and associate them with resources.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule-create.htm#)
- 

- 

Begin the steps for creating an events rule as described in[Creating an Events Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-events-rule.htm).
- Under Tags, select Add tag .

The tagging options appear.
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

Continue with creating the events rule.
- 

Use the`--defined-tags`or`--freeform-tags`options when running the[oci events rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/create.html)command to tag a rule policy when you create it:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/CreateRule)operation to create a rule. Include the`definedTags`and`freeformTags`
