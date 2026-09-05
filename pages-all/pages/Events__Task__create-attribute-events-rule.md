# Adding an Attribute to an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-attribute-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Adding an Attribute to an Events Rule

Add an attribute to a rule to specify how it should operate.

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)for more information on using event types in an events rule.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-attribute-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-attribute-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-attribute-events-rule.htm#)
- 

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule and then select Conditions .
- Under Attributes , select Add attribute .
- In the Add attribute panel, select the following values:
- Attribute name : Select an attribute name. The list of attribute names is based on the event types you selected. If you select no event types, you can't add an attribute.
Note  
  
If you specify an attribute here, you limit the events that match this rule.
- Attribute values : To specify one or more values for the attribute name, enter a value. As you type, the value appears under the field with (New) appended. Select the value with (New) appended to add the value. You can enter more values for the attribute name.

Here are some things to consider about attribute values:
- Use an asterisk to create a wildcard. See[Examples of Wildcard Matching in Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm#WildcardSamples).
- Multiple values for an attribute name broaden your results. If any of the values you enter here match a value in an event, the rule matches. See[Examples of Arrays in Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm#ArraySamples).
- Select Add attribute .
- 

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)for information on how to use attributes.

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)
