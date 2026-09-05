# Creating an Events Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-events-rule.htm
- Fetched: 2026-09-05 02:02 CDT

# Creating an Events Rule

Create a rule in Events to create automation based on the state changes of resources throughout your tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-events-rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-events-rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-events-rule.htm#)
- 

To create a rule:
- Navigate to the events list page. If you need help finding the list page, see[Listing Events Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Task/list-events-rule.htm).
- Select Create Rule .

## Create Rule

Under Create Rule , provide the following:
- Display name: Provide a friendly name for the rule.
- Description: A description of what the rule does. Avoid entering confidential information.

You can change the values later.

## Rule Conditions

Define the rule conditions. You can define filters based on event types, attributes, and tags to limit the events that trigger actions. See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm).

### Filter by Event Type

To filter events by add an event type, follow these steps.
- Condition: Select Event Type .
- Service name: Select a service.
- Event type: Select one or more types of events for this the service.
- To add event types for a different service, select Add Condition and select Event Type repeat the preceding steps to add event types for a different service.
Note  
  
You must create an event type condition before you can add an attribute.

To further filter event types by using attributes, follow these steps.
- After adding an event type, select Add Condition .
- Condition: Select Attribute .
- Attribute name: Select an attribute name.
- Attribute values: Select or enter values for the attribute.

### Filter by Filter Tags

Filter tags help you to hone automation by targeting only resources that contain a particular tag. If you want to use tags to organize your rules, use resource tags instead. For more information, see[Managing Tags for Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/eventsoverview.htm#Tags).

To filter events by using tags, follow these steps.
- Condition: Select Filter Tag
- Tag namespace: To specify a free-form tag, select None (add a free-form tag) .
- Tag key: Select a tag key.
- Tag value: Enter a tag value.
- To add another tag, select Add Condition and repeat the preceding steps.

### Helper Buttons

Helper buttons at the top of this section provide tools to evaluate your rules.
- Preview rule logic: Selecting this button provides a text representation of your rule. Select Close to close the dialog.
- View example events (JSON): Displays the JSON that represent your rule.

For more information, see[Contents of an Event Message](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Reference/eventenvelopereference.htm)and[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm).
- 

Validate rule: Validates the rule based on the conditions that you specified. You can evaluate a rule against one event type at a time. To test different event types, repeat these steps as necessary.
- Service Name: Select a service.
- Event Type: Select an event type.

An example event appears based on your selections you made. Edit the values in the event to match the values for any attributes and tags that you added to your rule. For more information, see[Contents of an Event Message](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Reference/eventenvelopereference.htm).
- Select Check if Example Event Matches Rule or Validate to validate your rule. If the rule matches, you get a Success message.
- If the rule doesn't match, use the rule editor to make the following changes as needed:
- Add or remove event types.
- Add or remove values or attributes.
- Add or remove tags.
- Insert wildcards.

For more information, see[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm).
- Select Cancel to close the dialog.

## Actions

Action type: Specify the resource to trigger when the filter finds a match.

The following options are available:
- Notifications: Select a compartment, then select the topic.
- Streaming: Select the compartment, then select the stream.
- Functions: Select the compartment, then select the function application, and then select the function.

To add another action, select Add Action .
Tip  
  
A notification, stream, or function must exist before you can select it from the list.

## Tags

You can apply tags to resources to help you organize them according to business needs. You can apply tags at the time you create a resource, or you can update the resource later with tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Complete Rule

Select Create Rule .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/events/rule/create.html)oci events rule create`command and required parameters to create a rule:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateRule](https://docs.oracle.com/iaas/api/#/en/events/latest/Rule/CreateRule)
