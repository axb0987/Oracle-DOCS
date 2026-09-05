# Matching Events with Filters
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm
- Fetched: 2026-09-05 02:01 CDT

# Matching Events with Filters

Match events with pattern filters in rules to build automation.

## Background

To understand filtering, it's helpful to review the structure of an actual event message. Events uses JSON objects to represent events. This is an event:

```

```

Two key points to remember about all events:
- Events all have the same set of top-level attributes, which are known as the event envelope. With one exception, most of these top-level attributes are not that useful for creating filters. The exception is`eventType`, which identifies the type of event included in the payload.
- 

The payload of the event appears within the`data`attribute. The information in this field depends on which service produced the event and the event type requested. The information in the payload is useful for isolating one event from another with a filter.

For more information about the envelope, see[Contents of an Event Message](https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/../Reference/eventenvelopereference.htm). For a list of all the services that produce events, see[Services that Produce Events](https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/../Reference/eventsproducers.htm).

## Event Matching with Filters

Rules use filters to select events and route them for delivery to action resources. A rule is represented as a JSON object, similar to an event. The filter is an attribute of the rule, and the attribute is named`condition`. A filter either matches an event or it does not.

A few important things to remember about filters:
- Fields not mentioned in a filter are ignored. You can create a valid filter that matches all event messages with two curly brackets.
- For a filter to match an event, the event must contain all the field names listed in the filter. Field names must appear in the filter with the same nesting structure used in the event.
- Rules apply to events in the compartment in which you create them and any child compartments. This means that a filter specified by a rule only matches events emitted from resources in the same compartment or any child compartments.
- 

Wildcard matching is supported with the asterisk (*) character. See[Examples of Wildcard Matching in Filters](https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm#WildcardSamples).

## Examples of Simple Filters

The following filter matches every event in the compartment and any child compartments where you create the rule.
```

```

When you add fields to the filter, you limit the events that the filter can match. For example, the following filter matches only`deletebucket`events.
```

```

To create a filter for more than one event type, use an array in`eventType`. The following filter matches`deletebucket`and`createbucket`events.
```

```

## Examples of Filters with Event Payload Attributes

Both of the following filters would match the event at the top of the page. The first because filter specifies two fields and both fields appear in the event, the second because the "NoPublicAccess" type appears in the event.

The important thing to note is how the field names in the filter match the nesting structure of the event.
```

```

```

```

Neither of the following filters would match the event at the top of this page. The first because the filter specifies a PublicAccessType not found in the event. The second because the event specifies a name for different bucket.
```

```

```

```

## Examples of Arrays in Filters

Arrays in filters match events if any of the values in the filter match a value in an event. The following filter would match the event at the top of the page because the name of the bucket in the event is included in an array in the filter.
```

```

You can use an array in`eventType`(or any of the top-level fields), the event payload as shown in the preceding example, or both the event payload and a top-level field.
```

```

## Examples of Wildcard Matching in Filters

The following are a few things to consider about wildcard matching with filters.
- Use the wildcard only in attribute values. You cannot use the asterisk for matching in keys.
- An attribute value with only an asterisk matches all values for the associated attribute name, but not null.
- The period character has no special meaning in a filter.

You can add the asterisk at the start of a string, in the middle, or at the end. All of the filters that follow match the event at the top of the page.
- The first matches because the wildcard in`displayName`matches the bucket naming pattern.
- The second one matches because the`publicAccessType`uses a wildcard. Because of the use of the wildcard, these first two filters would also match events from buckets with a similar naming pattern and would include events from buckets with or without public access.
- The third one matches because the event type includes all types of bucket events.
```

```

```

```

```

```
