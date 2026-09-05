# Managing Rules for Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Task/managingrules.htm
- Fetched: 2026-09-05 02:02 CDT

# Managing Rules for Events

Create and manage rules for the Events service.

Tasks for managing rules include managing the rules, as well as the actions, event types, and attributes that make up the rules. See[How Events Works](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/eventsoverview.htm#HowWorks)for more information on rules.

You can perform the following event rules tasks:
- 

[Creating a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-events-rule.htm)
- 

[Listing Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/list-events-rule.htm)
- 

[Getting a Rule's Details](https://docs.oracle.com/en-us/iaas/Content/Events/Task/get-events-rule.htm)
- 

[Editing a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-events-rule.htm)
- 

[Moving a Rule Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Events/Task/change-compartment-events-rule.htm)
- 

[Enabling and Disabling Rules](https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-events-rule.htm)
- 

[Validating a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/managingrules_topic-To_validate_a_rule.htm)
- 

[Tagging a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/tag-events-rule.htm)
- 

[Deleting a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-events-rule.htm)

You can perform the following tasks associated with actions:
- 

[Adding an Action to a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-action-events-rule.htm)
- 

[Editing an Action for a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-action-events-rule.htm)
- 

[Enabling and Disabling an Action for a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/enable-action-events-rule.htm)
- 

[Removing an Action from a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-action-events-rule.htm)

You can perform the following tasks associated with event types:
- 

[Adding an Event Type to a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-type-events-rule.htm)
- 

[Editing an Event Type for a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-type-events-rule.htm)
- 

[Removing an Event Type from a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-type-events-rule.htm)

You can perform the following tasks associated with attributes:
- 

[Adding an Attribute to a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-attribute-events-rule.htm)
- 

[Editing an Attribute for a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-attribute-events-rule.htm)
- 

[Removing an Attribute from a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/delete-attribute-events-rule.htm)

You can perform the following tasks associated with filter tags:
- 

[Adding a Filter Tag to a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/create-filter-tag-events-rule.htm)
- 

[Editing a Filter Tag for a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/update-filter-tag-events-rule.htm)
- 

[Removing a Filter Tag from a Rule](https://docs.oracle.com/en-us/iaas/Content/Events/Task/remove-filter-tag-events-rule.htm)

## Prerequisites for Creating Rules

- 

Action resources: You must have resources already set up to specify as an action. The Events service invokes the action specified in the rule by delivering the event message to action resources, which can include topics , streams, or functions. Every rule must have at least one action. The Events service can invoke any of the following services by delivering an event message for processing:

- [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)
- [Streaming](https://docs.oracle.com/iaas/Content/Streaming/home.htm)
- [Functions](https://docs.oracle.com/iaas/Content/Functions/home.htm)
- 

IAM policies: To manage or list rules, you must be given the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you try to perform a task and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you have been granted and which compartment you should work in. For more information, see[Events and IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/eventspolicy.htm).
- Event messages: To create rules, the resources you want to monitor with the rule must emit events. For more information, see[Services that Produce Events](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Reference/eventsproducers.htm).

## Working with Rules

Note  
  
Each rule can have a maximum of 10 actions.

A typical workflow for setting up rule might follow this pattern:
- Identify action resources

Set up or identify whatever action resources you intend to use with the rule. For example, you might set up a Notifications topic and create subscriptions for the DevOps team so that they are notified when backups complete. If a topic already exists, you can use it instead of creating a topic. The resources you specify for actions do not have to be in the same compartment as the rule.
- Plan filtering

Ensure the resources that you want to monitor emit events to the Events service and plan your pattern matching strategy. For example, you might want to monitor backups on Autonomous AI Lakehouse instances in the ABC compartment. Ensure Autonomous AI Lakehouse instances emit an event type you can use to create the automation you require. Review the example JSON event to determine the best way to identify those resources in filters. See[Matching Events with Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Concepts/filterevents.htm)and[Services that Produce Events](https://docs.oracle.com/en-us/iaas/Content/Events/Task/../Reference/eventsproducers.htm).
- Create the rule
