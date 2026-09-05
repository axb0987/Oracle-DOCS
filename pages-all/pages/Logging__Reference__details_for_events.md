# Details for Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_events.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Events

Logging details for Events logs.

## Resources
- rules

## Log Categories

API value (ID): Console (Display Name) Description
ruleexecutionlog Rule Execution Logs Describes how rules were evaluated against events emitted from resources.

## Availability

Events logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Events logging is not available in regions within the Government Cloud realm.

## Contents of an Events Log

Property Description
`logTime`The time of the event, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.
`ruleId`The events rule ID.
`eventId`The UUID of the event. This identifier is not an OCID, but just a unique ID for the event.
`message`The event message.
`target`The rule action. For example:
- For streaming, it means that the event was delivered to the stream.
- For a notification, it means it was delivered to the email subscribed to the topic.
- For a function, it means it triggered the function with the event data.

## An Example Events LogFor events there are two types of messages:
```

```

```

```

## Events Log Object Name

Objects that store Events log data use the following naming format:
```

```

For example:
```

```
