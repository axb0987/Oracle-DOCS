# Validating an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/managingrules_topic-To_validate_a_rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Validating an Events Rule

Validate a rule in Events to ensure that it operates correctly.

You can evaluate a rule against only one event type at a time. Repeat as necessary to test different event types. For more information, see[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)and[Contents of an Event Message](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Reference/eventenvelopereference.htm).

## Using the Console

- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select a rule.
- Select Actions , then select Validate rule .

The Validate Rule dialog box appears.
- Select the Service name Event type you want to test.
Note  
  
If you added attribute values or filter tags to the rule, edit the example data in the Example event to match the values in your rule.
- Under Rule logic , Select Check if example event matches rule .
-
